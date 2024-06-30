import tkinter as tk
from tkinter import *

import concurrent.futures
from fractions import *
from sympy import *

version_of_calc = "Ver. 1.4.1"
url_help = "https://docs.google.com/forms/d/e/1FAIpQLSfRlg5Wo8wQpya0evQ00vT6waKZlB-eNCyYJY4q9T8ApKBemw/viewform?usp=sf_link"
key = ""
language = "Vietnamese"
choose_language = ["English", "Vietnamese", "Chinese", "Japanese"]
solve_thread = None
executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
x = Symbol("x")

expression = ["|"]
output = ""
ans = 0
enter_eq = 0
limit_low = -10**300
limit_high = 10**300
limit_low_result = 10**(-7)
limit_high_result = 10**10
mode = "d"
imag = "OFF"
deci = "OFF"
fix_num = 9
shift_select = False

list_cal = ["h", "ħ", "c₀", "ε₀", "μ₀", "Z₀", "G", "lₚ", "tₚ", "μɴ", "μʙ", "e", "Φ₀", "G₀", "Kᴊ", "Rᴋ", "mₚ", "mₙ", "mₑ", "mμ", "a₀", "α", "rₑ", "λc", "γₚ", "λcₚ", "λcₙ", "R∞", "μₚ", "μₑ", "μₙ", "μμ", "mτ", "u", "F", "Nᴀ", "k", "Vₘ", "R", "c₁", "c₂", "σ", "g", "atm", "Rₖ_₉₀", "Kᴊ_₉₀", "t", "φ", "sin(", "cos(", "tan(", "asin(", "acos(", "atan(", "log(", "frac(", "GCD(", "LCM(", "(", "√(", "π", "e", "∆", "Ran#", "RanInt#(", "abs(", chr(1200), "x"]
list_num = ["0", "1", "2", "3", "4", "5", "6", "7" ,"8", "9", ".", ")", "∆", "π", "e", "h", "ħ", "c₀", "ε₀", "μ₀", "Z₀", "G", "lₚ", "tₚ", "μɴ", "μʙ", "e", "Φ₀", "G₀", "Kᴊ", "Rᴋ", "mₚ", "mₙ", "mₑ", "mμ", "a₀", "α", "rₑ", "λc", "γₚ", "λcₚ", "λcₙ", "R∞", "μₚ", "μₑ", "μₙ", "μμ", "mτ", "u", "F", "Nᴀ", "k", "Vₘ", "R", "c₁", "c₂", "σ", "g", "atm", "Rₖ_₉₀", "Kᴊ_₉₀", "t", "φ", "Ran#", chr(1200), "x"]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "%", "h", "ħ", "c₀", "ε₀", "μ₀", "Z₀", "G", "lₚ", "tₚ", "μɴ", "μʙ", "e", "Φ₀", "G₀", "Kᴊ", "Rᴋ", "mₚ", "mₙ", "mₑ", "mμ", "a₀", "α", "rₑ", "λc", "γₚ", "λcₚ", "λcₙ", "R∞", "μₚ", "μₑ", "μₙ", "μμ", "mτ", "u", "F", "Nᴀ", "k", "Vₘ", "R", "c₁", "c₂", "σ", "g", "atm", "Rₖ_₉₀", "Kᴊ_₉₀", "t", "φ", "∆", "π", "e", chr(1200), "x"]
power_number = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]

out1_cache = ""
out2_cache = ""
expression_cache = []
cache_count = -1
calc_mode = "Normal"
min_scroll, max_scroll, select_scroll = [0], [3], 0
address_select = []
select_item = []

Catalog_select = [
["Scientific Constant",
[["Math", ["π", "e", "i", "φ"]], ["Universal", ["h", "ħ", "c₀", "ε₀", "μ₀", "Z₀", "G", "lₚ", "tₚ"]],
["Electromagnetic", ["μɴ", "μʙ", "Cₑ", "Φ₀", "G₀", "Kᴊ", "Rᴋ"]],
["Atomic & Nuclear", ["mₚ", "mₙ", "mₑ", "mμ", "a₀", "α", "rₑ", "λc", "γₚ", "λcₚ", "λcₙ", "R∞", "μₚ", "μₑ", "μₙ", "μμ", "mτ"]],
["Physico - Chem", ["u", "F", "Nᴀ", "k", "Vₘ", "R", "c₁", "c₂", "σ"]],
["Adopted Values", ["g", "atm", "Rₖ_₉₀", "Kᴊ_₉₀"]],
["Other", ["t"]]]],

["Unit Conversions",
[["Length", ["in▶cm", "cm▶in", "ft▶m", "m▶ft", "yd▶m", "m▶yd", "mile▶km", "km▶mile", "n mile▶m", "m▶n mile", "pc▶km", "km▶pc"]],
["Area", ["acre▶m²", "m²▶acre"]],
["Volume", ["gal(US)▶L", "L▶gal(US)", "gal(UK)▶L", "L▶gal(UK)"]],
["Mass", ["oz▶g", "g▶oz", "lb▶kg", "kg▶lb"]],
["Velocity", ["km/h▶m/s", "m/s▶km/h"]],
["Pressure", ["atm▶Pa", "Pa▶atm", "mmHg▶Pa", "Pa▶mmHg", "kgf/cm²▶Pa", "Pa▶kgf/cm²", "lbf/in²▶kPa", "kPa▶lbf/in²"]],["Energy", ["kgf•m▶J", "J▶kgf•m", "J▶cal₁₅", "cal₁₅▶J"]],
["Power", ["hp▶kW", "kW▶hp"]],
["Temperature", ["°F▶°C", "°C▶°F"]]]],

["Probability",
["%", "!", "Ran#", "RanInt#("]],

["Numerical Calculation",
["GCD(", "LCM(", "abs("]],

["Hyperbolic/Trigonometric",
["sinh(", "cosh(", "tanh(", "asinh(", "acosh(", "atanh(", "sin(", "cos(", "tan(", "asin(", "acos(", "atan("]]]

name_conversions = [
["in▶cm", "(", "*2.54)"],
["cm▶in", "(", "/2.54)"],
["ft▶m", "(", "*0.3048)"],
["m▶ft", "(", "/0.3048)"],
["yd▶m", "(", "*0.9144)"],
["m▶yd", "(", "/0.9144)"],
["mile▶km", "(", "*1.60934)"],
["km▶mile", "(", "/1.60934)"],
["n mile▶m", "(", "*1852)"],
["m▶n mile", "(", "/1852)"],
["pc▶km", "(", "*30856778570831.27)"],
["km▶pc", "(", "/30856778570831.27)"],
["acre▶m²", "(", "*4046.873)"],
["m²▶acre", "(", "/4046.873)"],
["gal(US)▶L", "(", "*3.785411784)"],
["L▶gal(US)", "(", "/3.785411784)"],
["gal(UK)▶L", "(", "*4.54609)"],
["L▶gal(UK)", "(", "/4.54609)"],
["oz▶g", "(", "*28.3495231)"],
["g▶oz", "(", "/28.3495231)"],
["lb▶kg", "(", "*0.45359237)"],
["kg▶lb", "(", "/0.45359237)"],
["km/h▶m/s", "(", "/3.6)"],
["m/s▶km/h", "(", "*3.6)"],
["atm▶Pa", "(", "*101325)"],
["Pa▶atm", "(", "/101325)"],
["mmHg▶Pa", "(", "*133.322387415)"],
["Pa▶mmHg", "(", "/133.322387415)"],
["kgf/cm²▶Pa", "(", "*9.8066520482)"],
["Pa▶kgf/cm²", "(", "/9,8066520482)"],
["lbf/in²▶kPa", "(", "*6.89475729)"],
["kPa▶lbf/in²", "(", "/6.89475729)"],
["kgf•m▶J", "(", "*9.80665)"],
["J▶kgf•m", "(", "/9.80665)"],
["J▶cal₁₅", "(", "*0.2389029576)"],
["cal₁₅▶J", "(", "/0.2389029576)"],
["hp▶kW", "(", "*0.745699872)"],
["kW▶hp", "(", "/0.745699872)"],
["°F▶°C", "((", "-32)*5/9)"],
["°C▶°F", "((", "*9/5)+32)"]
]

#Task processing variable
x = 0
φ = 1.6180339887
h = 6.62607015*10**(-34)
ħ = 1.0545718*10**(-34)
c0 = 299792458
ε0 = 8.854187817*10**(-12)
μ0 = 1.2566370614*10**(-6)
Z0 = 376.730313461
G = 6.67408*10**(-11)
lₚ = 1.616229*10**(-35)
tₚ = 5.39116*10**(-44)
μɴ = 5.050783699*10**(-27)
μʙ = 9.274009994*10**(-24)
Cₑ = 1.6021766208*10**(-19)
Φ0 = 2.067833831*10**(-15)
G0 = 7.7480917310**10**(-5)
Kᴊ = 483597.8525*10**9
Rᴋ = 25812.8074555
mₚ = 1.672621898*10**(-27)
mₙ = 1.674927471*10**(-27)
mₑ = 9.10938356*10**(-31)
mμ = 1.883531594*10**(-28)
a0 = 0.52917721067*10**(-10)
α = 7.2973525664*10**(-3)
rₑ = 2.8179403227*10**(-15)
λc = 2.4263102367*10**(-12)
γₚ = 2.675221900*10**8
λcₚ = 1.32140985396*10**(-15)
λcₙ = 1.31959090481*10**(-15)
Rinf = 10973731.568508
μₚ = 1.4106067873*10**(-26)
μₑ = -928.4764620*10**(-26)
μₙ = -0.96623650*10**(-26)
μμ = -4.49044826*10**(-26)
mτ = 3.16747*10**(-27)
u = 1.660539040*10**(-27)
F = 96485.33289
Nᴀ = 6.022140857*10**23
k = 1.38064852*10**(-23)
Vₘ = 22.710947*10**(-3)
R = 8.3144598
c1 = 3.741771790*10**(-16)
c2 = 1.43877736*10**(-2)
σ = 5.670367*10**(-8)
g = 9.80665
atm = 101325
Rₖ_90 = 25812.807
Kᴊ_90 = 483597.9*10**9
t = 273.15

calculator_screen = ''
calculator_screen_out = ''
out1=tk.Label()
out2=tk.Label()
button_prime_number_analysis=tk.Label()
up_cache=tk.Label()
down_cache=tk.Label()
shift_screen=tk.Label()
button_Ans=tk.Label()
button_ON=tk.Label()
button_check=tk.Label()
button_OFF=tk.Label()
button_shift=tk.Label()
button_left=tk.Label()
button_right=tk.Label()
button_OK=tk.Label()
button_up=tk.Label()
button_down=tk.Label()
button_catalog=tk.Label()
button_end_left=tk.Label()
button_end_right=tk.Label()
button_1=tk.Label()
button_2=tk.Label()
button_3=tk.Label()
button_del=tk.Label()
button_ac=tk.Label()
button_4=tk.Label()
button_5=tk.Label()
button_6=tk.Label()
button_time=tk.Label()
button_div=tk.Label()
button_7=tk.Label()
button_8=tk.Label()
button_9=tk.Label()
button_plus=tk.Label()
button_minus=tk.Label()
button_0=tk.Label()
button_dot=tk.Label()
button_pi=tk.Label()
button_euler=tk.Label()
button_equal=tk.Label()
button_sin=tk.Label()
button_cos=tk.Label()
button_tan=tk.Label()
button_open_parenthesis=tk.Label()
button_sqrt=tk.Label()
button_asin=tk.Label()
button_acos=tk.Label()
button_atan=tk.Label()
button_close_parenthesis=tk.Label()
button_log=tk.Label()
button_sigma=tk.Label()
button_x_var=tk.Label()
button_comma=tk.Label()
button_frac=tk.Label()
degree_mode_txt=tk.Label()
button_d_mode=tk.Label()
button_r_mode=tk.Label()
text_imagnum_mode=tk.Label()
button_ON_imagnum_mode=tk.Label()
button_OFF_imagnum_mode=tk.Label()
text_decimal_mode=tk.Label()
button_ON_decimal_mode=tk.Label()
button_OFF_decimal_mode=tk.Label()
button_reset_mode=tk.Label()