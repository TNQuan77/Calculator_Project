import tkinter as tk
from tkinter import *
import re as r
import random
import sys
from sympy import *
from fractions import *

import threading
import math as m
import webbrowser

import inc.language
import inc.variable_global

def output_exp(output):
	output = str(output)
	output = output.replace("**", "^")
	output = output.replace("*", "×")
	output = output.replace("pi", "π")
	output = output.replace("e+", "×10^")
	output = output.replace("E", "e")
	output = output.replace("I", "i")
	output = output.replace("inc.variable_global.sqrt", "√")
	output = r.sub(r"exp\((.*?)\)", r"e^\1", output)
	return output

def solve_exp(real_exp):
	real_exp = str(real_exp)
	real_exp = real_exp.replace("∆", "(" + str(inc.variable_global.ans) + ")")
	real_exp = real_exp.replace("×", "*")
	real_exp = real_exp.replace("÷", "/")
	real_exp = real_exp.replace("√", "inc.variable_global.sqrt")
	real_exp = real_exp.replace("^", "**")
	real_exp = real_exp.replace("%", "/100")
	real_exp = real_exp.replace("#", "")
	real_exp = real_exp.replace("π", "pi")
	real_exp = real_exp.replace("e", "E")
	real_exp = real_exp.replace("₀", "0")
	real_exp = real_exp.replace("₁", "1")
	real_exp = real_exp.replace("₂", "2")
	real_exp = real_exp.replace("₉", "9")
	real_exp = real_exp.replace("∞", "inf")
	real_exp = real_exp.replace(str(chr(1200)), "I")
	real_exp = real_exp.replace("Σ", "sigma")
	return real_exp

def scr_exp(exp_input):
	exp_output = ""
	for i in exp_input:
		if i == chr(1200):
			exp_output += "i"
		else:
			exp_output += i
	return exp_output

def add(var):
	
	if inc.variable_global.calc_mode == "Catalog":
		return None
	
	if inc.variable_global.calc_mode == "Check":
		return None
		
	if inc.variable_global.calc_mode == "Calculating":
		return None
	
	if inc.variable_global.calc_mode == "Error":
		return None
	
	elif inc.variable_global.calc_mode == "Reset":
		return None
	
	elif "|" in inc.variable_global.expression:
		if inc.variable_global.enter_eq != 0:
			inc.variable_global.expression = ["|"]
			inc.variable_global.enter_eq = 0
		
		if var == "i":
			bar_add(chr(1200))
		
		else:
			bar_add(var)
			
		inc.variable_global.out1.config(text = scr_exp(inc.variable_global.expression))
		
	else:

		inc.variable_global.expression = ["|"]
		output = ""
		inc.variable_global.out1.config(text = "|")
		inc.variable_global.out2.config(text = output)
		inc.variable_global.button_prime_number_analysis.config(state = "disable")

		if (var == "×") or (var == "÷") or (var == "+") or (var == "-") or (var == "^"):
			if inc.variable_global.enter_eq != 0:
				bar_add("∆")
		bar_add(var)
		inc.variable_global.out1.config(text = scr_exp(inc.variable_global.expression))
	inc.variable_global.button_prime_number_analysis.config(state = "disable")
	
	inc.variable_global.enter_eq = 0

def up_down_cache():
	
	if inc.variable_global.expression_cache == []:
		inc.variable_global.up_cache.config(fg = "black")
		inc.variable_global.down_cache.config(fg = "black")
	
	elif len(inc.variable_global.expression_cache) == 1:
		inc.variable_global.up_cache.config(fg = "white")
		inc.variable_global.down_cache.config(fg = "black")
	
	elif len(inc.variable_global.expression_cache) > 1:
		if inc.variable_global.expression_cache[-1][1] == None:
			max = len(inc.variable_global.expression_cache) - 1
		else:
			max = len(inc.variable_global.expression_cache)
		if inc.variable_global.cache_count == 1:
			inc.variable_global.down_cache.config(fg = "white")
			inc.variable_global.up_cache.config(fg = "black")
		elif (inc.variable_global.cache_count == max) or (inc.variable_global.cache_count == 0):
			inc.variable_global.up_cache.config(fg = "white")
			inc.variable_global.down_cache.config(fg = "black")
		else:
			inc.variable_global.up_cache.config(fg = "white")
			inc.variable_global.down_cache.config(fg = "white")

def shift():
		
	if inc.variable_global.shift_select == False:	
		inc.variable_global.shift_select = True
		inc.variable_global.shift_screen.config(fg = "white")
	
	else:
		inc.variable_global.shift_select = False
		inc.variable_global.shift_screen.config(fg = "black")
	
def delete():
	
	if inc.variable_global.calc_mode == "Catalog":
		return None
	
	if inc.variable_global.calc_mode == "Check":
		return None
	
	if inc.variable_global.calc_mode == "Calculating":
		return None
	
	if inc.variable_global.calc_mode == "Error":
		return None
	elif inc.variable_global.calc_mode == "Reset":
		return None
		
	bar_del()
	inc.variable_global.out1.config(text = scr_exp(inc.variable_global.expression))
	inc.variable_global.button_prime_number_analysis.config(state = "disable")

	
def ac():
	
	if inc.variable_global.shift_select == True:
		off_calc_1()
	
	elif inc.variable_global.calc_mode == "Catalog":
		
		inc.variable_global.out1.config(text = out1_cache)
		inc.variable_global.out2.config(text = out2_cache)
		
		out1_cache = ""
		out2_cache = ""
		
		inc.variable_global.calc_mode = "Normal"
		inc.variable_global.min_scroll, inc.variable_global.max_scroll, select_scroll = [0], [3], 0
		inc.variable_global.address_select = []
		inc.variable_global.select_item = []
		
		inc.variable_global.calc_mode = "Normal"
		
		up_down_cache()
		
		return None
	
	elif inc.variable_global.calc_mode == "Check":
		return None
	
	elif inc.variable_global.calc_mode == "Reset":
		inc.variable_global.out1.config(text = out1_cache)
		inc.variable_global.out2.config(text = out2_cache)
		PNA_button()
		up_down_cache()
		inc.variable_global.calc_mode == "Normal"
		
	else:
		
		inc.variable_global.expression = ["|"]
		output = ""
		inc.variable_global.out1.config(text = "|")
		inc.variable_global.out2.config(text = "")
		inc.variable_global.button_prime_number_analysis.config(state = "disable")
		inc.variable_global.enter_eq = 0
		inc.variable_global.cache_count = 0
		up_down_cache()
		if inc.variable_global.expression_cache != []:
			if "|" in inc.variable_global.expression_cache[-1][0]:
				del inc.variable_global.expression_cache[-1][0][inc.variable_global.expression_cache[-1][0].index("|")]
		
		inc.variable_global.calc_mode = "Normal"

def on():
		
	if inc.variable_global.solve_thread != None:
		inc.variable_global.solve_thread.join()
		inc.variable_global.solve_thread = None
	
	inc.variable_global.expression = ["|"]
	inc.variable_global.expression_cache = []
	inc.variable_global.out1.config(text = "|")
	inc.variable_global.out2.config(text = "")
	inc.variable_global.cache_count = -1
	inc.variable_global.button_prime_number_analysis.config(state = "disable")
	inc.variable_global.enter_eq = 0
	up_down_cache()
	inc.variable_global.calc_mode = "Normal"
	inc.variable_global.min_scroll, inc.variable_global.max_scroll, select_scroll = [0], [3], 0
	inc.variable_global.address_select = []
	inc.variable_global.select_item = []
	inc.variable_global.out1.config(anchor = "nw")
	
def error_message():
		
	inc.variable_global.calc_mode = "Error"
	
	inc.variable_global.out1.config(anchor = "nw")


	
	if inc.variable_global.language == "English":
		inc.variable_global.out1.config(text = "Math ERROR")
		inc.variable_global.out2.config(text = "Return: [OK] or [=]")
	
	elif inc.variable_global.language == "Vietnamese":
		inc.variable_global.out1.config(text = "LỖI toán học")
		inc.variable_global.out2.config(text = "Trở lại: [OK] hoặc [=]")
	
	elif inc.variable_global.language == "Chinese":
		inc.variable_global.out1.config(text = "数学错误")
		inc.variable_global.out2.config(text = "返回: [OK]或者[=]")
	
	elif inc.variable_global.language == "Japanese":
		inc.variable_global.out1.config(text = "数学エラー")
		inc.variable_global.out2.config(text = "戻る： [OK]または[=]")
		
	inc.variable_global.cache_count = 0
	up_down_cache()

def check_result(result):
	real, inc.variable_global.imag = result.as_real_imag()
	if inc.variable_global.limit_low <= real <= inc.variable_global.limit_high:
		if inc.variable_global.limit_low <= inc.variable_global.imag <= inc.variable_global.limit_high:
			return True
	else:
		return False

def fix_result(result):
	
	if result % 1 == 0:
		return int(result)
	
	else:
		result = str(result)
		return float(result)

def simp(in_exp):
	
	in_exp += inc.variable_global.sqrt(0)
	
	if len(in_exp.as_ordered_terms()) >= 3:
		return fix_result(round(N(in_exp), inc.variable_global.fix_num))
		
	if inc.variable_global.deci == "ON":
		return fix_result(round(N(in_exp), inc.variable_global.fix_num))
	
	if "inc.variable_global.sqrt" in str(in_exp):
		
		sqrt_terms = []
		constant_terms = []
		
		for term in in_exp.as_ordered_terms():
			
			if "inc.variable_global.sqrt" in str(term):
				coeff, sqrt_part = term.as_coeff_Mul()
				sqrt_terms.append((coeff, sqrt_part))
			
			elif term.is_Number:
				constant_terms.append(term)
		
		if len(constant_terms) == 0:
				
			output_1 = str(together(ratsimp(in_exp)))
			output_2 = str(together(in_exp.simplify()))
				
			if output_1 == output_2:
				return output_1
						
			else:
					if len(output_1) < len(output_2):
						return output_1
					
					else:
						return output_2
		
		
		else:
			
			num_const = None
			num_sqrt = None
			make_frac = None
			
			if constant_terms[0] % 1 != 0:
				
				num_const = Fraction(float(constant_terms[0])).limit_denominator(10**(inc.variable_global.fix_num - 1))
				num_const = num_const.denominator
			
			if sqrt_terms[0][0] % 1 != 0:
				
				num_sqrt = Fraction(float(sqrt_terms[0][0])).limit_denominator(10**(inc.variable_global.fix_num - 1))
				num_sqrt = num_sqrt.denominator
			
			if num_const == None:
				if num_sqrt != None:
					make_frac = num_sqrt
				
				else:
					return in_exp
				
			else:
				if num_sqrt == None:
					make_frac = num_const
				
				else:
					make_frac = lcm(num_const, num_sqrt)
			
			if make_frac < 100:
				
				out = int(constant_terms[0] * make_frac) + int(sqrt_terms[0][0] * make_frac) * sqrt_terms[0][1]
				out = together(out/make_frac)
				return out
			
			else:
				
				return fix_result(round(N(in_exp), inc.variable_global.fix_num))
			
			
	else:
		
		out = Fraction(float(N(in_exp))).limit_denominator(10**inc.variable_global.fix_num)
		
		if (len(str(out)) <= 7) and ("-" not in str(out)):
			return out
		
		if (len(str(out)) <= 8) and ("-" in str(out)):
			return out
		
		else:
			return fix_result(round(N(out), inc.variable_global.fix_num))

def MB10(input_result, limit_low, limit_high):

	result = eval(str(N(input_result)))
	
	if result == 0:
		return "0"
	
	result += 0*I
	power = 0
	sign = ""
	
	if result.as_real_imag()[1] == 0:
		
		result = result.as_real_imag()[0]
	
		if result < 0:
			sign = "-"
			result *= -1
		
		if abs(result) >= limit_high:
			while round(result, 9) >= 10:
				result /= 10
				power += 1
			
			result = fix_result(round(result, inc.variable_global.fix_num))
			result = round(result, inc.variable_global.fix_num)
			
			return f"{sign}{result}×10^{power}"
		
		elif abs(result) < limit_low:
			while result < 1:
				result *= 10
				power -= 1
			
			result = fix_result(round(result, inc.variable_global.fix_num))
			result = round(result, inc.variable_global.fix_num)
		
			return f"{sign}{result}×10^{power}"
		
		else:
			
			result = simp(input_result)
			return f"{result}"
	
	elif result.as_real_imag()[0] == 0:
		
		result = result.as_real_imag()[1]
	
		if result < 0:
			sign = "-"
			result *= -1
		
		if abs(result) >= limit_high:
			while round(result, 9) >= 10:
				result /= 10
				power += 1
			
			result = fix_result(round(result, inc.variable_global.fix_num))
			result = round(result, inc.variable_global.fix_num)
			
			return f"{sign}{result}×10^{power}*I"
		
		elif abs(result) < limit_low:
			while result < 1:
				result *= 10
				power -= 1
			
			result = fix_result(round(result, inc.variable_global.fix_num))
			result = round(result, inc.variable_global.fix_num)
			
			return f"{sign}{result}×10^{power}*I"
		
		else:
			
			result = simp(result)
			return f"{result}*I"
	
	else:
		
		result_real, result_imag = result.as_real_imag()
		power_real = 0
		power_imag = 0
		output_result = ""
		
		if result_real < 0:
			sign = "-"
			result_real *= -1
		
		if abs(result_real) >= inc.variable_global.limit_high:
			while round(result_real, 9) >= 10:
				result_real /= 10
				power_real += 1
			
			result_real = fix_result(round(result_real, inc.variable_global.fix_num))
			result_real = round(result_real, inc.variable_global.fix_num)
			
			output_result = f"{sign}{result_real}×10^{power_real}"
		
		elif abs(result_real) < inc.variable_global.limit_low:
			while result_real < 1:
				result_real *= 10
				power_real -= 1
				
			result_real = fix_result(round(result_real, inc.variable_global.fix_num))
			result_real = round(result_real, inc.variable_global.fix_num)
		
			output_result = f"{sign}{result_real}×10^{power_real}"
		
		else:
			
			output_result = str(simp(input_result.as_real_imag()[0]))
		
		if result_imag < 0:
			sign = "-"
			result_imag *= -1
		
		else:
			sign = "+"
		
		if abs(result_imag) >= inc.variable_global.limit_high:
			while round(result_imag, 9) >= 10:
				result_imag /= 10
				power_imag += 1
			
			result_imag = fix_result(round(result_imag, inc.variable_global.fix_num))
			result_imag = round(result_imag, inc.variable_global.fix_num)
			
			output_result += f"{sign}{result_imag}×10^{power_imag}*I"
		
		elif abs(result_imag) < inc.variable_global.limit_low:
			while result_imag < 1:
				result_imag *= 10
				power_imag -= 1
			
			result_imag = fix_result(round(result_imag, inc.variable_global.fix_num))
			result_imag = round(result_imag, inc.variable_global.fix_num)
		
			output_result += f"{sign}{result_imag}×10^{power_imag}*I"
		
		else:
			
			output_result += f"{sign}{simp(input_result.as_real_imag()[1])}*I"
		
		return output_result

def GCD(a, b):
	if a % 1 != 0:
		return 0/0
	if b % 1 != 0:
		return 0/0
	while b != 0:
		a, b = b, a % b
	return a

def LCM(a, b):
	if a % 1 != 0:
		return 0/0
	if b % 1 != 0:
		return 0/0
	return (a * b) / GCD(a, b)

def frac(n):
	return factorial(n)

def RanInt(a, b):
	return random.randint(a, b)

def PNA_button():
	
	if inc.variable_global.calc_mode == "Catalog":
		inc.variable_global.button_prime_number_analysis.config(state = "disable")
		return None
		
	if inc.variable_global.calc_mode == "Check":
		inc.variable_global.button_prime_number_analysis.config(state = "disable")
		return None
		
	if inc.variable_global.calc_mode == "Error":
		inc.variable_global.button_prime_number_analysis.config(state = "disable")
		return None
	
	if inc.variable_global.calc_mode == "Calculating":
		inc.variable_global.button_prime_number_analysis.config(state = "disable")
	
	output = inc.variable_global.out2.cget("text")
	if (output == "") or (inc.variable_global.calc_mode == "Reset"):
		inc.variable_global.button_prime_number_analysis.config(state = "disable")
	else:
		output = output.replace("=", "")
		output = output.replace(" ", "")
		output = solve_exp(output)
		result = N(output)
		if result.is_complex == False:
			inc.variable_global.button_prime_number_analysis.config(state = "disable")
		elif result % 1 != 0:
			inc.variable_global.button_prime_number_analysis.config(state = "disable")
		elif result <= 1:
			inc.variable_global.button_prime_number_analysis.config(state = "disable")
		else:
			inc.variable_global.button_prime_number_analysis.config(state = "normal")

def PNA():
	output = inc.variable_global.out2["text"]

	for i in output:
		if i in inc.variable_global.power_number:
			return None
	output = output.replace("=", "")
	output = output.replace(" ", "")
	output = solve_exp(output)
	output = N(output)
	output = int(output)
	output = factorint(output)
	output = str(output)
	output = output.replace(" ", "")
	output = output.replace("{", "")
	output = output.replace("}", "")
	output = output.split(",")
	text = []
	for i in output:
		i = i.split(":")
		n = ""
		if i[1] != "1":
			for j in i[1]:
				j = str(j)
				k = inc.variable_global.number.index(j)
				n += inc.variable_global.power_number[k]
			text.append(str(i[0]) + n)
		else:
			text.append(str(i[0]))
	output = text
	output= " × ".join(output)
	inc.variable_global.out2.config(text = "= " + output)

def check():
	
	if inc.variable_global.calc_mode == "Catalog":
		return None
	
	if inc.variable_global.calc_mode == "Check":
		
		inc.variable_global.out1.config(text = out1_cache)
		inc.variable_global.out2.config(text = out2_cache)
		
		up_down_cache()
		
		inc.variable_global.calc_mode = "Normal"
	
		return None
	
	if inc.variable_global.calc_mode == "Error":
		return None
	
	if inc.variable_global.calc_mode == "Calculating":
		return None
	
	inc.variable_global.up_cache.config(fg = "black")
	inc.variable_global.down_cache.config(fg = "black")
	
	if inc.variable_global.calc_mode != "":
		out1_cache = inc.variable_global.out1.cget("text")
		out2_cache = inc.variable_global.out2.cget("text")
	
	inc.variable_global.calc_mode = "Check"
	
	if inc.variable_global.language == "English":
		text = f"Version: {inc.variable_global.version_of_calc}\n"
	
	elif inc.variable_global.language == "Vietnamese":
		text = f"Phiên bản: {inc.variable_global.version_of_calc}\n"
	
	elif inc.variable_global.language == "Chinese":
		text = f"版本: {inc.variable_global.version_of_calc}\n"
	
	elif inc.variable_global.language == "Japanese":
		text = f"バージョン: {inc.variable_global.version_of_calc}\n"
	
	inc.variable_global.button_prime_number_analysis.config(state = "disable")
	
	name_of_data = ["B", "KB", "MB"]
	
	all_of_code = inc.variable_global.inc.variable_global.expression, inc.variable_global.output, inc.variable_global.inc.variable_global.ans, inc.variable_global.inc.variable_global.enter_eq, inc.variable_global.inc.variable_global.mode, \
		inc.variable_global.inc.variable_global.imag, inc.variable_global.inc.variable_global.deci, inc.variable_global.out1_cache, inc.variable_global.out2_cache, inc.variable_global.inc.variable_global.expression_cache, \
			inc.variable_global.inc.variable_global.cache_count, inc.variable_global.inc.variable_global.calc_mode, inc.variable_global.inc.variable_global.min_scroll, inc.variable_global.inc.variable_global.max_scroll, \
				inc.variable_global.select_scroll, inc.variable_global.inc.variable_global.address_select, inc.variable_global.inc.variable_global.select_item, inc.variable_global.key
	
	all_of_code = str(all_of_code)
	data_of_code = sys.getsizeof(all_of_code)
	
	data_div = 0
	data_of_code_div = data_of_code
	
	while data_of_code_div > 1024:
		data_of_code_div /= 1024
		data_div += 1
	
	if inc.variable_global.language == "English":
		text += f"Data used: {data_of_code} Bytes"
	
	elif inc.variable_global.language == "Vietnamese":
		text += f"Dữ liệu đã sử dụng: {data_of_code} Bytes"
	
	elif inc.variable_global.language == "Chinese":
		text += f"使用的数据: {data_of_code} Bytes"
	
	elif inc.variable_global.language == "Japanese":
		text += f"使用されたデータ: {data_of_code} Bytes"
	
	if data_div != 0:
		text += f" ({round(data_of_code_div, 1)} {name_of_data[data_div]})"
	
	if inc.variable_global.language == "English":
		text += f"\nYour key: {inc.variable_global.key}"
		text += f"\nYour inc.variable_global.language: English"
		text_out = "Click [Check] again to exit\n"
		text_out += "Need help?  Press [˄] - Change inc.variable_global.language press [˅]"
	
	elif inc.variable_global.language == "Vietnamese":
		text += f"\nChìa khóa của bạn: {inc.variable_global.key}"
		text += f"\nNgôn ngữ của bạn: Tiếng Việt"
		text_out = "Bấm vào [Check] lần nữa để thoát\n"
		text_out += "Cần giúp đỡ?  Nhấn [˄] - Thay đổi ngôn ngữ nhấn [˅]"
	
	elif inc.variable_global.language == "Chinese":
		text += f"\n你的钥匙: {inc.variable_global.key}"
		text += f"\n您的语言： 中文"
		text_out = "再次点击[Check]退出\n"
		text_out += "需要帮助？按 [˄] - 更改语言按 [˅]"
	
	elif inc.variable_global.language == "Japanese":
		text += f"\nあなたの鍵: {inc.variable_global.key}"
		text += f"\nあなたの言語: 日本語"
		text_out = "終了するにはもう一度[Check]をクリックします\n"
		text_out += "お困りですか？[˄] - 言語変更は[˅]"
	
	inc.variable_global.out1.config(text = text)
	inc.variable_global.out2.config(text = text_out)
	return None

def sigma(exp_in, a, b):
	
	if a % 1 != 0:
		return None
		
	if b % 1 != 0:
		return None
		
	if -(10 ** 10) < a <= b < 10**10:
		
		exp_in = str(exp_in)
		exp_in = exp_in.replace("x", chr(1201))
		exp_in = sympify(exp_in)
		
		result = summation(exp_in, (chr(1201), a, b))
		
		return result
		
	else:
		return None

def sinh(a):
	return m.sinh(a)
		
def cosh(a):
	return m.cosh(a)
		
def tanh(a):
	return m.tanh(a)
		
def asinh(a):
	return m.asinh(a)
		
def acosh(a):
	return m.acosh(a)
		
def atanh(a):
	return m.atanh(a)

def sin(a):
	if inc.variable_global.mode == "r":
		return m.sin(a)
	if inc.variable_global.mode == "d":
		return m.sin(m.radians(a))
		
def cos(a):
	if inc.variable_global.mode == "r":
		return m.cos(a)
	if inc.variable_global.mode == "d":
		return m.cos(m.radians(a))
		
def tan(a):

	if inc.variable_global.mode == "r":
		return m.tan(a)
	if inc.variable_global.mode == "d":
		return m.tan(m.radians(a))
		
def asin(a):

	if inc.variable_global.mode == "r":
		return m.asin(a)
	if inc.variable_global.mode == "d":
		return m.degrees(m.asin(a))
		
def acos(a):

	if inc.variable_global.mode == "r":
		return m.acos(a)
	if inc.variable_global.mode == "d":
		return m.degrees(m.acos(a))
		
def atan(a):

	if inc.variable_global.mode == "r":
		return m.atan(a)
	if inc.variable_global.mode == "d":
		return m.degrees(m.atan(a))
		
def mode_degree(degree):

	if degree == "d":
		inc.variable_global.button_d_mode.config(state = "disabled")
		inc.variable_global.button_r_mode.config(state = "normal")
		inc.variable_global.mode = "d"
	if degree == "r":
		inc.variable_global.button_r_mode.config(state = "disabled")
		inc.variable_global.button_d_mode.config(state = "normal")
		inc.variable_global.mode = "r"
	
def on_imag_num():

	inc.variable_global.button_ON_imagnum_mode.config(state = "disabled")
	inc.variable_global.button_OFF_imagnum_mode.config(state = "normal")
	inc.variable_global.imag = "ON"
	
def off_imag_num():

	inc.variable_global.button_OFF_imagnum_mode.config(state = "disabled")
	inc.variable_global.button_ON_imagnum_mode.config(state = "normal")
	inc.variable_global.imag = "OFF"

def on_deci_num():

	inc.variable_global.button_ON_decimal_mode.config(state = "disabled")
	inc.variable_global.button_OFF_decimal_mode.config(state = "normal")
	inc.variable_global.deci = "ON"
	
def off_deci_num():

	inc.variable_global.button_OFF_decimal_mode.config(state = "disabled")
	inc.variable_global.button_ON_decimal_mode.config(state = "normal")
	inc.variable_global.deci = "OFF"

def end_left():

	
	if inc.variable_global.calc_mode == "Catalog":
		return None
	
	if inc.variable_global.calc_mode == "Check":
		return None

	if inc.variable_global.calc_mode == "Calculating":
		return None
	
	if inc.variable_global.calc_mode == "Error":
		return None
	
	elif inc.variable_global.calc_mode == "Reset":
		return None
	
	try:
		k = inc.variable_global.expression.index("|")
		del inc.variable_global.expression[k]
		inc.variable_global.expression = ["|"] + inc.variable_global.expression
	except:
		pass
	inc.variable_global.out1.config(text = scr_exp(inc.variable_global.expression))
	inc.variable_global.button_prime_number_analysis.config(state = "disable")

def end_right():

	
	if inc.variable_global.calc_mode == "Catalog":
		return None
	
	if inc.variable_global.calc_mode == "Check":
		return None
	
	if inc.variable_global.calc_mode == "Calculating":
		return None
	
	if inc.variable_global.calc_mode == "Error":
		return None
	
	elif inc.variable_global.calc_mode == "Reset":
		return None
	
	try:
		k = inc.variable_global.expression.index("|")
		del inc.variable_global.expression[k]
		inc.variable_global.expression += ["|"]
	except:
		pass
	inc.variable_global.out1.config(text = scr_exp(inc.variable_global.expression))
	inc.variable_global.button_prime_number_analysis.config(state = "disable")
	
def reset_message():
	
	if inc.variable_global.calc_mode == "Catalog":
		return None
	
	if inc.variable_global.calc_mode == "Check":
		return None
	
	if inc.variable_global.calc_mode == "Error":
		return None
	
	if inc.variable_global.calc_mode == "Calculating":
		return None
	
	if inc.variable_global.calc_mode != "Reset":
		out1_cache = inc.variable_global.out1.cget("text")
		out2_cache = inc.variable_global.out2.cget("text")
		
	inc.variable_global.calc_mode = "Reset"

	inc.variable_global.button_prime_number_analysis.config(state = "disable")

	if inc.variable_global.language == "English":
		inc.variable_global.out1.config(text = "Are you sure you want to reset?")
		inc.variable_global.out2.config(text = "Yes: [OK] or [=]\nNo: [AC]")
		
	elif inc.variable_global.language == "Vietnamese":
		inc.variable_global.out1.config(text = "Bạn có chắc chắn muốn đặt lại?")
		inc.variable_global.out2.config(text = "Có: [OK] hoặc [=]\nKhông: [AC]")
	
	elif inc.variable_global.language == "Chinese":
		inc.variable_global.out1.config(text = "您确定要重置吗？")
		inc.variable_global.out2.config(text = "可: [OK] 或者 [=]\n不: [AC]")
	
	elif inc.variable_global.language == "Japanese":
		inc.variable_global.out1.config(text = "本当にリセットしますか?")
		inc.variable_global.out2.config(text = "コ: [OK] または [=]\nいいえ: [AC]")
	
	inc.variable_global.up_cache.config(fg = "black")
	inc.variable_global.down_cache.config(fg = "black")

def reset():	
	inc.variable_global.expression = ["|"]
	output = ""
	inc.variable_global.ans = 0
	inc.variable_global.enter_eq = 0
	inc.variable_global.mode = "d"
	inc.variable_global.imag = "OFF"
	inc.variable_global.deci = "OFF"
	inc.variable_global.out1.config(text = scr_exp(inc.variable_global.expression))
	inc.variable_global.out2.config(text = "")
	inc.variable_global.button_Ans.config(text = "∆ = 0")
	mode_degree("d")
	off_imag_num()
	off_deci_num()
	inc.variable_global.button_prime_number_analysis.config(state = "disable")
	out1_cache = ""
	out2_cache = ""
	inc.variable_global.expression_cache = []
	inc.variable_global.cache_count = -1
	up_down_cache()
	inc.variable_global.calc_mode = "Normal"
	inc.variable_global.min_scroll, inc.variable_global.max_scroll, select_scroll = [0], [3], 0
	inc.variable_global.address_select = []
	inc.variable_global.select_item = []

def off_calc():
	return None

def off_calc_1(app):
		
	inc.variable_global.calc_mode = "OFF CALC"
	
	inc.variable_global.up_cache.config(fg = "black")
	inc.variable_global.down_cache.config(fg = "black")
	inc.variable_global.shift_screen.config(fg = "black")
	
	for widget in app.winfo_children():
		if isinstance(widget, tk.Button):
			widget.config(command = lambda: off_calc())
	
	inc.variable_global.out1.config(text = "KERAS", anchor = "center", font = ("", 20))
	inc.variable_global.out2.config(text = inc.variable_global.version_of_calc, anchor = "center", font = ("", 7))
	
	app.after(2000, off_calc_2(app))

def off_calc_2(app):
	
	inc.variable_global.out1.config(text = "Power Calculator")
	inc.variable_global.out2.config(text = "Made by Lê Ngọc Hà")
	
	app.after(2300, off_calc_3(app))

def off_calc_3(app):
	app.destroy()

def select(A, pos):
	
	
	for i in pos:
		if isinstance(A[i], list) == True:
			A = A[i][1]
		else:
			try:
				A = A[i]
			except:
				pass
	
	inc.variable_global.select_item = A
	text = []
	
	if isinstance(A, list) == True:
		
		if pos == []:
			for i in range(len(A)):
				text.append(f"{i + 1}. {A[i][0]}")
				
		else:
			for i in range(len(A)):
				if isinstance(A[i], list) == True:
					text.append(f"{i + 1}. {A[i][0]}")
				else:
					text.append(f"{i + 1}. {A[i]}")
	
	else:
	
		return None
	
	return text

def scroll(list):
	
	
	length_select = len(list)
	
	if select_scroll == length_select:
		if length_select <= 4:
			inc.variable_global.min_scroll[-1], inc.variable_global.max_scroll[-1], select_scroll = 0, length_select - 1, 0
		else:
			inc.variable_global.min_scroll[-1], inc.variable_global.max_scroll[-1], select_scroll = 0, 3, 0
	
	elif select_scroll == -1:
		if length_select <= 4:
			inc.variable_global.min_scroll[-1] = 0
		else:
			inc.variable_global.min_scroll[-1] = length_select - 4
		inc.variable_global.max_scroll[-1], select_scroll = length_select - 1, length_select - 1
		
	elif select_scroll < inc.variable_global.min_scroll[-1]:
		inc.variable_global.min_scroll[-1] -= 1
		inc.variable_global.max_scroll[-1] -= 1
	
	elif select_scroll > inc.variable_global.max_scroll[-1]:
		inc.variable_global.min_scroll[-1] += 1
		inc.variable_global.max_scroll[-1] += 1
		
	text = ""
	if length_select > 4:
		length_select = 4
	for i in range(0, length_select):
		if text != "":
			text += "\n"
		if i + (inc.variable_global.min_scroll[-1] - select_scroll) == 0:
			text += f"▶{list[inc.variable_global.min_scroll[-1] + i]}"
		else:
			text += f"    {list[inc.variable_global.min_scroll[-1] + i]}"

	return text

def catalog():
		
	if inc.variable_global.calc_mode == "Check":
		return None
	
	if inc.variable_global.calc_mode == "Catalog":
		return None
	
	if inc.variable_global.calc_mode == "Error":
		return None
	
	if inc.variable_global.calc_mode == "Calculating":
		return None
		
	inc.variable_global.calc_mode = "Catalog"
	
	out1_cache = inc.variable_global.out1.cget("text")
	out2_cache = inc.variable_global.out2.cget("text")
	
	inc.variable_global.up_cache.config(fg = "black")
	inc.variable_global.down_cache.config(fg = "black")
	
	inc.variable_global.out1.config(text = scroll(select(inc.variable_global.Catalog_select, inc.variable_global.address_select)))
	
	if inc.variable_global.language == "English":
		inc.variable_global.out2.config(text = "Scroll: [^] or [˅]\nSelect: [OK] or [=]")
	
	elif inc.variable_global.language == "Vietnamese":
		inc.variable_global.out2.config(text = "Cuộn: [^] hoặc [˅]\nChọn: [OK] hoặc [=]")
	
	elif inc.variable_global.language == "Chinese":
		inc.variable_global.out2.config(text = "滚动：[^] 或 [˅]\n选择：[OK] 或 [=]")
	
	elif inc.variable_global.language == "Japanese":
		inc.variable_global.out2.config(text = "スクロール: [^] または [˅]\n選択: [OK] または [=]")

def change_exp(real_exp):
	
	if "%" in real_exp:
			 
		time_parentheses = 0
			 
		for i in range(len(real_exp)):
			if real_exp[i + 2 * time_parentheses] == "%":
				try:
					if real_exp[i + 1 + 2 * time_parentheses] != ")":
							
						parentheses = 0
						change_parentheses = False
						exit = False
							
						for j in range(i - 1 + 2 * time_parentheses, -1, -1):
								
							if exit == True:
								continue
								
							if real_exp[j] == ")":
								parentheses += 1
								change_parentheses = True
									
							if real_exp[j] == "(":
								parentheses -= 1
								change_parentheses = True
								
							if (parentheses == 0) and (change_parentheses == True):
								real_exp = real_exp[: j] + "(" + real_exp[j : i + 1 + 2 * time_parentheses] + ")" + real_exp[i + 1 + 2 * time_parentheses :]
								time_parentheses += 1
								exit = True
						
				except:
						
					parentheses = 0
					change_parentheses = False
					exit = False
							
					for j in range(i - 1 + 2 * time_parentheses, -1, -1):
								
						if exit == True:
							continue
								
						if real_exp[j] == ")":
							parentheses += 1
							change_parentheses = True
									
						if real_exp[j] == "(":
							parentheses -= 1
							change_parentheses = True
								
						if (parentheses == 0) and (change_parentheses == True):
							real_exp = real_exp[: j] + "(" + real_exp[j :] + ")"
							time_parentheses += 1
							exit = True
		
		
	if "!" in real_exp:
			 
		time_frac = 0
			 
		for i in range(len(real_exp)):
			if real_exp[i + 3 * time_frac] == "!":
							
				parentheses = 0
				change_parentheses = False
				exit = False
							
				for j in range(i - 1 + 3 * time_frac, -1, -1):
								
					if exit == True:
						continue
								
					if real_exp[j] == ")":
						parentheses += 1
						change_parentheses = True
									
					if real_exp[j] == "(":
						parentheses -= 1
						change_parentheses = True
								
					if (parentheses == 0) and (change_parentheses == True):
						real_exp = real_exp[: j] + "frac" + real_exp[j : i + 3 * time_frac] + real_exp[i + 1 + 3 * time_frac :]
						time_frac += 1
						exit = True

	
	for k in range(len(inc.variable_global.name_conversions)):
	
		if inc.variable_global.name_conversions[k][0] in real_exp:
			
			real_exp = real_exp.replace(inc.variable_global.name_conversions[k][0], chr(1000 + k))
				 
			time_jump = 0
			time_skip = len(inc.variable_global.name_conversions[k][1]) + len(inc.variable_global.name_conversions[k][2])
				 
			for i in range(len(real_exp)):
				if real_exp[i + time_skip * time_jump] == chr(1000 + k):
					try:
						if real_exp[i + 1 + time_skip * time_jump] != ")":
								
							parentheses = 0
							change_parentheses = False
							exit = False
								
							for j in range(i - 1 + time_skip * time_jump, -1, -1):
									
								if exit == True:
									continue
									
								if real_exp[j] == ")":
									parentheses += 1
									change_parentheses = True
										
								if real_exp[j] == "(":
									parentheses -= 1
									change_parentheses = True
									
								if (parentheses == 0) and (change_parentheses == True):
									real_exp = real_exp[: j] + inc.variable_global.name_conversions[k][1] + real_exp[j : i + 1 + time_skip * time_jump] + inc.variable_global.name_conversions[k][2] + real_exp[i + 1 + time_skip * time_jump :]
									time_jump += 1
									exit = True
							
					except:
							
						parentheses = 0
						change_parentheses = False
						exit = False
								
						for j in range(i - 1 + time_skip * time_jump, -1, -1):
									
							if exit == True:
								continue
									
							if real_exp[j] == ")":
								parentheses += 1
								change_parentheses = True
										
							if real_exp[j] == "(":
								parentheses -= 1
								change_parentheses = True
									
							if (parentheses == 0) and (change_parentheses == True):
								real_exp = real_exp[: j] + inc.variable_global.name_conversions[k][1] + real_exp[j :] + inc.variable_global.name_conversions[k][2]
								time_jump += 1
								exit = True
		
			real_exp = real_exp.replace(chr(1000 + k), "")
	
	
	return real_exp

def solve_screen():
		
	if inc.variable_global.calc_mode == "Calculating":
		return None
	
	if (inc.variable_global.calc_mode == "Normal") and (inc.variable_global.expression != ["|"]):
	
		if inc.variable_global.language == "English":
			inc.variable_global.out1.config(text = "Calculating...", anchor = "center")
			
		elif inc.variable_global.language == "Vietnamese":
			inc.variable_global.out1.config(text = "Đang tính toán...", anchor = "center")
		
		elif inc.variable_global.language == "Chinese":
			inc.variable_global.out1.config(text = "计算...", anchor = "center")
		
		elif inc.variable_global.language == "Japanese":
			inc.variable_global.out1.config(text = "計算中...", anchor = "center")
	
		inc.variable_global.out2.config(text = "")
		
		inc.variable_global.calc_mode = "Calculating"
		
		inc.variable_global.solve_thread = threading.Thread(target = solve).start()
	
	else:
		solve()
		
def solve():	
	if inc.variable_global.calc_mode == "Catalog":
		
		inc.variable_global.address_select.append(select_scroll)
		if select(inc.variable_global.Catalog_select, inc.variable_global.address_select) == None:

			bar_add(inc.variable_global.select_item)
			inc.variable_global.calc_mode = "Normal"
			inc.variable_global.address_select = []
			inc.variable_global.out1.config(text = scr_exp(inc.variable_global.expression))
			inc.variable_global.out2.config(text = "")
			up_down_cache()
			inc.variable_global.min_scroll, inc.variable_global.max_scroll, select_scroll = [0], [3], 0
			
		else:
			inc.variable_global.min_scroll.append(0)
			inc.variable_global.max_scroll.append(3)
			select_scroll = 0
			inc.variable_global.out1.config(text = scroll(select(inc.variable_global.Catalog_select, inc.variable_global.address_select)))
	
		return None
	
	elif inc.variable_global.calc_mode == "Error":
		
		inc.variable_global.calc_mode = "Normal"
		inc.variable_global.expression = inc.variable_global.expression_cache[-1][0] + ["|"]
		inc.variable_global.out1.config(text = scr_exp(inc.variable_global.expression))
		inc.variable_global.out2.config(text = "")
		
		return None
	
	elif inc.variable_global.calc_mode == "Reset":
		
		reset()
		return None
	
	elif inc.variable_global.expression == ["|"]:
		pass
	
	else:
		
		try:
			k = inc.variable_global.expression.index("|")
			del inc.variable_global.expression[k]
		except:
			pass
		
		previous_character = None
		real_exp = []
		error = 0
		
		for i in range(len(inc.variable_global.expression)):
			if (previous_character in inc.variable_global.list_num) and (inc.variable_global.expression[i] in inc.variable_global.list_cal):
				real_exp += ["*"] + [inc.variable_global.expression[i]]
		
			elif (previous_character not in inc.variable_global.list_num) and (inc.variable_global.expression[i] == "."):
				real_exp += ["0", "."]
		
			else:
				real_exp += [inc.variable_global.expression[i]]
			
			previous_character = inc.variable_global.expression[i]
		
		number_handle = ""
		new_exp = ""
		real_exp += [""]
		
		for i in real_exp:
			
			if i in inc.variable_global.number:
				number_handle += i
				
			elif i == "Ran#":
				new_exp += f"({random.randint(0, 999)}/1000)"
				
			else:
				
				try:
					try:
						if "%" in number_handle:
							new_exp += "(" + str(int(number_handle[0 : -1])) + "%)" + i
						else:
							new_exp += "(" + str(int(number_handle)) + ")" + i
					
					except:
						if (number_handle != "%") or (number_handle != ""):
							if ("%" in number_handle) and (number_handle != "%"):
								new_exp += "(" + number_handle[0 : -1] + "%)" + i
							else:
								
								if number_handle != "":
									new_exp += "(" + number_handle + ")" + i						
								else:
									new_exp += number_handle + i
									
								
						else:
							new_exp += i
				
				except:
					
					try:
						try:
							if "%" in number_handle:
								new_exp += "(" + str(float(number_handle[0 : -1])) + "%)" + i
							else:
								new_exp += "(" + str(float(number_handle)) + ")" + i
								
						except:
							if (number_handle != "%") or (number_handle != ""):
								if ("%" in number_handle) and (number_handle != "%"):
									new_exp += "(" + number_handle[0 : -1] + "%)" + i
								else:
									
									if number_handle != "":
										new_exp += "(" + number_handle + ")" + i						
									else:
										new_exp += number_handle + i
							
							else:
								new_exp += i
					
					except:
						if number_handle == "":
							new_exp += i
			
				number_handle = ""
		
		inc.variable_global.ans = str(inc.variable_global.ans)
		inc.variable_global.ans = inc.variable_global.ans.replace(" ", "")
		inc.variable_global.ans = inc.variable_global.ans.replace("i", "I")
		
		real_exp = new_exp
		
		real_exp = change_exp(real_exp)
		
		real_exp = solve_exp(real_exp)
		
		real_exp = real_exp.replace("x", "symbols('x')")
		real_exp = str(real_exp)
		
		if inc.variable_global.imag == "OFF":
			try:
				if inc.variable_global.deci == "OFF":
					
					output = eval(real_exp)
					if "x" in str(output):
						output = eval(str(output))
						
				else:
					output = N(eval(real_exp))
				if "I" in str(output):
					error += 1
			except :
				error += 1
		else:
			try:
				if inc.variable_global.deci == "OFF":
					
					output = eval(real_exp)
					if "x" in str(output):
						output = eval(str(output))
					
				else:
					output = N(eval(real_exp))
			except:
				error += 1
		
		try:
			check = check_result(N(output))
			if check == False:
				error += 1
		except:
			error += 1
		
		if inc.variable_global.calc_mode != "Calculating":
			return None
	
		if error == 0:
			
			if inc.variable_global.calc_mode == "Calculating":
			
				output = MB10(output, inc.variable_global.limit_low_result, inc.variable_global.limit_high_result)
				output = output_exp(output)
				
				if inc.variable_global.calc_mode == "Calculating":
					
					inc.variable_global.out1.config(anchor = "nw")
					
					inc.variable_global.ans = str(output)
					inc.variable_global.enter_eq += 1
					
					inc.variable_global.out2.config(text = "= " + str(output))
					inc.variable_global.out1.config(text = scr_exp(inc.variable_global.expression))
					inc.variable_global.button_Ans.config(text = "∆ = " + output)
					
					try:
						if inc.variable_global.expression_cache[-1][1] != None:
							pass
						else:
							del inc.variable_global.expression_cache[-1]
					except:
						pass
					inc.variable_global.expression_cache.append([inc.variable_global.expression, output])
					if len(inc.variable_global.expression_cache) > 30:
						del inc.variable_global.expression_cache[0]
					
					inc.variable_global.calc_mode = "Normal"

		else:
			
			if inc.variable_global.calc_mode == "Calculating":
				
				try:
					if inc.variable_global.expression_cache[-1][1] == None:
						del inc.variable_global.expression_cache[-1]
				except:
					pass
				
				inc.variable_global.enter_eq = 0
				inc.variable_global.expression_cache.append([inc.variable_global.expression, None])
				inc.variable_global.out1.config(anchor = "nw")
				error_message()
		
		PNA_button()
		
	inc.variable_global.out1.config(anchor = "nw")
	inc.variable_global.cache_count = 0
	up_down_cache()

def bar_up():
		
	if inc.variable_global.calc_mode == "Catalog":
		
		select_scroll -= 1
		inc.variable_global.out1.config(text = scroll(select(inc.variable_global.Catalog_select, inc.variable_global.address_select)))
	
		return None
	
	if inc.variable_global.calc_mode == "Check":
		
		try:
			webbrowser.open(inc.variable_global.url_help)
		
		except:
			pass
		
		return None
		
	if inc.variable_global.calc_mode == "Calculating":
		return None
	
	inc.variable_global.button_prime_number_analysis.config(state = "disable")
	
	text = inc.variable_global.out1.cget("text")
	
	if inc.variable_global.calc_mode == "Error":
		return None
	
	elif inc.variable_global.calc_mode == "Reset":
		return None
	
	elif inc.variable_global.expression_cache == []:
		return None
	
	elif ("|" in inc.variable_global.expression) and (inc.variable_global.expression != ["|"]):
		return None
	
	else:
		
		try:
			if inc.variable_global.expression_cache[-1][1] == None:
				copy_expression_cache = inc.variable_global.expression_cache[0 : -1]
			else:
				copy_expression_cache = inc.variable_global.expression_cache
		except:
			pass
			
		if inc.variable_global.cache_count == 0:
				inc.variable_global.cache_count = len(copy_expression_cache)
	
		if "|" not in inc.variable_global.expression:
			if inc.variable_global.cache_count > 1:
				inc.variable_global.cache_count -= 1
		
		try:
				
			inc.variable_global.expression = copy_expression_cache[inc.variable_global.cache_count - 1][0]
			inc.variable_global.out1.config(text = scr_exp(inc.variable_global.expression))
			inc.variable_global.out2.config(text = f"= {copy_expression_cache[inc.variable_global.cache_count - 1][1]}")
			inc.variable_global.enter_eq = 0
			up_down_cache()
		
		except:
			pass

def bar_down():
	
	
	if inc.variable_global.calc_mode == "Catalog":
		
		select_scroll += 1
		inc.variable_global.out1.config(text = scroll(select(inc.variable_global.Catalog_select, inc.variable_global.address_select)))
	
		return None
	
	if inc.variable_global.calc_mode == "Check":
		
		if inc.variable_global.choose_language.index(inc.variable_global.language) == len(inc.variable_global.choose_language) - 1:
			inc.variable_global.language = inc.variable_global.choose_language[0]
		
		else:
			inc.variable_global.language = inc.variable_global.choose_language[inc.variable_global.choose_language.index(inc.variable_global.language) + 1]
		
		inc.variable_global.calc_mode = ""
		check()
		inc.language.change_language()
		
		return None
	
	if inc.variable_global.calc_mode == "Calculating":
		return None
	
	inc.variable_global.button_prime_number_analysis.config(state = "disable")
	
	text = inc.variable_global.out1.cget("text")
	
	if inc.variable_global.calc_mode == "Error":
		return None
	
	elif inc.variable_global.calc_mode == "Reset":
		return None
	
	elif inc.variable_global.expression_cache == []:
		return None
	
	elif ("|" in inc.variable_global.expression) and (inc.variable_global.expression != ["|"]):
		return None
	
	elif ("|" not in inc.variable_global.expression) or (inc.variable_global.expression == ["|"]):
		try:
			if inc.variable_global.expression_cache[-1][1] == None:
				copy_expression_cache = inc.variable_global.expression_cache[0 : -1]
			else:
				copy_expression_cache = inc.variable_global.expression_cache
		except:
			pass
		if inc.variable_global.cache_count == 0:
			inc.variable_global.cache_count = len(copy_expression_cache)
		if inc.variable_global.cache_count < len(copy_expression_cache):
			inc.variable_global.cache_count += 1
		else:
			pass
		
		try:
			
			inc.variable_global.expression = copy_expression_cache[inc.variable_global.cache_count - 1][0]
			inc.variable_global.out1.config(text = scr_exp(inc.variable_global.expression))
			inc.variable_global.out2.config(text = f"= {copy_expression_cache[inc.variable_global.cache_count - 1][1]}")
			inc.variable_global.enter_eq = 0
			up_down_cache()
		
		except:
			pass
		
def bar_left():
	
	
	if inc.variable_global.calc_mode == "Catalog":
		if inc.variable_global.address_select != []:
			select_scroll = inc.variable_global.address_select[-1]
			del inc.variable_global.address_select[-1], inc.variable_global.min_scroll[-1], inc.variable_global.max_scroll[-1]
			inc.variable_global.out1.config(text = scroll(select(inc.variable_global.Catalog_select, inc.variable_global.address_select)))
		
		return None
	
	if inc.variable_global.calc_mode == "Check":
		return None
	
	if inc.variable_global.calc_mode == "Error":
		return None
	
	if inc.variable_global.calc_mode == "Calculating":
		return None
	
	elif inc.variable_global.calc_mode == "Reset":
		return None
	
	elif inc.variable_global.enter_eq == 0:
		if inc.variable_global.expression == ["|"]:
			if inc.variable_global.expression_cache != []:
				inc.variable_global.expression = inc.variable_global.expression_cache[-1][0] + ["|"]
				inc.variable_global.out1.config(text = scr_exp(inc.variable_global.expression))
				inc.variable_global.out2.config(text = "")
				return None
			else:
				return None
		else:
			if "|" in inc.variable_global.expression:
				if inc.variable_global.expression[0] == "|":
					del inc.variable_global.expression[0]
					inc.variable_global.expression += ["|"]
				else:
					k = inc.variable_global.expression.index("|")
					inc.variable_global.expression[k - 1], inc.variable_global.expression[k] = inc.variable_global.expression[k], inc.variable_global.expression[k - 1]
			else:
				inc.variable_global.expression += ["|"]
					
	else:
		if "|" not in inc.variable_global.expression:
			inc.variable_global.expression += ["|"]
			inc.variable_global.enter_eq = 0
	
	output = ""
	inc.variable_global.out2.config(text = "")
	inc.variable_global.out1.config(text = scr_exp(inc.variable_global.expression))
	inc.variable_global.button_prime_number_analysis.config(state = "disable")
	inc.variable_global.cache_count = 0
	up_down_cache()

def bar_right():
		
	if inc.variable_global.calc_mode == "Catalog":
		if isinstance(inc.variable_global.select_item[select_scroll], list) == True:
			inc.variable_global.address_select.append(select_scroll)
			inc.variable_global.min_scroll.append(0)
			inc.variable_global.max_scroll.append(3)
			select_scroll = 0
			inc.variable_global.out1.config(text = scroll(select(inc.variable_global.Catalog_select, inc.variable_global.address_select)))
		
		return None
	
	if inc.variable_global.calc_mode == "Check":
		return None
	
	if inc.variable_global.calc_mode == "Error":
		return None
		
	if inc.variable_global.calc_mode == "Calculating":
		return None
	
	elif inc.variable_global.calc_mode == "Reset":
		return None
	
	elif inc.variable_global.enter_eq == 0:
		if inc.variable_global.expression == ["|"]:
			try:
				inc.variable_global.expression = ["|"] + inc.variable_global.expression_cache[-1][0]
				inc.variable_global.out1.config(text = scr_exp(inc.variable_global.expression))
				inc.variable_global.out2.config(text = "")
				return None
			except:
				pass
		else:
			if "|" in inc.variable_global.expression:
				if inc.variable_global.expression[-1] == "|":
					del inc.variable_global.expression[-1]
					inc.variable_global.expression = ["|"] + inc.variable_global.expression
				else:
					k = inc.variable_global.expression.index("|")
					inc.variable_global.expression[k + 1], inc.variable_global.expression[k] = inc.variable_global.expression[k], inc.variable_global.expression[k + 1]
			else:
				inc.variable_global.expression = ["|"] + inc.variable_global.expression
			
	else:
		if "|" not in inc.variable_global.expression:
			inc.variable_global.expression = ["|"] + inc.variable_global.expression
			inc.variable_global.enter_eq = 0
	
	output = ""
	inc.variable_global.out2.config(text = output)
	inc.variable_global.out1.config(text = scr_exp(inc.variable_global.expression))
	inc.variable_global.button_prime_number_analysis.config(state = "disable")
	inc.variable_global.cache_count = 0
	up_down_cache()

def bar_add(var):
	
	if var == "i":
		var = chr(1200)
		
	try:
		k = inc.variable_global.expression.index("|")
		inc.variable_global.expression = list(inc.variable_global.expression[: k]) + [var] + list(inc.variable_global.expression[k :])
		if ("(" in var) and (var != "(") and (")" not in var):
			del inc.variable_global.expression[k + 1]
			inc.variable_global.expression = list(inc.variable_global.expression[: k + 1]) + ["|", ")"] + list(inc.variable_global.expression[k + 1 :])
	except:
		inc.variable_global.expression = [var, "|"]
	inc.variable_global.cache_count = 0
	up_down_cache()

def bar_del():
	
	if inc.variable_global.calc_mode == "Check":
		return None
	
	if inc.variable_global.expression == ["|"]:
		pass
	
	if inc.variable_global.calc_mode == "Calculating":
		return None
	
	else:
		if "|" in inc.variable_global.expression:
			k = inc.variable_global.expression.index("|")
			if k == 0:
				del inc.variable_global.expression[1]
			else:
				del inc.variable_global.expression[k - 1]
		else:
			pass
	inc.variable_global.out1.config(text = scr_exp(inc.variable_global.expression))
	inc.variable_global.cache_count = 0
	up_down_cache()
