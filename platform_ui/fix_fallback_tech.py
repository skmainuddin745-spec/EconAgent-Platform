with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/fractal_zoom_engine.py', 'r', encoding='utf-8') as f:
    code = f.read()

target = """    var tech = data.technicalSOIC || {
      adx: { val: 34.8, cond: 'Healthy Trend (20-40 Range)', pts: 10, max: 20 },
      rsi: { val: 58.5, cond: 'Between 50 to 75 (High Momentum Sweet Spot)', pts: 10, max: 10 },
      stage: { val: 'Stage 2 (Mark Up)', cond: 'Confirmed breakout above rising 30-WMA', pts: 20, max: 20 },
      pva: { val: 'Positive Trend', cond: 'High volume on gain days / institutional accumulation', pts: 20, max: 20 },
      secondary: { val: 'Uptrend', cond: 'Orderly pullback to 10-WEMA with dry volume', pts: 10, max: 10 },
      vstop: { val: 'Holding Above Vol Stop', cond: 'Stop loss intact / trailing trend', pts: 10, max: 10 },
      baseCount: { val: 'Base 1 / Base 2', cond: 'Fresh structural accumulation base', pts: 20, max: 20 }
    };"""

replacement = """    var tech = data.technicalSOIC || {
      adx: { val: 34.8, cond: 'Above 40 (Monster Bullish Trend)', pts: 20, max: 20 },
      rsi: { val: 64.2, cond: 'Between 50 to 75 (High Momentum Sweet Spot)', pts: 10, max: 10 },
      stage: { val: 'Stage 2 (Mark Up)', cond: 'Confirmed breakout above rising 30-WMA', pts: 20, max: 20 },
      pva: { val: 'Positive Trend', cond: 'High volume on gain days / institutional accumulation', pts: 20, max: 20 },
      secondary: { val: 'Uptrend', cond: 'Orderly pullback to 10-WEMA with dry volume', pts: 10, max: 10 },
      primary: { val: 'Uptrend', cond: 'Trading above rising 30-WMA & 200-DMA', pts: 10, max: 10 },
      resistance: { val: 'Breakout', cond: 'Close to 52-Week High / ATH Breakout (<15%)', pts: 5, max: 5 },
      vstop: { val: 'Holding Above Vol Stop', cond: 'Trailing volatility stop intact', pts: 10, max: 10 }
    };"""

if target not in code:
    raise ValueError("target not found in fractal_zoom_engine.py")

code = code.replace(target, replacement)

with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/fractal_zoom_engine.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully updated fallback tech object with all 8 SOIC technical pillars!")

