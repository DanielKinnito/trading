# Model 1: CISD Breakout Close Entry

<span class="tt-badge-bull">High Probability</span>
<span class="tt-badge-neutral">Confirmation Style</span>
<span class="tt-badge-neutral">Win-Rate: 70%+</span>

> *"I refuse to guess the bottom. I want the algorithm to prove to me that buyers have taken control before I risk capital."*

---

## Visual Setup Schematic

Below is the photorealistic chart breaking down Model 1 execution with exact benchmark origin alignment and confirmed candle body close:

![Model 1 CISD Breakout Close](../assets/images/models/model1_cisd_breakout.png)
<div class="image-caption">Figure M1.1: Complete anatomical breakdown of Model 1 execution on confirmed candle body close above CISD.</div>

---

## 1. What You See on the Indicator

When running the **Fractal Model Pro+ [v6]** indicator on your chart, Model 1 presents the following visual sequence:

1. **C1 Range Marked**: Dotted bounds marking prior session or swing high/low.
2. **C2 Sweep Detected**: Price wicks past C1 into an HTF discount POI, and the indicator places a label at the extreme.
3. **CISD Benchmark Line Appears**: A solid horizontal ray originates strictly from the **`Open` of the first opposing candle** that led into the C2 extreme:
    - **Blue Line**: Bullish CISD benchmark level (`Open` of the first down-close candle into C2 low).
    - **Red Line**: Bearish CISD benchmark level (`Open` of the first up-close candle into C2 high).
4. **Dashboard State**: The live HUD changes status from `C2 Sweep` to `Watching CISD Level`.

---

## 2. Step-by-Step Execution Rules

### Bullish Execution:
1. **Pre-condition**: C2 sweeps sellside liquidity (SSL) into an HTF Point of Interest (FVG or Orderblock) and prints a rejection wick.
2. **Watch the Benchmark Origin**: Verify the blue CISD line originates at the `Open` of the first bearish candle into the C2 low.
3. **Wait for Candle Close**: Watch the 1-minute candle timer countdown to `0:00`.
4. **Trigger**: The candle **body must close strictly ABOVE the blue line**.
5. **Entry**:
    - **Market Order**: Click Buy Market the exact second the candle closes.
    - **Retest Limit**: Place a limit buy order directly on the blue line. Often the next candle dips 1-2 ticks to touch the line.
6. **Stop Loss**: 1-2 ticks below the lowest wick tip of **C2**.
7. **Take Profit**:
    - **TP1 (-1.0 Ext / BSL)**: Take 50% partial profits and move stop loss to Break-Even.
    - **TP2 (-2.0 to -2.5 Ext)**: Take 40% profits.
    - **Runner (-4.0 Ext)**: Leave 10% runner.

---

## 3. Wick Rejection Trap vs. Confirmed Close

Below is the technical deep dive demonstrating why wick probes fail and how true body close confirmation looks on institutional orderflow:

![CISD Deep Dive Anatomy](../assets/images/charts/cisd_anatomy_deep_dive.png)
<div class="image-caption">Figure M1.2: Scenario A (Wick Rejection Trap / Invalid) vs Scenario B (Solid Candle Body Close / Confirmed CISD).</div>

---

## 4. Invalidation & Common Mistakes

!!! danger "Never Enter on a Wick Probe!"
    If a candle wicks through the blue CISD line by 10 points but pulls back and closes *below* the line, **this is NOT an entry**. Wicks without body closes represent liquidity rejection, and price will frequently drop lower to take out the C2 low!

!!! warning "Invalidation Stop"
    If price breaks the CISD line but subsequently rolls over and pierces the C2 extreme by even 1 tick, the setup is **DEAD**. Close the trade immediately. Never hold through an invalidation.
