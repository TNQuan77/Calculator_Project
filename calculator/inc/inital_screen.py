import tkinter as tk
from tkinter import *

import inc.variable_global
from inc.func import *

def init_screen():
    app = tk.Tk()
    app.geometry("720x1080")
    app.title("Calculator Project")

    # Configure grid weights for resizing
    for i in range(15):  # Adjust number based on total rows
        app.grid_rowconfigure(i, weight=1)
    for j in range(10):  # Adjust number based on total columns
        app.grid_columnconfigure(j, weight=1)

    inc.variable_global.calculator_screen = Frame(app, bg="black")
    inc.variable_global.calculator_screen.grid(row=0, column=0, columnspan=10, sticky="nsew")

    inc.variable_global.calculator_screen_out = Frame(app, bg="black")
    inc.variable_global.calculator_screen_out.grid(row=1, column=0, columnspan=10, sticky="nsew")
    
    inc.variable_global.out1 = tk.Label(inc.variable_global.calculator_screen, text="expression", bg="black", fg="white", justify="left", anchor="nw")
    inc.variable_global.out1.grid(row=0, column=0, columnspan=10, sticky="nsew")

    inc.variable_global.out2 = tk.Label(inc.variable_global.calculator_screen_out, text="output", bg="black", fg="white", justify="right", anchor="e")
    inc.variable_global.out2.grid(row=0, column=0, columnspan=10, sticky="nsew")
    
    # row 3
    inc.variable_global.button_ON = tk.Button(app, text="ON", bg="white", command=lambda: on())
    inc.variable_global.button_ON.grid(row=3, column=0, sticky="nsew")
    
    inc.variable_global.button_check = tk.Button(app, text="Check", bg="white", font=("", 5), command=lambda: check())
    inc.variable_global.button_check.grid(row=3, column=1, sticky="nsew")
    
    inc.variable_global.button_up = tk.Button(app, text="˄", bg="white", command=lambda: bar_up())
    inc.variable_global.button_up.grid(row=3, column=4, sticky="nsew")
    
    inc.variable_global.shift_screen = tk.Label(app, text="S", bg="black", fg="black")
    inc.variable_global.shift_screen.grid(row=3, column=7, sticky="nsew")
    
    inc.variable_global.down_cache = tk.Label(app, text="↓", bg="black", fg="black")
    inc.variable_global.down_cache.grid(row=3, column=8, sticky="nsew")
    
    inc.variable_global.up_cache = tk.Label(app, text="↑", bg="black", fg="black")
    inc.variable_global.up_cache.grid(row=3, column=9, sticky="nsew")
    
    # row 4
    inc.variable_global.button_OFF = tk.Button(app, text="OFF", bg="white", command=lambda: off_calc_1(app))
    inc.variable_global.button_OFF.grid(row=4, column=0, sticky="nsew")
    
    inc.variable_global.button_shift = tk.Button(app, text="Shift", bg="white", command=lambda: shift())
    inc.variable_global.button_shift.grid(row=4, column=1, sticky="nsew")
    
    inc.variable_global.button_left = tk.Button(app, text="<", bg="white", command=lambda: bar_left())
    inc.variable_global.button_left.grid(row=4, column=3, sticky="nsew")

    inc.variable_global.button_OK = tk.Button(app, text="OK", bg="white", command=lambda: solve_screen())
    inc.variable_global.button_OK.grid(row=4, column=4, sticky="nsew")
    
    inc.variable_global.button_right = tk.Button(app, text=">", bg="white", command=lambda: bar_right())
    inc.variable_global.button_right.grid(row=4, column=5, sticky="nsew")

    inc.variable_global.button_Ans = tk.Button(app, text="∆ = 0", bg="black", fg="white", justify="left", anchor="nw", wraplength=330, font=("Arial", 5), command=lambda: add("∆"))
    inc.variable_global.button_Ans.grid(row=4, column=7, columnspan=3, sticky="nsew")

    # row 5
    inc.variable_global.button_down = tk.Button(app, text="˅", bg="white", command=lambda: bar_down())
    inc.variable_global.button_down.grid(row=5, column=4, sticky="nsew")
    
    inc.variable_global.button_catalog = tk.Button(app, text="ctl", bg="white", command=lambda: catalog())
    inc.variable_global.button_catalog.grid(row=5, column=7, sticky="nsew")
    
    inc.variable_global.button_end_left = tk.Button(app, text="←", fg="blue", command=lambda: end_left())
    inc.variable_global.button_end_left.grid(row=5, column=8, sticky="nsew")
    
    inc.variable_global.button_end_right = tk.Button(app, text="→", fg="blue", command=lambda: end_right())
    inc.variable_global.button_end_right.grid(row=5, column=9, sticky="nsew")
    
    # row 7
    inc.variable_global.button_1 = tk.Button(app, text="1", bg="white", command=lambda: add("1"))
    inc.variable_global.button_1.grid(row=7, column=0, sticky="nsew")
    
    inc.variable_global.button_2 = tk.Button(app, text="2", bg="white", command=lambda: add("2"))
    inc.variable_global.button_2.grid(row=7, column=1, sticky="nsew")
    
    inc.variable_global.button_3 = tk.Button(app, text="3", bg="white", command=lambda: add("3"))
    inc.variable_global.button_3.grid(row=7, column=2, sticky="nsew")
    
    inc.variable_global.button_del = tk.Button(app, text="Del", bg="white", command=lambda: delete())
    inc.variable_global.button_del.grid(row=7, column=3, sticky="nsew")
    
    inc.variable_global.button_ac = tk.Button(app, text="AC", bg="white", command=lambda: ac())
    inc.variable_global.button_ac.grid(row=7, column=4, sticky="nsew")
    
    # row 8
    inc.variable_global.button_4 = tk.Button(app, text="4", bg="white", command=lambda: add("4"))
    inc.variable_global.button_4.grid(row=8, column=0, sticky="nsew")
    
    inc.variable_global.button_5 = tk.Button(app, text="5", bg="white", command=lambda: add("5"))
    inc.variable_global.button_5.grid(row=8, column=1, sticky="nsew")
    
    inc.variable_global.button_6 = tk.Button(app, text="6", bg="white", command=lambda: add("6"))
    inc.variable_global.button_6.grid(row=8, column=2, sticky="nsew")
    
    inc.variable_global.button_time = tk.Button(app, text="×", bg="white", command=lambda: add("×"))
    inc.variable_global.button_time.grid(row=8, column=3, sticky="nsew")
    
    inc.variable_global.button_div = tk.Button(app, text="÷", bg="white", command=lambda: add("÷"))
    inc.variable_global.button_div.grid(row=8, column=4, sticky="nsew")
    
    # row 9
    inc.variable_global.button_7 = tk.Button(app, text="7", bg="white", command=lambda: add("7"))
    inc.variable_global.button_7.grid(row=9, column=0, sticky="nsew")
    
    inc.variable_global.button_8 = tk.Button(app, text="8", bg="white", command=lambda: add("8"))
    inc.variable_global.button_8.grid(row=9, column=1, sticky="nsew")
    
    inc.variable_global.button_9 = tk.Button(app, text="9", bg="white", command=lambda: add("9"))
    inc.variable_global.button_9.grid(row=9, column=2, sticky="nsew")
    
    inc.variable_global.button_plus = tk.Button(app, text="+", bg="white", command=lambda: add("+"))
    inc.variable_global.button_plus.grid(row=9, column=3, sticky="nsew")
    
    inc.variable_global.button_minus = tk.Button(app, text="-", bg="white", command=lambda: add("-"))
    inc.variable_global.button_minus.grid(row=9, column=4, sticky="nsew")
    
    # row 10
    inc.variable_global.button_0 = tk.Button(app, text="0", bg="white", command=lambda: add("0"))
    inc.variable_global.button_0.grid(row=10, column=0, sticky="nsew")
    
    inc.variable_global.button_dot = tk.Button(app, text=".", bg="white", command=lambda: add("."))
    inc.variable_global.button_dot.grid(row=10, column=1, sticky="nsew")
    
    inc.variable_global.button_pi = tk.Button(app, text="π", bg="white", command=lambda: add("π"))
    inc.variable_global.button_pi.grid(row=10, column=2, sticky="nsew")
    
    inc.variable_global.button_euler = tk.Button(app, text="e", bg="white", command=lambda: add("e"))
    inc.variable_global.button_euler.grid(row=10, column=3, sticky="nsew")
    
    inc.variable_global.button_equal = tk.Button(app, text="=", bg="white", command=lambda: solve())
    inc.variable_global.button_equal.grid(row=10, column=4, sticky="nsew")
    
    # row 11
    inc.variable_global.button_sin = tk.Button(app, text="sin(", bg="white", command=lambda: add("sin("))
    inc.variable_global.button_sin.grid(row=11, column=0, sticky="nsew")
    
    inc.variable_global.button_cos = tk.Button(app, text="cos(", bg="white", command=lambda: add("cos("))
    inc.variable_global.button_cos.grid(row=11, column=1, sticky="nsew")
    
    inc.variable_global.button_tan = tk.Button(app, text="tan(", bg="white", command=lambda: add("tan("))
    inc.variable_global.button_tan.grid(row=11, column=2, sticky="nsew")
    
    inc.variable_global.button_sqrt = tk.Button(app, text="√(", bg="white", command=lambda: add("√("))
    inc.variable_global.button_sqrt.grid(row=11, column=3, sticky="nsew")
    
    inc.variable_global.button_ln = tk.Button(app, text="ln(", bg="white", command=lambda: add("ln("))
    inc.variable_global.button_ln.grid(row=11, column=4, sticky="nsew")
    
    # row 12
    inc.variable_global.button_log = tk.Button(app, text="log(", bg="white", command=lambda: add("log("))
    inc.variable_global.button_log.grid(row=12, column=0, sticky="nsew")
    
    inc.variable_global.button_exp = tk.Button(app, text="exp(", bg="white", command=lambda: add("exp("))
    inc.variable_global.button_exp.grid(row=12, column=1, sticky="nsew")
    
    inc.variable_global.button_abs = tk.Button(app, text="abs(", bg="white", command=lambda: add("abs("))
    inc.variable_global.button_abs.grid(row=12, column=2, sticky="nsew")
    
    inc.variable_global.button_fact = tk.Button(app, text="!", bg="white", command=lambda: add("!"))
    inc.variable_global.button_fact.grid(row=12, column=3, sticky="nsew")
    
    inc.variable_global.button_lparen = tk.Button(app, text="(", bg="white", command=lambda: add("("))
    inc.variable_global.button_lparen.grid(row=12, column=4, sticky="nsew")
    
    # row 13
    inc.variable_global.button_rparen = tk.Button(app, text=")", bg="white", command=lambda: add(")"))
    inc.variable_global.button_rparen.grid(row=13, column=0, sticky="nsew")
    
    inc.variable_global.button_ee = tk.Button(app, text="EE", bg="white", command=lambda: add("E"))
    inc.variable_global.button_ee.grid(row=13, column=1, sticky="nsew")
    
    inc.variable_global.button_rad = tk.Button(app, text="Rad", bg="white", command=lambda: change_unit_rad())
    inc.variable_global.button_rad.grid(row=13, column=2, sticky="nsew")
    
    inc.variable_global.button_deg = tk.Button(app, text="Deg", bg="white", command=lambda: change_unit_deg())
    inc.variable_global.button_deg.grid(row=13, column=3, sticky="nsew")
    
    inc.variable_global.button_mplus = tk.Button(app, text="M+", bg="white", command=lambda: mplus())
    inc.variable_global.button_mplus.grid(row=13, column=4, sticky="nsew")
    
    # row 14
    inc.variable_global.button_mr = tk.Button(app, text="MR", bg="white", command=lambda: mr())
    inc.variable_global.button_mr.grid(row=14, column=0, sticky="nsew")
    
    inc.variable_global.button_ms = tk.Button(app, text="MS", bg="white", command=lambda: ms())
    inc.variable_global.button_ms.grid(row=14, column=1, sticky="nsew")
    
    inc.variable_global.button_mc = tk.Button(app, text="MC", bg="white", command=lambda: mc())
    inc.variable_global.button_mc.grid(row=14, column=2, sticky="nsew")

    inc.variable_global.button_prime_number_analysis = tk.Button(app, text = "PNA", fg = "blue", command = lambda: PNA(), state = "disable")
    inc.variable_global.button_prime_number_analysis.grid(row=14, column=3, sticky="nsew")


    return app

# app = init_screen()
# app.mainloop()
