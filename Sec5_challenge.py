# coding: UTF-8

# Q1
print("Q1：好きなミュージシャンのリストを作ろう")

musician = ["Mr.Children", "西野カナ", "乃木坂46"]
print(musician)

# Q2
print("Q2：タプルのリストを作ろう。各タプルにはあなたが行ったことのある場所の緯度と経度を持たせよう")

goto = [(35.6587512,139.3301011), (34.6410205,135.1009901)]
print(goto)

# Q3
print("Q3：辞書を作ろう。辞書にはあなたの特徴を表すキーバリューのペアを持たせよう。例えば、身長、好きな色、好きな作家、など。")

challactor = {"身長": "166.5cm", "好きな色": ["黄色","青"],"好きな作家": "海堂尊"}
print(challactor)

# Q4
print("Q4：任意のキーを入力させるプログラムを書こう。入力されたキーを使って、1つ前のチャレンジで用意した辞書から、バリューを取得して表示しよう。")

data = input("なに知りたい？\n1. 身長　2. 好きな色　3. 好きな作家\n->")

if data in challactor:
	print(challactor[data])
else:
	print("ちゃうので頼むわ、、")

#Q5
print("Q5：あなたが好きなミュージシャンを辞書のキーに入れ、そのバリューとしてそのミュージシャンの今日をリストで持たせよう。")

favorite_musician = {
								"Mr.Children": ["365日", "HANABI", "turn over?"],
								"西野カナ": ["Always", "たとえどんなに", "Esperanza"],
								"乃木坂46": ["逃げ水", "図書室の君へ", "裸足でsummer"],
								}
print(favorite_musician)

# Q6
print("Q6：リスト、タプル、辞書はPythonの組み込みコンテナの一部です。Pythonのset(コンテナの1つ)について調べよう。setは何に使えるだろう？")

# set関数（重複なし、要素の順番なし）
myset1 = set([1,1,2,2,3,4])
myset2 = set([1,2,3,4])
print(myset1)
print(myset2)

# set関数（要素を追加）
myset1.add(5)
print(myset1)

# set関数（要素を削除、要素を全削除）
myset1.remove(3)
myset2.clear()
print(myset1)
print(myset2)

# set関数（和集合、積集合、差集合、排他的論理和集合）
A = set([1,2,3])
B = set([3,4,5])
print(A | B)						# 和集合
print(A.union(B))				# 和集合

print(A & B)						# 積集合
print(A.intersection(B))	# 積集合

print(A - B)						# 差集合
print(A.difference(B))		# 差集合

print(A ^ B)										# 排他的論理和集合
print(A.symmetric_difference(B))		# 排他的論理和集合

# set関数（listからsetを作る）
list_number = [32,1,6,33,4,0,3,2,1,1,1,3,5,67]
set_number = set(list_number)
print(list_number)
print(set_number)














