# TTrades Fractal Model (TTFM) Knowledge Base

> **Algorithmic Multi-Timeframe Price Delivery & Execution Framework**  
> *Synthesized from TTrades' Fractal Model Series, YouTube Educational Playlists, and Pine Script v6 Implementations.*

---

## Navigation & Curriculum

This documentation library breaks down the **TTrades Fractal Model** into modular, detailed chapters. Each chapter is self-contained with mechanical rules, visual schematics, algorithmic formulas, and execution checklists.

| Chapter | Title | Focus Area |
| :--- | :--- | :--- |
| **[Chapter 01](./01_foundational_concepts_and_market_delivery.md)** | **Foundational Concepts & Market Delivery** | ICT Fractality, Sweeps vs. Closes, Dealing Ranges, and Equilibrium (0.5). |
| **[Chapter 02](./02_the_c1_c2_c3_c4_fractal_sequence.md)** | **The C1–C2–C3–C4 Fractal Sequence** | The mechanical 4-candle cycle: Reference, Sweep/Pivot, Expansion, and Delivery. |
| **[Chapter 03](./03_cisd_change_in_state_of_delivery.md)** | **CISD (Change in State of Delivery)** | Mechanical orderflow shift, opposing candle opens, Early vs Confirmed CISD, IC-CISD. |
| **[Chapter 04](./04_points_of_interest_and_the_tspot.md)** | **Points of Interest (POI) & The T-Spot** | HTF POI validation, C2 Wick Midpoint, and the mathematical "T-Spot" entry zone. |
| **[Chapter 05](./05_timeframe_alignment_and_bias.md)** | **Timeframe Alignment & Bias Matrix** | Multi-timeframe pairs (HTF/MTF/LTF), Pro Auto Bias rules, and Quarterly Theory cycles. |
| **[Chapter 06](./06_entry_models_and_execution_playbook.md)** | **Entry Models & Execution Playbook** | OSOK framework, C3 Open entries, Retracement entries, Stop Loss placement, and Invalidation. |
| **[Chapter 07](./07_targets_deviations_and_risk_management.md)** | **Targets, Deviations & SMT Confluence** | Standard Deviation projections (-1, -2, -2.5, -4), Draw on Liquidity, and SMT Divergence. |
| **[Chapter 08](./08_indicator_guide_and_tradingview_setup.md)** | **Indicator Guide & TradingView Setup** | Detailed breakdown of the TTFM / Fractal Model [Pro+] Pine Script v6 indicator and settings. |

---

## Is the Fractal Model Within ICT?

### Yes — 100% Founded on Core ICT Principles
The question frequently arises because **TTrades** introduced distinct terminology like **C1, C2, C3, CISD, and T-Spot**. However, the **Fractal Model is directly derived from Michael J. Huddleston's Inner Circle Trader (ICT) concepts**:

```
                         ┌──────────────────────────────────────────────┐
                         │              ICT CORE ENGINE                 │
                         │  - Algorithmic Price Delivery (IPDA)         │
                         │  - Time & Price Fractality                   │
                         │  - Power of 3 (AMD)                          │
                         │  - Liquidity Sweeps & PD Arrays              │
                         └──────────────────────┬───────────────────────┘
                                                │
                                                ▼
                         ┌──────────────────────────────────────────────┐
                         │         TTRADES FRACTAL MODEL (TTFM)         │
                         │  - Transforms ICT fractality into 4 candles  │
                         │  - C1 = Prior Range / External Liquidity     │
                         │  - C2 = Liquidity Sweep / Judas Swing        │
                         │  - CISD = Shift in State of Delivery         │
                         │  - C3 = Power of 3 Distribution / Expansion  │
                         │  - C4 = Continuation / Target Mitigation     │
                         └──────────────────────────────────────────────┘
```

1. **Fractality of OHLC**:
   * ICT teaches that every candle on every timeframe contains an **Open, High, Low, and Close (OHLC)** that operates under the **Power of 3 (AMD: Accumulation, Manipulation, Distribution)**.
   * A daily candle’s wick is a lower timeframe liquidity run; its body is lower timeframe expansion.
   * TTrades formalizes this: **A sweep on a Higher Timeframe (C2 wick) is simply a Change in State of Delivery (CISD) and expansion on a Lower Timeframe (C3)**.

2. **Liquidity Sweeps & Market Structure Shifts (MSS)**:
   * In ICT, price sweeps a previous session or swing high/low (Liquidity Pool), taps an institutional PD Array (FVG, Orderblock), and reverses.
   * In TTFM, this exact sequence is coded mechanically: **C1 high/low swept by C2 $\rightarrow$ CISD triggered on LTF $\rightarrow$ Enter on C3**.

3. **Change in State of Delivery (CISD)**:
   * ICT defines CISD as the moment price closes past the opening price of the opposing candle sequence that delivered price into a PD array, confirming algorithmic delivery has flipped from Buy to Sell (or vice-versa).
   * TTrades made this the core objective trigger of his entire model, removing discretionary guesswork.

---

## Indicator Availability in this Workspace

The Pine Script v6 indicators for the **Fractal Model** and **HTF SUITE** are located directly in your workspace:
* **Fractal Model Indicator**: [`scripts/indicators/fractal_model.pine`](file:///c:/Projects/trading/scripts/indicators/fractal_model.pine)
* **Unified Multi-Timeframe Suite**: [`scripts/indicators/htf_suite.pine`](file:///c:/Projects/trading/scripts/indicators/htf_suite.pine)
* **Fractal Model + POI Engine**: [`scripts/indicators/fractal_poi.pine`](file:///c:/Projects/trading/scripts/indicators/fractal_poi.pine)
* **Liquidity Suite**: [`scripts/indicators/liquidity_suite.pine`](file:///c:/Projects/trading/scripts/indicators/liquidity_suite.pine)
