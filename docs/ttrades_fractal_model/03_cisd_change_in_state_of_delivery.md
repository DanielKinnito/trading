# Chapter 03: CISD (Change in State of Delivery)

> **Previous**: [Chapter 02: The Fractal Sequence](./02_the_c1_c2_c3_c4_fractal_sequence.md) | **Next**: [Chapter 04: POI & The T-Spot](./04_points_of_interest_and_the_tspot.md)

---

## 1. What is a Change in State of Delivery (CISD)?

**Change in State of Delivery (CISD)** is the core algorithmic entry and confirmation mechanism in the TTrades model.

In institutional order flow:
* When price is pushing lower, every candle is delivered as a **sell program** (bearish delivery).
* For the algorithm to shift into a **buy program** (bullish delivery), it must actively violate the price origin of the last bearish delivery leg.
* That origin point is mathematically defined as the **opening price of the opposing candle(s)** that formed the extreme.

```
      ═════════════════════════════════════════════ CISD Level (Opposing Candle Open)
                                  ▲
                                  │ Candle Body CLOSES ABOVE this level
                                  │ (Confirms algorithmic delivery has flipped)
```

---

## 2. Mechanical Identification of CISD

### A. Bullish CISD (Shift from Selling to Buying)
1. **Identify the Extreme**: Locate the lowest point formed during the C2 liquidity sweep.
2. **Trace Back to Opposing Candles**: Find the last consecutive **down-close (bearish) candle(s)** that immediately led to that lowest point.
3. **Mark the Level**: Draw a horizontal line at the **Open price** of the *first* down-close candle in that series.
4. **Trigger Condition**: Wait for a subsequent candle **body to close strictly above** this marked Open price.
5. **Validation**: Once the candle body closes above, **Bullish CISD is confirmed**.

### B. Bearish CISD (Shift from Buying to Selling)
1. **Identify the Extreme**: Locate the highest point formed during the C2 liquidity sweep.
2. **Trace Back to Opposing Candles**: Find the last consecutive **up-close (bullish) candle(s)** that immediately led to that highest point.
3. **Mark the Level**: Draw a horizontal line at the **Open price** of the *first* up-close candle in that series.
4. **Trigger Condition**: Wait for a subsequent candle **body to close strictly below** this marked Open price.
5. **Validation**: Once the candle body closes below, **Bearish CISD is confirmed**.

---

## 3. Early CISD vs. Confirmed CISD

In both live discretionary trading and the Pine Script indicator, two stages of CISD exist:

| CISD State | Definition & Timing | Risk Profile | Best Use Case |
| :--- | :--- | :--- | :--- |
| **Early / Live CISD** | Triggers while C2 is **still actively forming** (intra-bar). Price sweeps C1 and breaks the opposing open before C2's HTF time finishes. | Higher reward, higher risk. If C2 expands further, the level can get invalidated. | Aggressive traders seeking tight stops right at the HTF wick turn. |
| **Confirmed CISD** | Triggers **after C2 has officially closed** as a valid sweep. C3 opens and breaks the CISD level, or respects the already-broken level. | High probability, conservative. C2 pivot is permanently locked in. | Standard rule-based execution for maximum win-rate. |

---

## 4. IC-CISD (Internal Change in State of Delivery)

Once the primary CISD occurs, price begins its C3 expansion. However, pullbacks will occur on lower timeframes:
* **IC-CISD** is an *internal* structural shift in the direction of the macro bias.
* When price retraces during C3, it creates micro counter-trend candles.
* When price breaks back in line with the main setup, an **IC-CISD** is generated.
* **Application**: Used for **re-entries, adding to winning positions (pyramiding), or entering if the initial C2 move was missed**.

---

## 5. Invalidation Rules

A CISD is immediately declared **INVALID** if:
1. After the CISD line is broken, price reverses and **closes beyond the C2 extreme** (the swing high for bearish, swing low for bullish).
2. The candle body fails to close beyond the level (wick only = rejection, not CISD).
3. More than 2 higher timeframe candles elapse without directional displacement.
