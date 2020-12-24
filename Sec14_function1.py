# coding: UTF-8

# クラス変数はどこからでもアクセスできるよ。
class Rectangle:
	recs = []
	
	def __init__ (self, w, l):
		self.width = w
		self.len = l
		self.recs.append((self.width, self.len))

	def print_size (self):
		print("{} by {}".format(self.width, self.len))

r1 = Rectangle(10, 24)
r2 = Rectangle(29,41)
r3 = Rectangle(57,32)

print(Rectangle.recs)

# 特殊メソッド。objectから継承したメソッドを使用する。（__repr__メソッド）
print(r1)

# objectクラスの__repr__メソッドをオーバーライドする
class Lion:
	def __init__ (self, name):
		self.name = name
	
	def __repr__ (self):
		return self.name

lion = Lion("Ookami")
print(lion)

# 特殊メソッド（__add__メソッド）
class AlwaysPositive:
	def __init__ (self, number):
		self.n = number
	
	def __add__ (self, other):
		return abs(self.n + other.n)		# abs関数は、絶対値を返す。

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)

# isキーワード
class Person:
	def __init__ (self):
		self.name = "Bob"

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)

# isキーワード（Noneかどうかを調べる）
x = 10
if x is None:
	print("x はNone :(")
else:
	print("x はNoneではない:)")

x = None
if x is None:
	print("x はNone :(")
else:
	print("x はNoneではない:)")
