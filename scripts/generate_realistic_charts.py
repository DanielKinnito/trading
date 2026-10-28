"""
High-Fidelity TradingView Realistic Chart Generator - Enhanced Edition
Creates photorealistic, high-resolution (1440x810 16:9 HD) TradingView light-theme chart graphics.
"""

import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs("docs/assets/images/models", exist_ok=True)
os.makedirs("docs/assets/images/indicator", exist_ok=True)
os.makedirs("docs/assets/images/charts", exist_ok=True)

TV_BG = (255, 255, 255)
TV_PANEL_BG = (248, 250, 252)
TV_GRID = (241, 245, 249)
TV_BORDER = (226, 232, 240)
TV_TEXT_MAIN = (15, 23, 42)
TV_TEXT_MUTED = (100, 116, 139)
TV_TEXT_LIGHT = (148, 163, 184)

TV_BULL_BODY = (8, 153, 129)       # TradingView Emerald Green
TV_BULL_WICK = (8, 153, 129)
TV_BEAR_BODY = (242, 54, 69)       # TradingView Crimson Red
TV_BEAR_WICK = (242, 54, 69)

TV_CISD_BLUE = (37, 99, 235)       # Royal Blue
TV_CISD_RED = (220, 38, 38)
TV_TSPOT_GREEN = (220, 252, 231)
TV_TSPOT_BORDER = (22, 163, 74)
TV_PREMIUM_RED = (254, 226, 226)
TV_FIB_PURPLE = (124, 58, 237)
TV_ORANGE_RUN = (234, 88, 12)

def get_font(size=13, bold=False):
    candidates = [
        "C:\\Windows\\Fonts\\segoeuib.ttf" if bold else "C:\\Windows\\Fonts\\segoeui.ttf",
        "C:\\Windows\\Fonts\\arialbd.ttf" if bold else "C:\\Windows\\Fonts\\arial.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return ImageFont.load_default()

class RealisticChartCanvas:
    def __init__(self, width=1440, height=810, symbol="NQ1!", timeframe="1m", market="NASDAQ 100 E-MINI FUTURES • CME", decimals=2):
        self.w = width
        self.h = height
        self.symbol = symbol
        self.tf = timeframe
        self.market = market
        self.decimals = decimals
        
        self.top_bar_h = 56
        self.bottom_bar_h = 36
        self.right_axis_w = 105
        
        self.chart_x1 = 0
        self.chart_y1 = self.top_bar_h
        self.chart_x2 = self.w - self.right_axis_w
        self.chart_y2 = self.h - self.bottom_bar_h
        
        self.img = Image.new("RGBA", (self.w, self.h), TV_BG)
        self.draw = ImageDraw.Draw(self.img)
        
        self.min_price = 0.0
        self.max_price = 100.0
        
    def setup_price_range(self, min_p, max_p):
        self.min_price = min_p
        self.max_price = max_p
        
    def price_to_y(self, price):
        ratio = (price - self.min_price) / (self.max_price - self.min_price)
        return self.chart_y2 - ratio * (self.chart_y2 - self.chart_y1)
        
    def draw_background_and_grid(self, price_step=10.0, time_labels=None):
        p = self.min_price
        while p <= self.max_price + (price_step * 0.1):
            y = self.price_to_y(p)
            if self.chart_y1 <= y <= self.chart_y2:
                self.draw.line([(self.chart_x1, y), (self.chart_x2, y)], fill=TV_GRID, width=1)
                price_str = f"{p:,.{self.decimals}f}"
                self.draw.text((self.chart_x2 + 8, y - 7), price_str, fill=TV_TEXT_MUTED, font=get_font(11))
            p += price_step
            
        if time_labels:
            for x, t_str in time_labels:
                self.draw.line([(x, self.chart_y1), (x, self.chart_y2)], fill=TV_GRID, width=1)
                self.draw.text((x - 16, self.chart_y2 + 8), t_str, fill=TV_TEXT_MUTED, font=get_font(11))
                
        self.draw.line([(self.chart_x2, self.chart_y1), (self.chart_x2, self.chart_y2)], fill=TV_BORDER, width=1)
        self.draw.line([(self.chart_x1, self.chart_y2), (self.w, self.chart_y2)], fill=TV_BORDER, width=1)
        
        font_wm = get_font(68, bold=True)
        wm_text = f"{self.symbol} {self.tf}"
        self.draw.text((self.chart_x1 + 60, self.chart_y1 + 80), wm_text, fill=(241, 245, 249), font=font_wm)
        
    def draw_top_bar(self, cur_price="20,457.25", change="+18.50 (+0.09%)", badge_txt="TTrades Fractal Model Pro+ [v6]"):
        self.draw.rectangle([(0, 0), (self.w, self.top_bar_h)], fill=TV_PANEL_BG)
        self.draw.line([(0, self.top_bar_h), (self.w, self.top_bar_h)], fill=TV_BORDER, width=1)
        
        self.draw.text((24, 16), self.symbol, fill=TV_TEXT_MAIN, font=get_font(16, bold=True))
        
        self.draw.rounded_rectangle([(92, 16), (128, 40)], radius=4, fill=(238, 242, 255), outline=TV_CISD_BLUE, width=1)
        self.draw.text((100, 19), self.tf, fill=TV_CISD_BLUE, font=get_font(12, bold=True))
        
        self.draw.text((142, 18), self.market, fill=TV_TEXT_MUTED, font=get_font(12))
        
        # Center-right price info
        self.draw.text((self.w - 530, 18), f"Live: {cur_price}", fill=TV_BULL_BODY, font=get_font(14, bold=True))
        self.draw.text((self.w - 410, 18), change, fill=TV_BULL_BODY, font=get_font(13))
        
        # Indicator badge positioned safely
        badge_w = 210
        badge_x1 = self.w - badge_w - 24
        self.draw.rounded_rectangle([(badge_x1, 12), (self.w - 24, 44)], radius=6, fill=TV_CISD_BLUE)
        self.draw.text((badge_x1 + 12, 19), badge_txt, fill=(255, 255, 255), font=get_font(11, bold=True))

    def draw_candle(self, x, open_p, high_p, low_p, close_p, width=16):
        is_bull = close_p >= open_p
        body_col = TV_BULL_BODY if is_bull else TV_BEAR_BODY
        wick_col = TV_BULL_WICK if is_bull else TV_BEAR_WICK
        
        y_open = self.price_to_y(open_p)
        y_close = self.price_to_y(close_p)
        y_high = self.price_to_y(high_p)
        y_low = self.price_to_y(low_p)
        
        center_x = x + width // 2
        self.draw.line([(center_x, y_high), (center_x, y_low)], fill=wick_col, width=2)
        
        top = min(y_open, y_close)
        bottom = max(y_open, y_close)
        if bottom - top < 2:
            bottom = top + 2
        self.draw.rectangle([(x, top), (x + width, bottom)], fill=body_col, outline=body_col)

    def draw_active_price_pill(self, price, is_bull=True):
        y = self.price_to_y(price)
        col = TV_BULL_BODY if is_bull else TV_BEAR_BODY
        
        self.draw.line([(self.chart_x1, y), (self.chart_x2, y)], fill=col, width=1)
        
        pill_x1 = self.chart_x2 + 2
        pill_y1 = y - 11
        pill_x2 = self.w - 6
        pill_y2 = y + 11
        self.draw.rounded_rectangle([(pill_x1, pill_y1), (pill_x2, pill_y2)], radius=4, fill=col)
        price_str = f"{price:,.{self.decimals}f}"
        self.draw.text((pill_x1 + 6, pill_y1 + 2), price_str, fill=(255, 255, 255), font=get_font(11, bold=True))

    def draw_dashboard_widget(self, x=1050, y=75, asset="NQ1! (NASDAQ)", model="1m - 15m Model", phase="C3 Active", cisd_status="Body Close Confirmed"):
        w = 265
        h = 150
        self.draw.rounded_rectangle([(x, y), (x + w, y + h)], radius=8, fill=(255, 255, 255), outline=TV_BORDER, width=1)
        self.draw.rectangle([(x, y), (x + w, y + 32)], fill=(241, 245, 249))
        self.draw.line([(x, y + 32), (x + w, y + 32)], fill=TV_BORDER, width=1)
        self.draw.text((x + 14, y + 8), "TTFM Pro+ Engine [Active]", fill=TV_TEXT_MAIN, font=get_font(12, bold=True))
        
        rows = [
            ("Asset:", asset),
            ("Active Model:", model),
            ("Fractal Phase:", phase),
            ("CISD Status:", cisd_status),
        ]
        cur_y = y + 42
        for lbl, val in rows:
            self.draw.text((x + 14, cur_y), lbl, fill=TV_TEXT_MUTED, font=get_font(11))
            val_col = TV_CISD_BLUE if "CISD" in lbl or "Phase" in lbl else TV_TEXT_MAIN
            self.draw.text((x + 105, cur_y), val, fill=val_col, font=get_font(11, bold=True))
            cur_y += 26

# =========================================================================
# 1. Model 1 Chart: Precise CISD Origin from Benchmark Candle Open
# =========================================================================
def build_model_1_chart():
    chart = RealisticChartCanvas(1440, 810, "NQ1!", "1m", "NASDAQ 100 E-MINI • CME", decimals=2)
    chart.setup_price_range(20410.0, 20490.0)
    
    time_labels = [
        (150, "09:30"), (350, "09:40"), (550, "09:50"), (750, "10:00"), (950, "10:10"), (1150, "10:20")
    ]
    chart.draw_background_and_grid(price_step=10.0, time_labels=time_labels)
    chart.draw_top_bar(cur_price="20,482.50", change="+46.50 (+0.23%)")
    
    benchmark_open_price = 20452.00
    c2_low_price = 20422.00
    c1_low_price = 20434.00
    
    candles_data = [
        (120, 20460.0, 20468.0, 20455.0, 20465.0),
        (150, 20465.0, 20467.0, 20448.0, 20450.0),
        (180, 20450.0, 20456.0, 20440.0, 20442.0),
        (210, 20442.0, 20446.0, 20434.0, 20436.0),
        (240, 20436.0, 20448.0, 20435.0, 20445.0),
        # Benchmark Candle (Candle 5)
        (280, 20452.0, 20454.0, 20438.0, 20440.0), # Benchmark Candle! Open = 20452.00
        (310, 20440.0, 20442.0, 20430.0, 20432.0),
        (340, 20432.0, 20435.0, 20426.0, 20428.0),
        # C2 Sweep Candle (Candle 8)
        (370, 20428.0, 20432.0, 20422.0, 20430.0),
        # Reversal into C3
        (410, 20430.0, 20442.0, 20428.0, 20440.0),
        (440, 20440.0, 20448.0, 20438.0, 20446.0),
        (470, 20446.0, 20451.0, 20444.0, 20450.0),
        # CISD Breakout Candle (Candle 12)
        (500, 20450.0, 20462.0, 20448.0, 20460.0),
        # Extension Candles
        (540, 20460.0, 20469.0, 20458.0, 20468.0),
        (575, 20468.0, 20475.0, 20466.0, 20474.0),
        (610, 20474.0, 20484.0, 20472.0, 20482.0),
        (645, 20482.0, 20488.0, 20480.0, 20486.0),
    ]
    for c in candles_data:
        chart.draw_candle(c[0], c[1], c[2], c[3], c[4], width=18)
        
    d = chart.draw
    
    # C1 Low
    c1_low_y = chart.price_to_y(c1_low_price)
    d.line([(200, c1_low_y), (420, c1_low_y)], fill=TV_TEXT_LIGHT, width=1)
    d.text((120, c1_low_y - 18), "C1 Range Low (Sell-Side Liquidity)", fill=TV_TEXT_MUTED, font=get_font(11))
    
    # C2 Sweep Low
    c2_low_y = chart.price_to_y(c2_low_price)
    d.line([(360, c2_low_y), (680, c2_low_y)], fill=TV_BEAR_BODY, width=2)
    d.rounded_rectangle([(360, c2_low_y + 12), (480, c2_low_y + 36)], radius=4, fill=(254, 226, 226), outline=TV_BEAR_BODY, width=1)
    d.text((370, c2_low_y + 16), "C2 Sweep Low", fill=TV_BEAR_BODY, font=get_font(11, bold=True))
    d.text((500, c2_low_y + 16), "STOP LOSS (1 Tick Below C2 Extreme)", fill=TV_BEAR_BODY, font=get_font(11, bold=True))
    
    # CISD Benchmark Ray originating at Candle 5 Open
    cisd_y = chart.price_to_y(benchmark_open_price)
    benchmark_x = 280
    breakout_x = 518
    
    d.line([(benchmark_x, cisd_y), (980, cisd_y)], fill=TV_CISD_BLUE, width=3)
    d.ellipse([(benchmark_x - 5, cisd_y - 5), (benchmark_x + 5, cisd_y + 5)], fill=TV_CISD_BLUE, outline=(255, 255, 255), width=2)
    
    d.rounded_rectangle([(benchmark_x - 140, cisd_y - 42), (benchmark_x + 75, cisd_y - 14)], radius=4, fill=(238, 242, 255), outline=TV_CISD_BLUE, width=1)
    d.text((benchmark_x - 132, cisd_y - 36), "Benchmark Candle Open (CISD Origin: 20,452.00)", fill=TV_CISD_BLUE, font=get_font(10, bold=True))
    
    # Breakout Close Trigger Annotation
    break_close_y = chart.price_to_y(20460.0)
    d.ellipse([(breakout_x - 5, break_close_y - 5), (breakout_x + 5, break_close_y + 5)], fill=TV_BULL_BODY, outline=(255, 255, 255), width=2)
    
    callout_box = [(breakout_x + 30, break_close_y - 45), (breakout_x + 380, break_close_y + 20)]
    d.rounded_rectangle(callout_box, radius=6, fill=(240, 253, 244), outline=TV_BULL_BODY, width=2)
    d.text((breakout_x + 44, break_close_y - 38), "MODEL 1 CONFIRMED ENTRY TRIGGER", fill=TV_BULL_BODY, font=get_font(12, bold=True))
    d.text((breakout_x + 44, break_close_y - 18), "1-Minute Candle Body Closes STRICTLY Above CISD Line", fill=TV_TEXT_MAIN, font=get_font(11))
    d.text((breakout_x + 44, break_close_y - 1), f"Entry Price: 20,460.00 | Benchmark: {benchmark_open_price:,.2f}", fill=TV_TEXT_MUTED, font=get_font(10))
    d.line([(breakout_x, break_close_y), (breakout_x + 30, break_close_y - 15)], fill=TV_BULL_BODY, width=2)
    
    # Targets
    tp1_y = chart.price_to_y(20468.0)
    tp2_y = chart.price_to_y(20482.0)
    
    d.line([(550, tp1_y), (1030, tp1_y)], fill=TV_TSPOT_BORDER, width=2)
    d.text((690, tp1_y - 16), "TP1: C1 High / BSL Purged (-1.0 Std)", fill=TV_TSPOT_BORDER, font=get_font(11, bold=True))
    
    d.line([(620, tp2_y), (1030, tp2_y)], fill=TV_TSPOT_BORDER, width=2)
    d.text((690, tp2_y - 16), "TP2: Institutional Target (-2.0 Std)", fill=TV_TSPOT_BORDER, font=get_font(11, bold=True))
    
    chart.draw_active_price_pill(20482.50, is_bull=True)
    chart.draw_dashboard_widget(1040, 75, "NQ1! (NASDAQ)", "1m - 15m Model", "C3 Expansion", "Body Close Shift Confirmed")
    chart.img.save("docs/assets/images/models/model1_cisd_breakout.png", "PNG")

# =========================================================================
# 2. Model 2 Chart: 50% T-Spot Equilibrium Limit Order Execution
# =========================================================================
def build_model_2_chart():
    chart = RealisticChartCanvas(1440, 810, "EURUSD", "1m", "EURO / US DOLLAR • FOREX COM • LONDON OPEN", decimals=5)
    chart.setup_price_range(1.08100, 1.08500)
    
    time_labels = [
        (150, "02:30"), (350, "02:45"), (550, "03:00"), (750, "03:15"), (950, "03:30"), (1150, "03:45")
    ]
    chart.draw_background_and_grid(price_step=0.00050, time_labels=time_labels)
    chart.draw_top_bar(cur_price="1.08442", change="+0.00210 (+0.19%)")
    
    c2_low_p = 1.08160
    c3_open_p = 1.08320
    tspot_50_p = 1.08240
    tp_p = 1.08450
    
    candles_data = [
        (130, 1.08360, 1.08380, 1.08310, 1.08320),
        (165, 1.08320, 1.08340, 1.08260, 1.08270),
        # Benchmark down-close candle
        (200, 1.08300, 1.08310, 1.08220, 1.08230), # Benchmark Open = 1.08300
        (235, 1.08230, 1.08250, 1.08180, 1.08190),
        (270, 1.08190, 1.08210, 1.08160, 1.08180), # C2 Sweep of Asian Low
        # Reversal & CISD Breakout
        (310, 1.08180, 1.08260, 1.08170, 1.08250),
        (345, 1.08250, 1.08340, 1.08240, 1.08320), # Closes above 1.08300
        # C3 Pullback into 50% T-Spot Box
        (385, 1.08320, 1.08330, 1.08270, 1.08280),
        (420, 1.08280, 1.08285, 1.08238, 1.08250), # Taps 1.08240 (50% T-Spot Filled!)
        (455, 1.08250, 1.08310, 1.08245, 1.08300),
        # Expansion
        (495, 1.08300, 1.08370, 1.08290, 1.08365),
        (535, 1.08365, 1.08410, 1.08355, 1.08405),
        (575, 1.08405, 1.08460, 1.08400, 1.08450),
    ]
    for c in candles_data:
        chart.draw_candle(c[0], c[1], c[2], c[3], c[4], width=18)
        
    d = chart.draw
    
    cisd_y = chart.price_to_y(1.08300)
    d.line([(200, cisd_y), (850, cisd_y)], fill=TV_CISD_BLUE, width=2)
    d.ellipse([(195, cisd_y - 4), (205, cisd_y + 4)], fill=TV_CISD_BLUE)
    d.text((120, cisd_y - 18), "Benchmark Open (CISD Level: 1.08300)", fill=TV_CISD_BLUE, font=get_font(10, bold=True))
    
    c2_y = chart.price_to_y(c2_low_p)
    d.line([(250, c2_y), (750, c2_y)], fill=TV_BEAR_BODY, width=2)
    d.text((250, c2_y + 12), "C2 Swing Low (Asian Low Swept: 1.08160)", fill=TV_BEAR_BODY, font=get_font(11, bold=True))
    
    c3_open_y = chart.price_to_y(c3_open_p)
    tspot_50_y = chart.price_to_y(tspot_50_p)
    
    box_x1 = 375
    box_x2 = 620
    
    overlay = Image.new("RGBA", (chart.w, chart.h), (255, 255, 255, 0))
    d_ov = ImageDraw.Draw(overlay)
    d_ov.rectangle([(box_x1, tspot_50_y), (box_x2, c2_y)], fill=(220, 252, 231, 140))
    d_ov.rectangle([(box_x1, c3_open_y), (box_x2, tspot_50_y)], fill=(254, 226, 226, 80))
    chart.img = Image.alpha_composite(chart.img, overlay)
    d = ImageDraw.Draw(chart.img)
    
    d.rectangle([(box_x1, c3_open_y), (box_x2, c2_y)], outline=TV_TSPOT_BORDER, width=1)
    d.line([(box_x1, tspot_50_y), (box_x2 + 250, tspot_50_y)], fill=TV_TSPOT_BORDER, width=2)
    d.text((box_x2 + 20, tspot_50_y - 18), "50% T-Spot (Equilibrium Limit Order Level: 1.08240)", fill=TV_TSPOT_BORDER, font=get_font(11, bold=True))
    
    d.text((box_x1 + 12, tspot_50_y + 18), "WHOLESALE DISCOUNT ZONE (<50%)", fill=TV_TSPOT_BORDER, font=get_font(10, bold=True))
    d.text((box_x1 + 12, tspot_50_y - 28), "PREMIUM ZONE (>50%)", fill=TV_BEAR_BODY, font=get_font(10, bold=True))
    
    fill_x = 428
    fill_y = tspot_50_y
    d.ellipse([(fill_x - 5, fill_y - 5), (fill_x + 5, fill_y + 5)], fill=TV_TSPOT_BORDER, outline=(255, 255, 255), width=2)
    
    callout_box = [(fill_x + 30, fill_y + 25), (fill_x + 380, fill_y + 85)]
    d.rounded_rectangle(callout_box, radius=6, fill=(240, 253, 244), outline=TV_TSPOT_BORDER, width=2)
    d.text((fill_x + 44, fill_y + 32), "MODEL 2 LIMIT ORDER FILLED", fill=TV_TSPOT_BORDER, font=get_font(12, bold=True))
    d.text((fill_x + 44, fill_y + 50), "Passively Tagged at Wholesale 50% Equilibrium", fill=TV_TEXT_MAIN, font=get_font(11))
    d.text((fill_x + 44, fill_y + 68), "Risk-to-Reward: 1:5.2 | Stop: 8 Pips below C2", fill=TV_TEXT_MUTED, font=get_font(10))
    d.line([(fill_x, fill_y), (fill_x + 30, fill_y + 40)], fill=TV_TSPOT_BORDER, width=2)
    
    tp_y = chart.price_to_y(tp_p)
    d.line([(520, tp_y), (1030, tp_y)], fill=TV_TSPOT_BORDER, width=2)
    d.text((620, tp_y - 18), "Take Profit Target (-2.0 Extension: 1.08450)", fill=TV_TSPOT_BORDER, font=get_font(11, bold=True))
    
    chart.draw_active_price_pill(1.08442, is_bull=True)
    chart.draw_dashboard_widget(1040, 75, "EURUSD (Forex)", "1m - 15m Model", "C3 T-Spot Fill", "Limit Order Executed")
    chart.img.save("docs/assets/images/models/model2_tspot_limit.png", "PNG")
    print("Model 2 chart generated successfully!")

# =========================================================================
# 3. Model 3 Chart: Dual Timeframe Micro CISD Inside HTF POI
# =========================================================================
def build_model_3_chart():
    chart = RealisticChartCanvas(1440, 810, "NQ1!", "1m (HTF 15m POI)", "NASDAQ 100 • MODEL 3: DUAL-TIMEFRAME MICRO CISD", decimals=2)
    chart.setup_price_range(20415.0, 20490.0)
    
    time_labels = [
        (150, "09:30"), (350, "09:40"), (550, "09:50"), (750, "10:00"), (950, "10:10"), (1150, "10:20")
    ]
    chart.draw_background_and_grid(price_step=10.0, time_labels=time_labels)
    chart.draw_top_bar(cur_price="20,481.50", change="+45.00 (+0.22%)")
    
    d = chart.draw
    
    # 15m HTF Discount POI (Shaded Box)
    htf_top_y = chart.price_to_y(20442.0)
    htf_bot_y = chart.price_to_y(20424.0)
    
    overlay = Image.new("RGBA", (chart.w, chart.h), (255, 255, 255, 0))
    d_ov = ImageDraw.Draw(overlay)
    d_ov.rectangle([(60, htf_top_y), (chart.chart_x2, htf_bot_y)], fill=(219, 234, 254, 90)) # Soft blue tint
    chart.img = Image.alpha_composite(chart.img, overlay)
    d = ImageDraw.Draw(chart.img)
    
    d.rectangle([(60, htf_top_y), (chart.chart_x2, htf_bot_y)], outline=TV_CISD_BLUE, width=1)
    d.text((75, htf_top_y + 8), "15-MINUTE HTF DISCOUNT POI / ORDERBLOCK ZONE [20,424.00 - 20,442.00]", fill=TV_CISD_BLUE, font=get_font(11, bold=True))
    d.text((75, htf_top_y + 26), "Wait for price to deliver inside before looking for 1m execution trigger", fill=TV_TEXT_MUTED, font=get_font(10))
    
    # 1m Execution Candles
    candles = [
        (120, 20468.0, 20472.0, 20458.0, 20460.0),
        (155, 20460.0, 20462.0, 20448.0, 20450.0),
        (190, 20450.0, 20452.0, 20438.0, 20440.0), # Taps into HTF POI!
        (225, 20440.0, 20444.0, 20432.0, 20436.0),
        # Micro Benchmark down candle inside POI
        (265, 20438.0, 20439.0, 20430.0, 20431.0), # Micro Benchmark Open = 20438.00!
        (300, 20431.0, 20433.0, 20424.0, 20426.0), # Micro C2 sweep low
        # Micro Reversal & Breakout
        (340, 20426.0, 20434.0, 20425.0, 20433.0),
        (375, 20433.0, 20443.0, 20432.0, 20442.0), # Micro CISD confirmed body close above 20438.00!
        # Expansion
        (415, 20442.0, 20452.0, 20440.0, 20450.0),
        (450, 20450.0, 20458.0, 20448.0, 20456.0),
        (485, 20456.0, 20468.0, 20454.0, 20466.0),
        (520, 20466.0, 20476.0, 20464.0, 20474.0),
        (555, 20474.0, 20484.0, 20472.0, 20481.5),
    ]
    for c in candles:
        chart.draw_candle(c[0], c[1], c[2], c[3], c[4], width=18)
        
    # Micro CISD Benchmark Line originating at x=265, y=20438.00
    micro_cisd_y = chart.price_to_y(20438.0)
    d.line([(265, micro_cisd_y), (850, micro_cisd_y)], fill=TV_CISD_BLUE, width=2)
    d.ellipse([(260, micro_cisd_y - 4), (270, micro_cisd_y + 4)], fill=TV_CISD_BLUE)
    d.text((150, micro_cisd_y - 18), "Micro Benchmark Open (20,438.00)", fill=TV_CISD_BLUE, font=get_font(10, bold=True))
    
    # Micro C2 Low
    micro_c2_y = chart.price_to_y(20424.0)
    d.line([(290, micro_c2_y), (650, micro_c2_y)], fill=TV_BEAR_BODY, width=2)
    d.text((290, micro_c2_y + 12), "Micro C2 Sweep Low: 20,424.00 (STOP LOSS: 20,423.00 -> 15 Pt Risk)", fill=TV_BEAR_BODY, font=get_font(11, bold=True))
    
    # Entry Trigger Callout
    trigger_x = 390
    trigger_y = chart.price_to_y(20442.0)
    d.ellipse([(trigger_x - 5, trigger_y - 5), (trigger_x + 5, trigger_y + 5)], fill=TV_BULL_BODY, outline=(255, 255, 255), width=2)
    
    callout_box = [(trigger_x + 25, trigger_y - 50), (trigger_x + 400, trigger_y + 15)]
    d.rounded_rectangle(callout_box, radius=6, fill=(240, 253, 244), outline=TV_BULL_BODY, width=2)
    d.text((trigger_x + 38, trigger_y - 42), "MODEL 3 CONFIRMED MICRO-CISD ENTRY", fill=TV_BULL_BODY, font=get_font(12, bold=True))
    d.text((trigger_x + 38, trigger_y - 24), "1m Body Closes ABOVE Micro Benchmark Open Inside 15m POI", fill=TV_TEXT_MAIN, font=get_font(11))
    d.text((trigger_x + 38, trigger_y - 6), "Sniper Entry with Minimal Stop Loss (1:4.8 R:R vs HTF High)", fill=TV_TEXT_MUTED, font=get_font(10))
    d.line([(trigger_x, trigger_y), (trigger_x + 25, trigger_y - 20)], fill=TV_BULL_BODY, width=2)
    
    # HTF Target
    target_y = chart.price_to_y(20482.0)
    d.line([(530, target_y), (1050, target_y)], fill=TV_TSPOT_BORDER, width=2)
    d.text((680, target_y - 18), "15m Buy-Side Liquidity Target (20,482.00)", fill=TV_TSPOT_BORDER, font=get_font(11, bold=True))
    
    chart.draw_active_price_pill(20481.50, is_bull=True)
    chart.draw_dashboard_widget(1040, 75, "NQ1! (NASDAQ)", "Dual TF (1m / 15m)", "C3 Micro Expansion", "Micro CISD Confirmed")
    chart.img.save("docs/assets/images/models/model3_micro_cisd.png", "PNG")
    print("Model 3 chart generated successfully!")

# =========================================================================
# 4. Model 4 Chart: C4 Continuation & Fibonacci Projection Targets
# =========================================================================
def build_model_4_chart():
    chart = RealisticChartCanvas(1440, 810, "NAS100", "1m", "NASDAQ 100 • MODEL 4: C4 EXPANSION & TARGET RUNS", decimals=2)
    chart.setup_price_range(20410.0, 20530.0)
    
    time_labels = [
        (150, "09:30"), (350, "09:45"), (550, "10:00"), (750, "10:15"), (950, "10:30"), (1150, "10:45")
    ]
    chart.draw_background_and_grid(price_step=15.0, time_labels=time_labels)
    chart.draw_top_bar(cur_price="20,518.00", change="+88.00 (+0.43%)")
    
    d = chart.draw
    
    # Levels
    c2_low = 20420.00
    c1_high = 20460.00
    c3_high = 20480.00
    tspot_50 = 20450.00
    ext_1 = 20500.00
    ext_2 = 20520.00
    
    candles = [
        # C1 range
        (100, 20448.0, 20455.0, 20442.0, 20445.0),
        (130, 20445.0, 20460.0, 20444.0, 20458.0), # C1 High = 20460.00
        # C2 sweep
        (165, 20458.0, 20460.0, 20435.0, 20438.0),
        (200, 20438.0, 20440.0, 20420.0, 20424.0), # C2 Low = 20420.00
        # C3 Impulse
        (235, 20424.0, 20445.0, 20422.0, 20442.0),
        (270, 20442.0, 20465.0, 20440.0, 20464.0), # Breaks C1 high
        (305, 20464.0, 20482.0, 20462.0, 20480.0), # C3 Peak = 20480.00
        # C4 Shallow Retest / Pullback
        (345, 20480.0, 20481.0, 20468.0, 20470.0),
        (380, 20470.0, 20472.0, 20460.0, 20462.0), # Retests broken C1 High (Support Flip!)
        # C4 Expansion continuation
        (420, 20462.0, 20478.0, 20460.0, 20476.0),
        (460, 20476.0, 20492.0, 20474.0, 20490.0),
        (500, 20490.0, 20502.0, 20488.0, 20500.0), # Hits -1.0 Ext
        (540, 20500.0, 20512.0, 20498.0, 20510.0),
        (580, 20510.0, 20522.0, 20508.0, 20520.0), # Hits -2.0 Ext
    ]
    for c in candles:
        chart.draw_candle(c[0], c[1], c[2], c[3], c[4], width=18)
        
    # C1 High line (Support Flip)
    c1_h_y = chart.price_to_y(c1_high)
    d.line([(120, c1_h_y), (850, c1_h_y)], fill=TV_TEXT_LIGHT, width=1)
    d.text((120, c1_h_y - 18), "Broken C1 High (Turned Institutional Support: 20,460.00)", fill=TV_TEXT_MUTED, font=get_font(10))
    
    # Fibonacci Expansion Lines
    c3_h_y = chart.price_to_y(c3_high)
    d.line([(290, c3_h_y), (850, c3_h_y)], fill=TV_FIB_PURPLE, width=1)
    d.text((315, c3_h_y - 16), "1.0 C3 High (20,480.00)", fill=TV_FIB_PURPLE, font=get_font(10, bold=True))
    
    ext1_y = chart.price_to_y(ext_1)
    d.line([(480, ext1_y), (950, ext1_y)], fill=TV_TSPOT_BORDER, width=2)
    d.text((620, ext1_y - 18), "TP1: -1.0 Std Dev Target (20,500.00)", fill=TV_TSPOT_BORDER, font=get_font(11, bold=True))
    
    ext2_y = chart.price_to_y(ext_2)
    d.line([(540, ext2_y), (950, ext2_y)], fill=TV_TSPOT_BORDER, width=2)
    d.text((620, ext2_y - 18), "TP2: -2.0 Standard Target (20,520.00)", fill=TV_TSPOT_BORDER, font=get_font(11, bold=True))
    
    # C4 Entry Callout
    entry_x = 390
    entry_y = chart.price_to_y(20462.0)
    d.ellipse([(entry_x - 5, entry_y - 5), (entry_x + 5, entry_y + 5)], fill=TV_ORANGE_RUN, outline=(255, 255, 255), width=2)
    
    callout_box = [(entry_x + 25, entry_y + 20), (entry_x + 390, entry_y + 85)]
    d.rounded_rectangle(callout_box, radius=6, fill=(255, 247, 237), outline=TV_ORANGE_RUN, width=2)
    d.text((entry_x + 38, entry_y + 28), "MODEL 4 C4 CONTINUATION ENTRY", fill=TV_ORANGE_RUN, font=get_font(12, bold=True))
    d.text((entry_x + 38, entry_y + 46), "Retest of Broken C1 High & C3 FVG Respect", fill=TV_TEXT_MAIN, font=get_font(11))
    d.text((entry_x + 38, entry_y + 64), "Targeting -1.0 to -2.0 Institutional Expansions", fill=TV_TEXT_MUTED, font=get_font(10))
    d.line([(entry_x, entry_y), (entry_x + 25, entry_y + 35)], fill=TV_ORANGE_RUN, width=2)
    
    chart.draw_active_price_pill(20518.00, is_bull=True)
    chart.draw_dashboard_widget(1040, 75, "NAS100 (Index)", "1m Trend Expansion", "C4 Run Active", "Fib Extension Triggered")
    chart.img.save("docs/assets/images/models/model4_c4_continuation.png", "PNG")
    print("Model 4 chart generated successfully!")

# =========================================================================
# 5. Master Fractal 4-Phase Delivery Cycle Chart (C1 - C4)
# =========================================================================
def build_cycle_chart():
    img = Image.new("RGBA", (1440, 810), TV_BG)
    draw = ImageDraw.Draw(img)
    
    # Top Bar
    draw.rectangle([(0, 0), (1440, 56)], fill=TV_PANEL_BG)
    draw.line([(0, 56), (1440, 56)], fill=TV_BORDER, width=1)
    draw.text((24, 16), "THE 4-PHASE DELIVERY CYCLE (C1 TO C4)", fill=TV_TEXT_MAIN, font=get_font(16, bold=True))
    draw.text((450, 18), "The Universal Macro Delivery Blueprint — Inner Circle Trader Mechanics", fill=TV_TEXT_MUTED, font=get_font(12))
    
    draw.rounded_rectangle([(1440 - 240, 12), (1440 - 24, 44)], radius=6, fill=TV_CISD_BLUE)
    draw.text((1440 - 225, 18), "Algorithmic Market Phases", fill=(255, 255, 255), font=get_font(11, bold=True))
    
    # 4 Columns
    col_w = 320
    col_h = 710
    top_y = 75
    
    cols = [
        ("PHASE 1: C1 CONSOLIDATION", "Range Foundation", (248, 250, 252), TV_BORDER, "Asian / Pre-Market Range build.\nEstablishes liquidity pools at both highs and lows."),
        ("PHASE 2: C2 MANIPULATION", "The Liquidity Sweep", (254, 242, 242), TV_BEAR_BODY, "Judas Swing stops out early retail longs into HTF POI discount.\nEngineers liquidity for institutional accumulation."),
        ("PHASE 3: C3 EXPANSION", "CISD Delivery Shift", (238, 242, 255), TV_CISD_BLUE, "Orderflow flips. Candle body closes strictly above benchmark candle open.\nPrice explodes violently out of the sweep low."),
        ("PHASE 4: C4 CONTINUATION", "Trend Run to DOL", (240, 253, 244), TV_TSPOT_BORDER, "Holds institutional discount / broken C1 high.\nExpands toward external targets (-2.0, -4.0 standard deviations)."),
    ]
    
    for i, (title, sub, bg, border_col, desc) in enumerate(cols):
        cx = 40 + i * (col_w + 25)
        # Background card
        draw.rounded_rectangle([(cx, top_y), (cx + col_w, top_y + col_h)], radius=10, fill=bg, outline=border_col, width=2)
        # Card header
        draw.rounded_rectangle([(cx, top_y), (cx + col_w, top_y + 60)], radius=8, fill=(255, 255, 255), outline=border_col, width=1)
        draw.text((cx + 14, top_y + 12), title, fill=border_col, font=get_font(12, bold=True))
        draw.text((cx + 14, top_y + 34), sub, fill=TV_TEXT_MUTED, font=get_font(11))
        
        # Bottom description
        draw.line([(cx + 15, top_y + col_h - 90), (cx + col_w - 15, top_y + col_h - 90)], fill=border_col, width=1)
        draw.text((cx + 15, top_y + col_h - 80), desc, fill=TV_TEXT_MAIN, font=get_font(10))
        
    # Draw illustrative candles inside each phase column
    # C1 Candles (Col 0)
    c1_candles = [
        (65, 300, 270, 320, 280),
        (95, 280, 260, 310, 305),
        (125, 305, 285, 330, 295),
        (155, 295, 275, 315, 310),
        (185, 310, 290, 335, 300),
        (215, 300, 270, 320, 275),
    ]
    for x, o, h, l, c in c1_candles:
        is_bull = c <= o
        col = TV_BULL_BODY if is_bull else TV_BEAR_BODY
        draw.line([(x + 10, h), (x + 10, l)], fill=col, width=2)
        draw.rectangle([(x, min(o, c)), (x + 20, max(o, c))], fill=col, outline=col)
    # Range lines
    draw.line([(55, 260), (250, 260)], fill=TV_TEXT_LIGHT, width=1)
    draw.text((60, 242), "C1 Range High (BSL)", fill=TV_TEXT_MUTED, font=get_font(10))
    draw.line([(55, 335), (250, 335)], fill=TV_TEXT_LIGHT, width=1)
    draw.text((60, 342), "C1 Range Low (SSL)", fill=TV_TEXT_MUTED, font=get_font(10))
    
    # C2 Candles (Col 1)
    c2_candles = [
        (410, 310, 300, 360, 350), # Benchmark down candle! Open = 310
        (445, 350, 345, 410, 400),
        (480, 400, 395, 470, 460), # C2 low sweeps SSL!
        (515, 460, 410, 465, 415),
    ]
    for x, o, h, l, c in c2_candles:
        is_bull = c <= o
        col = TV_BULL_BODY if is_bull else TV_BEAR_BODY
        draw.line([(x + 10, h), (x + 10, l)], fill=col, width=2)
        draw.rectangle([(x, min(o, c)), (x + 20, max(o, c))], fill=col, outline=col)
    draw.line([(400, 470), (550, 470)], fill=TV_BEAR_BODY, width=2)
    draw.text((410, 478), "C2 Sweep Low (Liquidity Purged)", fill=TV_BEAR_BODY, font=get_font(11, bold=True))
    
    # C3 Candles (Col 2)
    c3_candles = [
        (755, 415, 350, 420, 360),
        (790, 360, 290, 365, 300), # Closes above 310 benchmark!
        (825, 300, 240, 305, 245),
        (860, 245, 210, 250, 215),
    ]
    for x, o, h, l, c in c3_candles:
        is_bull = c <= o
        col = TV_BULL_BODY if is_bull else TV_BEAR_BODY
        draw.line([(x + 10, h), (x + 10, l)], fill=col, width=2)
        draw.rectangle([(x, min(o, c)), (x + 20, max(o, c))], fill=col, outline=col)
    draw.line([(740, 310), (900, 310)], fill=TV_CISD_BLUE, width=2)
    draw.text((750, 316), "CISD Confirmed Body Close", fill=TV_CISD_BLUE, font=get_font(10, bold=True))
    
    # C4 Candles (Col 3)
    c4_candles = [
        (1100, 215, 210, 250, 240), # Pullback
        (1135, 240, 238, 260, 255), # Retest support
        (1170, 255, 180, 258, 185), # Massive extension
        (1205, 185, 140, 188, 145), # DOL reach
    ]
    for x, o, h, l, c in c4_candles:
        is_bull = c <= o
        col = TV_BULL_BODY if is_bull else TV_BEAR_BODY
        draw.line([(x + 10, h), (x + 10, l)], fill=col, width=2)
        draw.rectangle([(x, min(o, c)), (x + 20, max(o, c))], fill=col, outline=col)
    draw.line([(1090, 140), (1240, 140)], fill=TV_TSPOT_BORDER, width=2)
    draw.text((1100, 122), "External DOL Target Reached (-2.0 Std)", fill=TV_TSPOT_BORDER, font=get_font(10, bold=True))
    
    img.save("docs/assets/images/models/fractal_c1_c4_cycle.png", "PNG")
    print("4-Phase Cycle chart generated successfully!")

# =========================================================================
# 6. SMT Divergence Anatomy Chart (Dual-Pane NQ vs ES Synchronized)
# =========================================================================
def build_smt_chart():
    img = Image.new("RGBA", (1440, 810), TV_BG)
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.rectangle([(0, 0), (1440, 56)], fill=TV_PANEL_BG)
    draw.line([(0, 56), (1440, 56)], fill=TV_BORDER, width=1)
    draw.text((24, 16), "SMT DIVERGENCE ANATOMY — INTERMARKET CORRELATION CRACK", fill=TV_TEXT_MAIN, font=get_font(16, bold=True))
    draw.text((640, 18), "Synchronized Time Comparison: NQ Sweeps Low while ES Holds Institutional Support", fill=TV_TEXT_MUTED, font=get_font(12))
    
    draw.rounded_rectangle([(1440 - 240, 12), (1440 - 24, 44)], radius=6, fill=TV_CISD_BLUE)
    draw.text((1440 - 225, 18), "Institutional Footprint", fill=(255, 255, 255), font=get_font(11, bold=True))
    
    pane_w = 1380
    pane_h = 325
    
    # Top Pane: NQ1! (Sweeps Lower Low)
    p1_y = 75
    draw.rounded_rectangle([(30, p1_y), (30 + pane_w, p1_y + pane_h)], radius=8, fill=(255, 255, 255), outline=TV_BORDER, width=1)
    draw.rectangle([(30, p1_y), (30 + pane_w, p1_y + 36)], fill=(248, 250, 252))
    draw.line([(30, p1_y + 36), (30 + pane_w, p1_y + 36)], fill=TV_BORDER, width=1)
    draw.text((45, p1_y + 8), "NQ1! (NASDAQ 100 E-MINI) — 1-MINUTE CHART", fill=TV_TEXT_MAIN, font=get_font(13, bold=True))
    draw.text((380, p1_y + 10), "Makes LOWER LOW (Retail Sell-Stop Purge)", fill=TV_BEAR_BODY, font=get_font(11, bold=True))
    
    # Bottom Pane: ES1! (Forms Higher Low)
    p2_y = 430
    draw.rounded_rectangle([(30, p2_y), (30 + pane_w, p2_y + pane_h)], radius=8, fill=(255, 255, 255), outline=TV_BORDER, width=1)
    draw.rectangle([(30, p2_y), (30 + pane_w, p2_y + 36)], fill=(248, 250, 252))
    draw.line([(30, p2_y + 36), (30 + pane_w, p2_y + 36)], fill=TV_BORDER, width=1)
    draw.text((45, p2_y + 8), "ES1! (S&P 500 E-MINI) — 1-MINUTE CHART", fill=TV_TEXT_MAIN, font=get_font(13, bold=True))
    draw.text((380, p2_y + 10), "Forms HIGHER LOW (Institutional Smart Money Accumulation)", fill=TV_TSPOT_BORDER, font=get_font(11, bold=True))
    
    # Draw Synchronized Time Grid Line at x = 700 (Time: 09:45 AM)
    sync_x = 700
    for y_step in range(p1_y + 36, p2_y + pane_h, 8):
        draw.line([(sync_x, y_step), (sync_x, y_step + 4)], fill=(217, 70, 239), width=2) # Magenta dashed line
    draw.rounded_rectangle([(sync_x - 70, p2_y - 20), (sync_x + 70, p2_y + 10)], radius=4, fill=(217, 70, 239))
    draw.text((sync_x - 58, p2_y - 15), "TIME: 09:45 AM", fill=(255, 255, 255), font=get_font(11, bold=True))
    
    # NQ Candles (Top)
    # Low 1 at x=400 (y=260). Low 2 at x=700 (y=320 -> LOWER LOW!)
    nq_candles = [
        (350, 200, 180, 250, 240),
        (400, 240, 230, 265, 260), # Low 1
        (450, 260, 210, 265, 215), # Bounce
        (500, 215, 200, 230, 225),
        (550, 225, 220, 255, 250),
        (600, 250, 245, 280, 275),
        (650, 275, 270, 315, 310),
        (700, 310, 305, 335, 325), # Low 2 (LOWER LOW!)
        (750, 325, 260, 330, 265), # Violent reversal
        (800, 265, 220, 270, 225),
        (850, 225, 180, 230, 185),
    ]
    for x, o, h, l, c in nq_candles:
        is_bull = c <= o
        col = TV_BULL_BODY if is_bull else TV_BEAR_BODY
        draw.line([(x + 10, h), (x + 10, l)], fill=col, width=2)
        draw.rectangle([(x, min(o, c)), (x + 20, max(o, c))], fill=col, outline=col)
        
    # NQ Trendline connecting Low 1 to Low 2
    draw.line([(410, 265), (710, 335)], fill=TV_BEAR_BODY, width=2)
    draw.text((720, 340), "LOWER LOW (Liquidity Swept)", fill=TV_BEAR_BODY, font=get_font(12, bold=True))
    
    # ES Candles (Bottom)
    # Low 1 at x=400 (y=690). Low 2 at x=700 (y=620 -> HIGHER LOW!)
    es_candles = [
        (350, 580, 560, 640, 630),
        (400, 630, 620, 695, 690), # Low 1
        (450, 690, 610, 695, 615), # Bounce
        (500, 615, 600, 625, 620),
        (550, 620, 615, 635, 630),
        (600, 630, 625, 645, 640),
        (650, 640, 635, 650, 645),
        (700, 645, 615, 650, 620), # Low 2 (HIGHER LOW - Failed to sweep Low 1!)
        (750, 620, 560, 625, 565), # Violent reversal
        (800, 565, 510, 570, 515),
        (850, 515, 470, 520, 475),
    ]
    for x, o, h, l, c in es_candles:
        is_bull = c <= o
        col = TV_BULL_BODY if is_bull else TV_BEAR_BODY
        draw.line([(x + 10, h), (x + 10, l)], fill=col, width=2)
        draw.rectangle([(x, min(o, c)), (x + 20, max(o, c))], fill=col, outline=col)
        
    # ES Trendline connecting Low 1 to Low 2
    draw.line([(410, 695), (710, 650)], fill=TV_TSPOT_BORDER, width=2)
    draw.text((720, 655), "HIGHER LOW (Accumulation / Smart Money Footprint)", fill=TV_TSPOT_BORDER, font=get_font(12, bold=True))
    
    # SMT Callout Badge
    callout_box = [(960, 360), (1380, 450)]
    draw.rounded_rectangle(callout_box, radius=8, fill=(255, 241, 242), outline=(225, 29, 72), width=2)
    draw.text((980, 372), "SMT DIVERGENCE CONFIRMED", fill=(225, 29, 72), font=get_font(13, bold=True))
    draw.text((980, 396), "Crack in correlation between ES and NQ.", fill=TV_TEXT_MAIN, font=get_font(11))
    draw.text((980, 416), "Indicates massive upside institutional expansion ahead!", fill=TV_TEXT_MUTED, font=get_font(10))
    
    img.save("docs/assets/images/models/smt_divergence_anatomy.png", "PNG")
    print("SMT Divergence chart generated successfully!")

# =========================================================================
# 7. Deep Dive: CISD Anatomy & Body Close Mechanics
# =========================================================================
def build_cisd_deep_dive_chart():
    img = Image.new("RGBA", (1440, 810), TV_BG)
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.rectangle([(0, 0), (1440, 56)], fill=TV_PANEL_BG)
    draw.line([(0, 56), (1440, 56)], fill=TV_BORDER, width=1)
    draw.text((24, 16), "CHANGE IN STATE OF DELIVERY (CISD) — TECHNICAL ANATOMY", fill=TV_TEXT_MAIN, font=get_font(16, bold=True))
    draw.text((540, 18), "Precise Benchmark Open Identification & Candle Body Close Validation", fill=TV_TEXT_MUTED, font=get_font(12))
    
    badge_txt = "Institutional Orderflow Shift"
    draw.rounded_rectangle([(1440 - 240, 12), (1440 - 24, 44)], radius=6, fill=TV_CISD_BLUE)
    draw.text((1440 - 228, 18), badge_txt, fill=(255, 255, 255), font=get_font(11, bold=True))
    
    # Split Two Panels: Left = INVALID (Wick Rejection), Right = VALID (Body Close)
    pw = 670
    ph = 700
    
    # Panel 1: False Trigger / Wick Trap (Left)
    draw.rounded_rectangle([(30, 75), (30 + pw, 75 + ph)], radius=10, fill=(255, 255, 255), outline=TV_BORDER, width=1)
    draw.rectangle([(30, 75), (30 + pw, 115)], fill=(254, 242, 242))
    draw.text((45, 87), "SCENARIO A: WICK REJECTION — INVALID (RETAIL TRAP)", fill=TV_BEAR_BODY, font=get_font(13, bold=True))
    
    # Draw candles in Scenario A
    # Benchmark candle open at y = 300
    # C2 low at y = 500
    # Breakout candle wicks past 300 to 240, but CLOSES back down at 320!
    c_a = [
        (90, 260, 255, 310, 305), # Up candle
        (130, 300, 302, 360, 350), # Benchmark down-close candle! Open = 300
        (170, 350, 352, 420, 410),
        (210, 410, 412, 510, 490), # C2 low
        (260, 490, 430, 495, 435),
        (300, 435, 360, 440, 370),
        # Wick-only probe candle:
        (350, 370, 240, 375, 320), # High is 240 (pierces 300!), but CLOSE is 320 (BELOW 300)!
        (400, 320, 310, 460, 450), # Huge dump lower
    ]
    for x, o, h, l, c in c_a:
        is_bull = c <= o
        col = TV_BULL_BODY if is_bull else TV_BEAR_BODY
        draw.line([(x + 12, h), (x + 12, l)], fill=col, width=2)
        draw.rectangle([(x, min(o, c)), (x + 24, max(o, c))], fill=col, outline=col)
        
    # Scenario A CISD line
    draw.line([(130, 300), (520, 300)], fill=TV_CISD_BLUE, width=2)
    draw.ellipse([(125, 295), (135, 305)], fill=TV_CISD_BLUE)
    draw.text((130, 275), "Benchmark Open", fill=TV_CISD_BLUE, font=get_font(11, bold=True))
    
    # Rejection callout
    draw.rounded_rectangle([(320, 180), (660, 250)], radius=6, fill=(254, 226, 226), outline=TV_BEAR_BODY, width=2)
    draw.text((330, 188), "DO NOT ENTER: WICK ONLY!", fill=TV_BEAR_BODY, font=get_font(12, bold=True))
    draw.text((330, 208), "Wick pierced the line, but body closed BELOW.", fill=TV_TEXT_MAIN, font=get_font(11))
    draw.text((330, 226), "Orderflow NOT flipped -> Leads to deeper lows!", fill=TV_TEXT_MUTED, font=get_font(10))
    draw.line([(362, 240), (362, 250)], fill=TV_BEAR_BODY, width=2)
    
    # Panel 2: Confirmed Body Close (Right)
    rx = 740
    draw.rounded_rectangle([(rx, 75), (rx + pw, 75 + ph)], radius=10, fill=(255, 255, 255), outline=TV_BORDER, width=1)
    draw.rectangle([(rx, 75), (rx + pw, 115)], fill=(240, 253, 244))
    draw.text((rx + 15, 87), "SCENARIO B: CANDLE BODY CLOSE — CONFIRMED CISD", fill=TV_TSPOT_BORDER, font=get_font(13, bold=True))
    
    # Draw candles in Scenario B
    # Breakout candle CLOSES at y = 260 (ABOVE 300!)
    c_b = [
        (rx + 60, 260, 255, 310, 305),
        (rx + 100, 300, 302, 360, 350), # Benchmark down-close candle! Open = 300
        (rx + 140, 350, 352, 420, 410),
        (rx + 180, 410, 412, 510, 490), # C2 low
        (rx + 230, 490, 430, 495, 435),
        (rx + 270, 435, 360, 440, 370),
        # Body close candle:
        (rx + 320, 370, 250, 375, 260), # High is 250, CLOSE is 260 (SOLID BODY ABOVE 300)!
        (rx + 365, 260, 220, 265, 225), # Huge green expansion
        (rx + 405, 225, 180, 230, 185),
    ]
    for x, o, h, l, c in c_b:
        is_bull = c <= o
        col = TV_BULL_BODY if is_bull else TV_BEAR_BODY
        draw.line([(x + 12, h), (x + 12, l)], fill=col, width=2)
        draw.rectangle([(x, min(o, c)), (x + 24, max(o, c))], fill=col, outline=col)
        
    # Scenario B CISD line
    draw.line([(rx + 100, 300), (rx + 480, 300)], fill=TV_CISD_BLUE, width=2)
    draw.ellipse([(rx + 95, 295), (rx + 105, 305)], fill=TV_CISD_BLUE)
    draw.text((rx + 100, 275), "Benchmark Open", fill=TV_CISD_BLUE, font=get_font(11, bold=True))
    
    # Confirmation callout
    draw.rounded_rectangle([(rx + 300, 160), (rx + 640, 230)], radius=6, fill=(240, 253, 244), outline=TV_TSPOT_BORDER, width=2)
    draw.text((rx + 312, 168), "CONFIRMED ENTRY: SOLID BODY CLOSE", fill=TV_TSPOT_BORDER, font=get_font(12, bold=True))
    draw.text((rx + 312, 188), "Candle body closed strictly ABOVE 300 benchmark.", fill=TV_TEXT_MAIN, font=get_font(11))
    draw.text((rx + 312, 206), "Algorithmic delivery flipped from Sell to Buy!", fill=TV_TEXT_MUTED, font=get_font(10))
    draw.line([(rx + 332, 260), (rx + 332, 230)], fill=TV_TSPOT_BORDER, width=2)
    
    img.save("docs/assets/images/charts/cisd_anatomy_deep_dive.png", "PNG")
    print("CISD Anatomy deep dive chart generated successfully!")

# =========================================================================
# 8. Indicator Interface Overview Chart (TradingView Mockup)
# =========================================================================
def build_indicator_interface_chart():
    chart = RealisticChartCanvas(1440, 810, "NQ1!", "1m - 15m Model", "TRADINGVIEW INDICATOR INTERFACE OVERVIEW", decimals=2)
    chart.setup_price_range(20410.0, 20500.0)
    
    time_labels = [
        (150, "09:30"), (350, "09:45"), (550, "10:00"), (750, "10:15"), (950, "10:30"), (1150, "10:45")
    ]
    chart.draw_background_and_grid(price_step=10.0, time_labels=time_labels)
    chart.draw_top_bar(cur_price="20,492.00", change="+56.00 (+0.28%)")
    
    d = chart.draw
    
    # 1. Right Margin: HTF Projection Cluster (Shows 4 completed 15m candles directly on chart)
    htf_x = 1180
    d.line([(htf_x - 15, chart.chart_y1), (htf_x - 15, chart.chart_y2)], fill=TV_BORDER, width=2)
    d.text((htf_x - 5, chart.chart_y1 + 10), "15m HTF Projection", fill=TV_CISD_BLUE, font=get_font(11, bold=True))
    
    htf_candles = [
        (htf_x + 5, 20450.0, 20465.0, 20435.0, 20440.0), # Red
        (htf_x + 35, 20440.0, 20445.0, 20420.0, 20438.0), # C2 sweep candle
        (htf_x + 65, 20438.0, 20485.0, 20435.0, 20482.0), # C3 massive green body
        (htf_x + 95, 20482.0, 20498.0, 20480.0, 20492.0), # C4 active candle
    ]
    for x, o, h, l, c in htf_candles:
        chart.draw_candle(x, o, h, l, c, width=22)
        
    # HTF timer
    d.rounded_rectangle([(htf_x + 10, chart.chart_y2 - 32), (htf_x + 115, chart.chart_y2 - 6)], radius=4, fill=(238, 242, 255), outline=TV_CISD_BLUE, width=1)
    d.text((htf_x + 18, chart.chart_y2 - 26), "15m Close: 04:18", fill=TV_CISD_BLUE, font=get_font(10, bold=True))
    
    # 2. Main Chart: Active 1m candles
    candles = [
        (130, 20455.0, 20462.0, 20448.0, 20450.0),
        (170, 20450.0, 20452.0, 20438.0, 20440.0), # Benchmark Open = 20450.00
        (210, 20440.0, 20442.0, 20428.0, 20430.0),
        (250, 20430.0, 20435.0, 20420.0, 20428.0), # C2 low
        (290, 20428.0, 20445.0, 20426.0, 20442.0),
        (330, 20442.0, 20458.0, 20440.0, 20456.0), # Breakout close!
        (370, 20456.0, 20457.0, 20451.0, 20452.0), # Retest
        (410, 20452.0, 20475.0, 20450.0, 20472.0),
        (450, 20472.0, 20488.0, 20470.0, 20486.0),
        (490, 20486.0, 20495.0, 20484.0, 20492.0),
    ]
    for c in candles:
        chart.draw_candle(c[0], c[1], c[2], c[3], c[4], width=20)
        
    # Phase Markers
    d.text((135, chart.price_to_y(20465.0) - 22), "C1", fill=TV_TEXT_MUTED, font=get_font(12, bold=True))
    d.text((255, chart.price_to_y(20420.0) + 12), "C2", fill=TV_BEAR_BODY, font=get_font(12, bold=True))
    d.text((415, chart.price_to_y(20475.0) - 22), "C3", fill=TV_TSPOT_BORDER, font=get_font(12, bold=True))
    d.text((495, chart.price_to_y(20495.0) - 22), "C4", fill=TV_ORANGE_RUN, font=get_font(12, bold=True))
    
    # CISD Benchmark line
    cisd_y = chart.price_to_y(20450.00)
    d.line([(170, cisd_y), (600, cisd_y)], fill=TV_CISD_BLUE, width=3)
    d.ellipse([(165, cisd_y - 4), (175, cisd_y + 4)], fill=TV_CISD_BLUE)
    d.text((120, cisd_y - 18), "CISD Benchmark Level (20,450.00)", fill=TV_CISD_BLUE, font=get_font(10, bold=True))
    
    # Dashboard in corner
    chart.draw_dashboard_widget(880, 75, "NQ1! (NASDAQ)", "1m - 15m Model", "C4 Continuation", "All Signals Valid")
    
    chart.img.save("docs/assets/images/indicator/indicator_interface_overview.png", "PNG")
    print("Indicator Interface Overview chart generated successfully!")

# =========================================================================
# 9. Dealing Range & Premium / Discount Equilibrium Chart
# =========================================================================
def build_dealing_range_chart():
    chart = RealisticChartCanvas(1440, 810, "ES1!", "15m", "S&P 500 E-MINI • DEALING RANGE & EQUILIBRIUM (T-SPOT)", decimals=2)
    chart.setup_price_range(5830.0, 5910.0)
    
    time_labels = [
        (150, "08:00"), (350, "09:30"), (550, "11:00"), (750, "12:30"), (950, "14:00"), (1150, "15:30")
    ]
    chart.draw_background_and_grid(price_step=10.0, time_labels=time_labels)
    chart.draw_top_bar(cur_price="5,882.50", change="+32.25 (+0.55%)")
    
    d = chart.draw
    high_p = 5900.00
    low_p = 5840.00
    eq_p = 5870.00
    
    high_y = chart.price_to_y(high_p)
    low_y = chart.price_to_y(low_p)
    eq_y = chart.price_to_y(eq_p)
    
    overlay = Image.new("RGBA", (chart.w, chart.h), (255, 255, 255, 0))
    d_ov = ImageDraw.Draw(overlay)
    # Premium zone (top half) - light red tint
    d_ov.rectangle([(60, high_y), (chart.chart_x2, eq_y)], fill=(254, 226, 226, 70))
    # Discount zone (bottom half) - light green tint
    d_ov.rectangle([(60, eq_y), (chart.chart_x2, low_y)], fill=(220, 252, 231, 80))
    chart.img = Image.alpha_composite(chart.img, overlay)
    d = ImageDraw.Draw(chart.img)
    
    # Grid lines & labels
    d.line([(60, high_y), (chart.chart_x2, high_y)], fill=TV_BEAR_BODY, width=2)
    d.text((80, high_y - 20), "100.0% DEALING RANGE HIGH (PREMIUM / BUY-SIDE LIQUIDITY: 5,900.00)", fill=TV_BEAR_BODY, font=get_font(11, bold=True))
    d.text((chart.chart_x2 - 280, high_y + 10), "EXPENSIVE / INSTITUTIONAL SHORT ZONE", fill=TV_BEAR_BODY, font=get_font(10, bold=True))
    
    d.line([(60, eq_y), (chart.chart_x2, eq_y)], fill=TV_CISD_BLUE, width=2)
    d.text((80, eq_y - 18), "50.0% EQUILIBRIUM / T-SPOT THRESHOLD (5,870.00)", fill=TV_CISD_BLUE, font=get_font(11, bold=True))
    d.text((chart.chart_x2 - 240, eq_y - 18), "FAIR VALUE TRANSITION", fill=TV_CISD_BLUE, font=get_font(10, bold=True))
    
    d.line([(60, low_y), (chart.chart_x2, low_y)], fill=TV_TSPOT_BORDER, width=2)
    d.text((80, low_y + 10), "0.0% DEALING RANGE LOW (DISCOUNT / SELL-SIDE LIQUIDITY: 5,840.00)", fill=TV_TSPOT_BORDER, font=get_font(11, bold=True))
    d.text((chart.chart_x2 - 280, low_y - 24), "CHEAP / WHOLESALE ACCUMULATION ZONE", fill=TV_TSPOT_BORDER, font=get_font(10, bold=True))
    
    # Illustrative candles delivering from Discount to Premium
    candles = [
        (120, 5885.0, 5892.0, 5878.0, 5880.0),
        (160, 5880.0, 5882.0, 5865.0, 5868.0),
        (200, 5868.0, 5870.0, 5850.0, 5852.0),
        (240, 5852.0, 5855.0, 5838.0, 5842.0), # Sweeps Low (0% Level)
        # Accumulation in Discount
        (280, 5842.0, 5858.0, 5840.0, 5855.0),
        (320, 5855.0, 5868.0, 5852.0, 5866.0),
        # Crosses 50% Equilibrium
        (360, 5866.0, 5878.0, 5864.0, 5876.0),
        (400, 5876.0, 5878.0, 5868.0, 5870.0), # Pullback to tap 50% from above!
        (440, 5870.0, 5885.0, 5869.0, 5884.0),
        (480, 5884.0, 5895.0, 5882.0, 5894.0),
        (520, 5894.0, 5904.0, 5892.0, 5900.0), # Hits 100% High!
    ]
    for c in candles:
        chart.draw_candle(c[0], c[1], c[2], c[3], c[4], width=20)
        
    chart.draw_active_price_pill(5882.50, is_bull=True)
    chart.draw_dashboard_widget(1040, 75, "ES1! (S&P 500)", "Dealing Range Engine", "Discount Delivered", "Equilibrium Respected")
    chart.img.save("docs/assets/images/charts/dealing_range_premium_discount.png", "PNG")
    print("Dealing Range chart generated successfully!")

# =========================================================================
# 10. Bearish CISD Anatomy & Setup Execution
# =========================================================================
def build_bearish_cisd_chart():
    chart = RealisticChartCanvas(1440, 810, "NQ1!", "1m", "NASDAQ 100 • BEARISH CISD ORDERFLOW INVERSION", decimals=2)
    chart.setup_price_range(20420.0, 20500.0)
    
    time_labels = [
        (150, "09:30"), (350, "09:40"), (550, "09:50"), (750, "10:00"), (950, "10:10"), (1150, "10:20")
    ]
    chart.draw_background_and_grid(price_step=10.0, time_labels=time_labels)
    chart.draw_top_bar(cur_price="20,432.00", change="-48.00 (-0.23%)")
    
    d = chart.draw
    
    c1_high = 20480.00
    c2_high = 20494.00
    benchmark_open = 20468.00
    tp1 = 20448.00
    tp2 = 20430.00
    
    candles = [
        (120, 20450.0, 20458.0, 20448.0, 20455.0),
        (155, 20455.0, 20468.0, 20452.0, 20466.0),
        (190, 20466.0, 20480.0, 20465.0, 20478.0), # C1 High
        # Leg into C2 Extreme: Benchmark Bullish Candle (Open = 20468.00)
        (225, 20468.0, 20485.0, 20466.0, 20482.0), # Benchmark Up-Close Candle! Open = 20468.00
        (260, 20482.0, 20494.0, 20480.0, 20490.0), # C2 Sweep of BSL
        # Reversal & Displacement
        (300, 20490.0, 20492.0, 20476.0, 20478.0),
        (335, 20478.0, 20480.0, 20468.0, 20470.0),
        # CISD Breakout Candle: Closes strictly BELOW 20468.00!
        (375, 20470.0, 20472.0, 20456.0, 20458.0), # Red body close below benchmark!
        # C3 Retest & C4 Run
        (415, 20458.0, 20468.0, 20457.0, 20465.0), # Retests line
        (450, 20465.0, 20466.0, 20448.0, 20449.0),
        (485, 20449.0, 20450.0, 20436.0, 20438.0),
        (520, 20438.0, 20440.0, 20428.0, 20430.0),
    ]
    for c in candles:
        chart.draw_candle(c[0], c[1], c[2], c[3], c[4], width=18)
        
    # C2 Sweep High
    c2_y = chart.price_to_y(c2_high)
    d.line([(240, c2_y), (600, c2_y)], fill=TV_BEAR_BODY, width=2)
    d.text((250, c2_y - 18), "C2 High (Buy-Side Liquidity Swept: 20,494.00 | STOP LOSS: 20,495.00)", fill=TV_BEAR_BODY, font=get_font(11, bold=True))
    
    # Bearish CISD line originating strictly from Candle Open at x=225, y=benchmark_open
    cisd_y = chart.price_to_y(benchmark_open)
    benchmark_x = 225
    d.line([(benchmark_x, cisd_y), (850, cisd_y)], fill=TV_CISD_RED, width=3)
    d.ellipse([(benchmark_x - 5, cisd_y - 5), (benchmark_x + 5, cisd_y + 5)], fill=TV_CISD_RED, outline=(255, 255, 255), width=2)
    
    d.rounded_rectangle([(benchmark_x - 180, cisd_y + 12), (benchmark_x + 35, cisd_y + 38)], radius=4, fill=(254, 242, 242), outline=TV_CISD_RED, width=1)
    d.text((benchmark_x - 172, cisd_y + 16), "Benchmark Candle Open (CISD Origin: 20,468.00)", fill=TV_CISD_RED, font=get_font(10, bold=True))
    
    # Trigger Callout
    trigger_x = 385
    trigger_y = chart.price_to_y(20458.0)
    d.ellipse([(trigger_x - 5, trigger_y - 5), (trigger_x + 5, trigger_y + 5)], fill=TV_BEAR_BODY, outline=(255, 255, 255), width=2)
    
    callout_box = [(trigger_x + 25, trigger_y + 15), (trigger_x + 390, trigger_y + 80)]
    d.rounded_rectangle(callout_box, radius=6, fill=(254, 242, 242), outline=TV_BEAR_BODY, width=2)
    d.text((trigger_x + 38, trigger_y + 24), "CONFIRMED SHORT TRIGGER: BEARISH CISD", fill=TV_BEAR_BODY, font=get_font(12, bold=True))
    d.text((trigger_x + 38, trigger_y + 42), "Candle Body Closes STRICTLY Below Benchmark Open", fill=TV_TEXT_MAIN, font=get_font(11))
    d.text((trigger_x + 38, trigger_y + 60), "Orderflow Shifts to Sell-Program | Target SSL Below", fill=TV_TEXT_MUTED, font=get_font(10))
    d.line([(trigger_x, trigger_y), (trigger_x + 25, trigger_y + 30)], fill=TV_BEAR_BODY, width=2)
    
    # TP Target
    tp_y = chart.price_to_y(tp2)
    d.line([(500, tp_y), (950, tp_y)], fill=TV_TSPOT_BORDER, width=2)
    d.text((620, tp_y - 18), "Institutional Target: Sell-Side Liquidity (20,430.00)", fill=TV_TSPOT_BORDER, font=get_font(11, bold=True))
    
    chart.draw_active_price_pill(20432.00, is_bull=False)
    chart.draw_dashboard_widget(1040, 75, "NQ1! (NASDAQ)", "1m Short Execution", "Bearish CISD", "Sell-Program Active")
    chart.img.save("docs/assets/images/charts/bearish_cisd_anatomy.png", "PNG")
    print("Bearish CISD chart generated successfully!")

# =========================================================================
# 11. TradingView Alert Dialog Realistic Graphic
# =========================================================================
def build_alert_dialog_graphic():
    w, h = 1000, 680
    img = Image.new("RGBA", (w, h), (241, 245, 249)) # Light gray background
    draw = ImageDraw.Draw(img)
    
    # Dialog Window Container (Centered)
    dx, dy = 180, 40
    dw, dh = 640, 600
    
    # Window shadow
    for i in range(8):
        draw.rounded_rectangle([(dx - i, dy - i), (dx + dw + i, dy + dh + i)], radius=12, outline=(226, 232, 240, 100 - i * 12), width=1)
        
    draw.rounded_rectangle([(dx, dy), (dx + dw, dy + dh)], radius=10, fill=(255, 255, 255), outline=TV_BORDER, width=1)
    
    # Modal Header
    draw.rounded_rectangle([(dx, dy), (dx + dw, dy + 54)], radius=10, fill=TV_PANEL_BG)
    draw.line([(dx, dy + 54), (dx + dw, dy + 54)], fill=TV_BORDER, width=1)
    draw.text((dx + 24, dy + 16), "Create Alert on NQ1! (NASDAQ)", fill=TV_TEXT_MAIN, font=get_font(15, bold=True))
    draw.text((dx + dw - 36, dy + 16), "✕", fill=TV_TEXT_MUTED, font=get_font(16, bold=True))
    
    # Tab Row: Settings | Notifications
    draw.text((dx + 24, dy + 68), "Settings", fill=TV_CISD_BLUE, font=get_font(13, bold=True))
    draw.line([(dx + 20, dy + 92), (dx + 85, dy + 92)], fill=TV_CISD_BLUE, width=2)
    draw.text((dx + 110, dy + 68), "Notifications", fill=TV_TEXT_MUTED, font=get_font(13))
    draw.line([(dx, dy + 93), (dx + dw, dy + 93)], fill=TV_BORDER, width=1)
    
    # Field 1: Condition
    draw.text((dx + 24, dy + 115), "Condition", fill=TV_TEXT_MUTED, font=get_font(11, bold=True))
    # Dropdown 1
    draw.rounded_rectangle([(dx + 24, dy + 135), (dx + dw - 24, dy + 175)], radius=6, fill=(255, 255, 255), outline=TV_CISD_BLUE, width=2)
    draw.text((dx + 38, dy + 146), "TTrades Fractal Model Pro+ [v6]", fill=TV_TEXT_MAIN, font=get_font(12, bold=True))
    draw.text((dx + dw - 50, dy + 146), "▼", fill=TV_TEXT_MUTED, font=get_font(10))
    
    # Dropdown 2 (Secondary condition)
    draw.text((dx + 24, dy + 195), "Trigger Event", fill=TV_TEXT_MUTED, font=get_font(11, bold=True))
    draw.rounded_rectangle([(dx + 24, dy + 215), (dx + dw - 24, dy + 255)], radius=6, fill=(255, 255, 255), outline=TV_BORDER, width=1)
    draw.text((dx + 38, dy + 226), "Any alert() function call", fill=TV_TEXT_MAIN, font=get_font(12, bold=True))
    draw.text((dx + dw - 50, dy + 226), "▼", fill=TV_TEXT_MUTED, font=get_font(10))
    
    # Expiration & Interval
    draw.text((dx + 24, dy + 275), "Expiration", fill=TV_TEXT_MUTED, font=get_font(11, bold=True))
    draw.rounded_rectangle([(dx + 24, dy + 295), (dx + 300, dy + 335)], radius=6, fill=(255, 255, 255), outline=TV_BORDER, width=1)
    draw.text((dx + 38, dy + 306), "Open-Ended (Permanent)", fill=TV_TEXT_MAIN, font=get_font(11))
    
    draw.text((dx + 325, dy + 275), "Alert Frequency", fill=TV_TEXT_MUTED, font=get_font(11, bold=True))
    draw.rounded_rectangle([(dx + 325, dy + 295), (dx + dw - 24, dy + 335)], radius=6, fill=(255, 255, 255), outline=TV_BORDER, width=1)
    draw.text((dx + 340, dy + 306), "Once Per Bar Close", fill=TV_TEXT_MAIN, font=get_font(11))
    
    # Message Preview Box
    draw.text((dx + 24, dy + 355), "Alert Message Preview", fill=TV_TEXT_MUTED, font=get_font(11, bold=True))
    draw.rounded_rectangle([(dx + 24, dy + 375), (dx + dw - 24, dy + 450)], radius=6, fill=(248, 250, 252), outline=TV_BORDER, width=1)
    draw.text((dx + 38, dy + 388), "[TTFM Pro+] Bullish CISD Confirmed on NQ1! (1m)", fill=TV_TEXT_MAIN, font=get_font(12, bold=True))
    draw.text((dx + 38, dy + 412), "Benchmark Open: 20,452.00 | Candle Body Close: 20,460.00 | Stop: 20,422.00", fill=TV_TEXT_MUTED, font=get_font(10))
    
    # Notification Checkboxes
    checks = [
        ("☑ Notify in App (Push)", dx + 24, dy + 475),
        ("☑ Show Pop-up Window", dx + 210, dy + 475),
        ("☑ Play Sound (Chime)", dx + 410, dy + 475),
    ]
    for lbl, cx, cy in checks:
        draw.text((cx, cy), lbl, fill=TV_TEXT_MAIN, font=get_font(11, bold=True))
        
    # Bottom Actions: Cancel & Create Button
    draw.line([(dx, dy + dh - 64), (dx + dw, dy + dh - 64)], fill=TV_BORDER, width=1)
    
    draw.rounded_rectangle([(dx + dw - 210, dy + dh - 50), (dx + dw - 110, dy + dh - 14)], radius=6, fill=(255, 255, 255), outline=TV_BORDER, width=1)
    draw.text((dx + dw - 180, dy + dh - 38), "Cancel", fill=TV_TEXT_MUTED, font=get_font(12, bold=True))
    
    draw.rounded_rectangle([(dx + dw - 95, dy + dh - 50), (dx + dw - 24, dy + dh - 14)], radius=6, fill=TV_CISD_BLUE)
    draw.text((dx + dw - 75, dy + dh - 38), "Create", fill=(255, 255, 255), font=get_font(12, bold=True))
    
    img.save("docs/assets/images/indicator/tradingview_alert_dialog.png", "PNG")
    print("TradingView Alert Dialog realistic graphic generated successfully!")

# =========================================================================
# 12. TradingView Settings Dialog Realistic Graphic
# =========================================================================
def build_settings_dialog_graphic():
    w, h = 1000, 720
    img = Image.new("RGBA", (w, h), (241, 245, 249))
    draw = ImageDraw.Draw(img)
    
    dx, dy = 180, 30
    dw, dh = 640, 650
    
    # Shadow
    for i in range(8):
        draw.rounded_rectangle([(dx - i, dy - i), (dx + dw + i, dy + dh + i)], radius=12, outline=(226, 232, 240, 100 - i * 12), width=1)
        
    draw.rounded_rectangle([(dx, dy), (dx + dw, dy + dh)], radius=10, fill=(255, 255, 255), outline=TV_BORDER, width=1)
    
    # Header
    draw.rounded_rectangle([(dx, dy), (dx + dw, dy + 54)], radius=10, fill=TV_PANEL_BG)
    draw.line([(dx, dy + 54), (dx + dw, dy + 54)], fill=TV_BORDER, width=1)
    draw.text((dx + 24, dy + 16), "TTrades Fractal Model Pro+ [v6]", fill=TV_TEXT_MAIN, font=get_font(15, bold=True))
    draw.text((dx + dw - 36, dy + 16), "✕", fill=TV_TEXT_MUTED, font=get_font(16, bold=True))
    
    # Tabs: Inputs | Style | Visibility
    draw.text((dx + 24, dy + 68), "Inputs", fill=TV_CISD_BLUE, font=get_font(13, bold=True))
    draw.line([(dx + 20, dy + 92), (dx + 70, dy + 92)], fill=TV_CISD_BLUE, width=2)
    draw.text((dx + 95, dy + 68), "Style", fill=TV_TEXT_MUTED, font=get_font(13))
    draw.text((dx + 160, dy + 68), "Visibility", fill=TV_TEXT_MUTED, font=get_font(13))
    draw.line([(dx, dy + 93), (dx + dw, dy + 93)], fill=TV_BORDER, width=1)
    
    # Rows
    y = dy + 115
    rows = [
        ("MODEL PRESET", "Preset Model Configuration", "1m - 15m Model (Scalping / NY AM)"),
        ("TIMEFRAME RESOLUTION", "HTF Reference Timeframe", "15 (Minutes)"),
        ("CYCLE ANNOTATIONS", "Show C1 - C4 Phase Labels", "Enabled (Checked)"),
        ("CISD BENCHMARK RAY", "Draw Opposing Open Level", "Enabled (Checked)"),
        ("50% T-SPOT BOX", "Project Equilibrium Box", "Enabled (Checked)"),
        ("HTF PROJECTION CLUSTER", "Overlay Margin Candles", "Enabled (Checked)"),
        ("CYCLE STATUS HUD", "Display Corner Dashboard", "Enabled (Checked)"),
    ]
    
    for cat, lbl, val in rows:
        draw.text((dx + 24, y), cat, fill=TV_CISD_BLUE, font=get_font(10, bold=True))
        draw.text((dx + 24, y + 16), lbl, fill=TV_TEXT_MAIN, font=get_font(12))
        
        # Pill on right
        draw.rounded_rectangle([(dx + dw - 280, y + 10), (dx + dw - 24, y + 38)], radius=4, fill=(248, 250, 252), outline=TV_BORDER, width=1)
        draw.text((dx + dw - 270, y + 16), val, fill=TV_TEXT_MAIN, font=get_font(11, bold=True))
        
        y += 56
        draw.line([(dx + 24, y - 8), (dx + dw - 24, y - 8)], fill=(241, 245, 249), width=1)
        
    # Bottom Actions
    draw.line([(dx, dy + dh - 60), (dx + dw, dy + dh - 60)], fill=TV_BORDER, width=1)
    draw.text((dx + 24, dy + dh - 40), "Reset Defaults", fill=TV_TEXT_MUTED, font=get_font(11))
    
    draw.rounded_rectangle([(dx + dw - 190, dy + dh - 48), (dx + dw - 100, dy + dh - 14)], radius=6, fill=(255, 255, 255), outline=TV_BORDER, width=1)
    draw.text((dx + dw - 165, dy + dh - 36), "Cancel", fill=TV_TEXT_MUTED, font=get_font(12, bold=True))
    
    draw.rounded_rectangle([(dx + dw - 85, dy + dh - 48), (dx + dw - 24, dy + dh - 14)], radius=6, fill=TV_CISD_BLUE)
    draw.text((dx + dw - 65, dy + dh - 36), "OK", fill=(255, 255, 255), font=get_font(12, bold=True))
    
    img.save("docs/assets/images/indicator/indicator_settings_dialog.png", "PNG")
    print("TradingView Settings Dialog realistic graphic generated successfully!")

if __name__ == "__main__":
    build_model_1_chart()
    build_model_2_chart()
    build_model_3_chart()
    build_model_4_chart()
    build_cycle_chart()
    build_smt_chart()
    build_cisd_deep_dive_chart()
    build_indicator_interface_chart()
    build_dealing_range_chart()
    build_bearish_cisd_chart()
    build_alert_dialog_graphic()
    build_settings_dialog_graphic()
    print("ALL 12 photorealistic TradingView visual graphics successfully built!")
