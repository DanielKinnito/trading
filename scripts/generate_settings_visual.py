"""
Generate settings dialog and indicator overview graphics.
"""
from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs("docs/assets/images/indicator", exist_ok=True)

BG_COLOR = (255, 255, 255)
BORDER_COLOR = (226, 232, 240)
TEXT_COLOR = (15, 23, 42)
MUTED_TEXT = (100, 116, 139)
BLUE_CISD = (37, 99, 235)

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

def generate_settings_dialog():
    img = Image.new("RGBA", (1000, 640), (248, 250, 252))
    draw = ImageDraw.Draw(img)
    
    # Dialog Window Box (Centered)
    wx, wy, ww, wh = 100, 40, 800, 560
    draw.rounded_rectangle([(wx, wy), (wx + ww, wy + wh)], radius=12, fill=(255, 255, 255), outline=BORDER_COLOR, width=2)
    
    # Title Bar
    draw.rectangle([(wx, wy), (wx + ww, wy + 55)], fill=(255, 255, 255))
    draw.line([(wx, wy + 55), (wx + ww, wy + 55)], fill=BORDER_COLOR, width=1)
    draw.text((wx + 25, wy + 16), "TTrades Fractal Model [Pro+] v6 - Inputs & Settings", fill=TEXT_COLOR, font=get_font(16, bold=True))
    
    # Close X button
    draw.text((wx + ww - 35, wy + 16), "✕", fill=MUTED_TEXT, font=get_font(16, bold=True))
    
    # Tabs
    tabs = ["Inputs", "Style", "Visibility"]
    tx = wx + 25
    for i, t in enumerate(tabs):
        is_active = (i == 0)
        t_font = get_font(13, bold=is_active)
        t_col = BLUE_CISD if is_active else MUTED_TEXT
        draw.text((tx, wy + 70), t, fill=t_col, font=t_font)
        if is_active:
            draw.line([(tx, wy + 95), (tx + 45, wy + 95)], fill=BLUE_CISD, width=3)
        tx += 80
    draw.line([(wx, wy + 96), (wx + ww, wy + 96)], fill=BORDER_COLOR, width=1)
    
    # Form Groups
    groups = [
        ("MODEL & TIMEFRAME CONFIGURATION", [
            ("Preset Model:", "1m - 15m Model (NY AM / London Scalp)", True),
            ("Higher Timeframe (HTF):", "15 minutes", True),
            ("Lower Timeframe (LTF):", "1 minute", True),
            ("Trading Session Filter:", "New York AM (08:30 - 11:00)", True),
            ("Exchange / NY Timezone:", "America/New_York (Automatic DST)", False),
        ]),
        ("VISUAL PLOTTING & PHASES", [
            ("Show C1, C2, C3, C4 Phase Markers:", "Checked", False),
            ("Show CISD Benchmark Dynamic Line:", "Checked (Royal Blue)", False),
            ("Show 50% T-Spot Equilibrium Box:", "Checked (Discount / Premium)", False),
            ("Overlay HTF Candles on Chart Right:", "Checked (Body + Wick)", False),
            ("Show Real-Time Cycle Status Dashboard:", "Checked (Bottom-Right)", False),
        ]),
        ("ALERTS & AUTOMATION", [
            ("Trigger Alert on CISD Body Close:", "Checked", False),
            ("Trigger Alert on C3 T-Spot Mitigation:", "Checked", False),
            ("Alert Execution Mode:", "Any alert() function call (Zero Repaint)", False),
        ])
    ]
    
    curr_y = wy + 115
    for grp_title, fields in groups:
        draw.text((wx + 25, curr_y), grp_title, fill=BLUE_CISD, font=get_font(11, bold=True))
        curr_y += 24
        
        for label, val, is_dropdown in fields:
            draw.text((wx + 40, curr_y + 4), label, fill=TEXT_COLOR, font=get_font(12, bold=False))
            
            # Value box
            bx = wx + 380
            bw = 360
            bh = 26
            draw.rounded_rectangle([(bx, curr_y), (bx + bw, curr_y + bh)], radius=4, fill=(248, 250, 252), outline=BORDER_COLOR, width=1)
            draw.text((bx + 10, curr_y + 4), val, fill=TEXT_COLOR if not is_dropdown else BLUE_CISD, font=get_font(11, bold=is_dropdown))
            if is_dropdown:
                draw.text((bx + bw - 20, curr_y + 4), "▼", fill=MUTED_TEXT, font=get_font(10))
            curr_y += 30
        curr_y += 8
        
    # Buttons at bottom
    bx = wx + ww - 180
    by = wy + wh - 45
    draw.rounded_rectangle([(bx, by), (bx + 70, by + 32)], radius=6, fill=(255, 255, 255), outline=BORDER_COLOR, width=1)
    draw.text((bx + 15, by + 6), "Defaults", fill=TEXT_COLOR, font=get_font(12))
    
    draw.rounded_rectangle([(bx + 80, by), (bx + 160, by + 32)], radius=6, fill=BLUE_CISD)
    draw.text((bx + 108, by + 6), "OK", fill=(255, 255, 255), font=get_font(12, bold=True))
    
    img.save("docs/assets/images/indicator/indicator_settings_dialog.png", "PNG")
    print("Indicator settings dialog image generated!")

if __name__ == "__main__":
    generate_settings_dialog()
