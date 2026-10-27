# Chapter 05: Timeframe Alignment & Bias Matrix

> **Previous**: [Chapter 04: POI & The T-Spot](./04_points_of_interest_and_the_tspot.md) | **Next**: [Chapter 06: Entry Models & Execution Playbook](./06_entry_models_and_execution_playbook.md)

---

## 1. Top-Down Alignment Hierarchy

The Fractal Model relies on a strict **3-tier timeframe hierarchy**:

```
     ┌────────────────────────┐
     │  Higher Timeframe (HTF) │  ───►  Determines Bias & Macro Draw on Liquidity (DOL)
     └───────────┬────────────┘
                 │
                 ▼
     ┌────────────────────────┐
     │  Middle Timeframe (MTF) │  ───►  Identifies C1/C2 Setup & Key POI (Dealing Range)
     └───────────┬────────────┘
                 │
                 ▼
     ┌────────────────────────┐
     │  Lower Timeframe (LTF)  │  ───►  Executes on CISD, T-Spot & C3 Expansion
     └────────────────────────┘
```

---

## 2. Standard Timeframe Pairing Matrix

To avoid chart clutter and conflicting signals, TTrades organizes execution charts into pre-defined pairing sets:

| Trading Style | Higher Timeframe (Bias) | Middle Timeframe (Setup/C2) | Lower Timeframe (Execution/CISD) | Best Session |
| :--- | :--- | :--- | :--- | :--- |
| **Intraday (Standard)** | **Daily (1D)** | **1-Hour (1H)** | **5-Minute (5m)** | NY AM / London Open |
| **Intraday (Fast)** | **4-Hour (4H)** | **15-Minute (15m)** | **1-Minute (1m)** | NY AM (08:30–11:00) |
| **Scalping (Micro)** | **1-Hour (1H)** | **5-Minute (5m)** | **1-Minute (1m)** | NY Cash Open (09:30–10:30) |
| **Swing (Macro)** | **Weekly (1W)** | **Daily (1D)** | **1-Hour (1H)** | Multi-day holds |
| **Quarterly (ICT QT)** | **6-Hour (6H)** | **90-Minute (90m)** | **22.5-Minute / 3m** | Quarterly AMDX cycles |

---

## 3. The "Pro Auto Bias" Engine

In discretionary trading, deciding whether you are bullish or bearish can become subjective. TTrades designed the **Auto Bias** algorithm to remove emotion:

### The Bias Rules:
1. **Bullish Bias Trigger**:
   * The previous HTF candle swept a low and closed **bullish** (Close > Open).
   * Or price closed **above** the high of a previous HTF candle (Expansion run).
   * Under Bullish Bias, the model **only looks for Bullish C2 sweeps and Bullish CISD**.
2. **Bearish Bias Trigger**:
   * The previous HTF candle swept a high and closed **bearish** (Close < Open).
   * Or price closed **below** the low of a previous HTF candle (Expansion run).
   * Under Bearish Bias, the model **only looks for Bearish C2 sweeps and Bearish CISD**.
3. **Neutral Bias**:
   * Displays all valid setups in both directions (recommended on ranging or consolidation days).

---

## 4. HTF Candle Projection Panel

A distinctive feature of TTrades' indicator is the **HTF Candle Projection cluster** drawn on the right-hand margin of the lower timeframe chart:
* It renders the last 4 to 10 completed HTF candles directly alongside the active LTF price.
* Shows you at a glance:
  * Current HTF candle open line (`showHtfOpen`).
  * Time remaining until the current HTF candle closes (`showHtfTimer`).
  * Day of the week stamps (`showHtfStamps`).
* **Why this matters**: You never have to leave your 1-minute or 5-minute execution chart to know the exact status of the 1-hour or 4-hour candle!
