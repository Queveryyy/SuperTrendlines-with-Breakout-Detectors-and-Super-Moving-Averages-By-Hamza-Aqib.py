// © HamzaAqib

//@version=5
indicator("SuperTrendlines with Breakout Detectors and Super Moving Averages By Hamza Aqib", "Hamza Aqib - SuperTrendlines with Breakout Detectors and Super Moving Averages", overlay = true)


Periods = input(title='ATR Period 1', defval=10)
srcc = input(hl2, title='Source 1')
Multiplier = input.float(title='ATR Multiplier 1', step=0.1, defval=1.0)

// calculations
atr = ta.atr(Periods)
up = srcc - Multiplier * atr
up1 = nz(up[1], up)
up := close[1] > up1 ? math.max(up, up1) : up
dn = srcc + Multiplier * atr
dn1 = nz(dn[1], dn)
dn := close[1] < dn1 ? math.min(dn, dn1) : dn
trend = 1
trend := nz(trend[1], trend)

// plotting
trend := trend == -1 and close > dn1 ? 1 : trend == 1 and close < up1 ? -1 : trend
upPlot = plot(trend == 1 ? up : na, title='Up Trend', style=plot.style_linebr, linewidth=2, color=color.rgb(0, 255, 213))
greenSignal_1 = trend == 1 and trend[1] == -1
plotshape(greenSignal_1 ? up : na, title='UpTrend Begins', location=location.absolute, style=shape.circle, size=size.tiny, color=color.rgb(0, 255, 213))
dnPlot = plot(trend == 1 ? na : dn, title='Down Trend', style=plot.style_linebr, linewidth=2, color=color.new(#ffffff, 0))
redSignal_1 = trend == -1 and trend[1] == 1
plotshape(redSignal_1 ? dn : na, title='DownTrend Begins', location=location.absolute, style=shape.circle, size=size.tiny, color=color.new(#ffffff, 0))

// inputs
Periods2 = input(title='ATR Period 2', defval=11)
src2 = input(hl2, title='Source 2')
Multiplier2 = input.float(title='ATR Multiplier 2', step=0.1, defval=2.0)

// calculations
atr_2 = ta.atr(Periods2)
up_2 = src2 - Multiplier2 * atr_2
up1_2 = nz(up_2[1], up_2)
up_2 := close[1] > up1_2 ? math.max(up_2, up1_2) : up_2
dn_2 = src2 + Multiplier2 * atr_2
dn1_2 = nz(dn_2[1], dn_2)
dn_2 := close[1] < dn1_2 ? math.min(dn_2, dn1_2) : dn_2
trend_2 = 1
trend_2 := nz(trend_2[1], trend_2)

// plotting
trend_2 := trend_2 == -1 and close > dn1_2 ? 1 : trend_2 == 1 and close < up1 ? -1 : trend_2
upPlot_2 = plot(trend_2 == 1 ? up_2 : na, title='Up Trend', style=plot.style_linebr, linewidth=2, color=color.rgb(0, 174, 255))
greenSignal_2 = trend_2 == 1 and trend_2[1] == -1
plotshape(greenSignal_2 ? up_2 : na, title='UpTrend Begins', location=location.absolute, style=shape.circle, size=size.tiny, color=color.rgb(0, 174, 255))
dnPlot_2 = plot(trend_2 == 1 ? na : dn_2, title='Down Trend', style=plot.style_linebr, linewidth=2, color=color.new(#b1b1b1, 0))
redSignal_2 = trend_2 == -1 and trend_2[1] == 1
plotshape(redSignal_2 ? dn_2 : na, title='DownTrend Begins', location=location.absolute, style=shape.circle, size=size.tiny, color=color.new(#b1b1b1, 0))

// inputs
Periods3 = input(title='ATR Period 3', defval=12)
src3 = input(hl2, title='Source 3')
Multiplier3 = input.float(title='ATR Multiplier 3', step=0.1, defval=3.0)

// calculations
atr_3 = ta.atr(Periods3)
up_3 = src3 - Multiplier3 * atr_3
up1_3 = nz(up_3[1], up_3)
up_3 := close[1] > up1_3 ? math.max(up_3, up1_3) : up_3
dn_3 = src3 + Multiplier3 * atr_3
dn1_3 = nz(dn_3[1], dn_3)
dn_3 := close[1] < dn1_3 ? math.min(dn_3, dn1_3) : dn_3
trend_3 = 1
trend_3 := nz(trend_3[1], trend_3)

// plotting
trend_3 := trend_3 == -1 and close > dn1_3 ? 1 : trend_3 == 1 and close < up1 ? -1 : trend_3
upPlot_3 = plot(trend_3 == 1 ? up_3 : na, title='Up Trend', style=plot.style_linebr, linewidth=2, color=color.rgb(0, 47, 255))
greenSignal_3 = trend_3 == 1 and trend_3[1] == -1
plotshape(greenSignal_3 ? up_3 : na, title='UpTrend Begins', location=location.absolute, style=shape.circle, size=size.tiny, color=color.rgb(0, 47, 255))
dnPlot_3 = plot(trend_3 == 1 ? na : dn_3, title='Down Trend', style=plot.style_linebr, linewidth=2, color=color.new(#666565, 0))
redSignal_3 = trend_3 == -1 and trend_3[1] == 1
plotshape(redSignal_3 ? dn_3 : na, title='DownTrend Begins', location=location.absolute, style=shape.circle, size=size.tiny, color=color.new(#666565, 0))

green_alert = not ( trend == -1 or trend_2 == -1 or trend_3 == -1 ) and ( trend[1] == -1 or trend_2[1] == -1 or trend_3[1] == -1 )
red_alert = not ( trend == 1 or trend_2 == 1 or trend_3 == 1 ) and ( trend[1] == 1 or trend_2[1] == 1 or trend_3[1] == 1 )

alertcondition(green_alert, "Triple Supertrend Green", "Triple Supertrend lines are all green.")
alertcondition(red_alert, "Triple Supertrend Red", "Triple Supertrend lines are all red.")

//------------------------------------------------------------------------------
//Settings
//-----------------------------------------------------------------------------{
length = input.int(14, 'Swing Detection Lookback')
mult = input.float(1., 'Slope', minval = 0, step = .1)
calcMethod = input.string('Atr', 'Slope Calculation Method', options = ['Atr','Stdev','Linreg'])
backpaint = input(true, tooltip = 'Backpainting offset displayed elements in the past. Disable backpainting to see real time information returned by the indicator.')

//Style
upCss = input.color(color.rgb(0, 68, 255), 'Up Trendline Color', group = 'Style')
dnCss = input.color(color.rgb(0, 255, 255), 'Down Trendline Color', group = 'Style')
showExt = input(true, 'Show Extended Lines')

//-----------------------------------------------------------------------------}
//Calculations
//-----------------------------------------------------------------------------{
var upper = 0.
var lower = 0.
var slope_ph = 0.
var slope_pl = 0.

var offset = backpaint ? length : 0

n = bar_index
src = close

ph = ta.pivothigh(length, length)
pl = ta.pivotlow(length, length)

//Slope Calculation Method
slope = switch calcMethod
    'Atr'    => ta.atr(length) / length * mult
    'Stdev'  => ta.stdev(src,length) / length * mult
    'Linreg' => math.abs(ta.sma(src * n, length) - ta.sma(src, length) * ta.sma(n, length)) / ta.variance(n, length) / 2 * mult

//Get slopes and calculate trendlines
slope_ph := ph ? slope : slope_ph
slope_pl := pl ? slope : slope_pl

upper := ph ? ph : upper - slope_ph
lower := pl ? pl : lower + slope_pl

var upos = 0
var dnos = 0
upos := ph ? 0 : close > upper - slope_ph * length ? 1 : upos
dnos := pl ? 0 : close < lower + slope_pl * length ? 1 : dnos

//-----------------------------------------------------------------------------}
//Extended Lines
//-----------------------------------------------------------------------------{
var uptl  = line.new(na,na,na,na, color = upCss, style = line.style_dashed, extend = extend.right)
var dntl  = line.new(na,na,na,na, color = dnCss, style = line.style_dashed, extend = extend.right)

if ph and showExt
    uptl.set_xy1(n-offset, backpaint ? ph : upper - slope_ph * length)
    uptl.set_xy2(n-offset+1, backpaint ? ph - slope : upper - slope_ph * (length+1))

if pl and showExt
    dntl.set_xy1(n-offset, backpaint ? pl : lower + slope_pl * length)
    dntl.set_xy2(n-offset+1, backpaint ? pl + slope : lower + slope_pl * (length+1))

//-----------------------------------------------------------------------------}
//Plots
//-----------------------------------------------------------------------------{
plot(backpaint ? upper : upper - slope_ph * length, 'Upper', color = ph ? na : upCss, offset = -offset)
plot(backpaint ? lower : lower + slope_pl * length, 'Lower', color = pl ? na : dnCss, offset = -offset)

//Breakouts
plotshape(upos > upos[1] ? low : na, "Upper Break"
  , shape.labelup
  , location.absolute
  , upCss
  , text = "Breakout Detected"
  , textcolor = color.rgb(0, 255, 213)
  , size = size.tiny)

plotshape(dnos > dnos[1] ? high : na, "Lower Break"
  , shape.labeldown
  , location.absolute
  , dnCss
  , text = "Breakout Detected"
  , textcolor = color.rgb(0, 68, 255)
  , size = size.tiny)

//-----------------------------------------------------------------------------}
//Alerts
//-----------------------------------------------------------------------------{
alertcondition(upos > upos[1], 'Upward Breakout', 'Price broke the down-trendline upward')
alertcondition(dnos > dnos[1], 'Downward Breakout', 'Price broke the up-trendline downward')

//-----------------------------------------------------------------------------}


//Format for a 10
len4 = input.int(8, minval=1, title="Length of the 1st Super Moving Average!")
src4 = input(close, title="Source")
out4 = ta.ema(src4, len4)
plot(out4, color=color.rgb(0, 81, 255), title="The First Super Moving Average", style=plot.style_stepline, linewidth = 3)
//End of format

//Format for a 50
len5 = input.int(55, minval=1, title="Length of the 2nd Super Moving Average!")
src5 = input(close, title="Source")
out5 = ta.ema(src5, len5)
plot(out5, color=color.rgb(0, 247, 255), title="The Second Super Moving Average", style=plot.style_stepline, linewidth = 3)
//End of format

//Format for a 200
len6 = input.int(200, minval=1, title="Length of the 3rd Super Moving Average!")
src6 = input(close, title="Source")
out6 = ta.ema(src6, len6)
plot(out6, color=color.white, title="The Third Super Moving Average", style=plot.style_stepline, linewidth = 3)
//End of format
//Come Check out some of my other projects at https://github.com/Queveryyy!!!