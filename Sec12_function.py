# coding: UTF-8

# Orangeのクラスを定義
class Orange:
	def __init__ (self, w, c):
		""" weight（重さ）はグラム """
		self.weight = w
		self.color = c
		self.mold = 0
		print("Created !!")
	
	def rot(self, days, temp):
		""" temp（温度）は摂氏 """
		self.mold = days * temp

# Orangeクラスのインスタンス化
orl1 = Orange(10, "dark orange")
orl2 = Orange(8, "light orange")
orl3 = Orange(4, "yellow")

print(orl1)
print(orl2)
print(orl3)

print(orl1.weight)
print(orl1.color)

orl1.rot(10, 37)
print(orl1.mold)

# 長方形を表すクラス
class Rectangle:
	def __init__ (self, w, l):
		self.width = w
		self.len = l
	
	def area (self):
		return self.width * self.len
	
	def change_size (self, w, l):
		self.width = w
		self.len = l

rectangle = Rectangle(20, 45)
print(rectangle.area())
rectangle.change_size(49, 53)
print(rectangle.area())