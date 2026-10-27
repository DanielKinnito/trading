# Chapter 06: Entry Models & Execution Playbook

> **Previous**: [Chapter 05: Timeframe Alignment & Bias](./05_timeframe_alignment_and_bias.md) | **Next**: [Chapter 07: Targets, Deviations & Risk](./07_targets_deviations_and_risk_management.md)

---

## 1. Executive Overview & Setup Pre-Conditions

Before looking for an entry, the baseline market structure **must already be established** on your chart:

```
  1. [ C1 ] High and Low are marked (Reference Liquidity).
  2. [ C2 ] Sweeps C1's High or Low and pulls back (Institutional Manipulation).
  3. [ BIAS ] Confirmed via HTF context or Pro Auto Bias.
```

Once the `C2` sweep occurs, you are preparing to trade the **expansion** (`C3` or continuation `C4`). Depending on market speed and your personal risk tolerance, TTrades' Fractal Model provides **Four Distinct Entry Models**.

---

## 2. Model 1: The CISD Body Break & Close (Momentum Confirmation Entry)

> *"I refuse to guess the bottom. I want the algorithm to prove to me that buyers have taken control before I risk capital."*

This is the most popular, high-win-rate entry model in the framework.

```
                                                                 [ ENTER HERE: On Body Close ]
                                                                             ┌───┐
                                                                             │   │
  ═══════════════════════════════════════════════════════════════════════════│───│════  BLUE CISD LINE
                                                                             │   │
                                                               ┌───┐  ┌───┐  │   │
                                                        ┌───┐  │   │  │   │  │   │
                                                 ┌───┐  │   │  │   │  │   │  └───┘
                                                 │   │  │   │  │   │  └───┘
  ───────────────────────────────────────────────│───│──└───┘──└───┘────────────────────  Top of C3 Box (Open)
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│░░░│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
  - - - - - - - - - - - - - - - - - - - - - - - -└───┘- - - - - - - - - - - - - - - - -  Dotted Line (50% EQ)
                                                   C3
```

### A. How It Works
1. **Identify the Trigger Line**:
   * The indicator draws a **Blue Horizontal Line** (for Bullish CISD) or a **Red Horizontal Line** (for Bearish CISD).
   * This line is mathematically defined as the **opening price of the opposing candle(s)** that delivered price into the `C2` sweep.
2. **The Waiting Period**:
   * Even if `C3` opens, if price is still trading *below* the blue line (for longs) or *above* the red line (for shorts), **YOU DO NOT ENTER YET**. You have zero confirmation.
3. **The Exact Trigger**:
   * Watch the 1-minute execution candle approaching the line.
   * You wait for that candle timer to reach `0:00` and for the **candle body to close strictly beyond the CISD line**.
   * A wick piercing the line does **NOT** count. The solid body must close past it.
4. **Order Execution**:
   * **Variant A (Immediate Market Order)**: The exact second the candle body closes across the line, click **Buy/Sell Market**.
   * **Variant B (The Retest Dip)**: Place a limit order on the CISD line. Frequently, the very next candle takes a quick 1–3 tick dip to test/mitigate the line before rocketing.
5. **Stop Loss (SL)**:
   * **Structural SL**: Placed 1–2 ticks beyond the extreme wick tip of **`C2`**.
   * **Aggressive SL**: Placed 1–2 ticks below the low of the specific candle that broke the CISD line.
6. **Pros & Cons**:
   * **Pros**: Highest win rate. Eliminates catching falling knives. Momentum is immediately on your side.
   * **Cons**: Slightly larger stop distance than a limit order.

---

## 3. Model 2: The T-Spot / Equilibrium Limit Entry (The Discount Hunter)

> *"I refuse to chase green candles. I want to buy at a wholesale discount inside the manipulation wick."*

This is the classic limit order model designed for maximum Risk-to-Reward (often 1:4 to 1:6+).

```
                             C3 Candle Opens
  ──────────────────────────────────┬──────────────────────────────────────── Top of Green Box (C3 Open)
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ THE T-SPOT BOX ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  <-- Wholesale Discount Zone
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
  - - - - - - - - - - - - - - - - - X - - - - - - - - - - - - - - - - - - -  Dotted Line (50% Equilibrium)
                                    │                                        [ BUY LIMIT ORDER PLACED HERE! ]
                                    │ Lower manipulation wick dips in,
                                    │ tags your order, and launches!
```

### A. How It Works
1. **The Candlestick Mechanics (AMD / Power of 3)**:
   * 95% of all expansion candles do not move straight to target from the open.
   * A bullish candle first dips *below its open* to form a lower wick (Accumulation $\rightarrow$ Manipulation) before expanding upward (Distribution).
2. **Anatomy of the T-Spot Box**:
   * **Upper Bound**: The **Opening price** of the `C3` candle.
   * **Lower Bound**: The **50% Equilibrium (midpoint)** of the preceding `C2` candle (`[C2 High + C2 Low] / 2`), rendered as the **dotted line**.
3. **Order Execution**:
   * As soon as `C3` opens and the green T-Spot box appears, place a **Buy Limit Order** sitting on the **dotted line** (or in the upper half of the box).
   * As minute 1, 2, or 3 dips into discount, your limit order gets filled passively.
4. **Stop Loss (SL)**:
   * **Tight Stop**: 1–2 ticks below the **dotted line** (the bottom of the T-Spot box). If price closes below that dotted line, the T-Spot failed.
   * **Structural Stop**: Below the lowest wick of **`C2`**.
5. **Pros & Cons**:
   * **Pros**: Incredible Risk-to-Reward. Enters at wholesale prices.
   * **Cons**: If market momentum is extraordinarily violent, price may only dip a few ticks and leave your limit order unfilled.

---

## 4. Model 3: The Micro-Structure Sniper (Fractal Inside a Fractal)

> *"I want the wholesale discount of the T-Spot, but I want lower-timeframe confirmation before I click buy."*

This is the hybrid model combining the safety of Model 1 with the discount pricing of Model 2.

```
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ 1. HTF Setup: 15m or 1H candle pulls into the T-Spot Box.                │
  │ 2. Drop to LTF: Switch to the 1-minute (or 15-second) chart.             │
  │ 3. Micro Confirmation: Look for a micro-sweep + micro-FVG inside the box.│
  │ 4. Execution: Enter on the micro CISD close.                             │
  └──────────────────────────────────────────────────────────────────────────┘
```

### A. How It Works
1. You identify a setup on the `5m-1H` or `1m-15m` model.
2. Price enters the shaded **T-Spot Box**.
3. Instead of placing a blind limit order, you zoom into the **1-minute chart inside the box**:
   * Watch for a 1-minute candle to take a tiny internal low.
   * Watch for an immediate 1-minute green candle to close with displacement, printing a micro Fair Value Gap (FVG).
4. **Order Execution**:
   * Enter Market Long on the close of that micro 1-minute green candle (or limit on the micro FVG).
5. **Stop Loss (SL)**:
   * Placed strictly below the micro swing low formed inside the box (often just 5–10 points on NQ!).
6. **Pros & Cons**:
   * **Pros**: Surgical precision. Allows larger position sizing due to ultra-tight invalidation.
   * **Cons**: Requires active screen concentration and rapid execution.

---

## 5. Model 4: The `C4` Trend Continuation Entry (The Second Chance)

> *"I was away from my desk when C2 swept and C3 exploded. How do I get into this running trend without buying the top?"*

This model protects traders from FOMO (Fear Of Missing Out).

```
                                  │ C3 Expansion Peak
                                ┌─┴─┐
                                │   │
  ──────────────────────────────│───│─────────────────────────────── Top of C4 Box (C4 Open)
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│░░░│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
  ░░░░░░░░░░░░░░░░░░░░░░░░░ THE C4 T-SPOT BOX ░░░░░░░░░░░░░░░░░░░░░░  <-- Secondary Pullback Zone
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│░░░│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
  - - - - - - - - - - - - - - - └───┘ - - - - - - - - - - - - - - -  Dotted Line (50% EQ of C3)
                                 C4
                                 [ Price dips in to test C3 midpoint, then expands to TP2! ]
```

### A. How It Works
1. **The Mistake to Avoid**:
   * When `C3` expands 60–100 points, retail traders panic and buy at the very top. Institutional algorithms then initiate a pullback, stopping them out.
2. **The Rule**:
   * Never buy the top of `C3`. **Wait for `C3` to close.**
3. **Anatomy of the `C4` Box**:
   * When `C3` ends, the new candle **`C4`** opens.
   * The indicator automatically draws the **`C4` T-Spot Box**.
   * The dotted line at the bottom is the **50% midpoint of the giant `C3` candle**.
4. **Order Execution**:
   * Price retraces from the high and dips down into the **`C4` green box**.
   * Enter long inside the box (either via limit order or after a 1m green rejection candle).
5. **Targets**:
   * Ride the continuation leg into the final macro standard deviation targets (**`-4.0` / `-4.5`**).
6. **Stop Loss (SL)**:
   * Placed below the low of the `C4` pullback wick (or below the C4 dotted Equilibrium line).

---

## 6. Master Comparison Matrix

| Model | Primary Trigger | Order Type | Confirmation | Typical RR | Best Used When... |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Model 1 (CISD Break)** | Candle body closes past Blue/Red line | Market on Close (or Retest Limit) | **Highest** (Full Body Confirmation) | 1:2 to 1:3.5 | You want zero ambiguity and momentum proof. |
| **Model 2 (T-Spot Limit)** | Price dips into 50% Equilibrium | Limit Order on Dotted Line | **Medium** (Assumes HTF POI holds) | **1:4 to 1:8+** | Clean trending days where you demand a discount. |
| **Model 3 (Micro Sniper)** | 1m FVG / CISD inside T-Spot box | Market on Micro Close | **High** (Multi-timeframe alignment) | **1:5 to 1:10+** | Scalping volatile index futures (NQ/ES). |
| **Model 4 (C4 Continuation)**| Pullback into C4 T-Spot box | Limit or Market inside Box | **Medium** (Trend Continuation) | 1:2 to 1:3 | You completely missed C2 and C3. |

---

## 7. The Invalidation Law & Risk Management

Regardless of which model you choose, the invalidation rules are absolute:

1. **The C2 Extreme Law**:
   * If price trades **even 1 tick beyond the C2 Extreme**, the entire setup is dead. Exit immediately. Never widen your stop loss.
2. **The 2-Trade Rule (OSOK)**:
   * Max 2 trades per session. If both lose, your read on the daily profile is flawed. Shut down the charts.
3. **Partial Profit Taking Protocol**:
   * At **`-1.0` to `-2.0` Standard Deviation**: Close 50% of the position and move Stop Loss to **Break-Even (BE)**.
   * At **`-2.0` to `-2.5` Standard Deviation**: Close another 30%–40% (Institutional Delivery Zone).
   * Leave 10% runner for **`-4.0`**.
