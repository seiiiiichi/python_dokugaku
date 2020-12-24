# coding: UTF-8

# カプセル化（clientコードを利用しない方がいい）
class Data:
	def __init__ (self):
		self.nums = [1,2,3,4,5]
	
	def change_data (self, index, n):
		self.nums[index] = n

data_one = Data()
data_one.nums[0] = 100					# clientコード（この変更はやらな方がよい）
print("data_one.numsのデータは、" + str(data_one.nums) + "です。")

data_two = Data()
data_two.change_data(0, 100)		# クラス内の状態は、クラス内のメソッドを通じて操作する
print("data_two.numsのデータは、" + str(data_two.nums) + "です。")

# 継承

class Shape:					# 親クラス
	def __init__ (self, w, l):
		self.width = w
		self.length = l
	
	def print_size(self):
		print("{} by {}".format(self.width,self.length))

oya_shape1 = Shape(20,24)
oya_shape1.print_size()

class Square1 (Shape):		# 子クラス
	pass								# スイートがいるが、処理をスキップしたい場合にpassを記載する

ko_square = Square1(20,20)
ko_square.print_size()

# 子クラスにメソッドを追加できる
class Square2 (Shape):
	def area(self):
		return self.width * self.length

ko_square2 = Square2(10,10)
print(ko_square2.area())

# メソッドオーバーライド
class Square3 (Square2):
	def print_size(self):
		print("I am {} by {}".format(self.width, self.length))

ko_square3 = Square3(9,2)
ko_square3.print_size()

# コンポジション(has-a関係)
class Dog:
	def __init__ (self, name, breed, owner):
		self.name = name
		self.breed = breed
		self.owner = owner

class Person:
	def __init__ (self, name):
		self.name = name

sayaka = Person("Sayaka Kakehashi")
kosuke = Dog("Kosuke Nakahara", "Chihuahua", sayaka)
print(kosuke.owner.name)























