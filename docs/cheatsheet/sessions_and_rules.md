# Session Times & Daylight Saving Rules

> **Quick reference guide for global session killzones, key macros, and Daylight Saving Time (DST) desynchronization shifts.**

---

## 1. Standard Session Killzones (New York Time)

All algorithmic delivery is calculated in **New York Time (`America/New_York`)**:

| Session / Event | New York Time | UTC Time | London Time | Ethiopia / East Africa (UTC+3) | Best Assets |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **NY Midnight Open** | 00:00 | 05:00 UTC | 05:00 | 07:00 AM | Benchmark price |
| **London Open Killzone** | 02:00 – 05:00 | 07:00 – 10:00 UTC | 07:00 – 10:00 | 09:00 AM – 12:00 PM | EURUSD, GBPUSD |
| **London Macro** | 02:30 – 03:00 | 07:30 – 08:00 UTC | 07:30 – 08:00 | 09:30 AM – 10:00 AM | Asian sweep reversal |
| **NY AM Open Killzone** | 08:30 – 11:00 | 13:30 – 16:00 UTC | 13:30 – 16:00 | 03:30 PM – 06:00 PM | NQ, ES, Gold, US30 |
| **NY Cash Equity Open** | 09:30 | 14:30 UTC | 14:30 | 04:30 PM | Index opening bell |
| **Key Morning Macro** | 09:50 – 10:10 | 14:50 – 15:10 UTC | 14:50 – 15:10 | 04:50 PM – 05:10 PM | Primary reversal / trend run |
| **NY PM Killzone** | 13:30 – 16:00 | 18:30 – 21:00 UTC | 18:30 – 21:00 | 08:30 PM – 11:00 PM | Afternoon delivery |

---

## 2. Daylight Saving Time (DST) Desynchronization Week

Twice every year, international daylight saving rules cause a **1-week or 2-week time difference**:
- **Fall (Late October / Early November)**: Europe ends British Summer Time (BST) / Central European Summer Time (CEST) on the last Sunday of October, while the United States does not fall back until the first Sunday of November.
- **Spring (March)**: The United States springs forward 2-3 weeks before Europe.

### What Happens During the Fall DST Gap Week:
During this week:
- **London Session in New York Time**: Shifts by 1 hour to **03:00 – 06:00 NY Time** (or 03:00–07:00).
- **London Session in Local Ethiopia Time**: The physical London morning does not change; it opens at 07:00 London Time. However, relative to New York clocks, London starts 1 hour later (at 03:00 NY time instead of 02:00 NY time).
- **C2 Candle Alignment**: For London session traders using the 1-hour chart, the C2 manipulation candle during this week is the **03:00 – 04:00 candle**, rather than the standard 02:00 – 03:00 candle!
- **NY Cash Open (09:30 NY)**: Still occurs at 09:30 NY Time (which aligns to 04:30 PM in Ethiopia).

---

## 3. The 3 Macro Trading Windows

TTrades and ICT emphasize three specific 20-minute macro windows where algorithms inject high-velocity liquidity:

1. **09:50 – 10:10 NY Time**: The ultimate morning macro. If a C2 sweep occurs right before or during this window, expect explosive C3 expansion.
2. **10:50 – 11:10 NY Time**: Midday reversal or high-of-day / low-of-day lock.
3. **13:50 – 14:10 NY Time**: Afternoon continuation macro.
