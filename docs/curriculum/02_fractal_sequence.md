# Chapter 02: The C1–C2–C3–C4 Fractal Sequence

> **Core Curriculum** | Previous: [Chapter 01: Foundational Concepts](01_foundational_concepts.md) | Next: [Chapter 03: CISD](03_cisd_deep_dive.md)

---

## 1. Overview of the 4-Candle Lifecycle

The hallmark of TTrades' methodology is organizing market fractals into an exact sequence of **four consecutive candles**. This sequence applies across all timeframes:

```
      [ C1 ]              [ C2 ]              [ C3 ]              [ C4 ]
  Reference Base   ───►   Liquidity Sweep  ───►  Execution/   ───►  Delivery /
  & Range Bounds          & Pivot Wick           Expansion          Continuation
```

### Visual Cycle Diagram
![The C1-C2-C3-C4 Sequence](../assets/images/models/fractal_c1_c4_cycle.png)
<div class="image-caption">Figure 2.1: The 4-candle delivery cycle showing C1 reference range, C2 liquidity sweep, C3 displacement & CISD, and C4 distribution.</div>

---

## 2. Candle Roles & Algorithmic Mechanics

### Candle 1 (C1) — The Reference Anchor
* **Role**: Sets the liquidity bounds and benchmark levels for the setup.
* **Key Levels Marked**:
    * `C1 High`: Buyside Liquidity (BSL) target or sweep level.
    * `C1 Low`: Sellside Liquidity (SSL) target or sweep level.
    * `C1 Equilibrium`: 50% midpoint of the candle range.

### Candle 2 (C2) — The Liquidity Sweep & Pivot Formation
* **Role**: The pivot candidate. C2 tests or purges the liquidity established by C1.
* **Bullish Setup Requirements**:
    * C2 wicks **below** the C1 Low (sweeping sellside liquidity).
    * C2 candle body **closes back inside** the C1 range or above the sweep level.
    * The lowest point of C2 becomes the **Extreme Low** (`c2_extreme`), which serves as the invalidation level.
* **Bearish Setup Requirements**:
    * C2 wicks **above** the C1 High (sweeping buyside liquidity).
    * C2 candle body **closes back inside** the C1 range or below the sweep level.
    * The highest point of C2 becomes the **Extreme High** (`c2_extreme`), which serves as the invalidation level.
* **Confirmation Rule**: C2 is only an official pivot **after it closes**. If C2 is still open, it is treated as a *potential/live setup*.

### Candle 3 (C3) — The Execution & Expansion Candle
* **Role**: The primary execution candle. This is where Power of 3 (AMD) delivers explosive, directional movement.
* **Execution Rules**:
    * C3 opens and forms its initial manipulation wick (accumulating orders).
    * Retraces into the **C2 Wick Midpoint (EQ)** or **T-Spot Zone**.
    * Confirms via a lower-timeframe **Change in State of Delivery (CISD)**.
    * Expands aggressively toward the projected targets.

### Candle 4 (C4) — The Delivery & Extension Candle
* **Role**: Delivery completion, runner trailing, or continuation checkpoint.
* **Rules**:
    * C4 should not violate the extreme of C3 in a healthy trend.
    * Once price reaches `-2.0` or `-2.5` standard deviations, runner targets are closed or trailed aggressively.

---

## 3. Real TradingView Chart Example

Below is a live 1-minute chart on **NAS100** running the **1m - 15m Model**, showing the exact transition from C2 sweep to C3 execution and C4 expansion:

![NAS100 1m - 15m C2-C3 Sequence](../assets/images/charts/nas100_1m_15m_c2_c3_sequence.png)
<div class="image-caption">Figure 2.2: Live TradingView indicator execution showing C2 sweep, CISD line (blue), C3 entry box, C4 target, and HTF candles on the right.</div>

---

## 4. Summary Checklist for C1–C3

!!! example "Pre-Execution Checklist"
    - [x] **C1 Range**: Has C1 established a clear high and low?
    - [x] **C2 Sweep**: Has C2 swept C1's high/low and closed back within the range without body acceptance?
    - [x] **HTF POI**: Did the C2 sweep tap into a higher-timeframe FVG or Orderblock?
    - [x] **C3 Expansion**: Is C3 ready to expand in the direction of the reversal?
    - [x] **CISD Confirmed**: Has the candle body closed beyond the benchmark open?
