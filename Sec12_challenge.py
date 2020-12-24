# coding: UTF-8
import time, math

# Q1
print("""Q1：リンゴと言われて思い浮かぶ、4つの属性を考えよう。
その4つの属性をインスタンス変数にもつ、Appleクラスを定義しよう。""")

# Appleクラスの定義（w: wright(重さ)、s: size(サイズ)、c: cost(値段)、h: hardness(硬さ)）
class Apple:
	def __init__ (self, w, s, c, h):
		self.weight = w
		self.size = s
		self.cost = c
		self.hardness = h
		print("Create!!")

apple = Apple(10, 100, 120, 90)

print("このリンゴの重さは" + str(apple.weight) + "です。")
print("このリンゴのサイズは" + str(apple.size) + "です。")
print("このリンゴの値段は" + str(apple.cost) + "です。")
print("このリンゴの硬さは" + str(apple.hardness) + "です。")

time.sleep(1)
# Q2
print("""Q2：円を表すCircleクラスを定義しよう。そのクラスに、面積を計算して返すメソッドをareaを持たせよう。
面積の計算には、Pythonの組み込みモジュールmathのpi定数が使えます。
次に、Circleオブジェクトを作って、areaメソッドを呼び出し、結果を出力しよう。""")

# Circleクラスの定義（r: 半径(radius)）
class Circle:
	def __init__ (self, r):
		self.radius = r
		print("Create!!")
	
	# 円の面積を返す
	def area (self):
		return self.radius ** 2 *math.pi

circle = Circle(4)

print("半径" + str(circle.radius) + " cmの円の面積は、" + str(circle.area()) + " cm^2です。")

time.sleep(1)
# Q3
print("""Q3：三角形を表すTriangleクラスを定義して、面積を返すareaメソッドを持たせよう。
そしてTriangleオブジェクトを作って、areaメソッドを呼び出して、結果を出力しよう。""")

# Triangleクラスの定義（b: 底辺(bottom)、h: 高さ(hight)）
class Triangle:
	def __init__ (self, b, h):
		self.bottom = b
		self.height = h
		print("Create!!")
	
	# areaメソッドの定義：三角形の面積を返すメソッド
	def area (self):
		return self.bottom * self.height / 2

# Triangleクラスのインスタンス化
triangle = Triangle(12,13)

print("底辺" + str(triangle.bottom) + " cm、高さ" + str(triangle.height) + " cmの三角形の面積は、" + str(triangle.area()) + " cm^2です。")

time.sleep(1)
# Q4
print("""Q4：六角形を表すHexanagonクラスを定義しよう。
そのクラスには、外周の長さを計算して返すメソッドcalculate_perimeterメソッドを呼び出し、結果を出力しよう。""")

# Hexagonクラスの定義（osh: 1辺の長さ(one side length)）
class Hexagon:
	def __init__ (self, osh):
		self.one_side_length = osh
		print("Create!!")

	def calculate_perimeter (self):
		return self.one_side_length * 6

# Hexagonクラスのインスタンス化
hexagon = Hexagon(4)

print("1辺の長さが" + str(hexagon.one_side_length) + "cmの六角形の外周の長さは、" + str(hexagon.calculate_perimeter()) + "cmです。")













