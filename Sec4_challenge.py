# coding: UTF-8
# Q1
print("Q1：数字を入力値として受け取り、その数字を2乗した戻り値を返す関数を書いてみよう")

def f_1():
	"""
	Returns number**2
	:return: number変数に入力された数を2乗した値
	"""
	number = input("2乗する値を入力: ")
	number = int(number)
	return number ** 2

print(f_1())

# Q2
print("Q2：文字列を引数とし、その文字列を出力する関数を書いてみよう。")

def f_2(lyric):
	"""
	Returns None.
	:param lyric: str.
	:return: None.
	"""
	print(lyric)

f_2("逃げ水が好き")

# Q3
print("Q3：3つの必須引数と2つのオプション引数がある関数を書いてみよう。")

def f_3(a, b, c, d = 5, e =6):
	"""
	Returns e%a+(b+c)*d
	:param a: int.
	:param b: int.
	:param c: int.
	:param d: int. (d = 5)
	:param e: int. (e = 6)
	:return: eをaで割った時の剰余と、bとcの和とdの積を足した値.
	"""
	print(e%a+(b+c)*d)

f_3(2,4,6,8,10)
f_3(5,10,9)

# Q4
print("""Q4：2つの関数からなるプログラムを書いてみよう。
1つ目の関数は、整数を引数として受け取り、その整数を2で割って求められる整数を出力として返そう。
2つ目の関数は、整数を引数として受け取り、4でかけた整数を返そう。
プログラム内で、1つ目の関数を呼び、戻り値を変数として保存し、2つ目の関数の引数として渡そう。""")

def f_4_1(number1):
	"""
	Returns number1 // 2.
	:param number1: int.
	:return: number1 を2で割った整数の値
	"""
	return number1 // 2

def f_4_2(number2):
	"""
	Returns number2 * 4
	:param number2: int.
	:return: number2を4でかけた整数
	"""
	return number2 * 4

master_number1 = f_4_1(7)
print(master_number1)
print(f_4_2(master_number1))

# Q5
print("""文字列をfloat型に変換して戻り値をする関数を書いてみよう。
起こり得る例外をキャッチする例外処理を書こう。""")

def f_5(number3):
	"""
	Returns float number3
	:param number3: str.
	:return: number3を文字列からfloat型に変換した値
	"""
	try:
		return float(number3)
	except (ValueError):
		print("Input data is only number.")

master_number2 = input("float型に変換したい値を入力してください。\n->")
print_number = f_5(master_number2)
print(print_number)







