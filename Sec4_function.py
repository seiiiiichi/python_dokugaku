# coding: UTF-8

# 関数の使い方
def f(x):
	return x * 2

result = f(2)
print(result)

# 関数の使い方2
def f_2(x, y, z):
	return x + y + z

result = f_2(1, 2, 3)
print(result)

# 関数の使い方3
def f_3():
	x_2 = 1+1

result = f_3()
print(result)

# 組み込み関数(文字列の長さ)
print(len("いつもの夏と違うんだ。誰も気づいていないけど"))
print(len("KobeBryant"))

# 組み込み関数(整数→文字列, 文字列→整数, 文字列→浮動小数点数)
print(str(100))
print(int("1"))
print(float("16.4"))
print(float(4))

# 組み込み関数(文字列を受け取る)

age = input("Enter your age: ")

int_age = int(age)

if int_age < 20:
	print("お前まだ酒飲むなよ")
else:
	print("コロナウイルスに気をつけて")

# 関数の複数回利用

def even_odd():
	number = input("Type a number: ")
	int_number = int(number)
	if int_number % 2 == 0:
		print("グースー")
	else:
		print("キスー")

even_odd()
even_odd()
even_odd()

# 必須引数、オプション引数

def f_4(x, y=3):
	return x + y

print(f_4(2))
print(f_4(2,4))

# スコープ、グローバル変数

x = 10

def f_5():
	print(x)
	global x
	x += 4
	print(x)

f_5()
print(x**3);
f_5()

# 例外処理(try, except)
print("例外処理(try, except)")

a = input("number of a:")
b = input("number of b: ")
a = int(a)
b = int(b)
try:
	print(a/b)
except (ZeroDivisionError, ValueError):
	print("b cannot be zero.")

