# coding: UTF-8
import time

# Q1
print("""Q1：RectangleとSquareクラスを作ろう。両方のクラスに、その図形の外周の長さを計算して返すcalculate_perimeterメソッドを定義しよう。
そして、RectangleとSquareのオブジェクトを作って、それぞれのcalculate_perimeterメソッドを呼ぼう。""")

class Rectangle1:							# Rectangle1クラスの定義
	def __init__ (self, width, length):
		self.width = width
		self.length = length
	
	def calculate_perimeter (self):
		return (self.width + self.length) * 2

class Square1 (Rectangle1):			# Square1クラスの定義
	pass

rectangle1 = Rectangle1(34, 82)
square1 = Square1 (89, 46)

print(rectangle1.calculate_perimeter())
print(square1.calculate_perimeter())

time.sleep(1)
# Q2
print("""Squareクラスにchange_sizeメソッドを定義して、そこに渡した数値分だけSquareオブジェクトの横幅を増やしたり、減らしたり（マイナス値の場合）しよう。""")

class Square2 (Square1):
	def change_size(self, offset):
		return self.width + offset

square2 = Square2(2896, 1876)
offset = input("変化させたい値を入力してください。\n->")
print("横幅のサイズは、{}です。".format(square2.change_size(int(offset))))

time.sleep(1)
# Q3
print("""Q3：Shapeクラスを定義しよう。呼ばれたら\"I am a shape \"を返すメソッドwhat_am_iを定義しよう。
前のチャレンジで定義したRectangleとSquareクラスを変更して、このShapeクラスを継承させよう。
そして、RectangleとSquareのオブジェクトを生成して、このチャレンジで追加したメソッドwhat_am_iを呼んでみよう。""")

class Shape:
	def __init__ (self):
		pass
	
	def what_am_i (self):
		print("I am a shape.")

class Rectangle3(Shape):
	pass

class Square3(Shape):
	pass

rectangle3 = Rectangle3()
square3 = Square3()
rectangle3.what_am_i()
square3.what_am_i()

time.sleep(1)
# Q4
print("""Q4：HorseクラスとRiderクラスを定義しよう。
コンポジションを使って、馬（Horse）に騎手（Rider）を持たせよう。""")

class Horse:
	def __init__ (self, name, owner):
		self.name = name
		self.owner = owner
	
class Rider:
	def __init__ (self, name):
		self.name = name

yutaka = Rider("武豊")
hisha = Horse("飛車", yutaka)

print("{}の騎手は、{}です。".format(hisha.name,hisha.owner.name))














