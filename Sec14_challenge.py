# coding: UTF-8
import time

# Q1
print("""Q1：Squareクラスにsquare_listクラス変数を追加しよう。そして、新しくSquareクラスのオブジェクトが作られるたびに、
そのオブヘクトをこのリストに追加しよう。""")
time.sleep(1)

class Square1:
	square_list = []
	def __init__ (self, w, l):
		self.width = w
		self.length = l
		self.square_list.append((self.width, self.length))

s1 = Square1(10,10)
s2 = Square1(342, 482)
s3 = Square1(234, 932)

print(Square1.square_list)

time.sleep(1)
# Q2
print("""Q2：Squareクラスのオブジェクトをprint関数に渡したら、4辺それぞれの長さを出力しよう。
たとえば、Square(29)のようにオブジェクトを作ったら、print関数では29 by 29 by 29 by 29と出力しよう。""")
time.sleep(1)

class Square2:
	def __init__ (self, s1, s2, s3, s4):
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3
		self.s4 = s4
	
	def __repr__ (self):
		return "{} by {} by {} by {}".format(self.s1, self.s2, self.s3, self.s4)

square2 = Square2(23,65,43,62)
print(square2)

time.sleep(1)
# Q3
print("""Q3：2つのパラメータを受け取る関数を書こう。
この関数は同じオブジェクトを渡されたらTrueを返し、そうじゃなかったらFalseを返そう。""")
time.sleep(1)

def Nogizaka(oshi1, oshi2):
	if oshi1 is oshi2:
		return True
	else:
		return False
		

oshi = Nogizaka("Momoko Oozono", "Sayaka Kakehashi")
print(oshi)







