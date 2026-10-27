# Chapter 02: The C1–C2–C3–C4 Fractal Sequence

> **Previous**: [Chapter 01: Foundational Concepts](./01_foundational_concepts_and_market_delivery.md) | **Next**: [Chapter 03: CISD](./03_cisd_change_in_state_of_delivery.md)

---

## 1. Overview of the 4-Candle Lifecycle

The hallmark of TTrades' methodology is organizing market fractals into an exact sequence of **four consecutive candles**. This sequence applies across all timeframes:

```
          [ C1 ]              [ C2 ]              [ C3 ]              [ C4 ]
      Reference Base   ───►   Liquidity Sweep  ───►  Execution/   ───►  Delivery /
      & Range Bounds          & Pivot Wick           Expansion          Continuation
```

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
* **Role**: The money-making candle. This is where Power of 3 (AMD) delivers explosive, one-sided movement.
* **Execution Rules**:
  * C3 opens and immediately forms its initial manipulation wick (accumulating orders).
  * Retraces into the **C2 Wick Midpoint (EQ)** or **T-Spot Zone**.
  * Confirms via a lower-timeframe **Change in State of Delivery (CISD)**.
  * Expands aggressively toward the projected targets.

### Candle 4 (C4) — The Delivery & Extension Candle
* **Role**: Delivery completion, runner trailing, or invalidation checkpoint.
* **Rules**:
  * C4 should not violate the extreme of C3 in a healthy trend.
  * If price reaches `-2.0` or `-2.5` standard deviations, runners are closed.

---

## 3. Visual Schematics

### Bullish C1–C2–C3 Sequence (Reversal from Lows)
```
          C1 (Base)            C2 (Sweep)            C3 (Expansion)
              │                    │                       │ High
            ┌───┐                ┌───┐                   ┌───┐
            │   │                │   │                   │   │ Close
            │   │                │   │                   │   │
            └───┘                └───┘                   │   │
              │                    │                     │   │
    ══════════╪════ C1 Low ════════╪═════════════════════│───│
              │                    │ (Sweeps C1 Low)     └───┘
                                   │                       │ Open / Retrace
                                   │ Extreme Low          Low (into C2 wick EQ)
```

### Bearish C1–C2–C3 Sequence (Reversal from Highs)
```
                                   │ Extreme High
                                   │ (Sweeps C1 High)
    ══════════╪════ C1 High ═══════╪═════════════════════┌───┐
              │                    │                     │   │ Open / Retrace
            ┌───┐                ┌───┐                   │   │
            │   │                │   │                   │   │
            │   │                │   │                   │   │
            └───┘                └───┘                   └───┘ Close
              │                    │                       │
              C1                   C2                      │ Low
                                                           C3 (Expansion)
```

---

## 4. Summary Checklist for C1–C3

- [ ] Has **C1** established a clear high and low?
- [ ] Has **C2** swept C1's high/low and closed back within acceptable range?
- [ ] Has C2 closed without body acceptance beyond the sweep level?
- [ ] Is **C3** ready to expand in the direction of the reversal?
- [ ] Has lower timeframe **CISD** confirmed the turn during C2's wick or C3's open?
