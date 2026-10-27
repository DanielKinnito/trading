# Session Liquidity Suite (v6)

<span class="tt-badge-bull">Pine Script v6</span>
<span class="tt-badge-neutral">Session Automation</span>
<span class="tt-badge-bull">Zero Repaint</span>

> **Automated session high/low tracking, range boxes, and liquidity sweep detection for Asian, London, and New York sessions.**

---

## 1. What It Does

Institutions operate on fixed session liquidity cycles. The **Liquidity Suite** automates:

- **Asian Session Range (18:00 – 00:00 or 02:00 NY Time)**:
    - Plots Asian High (Asia BSL) and Asian Low (Asia SSL).
    - Shaded background box with upper/lower bounds.
- **London Session Range (02:00 – 05:00 NY Time)**:
    - Plots London High and Low.
    - Tracks whether London swept the Asian session range.
- **New York Session Range (08:30 – 11:00 NY Time)**:
    - Tracks NY AM Judas swings and afternoon settlement runs.
- **Previous Day High / Low (PDH / PDL)**:
    - Automatically updates previous day extremes as key external draw on liquidity (DOL).

Below is the photorealistic chart showing London session sweeping the Asian low on EURUSD into a 50% T-Spot equilibrium:

![London Session Asian Low Sweep](../assets/images/models/model2_tspot_limit.png)
<div class="image-caption">Figure L.1: London Open Asian Low sweep on EURUSD with 50% T-Spot limit execution.</div>

---

## 2. Liquidity Sweep Alerts

The indicator can automatically alert you whenever a session high or low is swept:

| Alert Trigger | Market Condition | Execution Meaning |
| :--- | :--- | :--- |
| `Asian Low Swept` | Price wicks below Asian range low into discount | Potential C2 low forming; watch for Bullish CISD |
| `Asian High Swept` | Price wicks above Asian range high into premium | Potential C2 high forming; watch for Bearish CISD |
| `London Low Swept` | NY AM purges London session low | London low Judas swing purged; watch for NY AM reversal |
| `London High Swept` | NY AM purges London session high | London high Judas swing purged; watch for NY AM reversal |

---

## 3. Source Code Location

The source code is located in:

```
scripts/indicators/liquidity_suite.pine
```

[View Raw Script on GitHub →](https://github.com/DanielKinnito/trading/blob/master/scripts/indicators/liquidity_suite.pine)
