# Session Liquidity Suite (v6)

<span class="badge-bullish">Pine Script v6</span>
<span class="badge-neutral">Session Automation</span>
<span class="badge-neutral">Zero Repaint</span>

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

---

## 2. Liquidity Sweep Alerts

The indicator can automatically alert you whenever a session high or low is swept:

- `Asian Low Swept`: Fires when price wicks below the Asian range low.
- `Asian High Swept`: Fires when price wicks above the Asian range high.
- `London High/Low Swept`: Fires when New York price purges London session liquidity.

---

## 3. Source Code Location

The source code is located in:

```
scripts/indicators/liquidity_suite.pine
```

[:octicons-mark-github-16: View Raw Script on GitHub](https://github.com/DanielKinnito/trading/blob/main/scripts/indicators/liquidity_suite.pine)
