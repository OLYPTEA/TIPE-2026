import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
from dataclasses import dataclass
from math import isfinite


@dataclass
class State:
    x: float
    y: float
    u: float
    v: float

def collision_elastique_blocs(m, M, u, v):
    u_new = ((m - M) / (m + M)) * u + (2 * M / (m + M)) * v
    v_new = (2 * m / (m + M)) * u + ((M - m) / (m + M)) * v
    return u_new, v_new

def simulate(m=1.0, M=100.0, x0=1.0, y0=3.0, u0=0.0, v0=-1.0, eps=1e-14, max_events=10_000_000):
    s = State(x0, y0, u0, v0)
    t = 0.0
    uv = [(s.u, s.v)]

    for _ in range(max_events):
        if s.u >= -eps and s.v >= -eps and s.u <= s.v + eps:
            break

        t_wall = s.x / (-s.u) if s.u < -eps else float("inf")
        t_bb = (s.y - s.x) / (s.u - s.v) if s.v < s.u - eps else float("inf")
        
        t_next = min(t_wall, t_bb)
        if not isfinite(t_next):
            break

        s.x += s.u * t_next
        s.y += s.v * t_next
        t += t_next

        if t_wall < t_bb - eps:
            s.x = 0.0
            s.u = -s.u
        else:
            s.u, s.v = collision_elastique_blocs(m, M, s.u, s.v)

        uv.append((s.u, s.v))

    return uv


m = 1
M = 100



uv = simulate(m=m, M=M, x0=1.0, y0=3.0, u0=0.0, v0=-1.0)


# Variables réduites
U_vals = [np.sqrt(m) * u for (u, v) in uv]
V_vals = [np.sqrt(M) * v for (u, v) in uv]
N_total = len(uv)


fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(bottom=0.25) 


rayon = np.sqrt(U_vals[0]**2 + V_vals[0]**2)
theta = np.linspace(0, 2*np.pi, 200)
ax.plot(rayon * np.cos(theta), rayon * np.sin(theta), color='lightgray', linestyle='--', label='Cercle théorique (Énergie const.)')


trajectoire_line, = ax.plot(V_vals[0:1], U_vals[0:1], marker='', linestyle='-', color='blue')
point_actuel, = ax.plot(V_vals[0], U_vals[0], marker='o', color='red', markersize=8, label='État actuel')


ax.set_aspect("equal")
ax.set_xlabel(r"$\sqrt{M}\,v$ (vitesse gros bloc)")
ax.set_ylabel(r"$\sqrt{m}\,u$ (vitesse petit bloc)")
ax.set_title(f"Évolution pas à pas des collisions (M/m = {M/m})")
ax.grid(True)
ax.legend()


lim = rayon * 1.2
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)


ax_slider = plt.axes([0.15, 0.1, 0.7, 0.03]) # Position [gauche, bas, largeur, hauteur]
slider_choc = Slider(
    ax=ax_slider,
    label='Numéro du choc',
    valmin=0,
    valmax=N_total - 1,
    valinit=0,
    valstep=1 )


def update(val):
    index = int(slider_choc.val)
    
    
    trajectoire_line.set_xdata(V_vals[:index + 1])
    trajectoire_line.set_ydata(U_vals[:index + 1])
    
    
    point_actuel.set_xdata([V_vals[index]]) 
    point_actuel.set_ydata([U_vals[index]])
    
    
    ax.set_title(f"Collisions : {index} / {N_total - 1} (La valeur de $\pi$ approche...)")
    
    
    fig.canvas.draw_idle()


slider_choc.on_changed(update)

plt.show()