# Chapter 08: Indicator Guide & TradingView Setup

> **Previous**: [Chapter 07: Targets, Deviations & Risk](./07_targets_deviations_and_risk_management.md) | **Home**: [Main Index](./README.md)

---

## 1. Overview & Video Breakdown

This guide breaks down the custom TradingView indicator shown in TTrades' tutorial:  
**YouTube Video**: [Intro To TTrades Fractal Model [Indicator & Settings] (https://www.youtube.com/watch?v=CqMIh-Vvhbg)](https://www.youtube.com/watch?v=CqMIh-Vvhbg)

The open-source Pine Script v6 indicators that reproduce this system are located in your workspace:
* **Primary Fractal Model Indicator**: [`scripts/indicators/fractal_model.pine`](file:///c:/Projects/trading/scripts/indicators/fractal_model.pine)
* **Unified Multi-Timeframe Suite**: [`scripts/indicators/htf_suite.pine`](file:///c:/Projects/trading/scripts/indicators/htf_suite.pine)

---

## 2. Complete Settings Reference

Below is the exhaustive breakdown of each configuration section from the video and Pine Script code:

### A. General Settings (`grpModel`)
* **Alerts?** (`showAlerts`): Master switch for TradingView alerts. Must be turned ON before creating an alert.
* **Early CISD Alerts?** (`showEarlyCisdAlerts`): Triggers an alert when an intra-bar CISD forms during C2 before the HTF candle closes.
* **History** (`showHistory`): Number of past completed setups to keep drawn on chart (default: `1` to `3` to keep charts clean).
* **Bias** (`biasFilter`): `Neutral` (shows both bullish/bearish), `Bullish` (low sweeps only), `Bearish` (high sweeps only).
* **Fractal Alignment** (`modelType`):
  * `Auto`: Automatically selects the best HTF based on your current chart timeframe.
  * Presets: `1m-15m`, `5m-1H`, `15m-4H`, `1H-1D`, `4H-1W`.
  * `Custom`: Allows manual entry of custom LTF and HTF resolutions.
* **Early CISD** (`showEarlyCisd`): Toggles the visual dashed preview line of the pending CISD level.

---

### B. HTF Candles Panel (`grpCandles`)
* **HTF Candles** (`htfCandleCount`): Number of HTF candles to render on the chart edge (default: `4` to `5`).
* **Hide?** (`hideHtf`): Hides the candle preview if you prefer a minimalist chart.
* **Offset** (`candleOffsetIn`): Horizontal distance (bars) from the current price bar to the HTF candle cluster.
* **HTF Open** (`showHtfOpen`): Draws a continuous horizontal line across the chart at the opening price of the live HTF candle.
* **HTF Info & Countdown** (`showHtfTf`, `showHtfTimer`): Displays the timeframe name and active countdown timer (minutes/seconds until HTF candle closes).
* **O/C Time** (`showVlines`): Plots vertical dotted lines at the open and close timestamps of each HTF candle.
* **L/H Lines** (`showLH`): Extends horizontal lines from the high and low of the active HTF candle across your execution chart.

---

### C. Model Style & Drawings (`grpVisuals`)
* **Candle 1 Sweep** (`showSweep`): Draws the solid line marking the swept C1 high or low.
* **C2 / C3 / C4 Labels** (`showLabels`): Places clean text labels on the pivot bar (`C2`), the expansion bar (`C3`), and continuation (`C4`).
* **Bullish / Bearish CISD Lines** (`showBullCisd`, `showBearCisd`): Draws the key horizontal break line when the opposing candle open is violated.
* **Candle Equilibrium** (`showEQ`): Dotted line marking the 50% midpoint of the C2 candle.
* **T-Spot Box** (`showTSpot`): Draws the semi-transparent entry zone box between the C3 open and C2 wick midpoint.

---

### D. Orderblock Projections & Deviations (`grpStdDev`)
* **Enable Projections?** (`showStdDev`): Enables the Fibonacci standard deviation grid.
* **Deviations** (`stdDevInput`): `-1, -2, -2.5, -4, -4.5`.
* **Method** (`stdDevCalc`):
  * `Wick`: Measures from C2 extreme wick tip to CISD trigger bar (standard).
  * `Body`: Measures from C2 candle body close to CISD trigger bar.

---

### E. SMT Divergence Engine (`GRP_SMT`)
* **Show SMT** (`show_smt`): Plots SMT divergence markers and lines.
* **Comparison Symbol** (`smt_manualPair`): Defaults to `CME_MINI:MNQ1!` (when viewing ES) or `CME_MINI:ES1!` (when viewing NQ).
* **Inverse?** (`smt_pair1_inverse`): Turn ON when comparing negatively correlated assets like **DXY vs. EURUSD** or **VIX vs. SPX**.

---

### F. Info Table Settings (`grpDash`)
* **Show Dashboard?** (`tbl_show`): Small HUD table in the corner of your chart showing Symbol, Bias, Active Model Timeframe, Date, and Time.

---

## 3. How to Deploy to TradingView

1. Open your workspace file: [`scripts/indicators/fractal_model.pine`](file:///c:/Projects/trading/scripts/indicators/fractal_model.pine).
2. Copy the entire code (`Ctrl+A`, `Ctrl+C`).
3. Open **TradingView** in your browser or desktop app.
4. Click **Pine Editor** at the bottom of the screen.
5. Create a new blank script, paste the code, and click **Save**.
6. Click **Add to Chart**.
7. In the indicator settings:
   * For **Index Futures (NQ/ES)**: Set timeframe alignment to `5m-1H` or `15m-4H`. Turn on `SMT Divergence` and set the secondary pair to `ES1!` or `NQ1!`.
   * For **Forex (EURUSD/GBPUSD)**: Set timeframe alignment to `15m-4H` or `1H-1D`. Turn on `SMT Divergence` with `GBPUSD`.
