//=============================================================================================================
// C'est le code utilisé pour la simulation Unity 3D de la méthode de calcul de π par collisions élastiques.
// Simule la physique de deux blocs sur une ligne, avec des collisions élastiques entre eux et avec un mur fixe.
// Y a pas grand chose à voir, c'est juste de la physique basique et de la gestion d'UI 
//=============================================================================================================



using System;
using UnityEngine;
using TMPro;

public class PiCollisionsSimulation3D : MonoBehaviour
{
    [Header("Scene refs")]
    public Transform blockSmall;
    public Transform blockBig;
    public Transform wallVisual;

    [Header("UI (TMP)")]
    public TMP_InputField input_m;
    public TMP_InputField input_M;
    public TMP_InputField input_v0Big;
    public TMP_Text textCollisions;
    public TMP_Text textPi;
    public TMP_Text textUV;

    [Header("Physics")]
    public double m = 1.0;
    public double M = 10000.0;
    public double v0Big = -1.0;
    public double wallX = 0.0;

    [Header("Initial positions (center)")]
    public double xSmall0 = 2.0;
    public double xBig0 = 6.0;

    [Header("Visual half-sizes on X")]
    public double halfSmall = 0.5;
    public double halfBig = 0.75;

    [Header("Run")]
    public bool running = false;

    // state
    double xSmall, xBig;
    double uSmall, vBig;
    long collisions;

    // animation
    bool animating = false;
    double remainingTimeToCollision = 0.0;

    void Start()
    {
        PullUIToParams();
        ResetSim();
        ApplyTransforms();
        UpdateUI();
    }

    void Update()
    {
        if (!running)
        {
            ApplyTransforms();
            UpdateUI();
            return;
        }

        if (!animating)
        {
            if (IsFinished())
            {
                running = false;
                return;
            }

            remainingTimeToCollision = ComputeTimeToNextCollision();
            animating = true;
        }

        double dt = Time.deltaTime;

        if (dt >= remainingTimeToCollision)
        {
            xSmall += uSmall * remainingTimeToCollision;
            xBig += vBig * remainingTimeToCollision;

            ApplyCollision();
            animating = false;
        }
        else
        {
            xSmall += uSmall * dt;
            xBig += vBig * dt;
            remainingTimeToCollision -= dt;
        }

        ApplyTransforms();
        UpdateUI();
    }

    public void ToggleRun()
    {
        PullUIToParams();
        // si on relance après un reset, faut remettre v0
        if (collisions == 0 && Math.Abs(vBig) < 1e-12) vBig = v0Big;

        running = !running;
    }

    public void ApplyUIValuesAndReset()
    {
        PullUIToParams();
        ResetSim();
        animating = false;
        ApplyTransforms();
        UpdateUI();
    }

    public void StepOnce()
    {
        PullUIToParams();
        running = false;
        animating = false;
        if (!IsFinished())
        {
            // saute directement à la prochaine collision (mode “explication”)
            double t = ComputeTimeToNextCollision();
            xSmall += uSmall * t;
            xBig += vBig * t;
            ApplyCollision();
        }
        ApplyTransforms();
        UpdateUI();
    }

    void ResetSim()
    {
        collisions = 0;
        xSmall = xSmall0;
        xBig = xBig0;
        uSmall = 0.0;
        vBig = v0Big;
    }

    void PullUIToParams()
    {
        if (input_m && double.TryParse(input_m.text.Replace(',', '.'), out var mv)) m = Math.Max(1e-12, mv);
        if (input_M && double.TryParse(input_M.text.Replace(',', '.'), out var Mv)) M = Math.Max(1e-12, Mv);
        if (input_v0Big && double.TryParse(input_v0Big.text.Replace(',', '.'), out var vv)) v0Big = vv;
    }

    bool IsFinished()
    {
        // both moving right and big won't catch small
        return (uSmall >= 0.0 && vBig >= 0.0 && vBig >= uSmall);
    }

    double ComputeTimeToNextCollision()
    {
        double tWall = double.PositiveInfinity;
        if (uSmall < 0.0)
        {
            double dist = wallX - (xSmall - halfSmall);
            tWall = dist / uSmall;
        }

        double tBlocks = double.PositiveInfinity;
        double relV = uSmall - vBig;
        double gap = (xBig - halfBig) - (xSmall + halfSmall);
        if (relV > 0.0 && gap > 0.0)
            tBlocks = gap / relV;

        return Math.Min(tWall, tBlocks);
    }

    void ApplyCollision()
    {
        // recompute which collision is next
        double tWall = double.PositiveInfinity;
        if (uSmall < 0.0)
        {
            double dist = wallX - (xSmall - halfSmall);
            tWall = dist / uSmall;
        }

        double tBlocks = double.PositiveInfinity;
        double relV = uSmall - vBig;
        double gap = (xBig - halfBig) - (xSmall + halfSmall);
        if (relV > 0.0 && gap > 0.0)
            tBlocks = gap / relV;

        if (tWall < tBlocks)
        {
            uSmall = -uSmall;
        }
        else
        {
            (uSmall, vBig) = ElasticCollision1D(m, M, uSmall, vBig);
        }

        collisions++;
    }

    (double, double) ElasticCollision1D(double m1, double m2, double u1, double u2)
    {
        double denom = (m1 + m2);
        double u1p = ((m1 - m2) / denom) * u1 + (2.0 * m2 / denom) * u2;
        double u2p = (2.0 * m1 / denom) * u1 + ((m2 - m1) / denom) * u2;
        return (u1p, u2p);
    }

    void ApplyTransforms()
    {
        if (blockSmall) blockSmall.position = new Vector3((float)xSmall, blockSmall.position.y, blockSmall.position.z);
        if (blockBig) blockBig.position = new Vector3((float)xBig, blockBig.position.y, blockBig.position.z);
        if (wallVisual) wallVisual.position = new Vector3((float)wallX, wallVisual.position.y, wallVisual.position.z);
    }

    void UpdateUI()
    {
        if (textCollisions) textCollisions.text = $"Collisions : {collisions}";
        if (textUV) textUV.text = $"u = {uSmall:0.####}   |   v = {vBig:0.####}";

        if (textPi)
        {
            double ratio = M / m;
            double n = Math.Log(ratio) / Math.Log(100.0);
            double scale = Math.Pow(10.0, Math.Round(n));
            double approxPi = (scale > 0) ? collisions / scale : 0.0;
            textPi.text = $"π ≈ {approxPi}   (M/m={ratio:0.###})";
        }
    }
}

