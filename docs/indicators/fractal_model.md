# TTrades Fractal Model [Pro+] (v6)

<span class="badge-bullish">Pine Script v6</span>
<span class="badge-neutral">Zero Repaint</span>
<span class="badge-neutral">Memory Managed</span>

> **The flagship institutional indicator recreating the complete 4-candle delivery cycle on TradingView.**

---

## 1. Key Technical Features

- **Strict Pine Script v6 Standard**: Written strictly using `//@version=6` with strong typing and zero deprecated functions.
- **Zero Repaint Architecture**: Multi-timeframe requests utilize `lookahead=barmerge.lookahead_off` and historical bar index offsets `[1]` to ensure historical replay matches live execution 100%.
- **Memory Management**: TradingView limits drawings to 500 instances. The script uses FIFO drawing queues (`array.push` and `array.shift` with `box.delete` and `line.delete`) to prevent script crashes on long sessions.
- **Dynamic CISD Engine**: Automatically identifies the opposing candle open benchmark and tracks body close confirmations in real time.
- **Automatic Standard Deviation Projections**: Plots `-1.0`, `-2.0`, `-2.5`, `-4.0`, and `-4.5` extensions instantly upon C2 confirmation.

---

## 2. Real Chart Presentation

![NAS100 4H Macro Execution](../assets/images/charts/nas100_4h_macro_run.png)
<div class="image-caption">Figure F.1: Fractal Model Pro+ running live on NAS100 with C2 sweep, CISD line, and Fibonacci extension targets.</div>

---

## 3. Inputs Reference Table

| Category | Input Name | Type | Options / Defaults | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Model Configuration** | `modelPreset` | Dropdown | `1m - 15m`, `1m - 1H`, `5m - 1H`, `15m - 4H`, `1H - Daily`, `Custom` | Automatically configures HTF resolution and display parameters. |
| **Model Configuration** | `htfResolution` | Timeframe | `15`, `60`, `240`, `D` | Timeframe used to calculate C1-C4 cycles when Custom is selected. |
| **Visual Markers** | `showPhases` | Boolean | `true` | Displays `C1`, `C2`, `C3`, `C4` text labels on the chart. |
| **CISD Settings** | `showCisdLine` | Boolean | `true` | Draws dynamic blue/red benchmark trigger lines. |
| **T-Spot Settings** | `showTSpot` | Boolean | `true` | Projects the shaded 50% equilibrium entry box during C3. |
| **HTF Projections** | `showHtfCandles` | Boolean | `true` | Overlays higher-timeframe candles on the right margin of the chart. |
| **Dashboard** | `showDashboard` | Boolean | `true` | Renders the real-time cycle status widget in the corner. |

---

## 4. Source Code Location

The complete, unabridged Pine Script v6 source code is available in the repository at:

```
scripts/indicators/fractal_model.pine
```

[:octicons-mark-github-16: View Raw Script on GitHub](https://github.com/DanielKinnito/trading/blob/main/scripts/indicators/fractal_model.pine)
