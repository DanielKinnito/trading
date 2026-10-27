# Chapter 07: Targets, Deviations & Risk Management

> **Previous**: [Chapter 06: Entry Models & Execution Playbook](./06_entry_models_and_execution_playbook.md) | **Next**: [Chapter 08: Indicator Guide & TradingView Setup](./08_indicator_guide_and_tradingview_setup.md)

---

## 1. Standard Deviation Projections

A major technical strength of the Fractal Model is its **mathematical price projection engine**. Rather than guessing arbitrary profit targets, TTrades uses **Fibonacci Standard Deviations** anchored to the manipulation swing:

### Anchor Points for Projections:
* **Point "1.0"**: The **C2 Extreme Swing Point** (the tip of the sweep wick).
* **Point "0.0"**: The **CISD Trigger Candle extreme** (the low for bearish, high for bullish).

```pinescript
// Standard Deviation Targets
std_dev_levels = "-1.0, -2.0, -2.5, -4.0, -4.5"
```

```
   [Point 1.0] ════════════════════════════════════ C2 Extreme High (Bearish Sweep)
               \
                \  Manipulation Leg
                 \
   [Point 0.0] ───▼──────────────────────────────── CISD Trigger Low
   
   [-1.0 Std]  ──────────────────────────────────── Target 1: Take 50% Partials (Move SL to BE)
   [-2.0 Std]  ──────────────────────────────────── Target 2: High Probability TP (Close 80%)
   [-2.5 Std]  ──────────────────────────────────── Target 3: Full Delivery / Institutional Objective
   [-4.0 Std]  ──────────────────────────────────── Target 4: Trend Day Runner Extension
```

### The Key Target Zones:
1. **`-1.0` to `-2.0` (Target 1 - Scale Out)**:
   * 50% of the position is closed.
   * Stop Loss is immediately moved to **Break-Even (BE)** or entry price.
2. **`-2.0` to `-2.5` (Target 2 - Institutional Delivery)**:
   * ICT and algorithmic price delivery models frequently exhaust between **`-2.0` and `-2.5`**.
   * Take 80–90% off or close the entire trade.
3. **`-4.0` (Target 3 - Mega Expansion)**:
   * Reserved for runners on high-impact news days or strong trend-continuation days.

---

## 2. Draw on Liquidity (DOL) Hierarchy

In addition to standard deviations, target exits must align with natural market liquidity:
1. **Opposing Session Extremes (PxL)**:
   * If going long from London Low, target the **Asian High** or **London High**.
   * If going short from NY Open, target **PDL (Previous Day Low)**.
2. **Relative Equal Highs / Lows (REH/REL)**:
   * Clusters of double/triple tops or bottoms represent Low Resistance Liquidity (LRL). Price will accelerate through them.

---

## 3. SMT Divergence: The A+ Setup Qualifier

**SMT (Smart Money Technique) Divergence** is the ultimate institutional confluence in the Fractal Model.

### Correlated Instruments:
* **Indices**: Nasdaq (NQ1!), S&P 500 (ES1!), Dow Jones (YM1!).
* **Forex**: EURUSD vs. GBPUSD; or inverse against the US Dollar Index (DXY).

| SMT Type | Primary Asset (e.g. NQ) | Correlated Asset (e.g. ES) | Institutional Interpretation |
| :--- | :--- | :--- | :--- |
| **Bearish SMT** | Makes a **Higher High** (sweeps liquidity) | Makes a **Lower High** (fails to sweep) | Institutional distribution; ES refuses to go higher $\rightarrow$ **Huge Selloff Expected**. |
| **Bullish SMT** | Makes a **Lower Low** (sweeps liquidity) | Makes a **Higher Low** (fails to sweep) | Institutional accumulation; ES refuses to go lower $\rightarrow$ **Huge Rally Expected**. |

> **Rule of Thumb**: When a C2 sweep coincides with an active SMT divergence, it is classified as an **A+ Setup**.

---

## 4. Professional Risk Management Rules

1. **Max 2 Trades Per Day**: If both trades lose, walk away. Your bias or session timing is off.
2. **1% Maximum Account Risk**: Calculate position size based on the distance between your entry price and the C2 extreme stop loss:
   $$\text{Contracts} = \frac{\text{Account Balance} \times 0.01}{\text{Stop Loss Distance in Dollars}}$$
3. **Never Move Stops Away**: Only trail stops toward profit; never widen risk.
