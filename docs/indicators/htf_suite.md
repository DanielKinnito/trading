# HTF Candle Projection Suite (v6)

<span class="badge-bullish">Pine Script v6</span>
<span class="badge-neutral">Multi-Timeframe</span>
<span class="badge-neutral">Zero Repaint</span>

> **A standalone multi-timeframe candle projector displaying 15m, 1H, 4H, and Daily candles with open lines, wick ranges, and live close countdown timers on your execution chart.**

---

## 1. What It Does

When trading on a 1-minute or 5-minute execution chart, flipping back and forth between multiple chart tabs wastes precious seconds. 

The **HTF Suite** projects the higher timeframe candles directly onto the right-hand margin of your chart:

```
[ Active 1m Candlestick Chart ]        |   [ HTF Projection Margin ]
                                       |
    Price is actively moving...        |      ┌───┐  <- Previous 1H Candle
                                       |      │   │
                                       |      └───┘
                                       |        │
                                       |      ┌───┐  <- Current 1H Candle
                                       |   ───│───│  <- Current 1H Open Line
                                       |      └───┘     Timer: (14:32 remaining)
```

---

## 2. Features

- **Candle Projection Count**: Customize how many completed HTF candles are rendered (from 3 up to 15).
- **Live Candle Open Line**: Projects a horizontal ray showing the exact opening price of the currently active HTF bar.
- **Bar Close Countdown Timer**: Displays minutes and seconds remaining until the higher timeframe candle closes.
- **Day of Week Stamps**: Labels each candle with the day of the week (Mon, Tue, Wed, Thu, Fri).
- **Pro Auto Bias Integration**: Colors the projected HTF candles green (bullish bias) or red (bearish bias).

---

## 3. Source Code Location

The source code is located in:

```
scripts/indicators/htf_suite.pine
```

[:octicons-mark-github-16: View Raw Script on GitHub](https://github.com/DanielKinnito/trading/blob/main/scripts/indicators/htf_suite.pine)
