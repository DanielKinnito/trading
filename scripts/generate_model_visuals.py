"""
Generate high-resolution, professional light-theme TradingView-style visual chart images
for the TTrades Fractal Model documentation website.
"""

from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs("docs/assets/images/models", exist_ok=True)
os.makedirs("docs/assets/images/indicator", exist_ok=True)
os.makedirs("docs/assets/images/charts", exist_ok=True)

# Common palette matching modern TradingView light mode
BG_COLOR = (255, 255, 255)
GRID_COLOR = (245, 247, 250)
TEXT_COLOR = (15, 23, 42)
MUTED_TEXT = (100, 116, 139)
GREEN_CANDLE = (8, 153, 129)
GREEN_WICK = (8, 153, 129)
RED_CANDLE = (242, 54, 69)
RED_WICK = (242, 54, 69)
BLUE_CISD = (37, 99, 235)
ORANGE_ACCENT = (234, 88, 12)
PURPLE_ACCENT = (147, 51, 234)
GREEN_BOX = (220, 252, 231, 160)
GREEN_BORDER = (22, 163, 74)
RED_BOX = (254, 226, 226, 160)
RED_BORDER = (220, 38, 38)
BORDER_COLOR = (226, 232, 240)

def get_font(size=14, bold=False):
    font_paths = [
        "C:\\Windows\\Fonts\\segoeuib.ttf" if bold else "C:\\Windows\\Fonts\\segoeui.ttf",
        "C:\\Windows\\Fonts\\arialbd.ttf" if bold else "C:\\Windows\\Fonts\\arial.ttf",
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def draw_header(draw, title, subtitle, badge_text="Fractal Model Pro+ [v6]", badge_color=(37, 99, 235)):
    draw.rectangle([(0, 0), (1280, 75)], fill=(248, 250, 252))
    draw.line([(0, 75), (1280, 75)], fill=BORDER_COLOR, width=2)
    
    font_title = get_font(20, bold=True)
    font_sub = get_font(13, bold=False)
    font_badge = get_font(12, bold=True)
    
    draw.text((35, 15), title, fill=TEXT_COLOR, font=font_title)
    draw.text((35, 45), subtitle, fill=MUTED_TEXT, font=font_sub)
    
    bbox = font_badge.getbbox(badge_text)
    bw = bbox[2] - bbox[0] + 24
    draw.rounded_rectangle([(1280 - 35 - bw, 22), (1280 - 35, 53)], radius=6, fill=badge_color)
    draw.text((1280 - 35 - bw + 12, 28), badge_text, fill=(255, 255, 255), font=font_badge)

def draw_dashboard_table(draw, x=1010, y=90, asset="NQ1! (NASDAQ)", model="1m - 15m Model", status="C3 Active"):
    font_t = get_font(12, bold=True)
    font_v = get_font(11, bold=False)
    
    draw.rounded_rectangle([(x, y), (x + 235, y + 140)], radius=6, fill=(255, 255, 255), outline=BORDER_COLOR, width=1)
    draw.rectangle([(x, y), (x + 235, y + 30)], fill=(241, 245, 249))
    draw.line([(x, y + 30), (x + 235, y + 30)], fill=BORDER_COLOR, width=1)
    draw.text((x + 12, y + 8), "TTFM Pro+ Engine", fill=TEXT_COLOR, font=font_t)
    
    rows = [
        ("Asset:", asset),
        ("Current Model:", model),
        ("Cycle Phase:", status),
        ("CISD Status:", "Body Close Shift")
    ]
    cur_y = y + 38
    for label, val in rows:
        draw.text((x + 12, cur_y), label, fill=MUTED_TEXT, font=font_v)
        draw.text((x + 105, cur_y), val, fill=TEXT_COLOR, font=font_t if "Phase" in label or "Status" in label else font_v)
        cur_y += 24

def draw_candle(draw, x, open_p, high_p, low_p, close_p, width=14):
    # In screen coordinates, lower y value means higher price (bullish close < open)
    is_bull = close_p <= open_p
    c_color = GREEN_CANDLE if is_bull else RED_CANDLE
    w_color = GREEN_WICK if is_bull else RED_WICK
    
    draw.line([(x + width // 2, high_p), (x + width // 2, low_p)], fill=w_color, width=2)
    top = min(open_p, close_p)
    bottom = max(open_p, close_p)
    if bottom == top:
        bottom += 2
    draw.rectangle([(x, top), (x + width, bottom)], fill=c_color, outline=c_color)

def generate_model_1_image():
    img = Image.new("RGBA", (1280, 720), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    for gx in range(50, 1280, 60):
        draw.line([(gx, 75), (gx, 720)], fill=GRID_COLOR, width=1)
    for gy in range(100, 720, 50):
        draw.line([(0, gy), (1280, gy)], fill=GRID_COLOR, width=1)
        
    draw_header(draw, "Model 1: CISD Breakout Close Entry", "Systematic entry on candle body close past Change in State of Delivery benchmark", "Model 1 - Confirmation", BLUE_CISD)
    
    c2_low_y = 560
    cisd_level_y = 390
    tp1_y = 250
    tp2_y = 150
    
    # Horizontal reference lines
    draw.line([(80, cisd_level_y), (980, cisd_level_y)], fill=BLUE_CISD, width=2)
    draw.text((80, cisd_level_y - 22), "CISD Benchmark Level (Body Close Trigger)", fill=BLUE_CISD, font=get_font(12, bold=True))
    
    draw.line([(80, c2_low_y), (980, c2_low_y)], fill=MUTED_TEXT, width=1)
    draw.text((80, c2_low_y + 8), "C2 Swing Low (Sell-Side Liquidity Purged)", fill=MUTED_TEXT, font=get_font(12))
    
    draw.line([(480, tp1_y), (980, tp1_y)], fill=GREEN_BORDER, width=2)
    draw.text((490, tp1_y - 20), "TP1: Buy-Side Liquidity (BSL) / -1.0 Ext", fill=GREEN_BORDER, font=get_font(12, bold=True))
    
    draw.line([(580, tp2_y), (980, tp2_y)], fill=GREEN_BORDER, width=2)
    draw.text((590, tp2_y - 20), "TP2: Macro External Target (-2.0 to -2.5 Ext)", fill=GREEN_BORDER, font=get_font(12, bold=True))
    
    candles = [
        # Bearish leg down to C2
        (120, 320, 310, 380, 370),
        (150, 370, 360, 430, 420),
        (180, 420, 390, 480, 470), # Benchmark candle whose OPEN establishes 390 CISD level
        (210, 470, 460, 520, 510),
        (240, 510, 500, 575, 560), # C2 manipulation sweep candle
        # Reversal inside C3
        (275, 550, 500, 555, 510),
        (305, 510, 460, 515, 470),
        (335, 470, 430, 475, 440),
        (365, 440, 395, 445, 405),
        # CISD breakout candle: CLOSES ABOVE 390
        (395, 405, 340, 410, 345),
        # Post-confirmation run to targets
        (435, 345, 290, 350, 300),
        (470, 300, 245, 305, 250), # Hits TP1
        (505, 250, 205, 255, 210),
        (540, 210, 170, 215, 175),
        (575, 175, 140, 180, 145), # Hits TP2
    ]
    
    for c in candles:
        draw_candle(draw, c[0], c[1], c[2], c[3], c[4], width=16)
        
    font_ann = get_font(13, bold=True)
    font_sm = get_font(11, bold=False)
    
    # C2 Label
    draw.text((225, 590), "C2 (SSL Swept)", fill=RED_BORDER, font=font_ann)
    draw.line([(248, 585), (248, 575)], fill=RED_BORDER, width=2)
    
    # CISD Benchmark Open marker
    draw.ellipse([(180 + 8 - 4, 390 - 4), (180 + 8 + 4, 390 + 4)], fill=BLUE_CISD)
    draw.text((150, 365), "Benchmark Open", fill=BLUE_CISD, font=get_font(11, bold=True))
    
    # Breakout close marker
    draw.rounded_rectangle([(425, 330), (645, 385)], radius=6, fill=(238, 242, 255), outline=BLUE_CISD, width=2)
    draw.text((435, 338), "MODEL 1 ENTRY TRIGGER", fill=BLUE_CISD, font=font_ann)
    draw.text((435, 360), "Candle Body Closes Above CISD", fill=TEXT_COLOR, font=font_sm)
    draw.line([(425, 355), (411, 345)], fill=BLUE_CISD, width=2)
    
    # Stop loss marker
    draw.line([(395, 575), (470, 575)], fill=RED_BORDER, width=3)
    draw.rounded_rectangle([(475, 560), (630, 590)], radius=4, fill=(254, 226, 226), outline=RED_BORDER, width=1)
    draw.text((482, 568), "STOP LOSS (Below C2 Low)", fill=RED_BORDER, font=get_font(11, bold=True))
    
    draw_dashboard_table(draw, 1010, 90, "NAS100 / NQ", "1m - 15m Model", "C3 Expansion")
    img.save("docs/assets/images/models/model1_cisd_breakout.png", "PNG")

def generate_model_2_image():
    img = Image.new("RGBA", (1280, 720), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    for gx in range(50, 1280, 60):
        draw.line([(gx, 75), (gx, 720)], fill=GRID_COLOR, width=1)
    for gy in range(100, 720, 50):
        draw.line([(0, gy), (1280, gy)], fill=GRID_COLOR, width=1)
        
    draw_header(draw, "Model 2: T-Spot Equilibrium Limit Entry", "Optimal discount pullback execution into the 50% equilibrium box / FVG during C3", "Model 2 - Discount Limit", GREEN_BORDER)
    
    c2_low_y = 560
    cisd_y = 360
    tspot_50_y = 460
    tp_y = 170
    
    # Discount Box Overlay
    overlay = Image.new("RGBA", (1280, 720), (255, 255, 255, 0))
    d_overlay = ImageDraw.Draw(overlay)
    d_overlay.rectangle([(360, tspot_50_y), (580, c2_low_y)], fill=(220, 252, 231, 140))
    d_overlay.rectangle([(360, cisd_y), (580, tspot_50_y)], fill=(254, 226, 226, 90))
    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)
    
    draw.line([(80, cisd_y), (980, cisd_y)], fill=BLUE_CISD, width=2)
    draw.text((80, cisd_y - 20), "CISD Shift Level (Body Close Confirmed)", fill=BLUE_CISD, font=get_font(12, bold=True))
    
    draw.line([(360, tspot_50_y), (980, tspot_50_y)], fill=GREEN_BORDER, width=2)
    draw.text((370, tspot_50_y - 20), "50% T-Spot (Equilibrium Limit Order Level)", fill=GREEN_BORDER, font=get_font(12, bold=True))
    
    draw.line([(80, c2_low_y), (980, c2_low_y)], fill=RED_BORDER, width=1)
    draw.text((80, c2_low_y + 8), "C2 Swing Low (SSL Swept / 100% Invalidation)", fill=RED_BORDER, font=get_font(12))
    
    draw.line([(550, tp_y), (980, tp_y)], fill=GREEN_BORDER, width=2)
    draw.text((560, tp_y - 20), "Take Profit Target (-2.0 Extension)", fill=GREEN_BORDER, font=get_font(12, bold=True))
    
    candles = [
        (130, 350, 340, 410, 400),
        (160, 400, 390, 460, 450),
        (190, 450, 440, 510, 500),
        (220, 500, 490, 570, 560), # C2 low
        # Displacement
        (255, 545, 470, 550, 480),
        (285, 480, 400, 485, 410),
        (315, 410, 340, 415, 350), # CISD breakout candle!
        (345, 350, 340, 365, 355),
        # Pullback into T-Spot
        (380, 355, 350, 420, 415),
        (410, 415, 410, 470, 465), # Reaches 50% discount box!
        (440, 465, 440, 475, 445), # Rejection wick out of discount!
        # Expansion to target
        (475, 445, 375, 450, 380),
        (505, 380, 315, 385, 320),
        (535, 320, 255, 325, 260),
        (565, 260, 205, 265, 210),
        (595, 210, 165, 215, 170), # Target reached!
    ]
    for c in candles:
        draw_candle(draw, c[0], c[1], c[2], c[3], c[4], width=16)
        
    font_ann = get_font(13, bold=True)
    draw.text((215, 580), "C2 Liquidity Sweep", fill=RED_BORDER, font=font_ann)
    
    draw.rounded_rectangle([(450, 480), (690, 535)], radius=6, fill=(220, 252, 231), outline=GREEN_BORDER, width=2)
    draw.text((460, 488), "MODEL 2 LIMIT ENTRY", fill=GREEN_BORDER, font=font_ann)
    draw.text((460, 510), "Limit Order Filled at 50% Discount T-Spot", fill=TEXT_COLOR, font=get_font(11))
    draw.line([(450, 495), (418, 465)], fill=GREEN_BORDER, width=2)
    
    draw.text((375, 510), "DISCOUNT ZONE (<50%)", fill=GREEN_BORDER, font=get_font(11, bold=True))
    draw.text((375, 410), "PREMIUM ZONE (>50%)", fill=RED_BORDER, font=get_font(11, bold=True))
    
    draw_dashboard_table(draw, 1010, 90, "EURUSD", "1m - 1H Model", "C3 T-Spot Fill")
    img.save("docs/assets/images/models/model2_tspot_limit.png", "PNG")

def generate_model_3_image():
    img = Image.new("RGBA", (1280, 720), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    for gx in range(50, 1280, 60):
        draw.line([(gx, 75), (gx, 720)], fill=GRID_COLOR, width=1)
    for gy in range(100, 720, 50):
        draw.line([(0, gy), (1280, gy)], fill=GRID_COLOR, width=1)
        
    draw_header(draw, "Model 3: LTF Micro CISD Sniper Entry", "Sub-timeframe confirmation nested inside the HTF C3 Point of Interest / T-Spot", "Model 3 - Micro Structure", PURPLE_ACCENT)
    
    # HTF POI Box
    overlay = Image.new("RGBA", (1280, 720), (255, 255, 255, 0))
    d_overlay = ImageDraw.Draw(overlay)
    d_overlay.rectangle([(300, 400), (750, 520)], fill=(243, 232, 255, 140))
    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(300, 400), (750, 520)], outline=PURPLE_ACCENT, width=1)
    draw.text((310, 408), "HTF Point of Interest (15m C3 FVG / T-Spot)", fill=PURPLE_ACCENT, font=get_font(12, bold=True))
    
    candles = [
        # Pullback down into HTF POI
        (220, 340, 330, 390, 380),
        (245, 380, 370, 430, 420),
        (270, 420, 415, 460, 450),
        # Micro Structure inside POI
        (305, 450, 445, 480, 475), # Micro C1
        (330, 475, 465, 515, 505), # Micro C2 sweep inside POI!
        (355, 500, 460, 505, 465), # Micro displacement
        (380, 465, 430, 470, 435), # Micro CISD breakout candle!
        (405, 435, 425, 445, 440), # Micro retest
        # Micro expansion outwards
        (435, 440, 380, 445, 385),
        (465, 385, 330, 390, 335),
        (495, 335, 280, 340, 285),
        (525, 285, 235, 290, 240),
        (555, 240, 190, 245, 195),
    ]
    for c in candles:
        draw_candle(draw, c[0], c[1], c[2], c[3], c[4], width=14)
        
    draw.line([(305, 450), (430, 450)], fill=BLUE_CISD, width=2)
    draw.text((435, 445), "1m Micro CISD Level", fill=BLUE_CISD, font=get_font(11, bold=True))
    
    draw.rounded_rectangle([(440, 320), (690, 375)], radius=6, fill=(243, 232, 255), outline=PURPLE_ACCENT, width=2)
    draw.text((450, 328), "MODEL 3 SNIPER ENTRY", fill=PURPLE_ACCENT, font=get_font(13, bold=True))
    draw.text((450, 350), "1m Body Closes Past Micro CISD", fill=TEXT_COLOR, font=get_font(11))
    draw.line([(440, 350), (390, 435)], fill=PURPLE_ACCENT, width=2)
    
    draw.line([(330, 515), (410, 515)], fill=RED_BORDER, width=2)
    draw.text((415, 508), "Sniper SL (Under Micro C2)", fill=RED_BORDER, font=get_font(10, bold=True))
    
    draw.rounded_rectangle([(780, 240), (930, 280)], radius=6, fill=(220, 252, 231), outline=GREEN_BORDER, width=1)
    draw.text((792, 252), "Risk/Reward: 1:5+", fill=GREEN_BORDER, font=get_font(12, bold=True))
    
    draw_dashboard_table(draw, 1010, 90, "NAS100 / NQ", "1m inside 15m POI", "Micro CISD Confirmed")
    img.save("docs/assets/images/models/model3_micro_cisd.png", "PNG")

def generate_model_4_image():
    img = Image.new("RGBA", (1280, 720), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    for gx in range(50, 1280, 60):
        draw.line([(gx, 75), (gx, 720)], fill=GRID_COLOR, width=1)
    for gy in range(100, 720, 50):
        draw.line([(0, gy), (1280, gy)], fill=GRID_COLOR, width=1)
        
    draw_header(draw, "Model 4: C4 Trend Continuation Entry", "High-probability trend continuation entry as C3 closes strong and C4 begins distribution", "Model 4 - Expansion", ORANGE_ACCENT)
    
    c3_high_y = 310
    
    overlay = Image.new("RGBA", (1280, 720), (255, 255, 255, 0))
    d_overlay = ImageDraw.Draw(overlay)
    d_overlay.rectangle([(230, 310), (410, 540)], fill=(241, 245, 249, 140))
    d_overlay.rectangle([(420, 140), (640, 330)], fill=(254, 243, 199, 140))
    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(230, 310), (410, 540)], outline=BORDER_COLOR, width=1)
    draw.text((240, 515), "C3 Expansion Candle Range", fill=MUTED_TEXT, font=get_font(11, bold=True))
    
    draw.rectangle([(420, 140), (640, 330)], outline=ORANGE_ACCENT, width=1)
    draw.text((430, 150), "C4 Run to Macro -4.0 Extension", fill=ORANGE_ACCENT, font=get_font(11, bold=True))
    
    candles = [
        # C2 base
        (160, 510, 500, 550, 540),
        (190, 540, 515, 545, 520),
        # C3 massive body
        (230, 520, 440, 525, 445),
        (260, 445, 380, 450, 385),
        (290, 385, 335, 390, 340),
        (320, 340, 305, 345, 310), # C3 closes strong near high!
        # C4 Open & Shallow pullback
        (360, 310, 305, 340, 335), # Shallow dip
        (390, 335, 315, 340, 320), # Rejection & continuation
        # C4 Distribution
        (430, 320, 260, 325, 265),
        (470, 265, 210, 270, 215),
        (510, 215, 170, 220, 175),
        (550, 175, 135, 180, 140),
    ]
    for c in candles:
        draw_candle(draw, c[0], c[1], c[2], c[3], c[4], width=18)
        
    draw.line([(310, c3_high_y), (450, c3_high_y)], fill=BLUE_CISD, width=2)
    draw.text((455, c3_high_y - 8), "C3 High Broken", fill=BLUE_CISD, font=get_font(11, bold=True))
    
    draw.rounded_rectangle([(410, 360), (670, 420)], radius=6, fill=(254, 243, 199), outline=ORANGE_ACCENT, width=2)
    draw.text((420, 368), "MODEL 4 CONTINUATION", fill=ORANGE_ACCENT, font=get_font(13, bold=True))
    draw.text((420, 390), "Enter on C4 Shallow Retest / Breakout", fill=TEXT_COLOR, font=get_font(11))
    draw.line([(410, 390), (375, 338)], fill=ORANGE_ACCENT, width=2)
    
    draw.line([(310, 460), (400, 460)], fill=RED_BORDER, width=2)
    draw.text((405, 455), "Trailing Stop (Below C3 Midpoint)", fill=RED_BORDER, font=get_font(10, bold=True))
    
    draw_dashboard_table(draw, 1010, 90, "NAS100 / NQ", "15m - 4H Model", "C4 Distribution Active")
    img.save("docs/assets/images/models/model4_c4_continuation.png", "PNG")

def generate_cycle_image():
    img = Image.new("RGBA", (1280, 720), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    for gx in range(50, 1280, 60):
        draw.line([(gx, 75), (gx, 720)], fill=GRID_COLOR, width=1)
    for gy in range(100, 720, 50):
        draw.line([(0, gy), (1280, gy)], fill=GRID_COLOR, width=1)
        
    draw_header(draw, "The Complete C1-C2-C3-C4 Fractal Sequence", "Anatomy of the 4-candle market delivery cycle: Setup, Manipulation, Displacement, Distribution", "Core Mechanics", BLUE_CISD)
    
    phases = [
        ("C1: SETUP & RANGE", "Initial consolidation defining boundaries", 60, 330, (241, 245, 249), BORDER_COLOR),
        ("C2: MANIPULATION / SWEEP", "Judas swing purging SSL/BSL into HTF POI", 350, 620, (254, 226, 226), RED_BORDER),
        ("C3: DISPLACEMENT & CISD", "Displacement confirming trend shift & T-Spot fill", 640, 910, (220, 252, 231), GREEN_BORDER),
        ("C4: DISTRIBUTION / RUN", "Expansion candle running to external targets", 930, 1200, (254, 243, 199), ORANGE_ACCENT)
    ]
    
    for title, desc, x1, x2, bg, border in phases:
        draw.rounded_rectangle([(x1, 100), (x2, 170)], radius=6, fill=bg, outline=border, width=2)
        draw.text((x1 + 12, 112), title, fill=TEXT_COLOR, font=get_font(13, bold=True))
        draw.text((x1 + 12, 136), desc, fill=MUTED_TEXT, font=get_font(10))
        
    candles = [
        # C1 range
        (140, 400, 380, 430, 410),
        (170, 410, 390, 440, 405),
        (200, 405, 395, 435, 425),
        # C2 sweep
        (420, 425, 415, 490, 480),
        (450, 480, 470, 550, 535), # C2 wick purges low!
        (480, 535, 490, 540, 495),
        # C3 Displacement
        (710, 495, 420, 500, 425),
        (740, 425, 360, 430, 365), # Crosses CISD level!
        (770, 365, 310, 370, 315),
        # C4 Distribution
        (980, 315, 260, 320, 265),
        (1010, 265, 210, 270, 215),
        (1040, 215, 165, 220, 170)
    ]
    for c in candles:
        draw_candle(draw, c[0], c[1], c[2], c[3], c[4], width=20)
        
    draw.line([(200, 405), (900, 405)], fill=BLUE_CISD, width=2)
    draw.text((910, 397), "CISD Benchmark Level", fill=BLUE_CISD, font=get_font(11, bold=True))
    
    draw.line([(140, 440), (520, 440)], fill=RED_BORDER, width=1)
    draw.text((530, 432), "C1 Low Purged by C2 Manipulation", fill=RED_BORDER, font=get_font(11))
    
    img.save("docs/assets/images/models/fractal_c1_c4_cycle.png", "PNG")

def generate_smt_image():
    img = Image.new("RGBA", (1280, 720), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    for gx in range(50, 1280, 60):
        draw.line([(gx, 75), (gx, 720)], fill=GRID_COLOR, width=1)
    for gy in range(100, 720, 50):
        draw.line([(0, gy), (1280, gy)], fill=GRID_COLOR, width=1)
        
    draw_header(draw, "SMT Divergence Mechanics (NQ vs ES Correlation)", "Intermarket crack: When one asset sweeps the C2 swing low but correlated asset makes a higher low", "High Probability Filter", PURPLE_ACCENT)
    
    # Left Box: NQ
    draw.rounded_rectangle([(60, 100), (590, 640)], radius=8, fill=(255, 255, 255), outline=BORDER_COLOR, width=1)
    draw.rectangle([(60, 100), (590, 145)], fill=(241, 245, 249))
    draw.text((80, 112), "NASDAQ (NQ) - Sweeps C2 Low (Lower Low)", fill=TEXT_COLOR, font=get_font(14, bold=True))
    
    # Right Box: ES
    draw.rounded_rectangle([(650, 100), (1180, 640)], radius=8, fill=(255, 255, 255), outline=BORDER_COLOR, width=1)
    draw.rectangle([(650, 100), (1180, 145)], fill=(241, 245, 249))
    draw.text((670, 112), "S&P 500 (ES) - Fails to Sweep (Higher Low)", fill=TEXT_COLOR, font=get_font(14, bold=True))
    
    # NQ Candles
    nq_candles = [
        (130, 330, 320, 400, 390),
        (170, 390, 380, 460, 450), # Low 1 (460)
        (210, 450, 420, 455, 425),
        (250, 425, 420, 510, 500), # Low 2 sweeps Low 1! (510) -> LOWER LOW
        (290, 495, 430, 500, 435),
        (330, 435, 370, 440, 375),
    ]
    for c in nq_candles:
        draw_candle(draw, c[0], c[1], c[2], c[3], c[4], width=20)
        
    draw.line([(180, 460), (260, 510)], fill=RED_BORDER, width=3)
    draw.text((180, 525), "NQ: Lower Low (C2 Manipulation Sweep)", fill=RED_BORDER, font=get_font(12, bold=True))
    
    # ES Candles
    es_candles = [
        (720, 330, 320, 400, 390),
        (760, 390, 380, 470, 460), # Low 1 (470)
        (800, 460, 420, 465, 425),
        (840, 425, 420, 445, 440), # Low 2 stays above Low 1! (445) -> HIGHER LOW
        (880, 440, 380, 445, 385),
        (920, 385, 330, 390, 335),
    ]
    for c in es_candles:
        draw_candle(draw, c[0], c[1], c[2], c[3], c[4], width=20)
        
    draw.line([(770, 470), (850, 445)], fill=GREEN_BORDER, width=3)
    draw.text((770, 525), "ES: Higher Low (Smart Money Accumulation)", fill=GREEN_BORDER, font=get_font(12, bold=True))
    
    draw.rounded_rectangle([(510, 250), (750, 310)], radius=8, fill=(243, 232, 255), outline=PURPLE_ACCENT, width=2)
    draw.text((525, 265), "SMT DIVERGENCE CONFIRMED", fill=PURPLE_ACCENT, font=get_font(13, bold=True))
    draw.text((545, 285), "Heavy Institutional Accumulation", fill=TEXT_COLOR, font=get_font(11))
    
    img.save("docs/assets/images/models/smt_divergence_anatomy.png", "PNG")

if __name__ == "__main__":
    generate_model_1_image()
    generate_model_2_image()
    generate_model_3_image()
    generate_model_4_image()
    generate_cycle_image()
    generate_smt_image()
    print("All visual chart assets regenerated successfully!")
