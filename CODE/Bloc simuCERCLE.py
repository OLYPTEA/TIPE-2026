from dataclasses import dataclass
from math import isfinite
import matplotlib.pyplot as plt
import numpy as np

@dataclass
class State:
    x: float
    y: float
    u: float
    v: float

def energies_cinetiques(m, M, u, v):
    E1 = 0.5 * m * u*u
    E2 = 0.5 * M * v*v
    return E1, E2, E1 + E2

def quantite_de_mouvement(m, M, u, v):
    return m*u + M*v

def collision_elastique_blocs(m, M, u, v):
    u_new = ((m - M) / (m + M)) * u + (2 * M / (m + M)) * v
    v_new = (2 * m / (m + M)) * u + ((M - m) / (m + M)) * v
    return u_new, v_new

def simulate(m=1.0, M=100.0, x0=1.0, y0=3.0, u0=0.0, v0=-1.0, eps=1e-14, max_events=10_000_000):
    """
    Retourne:
      - état final
      - liste d'événements (dict)
      - liste uv : [(u0,v0), (u1,v1), ...] enregistrée à chaque passage/événement
    """
    s = State(x0, y0, u0, v0)
    t = 0.0
    events = []

    uv = [(s.u, s.v)]

    for _ in range(max_events):

        if s.u >= -eps and s.v >= -eps and s.u <= s.v + eps:
            break

        t_wall = float("inf")
        if s.u < -eps:
            t_wall = s.x / (-s.u)

        t_bb = float("inf")
        if s.v < s.u - eps:
            t_bb = (s.y - s.x) / (s.u - s.v)

        t_next = min(t_wall, t_bb)
        if not isfinite(t_next):
            break

        s.x += s.u * t_next
        s.y += s.v * t_next
        t += t_next

        E1_b, E2_b, Etot_b = energies_cinetiques(m, M, s.u, s.v)
        p_b = quantite_de_mouvement(m, M, s.u, s.v)

        if t_wall < t_bb - eps:

            u_before, v_before = s.u, s.v
            s.x = 0.0
            s.u = -s.u

            E1_a, E2_a, Etot_a = energies_cinetiques(m, M, s.u, s.v)
            p_a = quantite_de_mouvement(m, M, s.u, s.v)

            J_wall = m * (s.u - u_before)

            events.append({
                "t": t, "type": "wall",
                "u_before": u_before, "v_before": v_before,
                "u_after": s.u, "v_after": s.v,
                "p_before": p_b, "p_after": p_a, "dp": p_a - p_b,
                "Etot_before": Etot_b, "Etot_after": Etot_a, "dEtot": Etot_a - Etot_b,
                "dE1": E1_a - E1_b, "dE2": E2_a - E2_b,
                "J_wall": J_wall, "J_blocks": 0.0
            })

        else:

            u_before, v_before = s.u, s.v
            s.u, s.v = collision_elastique_blocs(m, M, u_before, v_before)

            E1_a, E2_a, Etot_a = energies_cinetiques(m, M, s.u, s.v)
            p_a = quantite_de_mouvement(m, M, s.u, s.v)

            J = m * (s.u - u_before)

            events.append({
                "t": t, "type": "block",
                "u_before": u_before, "v_before": v_before,
                "u_after": s.u, "v_after": s.v,
                "p_before": p_b, "p_after": p_a, "dp": p_a - p_b,
                "Etot_before": Etot_b, "Etot_after": Etot_a, "dEtot": Etot_a - Etot_b,
                "dE1": E1_a - E1_b, "dE2": E2_a - E2_b,
                "J_wall": 0.0, "J_blocks": J
            })

        uv.append((s.u, s.v))

    return s, events, uv

m = 1
M = 100

final_state, events, uv = simulate(m=m, M=M, x0=1.0, y0=3.0, u0=0.0, v0=-1.0)

u_vals = [p[0] for p in uv]
v_vals = [p[1] for p in uv]

plt.figure()
plt.plot(v_vals, u_vals, marker='o', linestyle='-')
plt.xlabel("u (vitesse gros bloc)")
plt.ylabel("v (vitesse petit bloc)")
plt.title("Portrait de phase : v en fonction de u (aux instants de collision)")
plt.grid(True)
plt.show()

U_vals = [np.sqrt(m) * u for (u, v) in uv]
V_vals = [np.sqrt(M) * v for (u, v) in uv]

plt.figure()
plt.plot(V_vals, U_vals, marker='o', linestyle='-')
plt.xlabel(r"$\sqrt{m}\,u$")
plt.ylabel(r"$\sqrt{M}\,v$")
plt.title("Portrait de phase : variables réduites (énergie conservée)")
plt.axis("equal")
plt.grid(True)
plt.show()
