# Timeframe Matrix & Asset Guide

> **Recommended combinations of Higher Timeframe (HTF), Middle Timeframe (MTF), and Lower Timeframe (LTF) for every asset class based on TTrades' native ratios.**

---

## 1. Master Timeframe Matrix

TTrades strictly enforces proportional multi-timeframe ratios (**5:1 to 16:1**) to ensure that lower-timeframe execution triggers align with higher-timeframe expansion legs without lagging behind:

| Asset Class | Execution Style | Primary Model Preset | Higher Timeframe (Bias / Context) | Middle Timeframe (C1 / C2 Setup) | Lower Timeframe (Execution / CISD) | Recommended Session |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **EURUSD (Forex)** | **1m Scalp / Day Trade** | `1m - 15m Model` | **1-Hour (1H)** | **15-Minute (15m)** | **1-Minute (1m)** | London Open (02:00–05:00) |
| **GBPUSD (Forex)** | **1m Scalp / Day Trade** | `1m - 15m Model` | **1-Hour (1H)** | **15-Minute (15m)** | **1-Minute (1m)** | London Open (02:00–05:00) |
| **EURUSD / GBPUSD** | **Standard Intraday** | `5m - 1H Model` | **4-Hour (4H)** | **1-Hour (1H)** | **5-Minute (5m)** | London & NY AM |
| **NQ (Nasdaq Futures)** | **Fast Scalp** | `1m - 15m Model` | **1-Hour (1H)** | **15-Minute (15m)** | **1-Minute (1m)** | NY AM (08:30–11:00) |
| **ES (S&P 500 Futures)**| **Fast Scalp** | `1m - 15m Model` | **1-Hour (1H)** | **15-Minute (15m)** | **1-Minute (1m)** | NY AM (08:30–11:00) |
| **Gold (XAUUSD)** | **Intraday** | `5m - 1H Model` | **Daily (1D)** | **1-Hour (1H)** | **5-Minute (5m)** | London & NY AM |
| **Bitcoin / Crypto** | **Trend Day** | `15m - 4H Model` | **Daily (1D)** | **4-Hour (4H)** | **15-Minute (15m)** | 24/7 Volatility Windows |
| **Swing Trading** | **Macro Swing** | `1H - Daily Model` | **Weekly (1W)** | **Daily (1D)** | **1-Hour (1H)** | Daily Settlement |

---

## 2. Why "1m - 1H" is Mathematically Invalid for Model 1

!!! danger "The 60:1 Timeframe Ratio Trap"
    A common beginner error is trying to pair a **1-Hour candle as C2** with a **1-Minute chart for Model 1 (candle close)** execution:
    
    * **The 60-Minute Lag**: Waiting 60 minutes for a 1-Hour candle to close means **60 individual 1-minute bars have already elapsed**.
    * **Premature Delivery**: In London Open Forex, the entire Asian range sweep and directional run often takes only **25 to 40 minutes**.
    * By the time the 1-Hour candle closes, the move has **already reached its opposing Draw on Liquidity (DOL)**.
    * When the next 1-Hour candle (C3) opens, institutional orderflow takes profits and retraces, causing traders who wait for the 1H close to enter at the very ceiling/floor right as price reverses!

---

## 3. Official TTrades Model Presets Explained

### 1m - 15m Model (The London & NY 1-Minute Execution Standard)
- **Target Audience**: Active Forex and Index traders who execute on the **1-minute chart**.
- **The Mechanics**:
  - **C1 Reference**: Prior session bounds (e.g. Asian Session High and Low).
  - **C2 Setup**: A single **15-minute candle** sweeps the Asian Low/High and closes back inside.
  - **Confirmation Speed**: C2 confirms in **15 minutes** (e.g., at 02:15, 02:30, 03:15, or 03:30 NY time).
  - **1m Execution**: Price is still right near the extreme. The 1m CISD benchmark line is only 3–6 pips away. The 1m body close triggers Model 1 immediately with a tight 6–8 pip stop loss.
  - **Trade Duration**: **15 to 45 minutes**.

### 5m - 1H Model (The Standard Forex Intraday Standard)
- **Target Audience**: Traders who want a calmer chart without 1-minute noise.
- **The Mechanics**:
  - **C2 Setup**: The **1-Hour candle** sweeps the Asian session or key level and closes back inside.
  - **5m Execution**: As the next 1-Hour candle opens, you execute on the **5-minute chart** (12:1 ratio), looking for a 5m CISD body close or 5m FVG retest.
  - **Stop Loss**: 12 to 18 pips below the 1-Hour sweep low.
  - **Trade Duration**: **1 to 3 hours**.

### 15m - 4H Model (Full-Day Trend Runs)
- **Target Audience**: Full-day intraday trend traders (NQ, ES, Gold).
- **The Mechanics**:
  - Captures the massive 4-hour directional expansion leg.
  - Setup candle is the 4H bar; execution is confirmed on the 15-minute chart (16:1 ratio).
  - Setups are less frequent but yield 80–150+ points on index futures.
