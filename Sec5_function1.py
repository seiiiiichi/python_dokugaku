# coding: UTF-8

# メソッド（文字列を大文字にする）
print("Hello".upper())

# メソッド（文字を置き換える）
print("Kobe Bryant".replace("b","d"))

# リスト（空のリストを作成）
fruit = list()
print(fruit)
vegetable = []
print(vegetable)

# リスト（空でないリストを作成）
fruit2 = ["Apple", "Orange", "Pear"]
print(fruit2)

# リスト（要素を追加）
fruit2.append("Banana")
print(fruit2)
fruit2.append("Peach")
print(fruit2)

# リスト（要素は文字列でも整数でもブール型でも可能。どんなオブジェクトでも格納できる。）
random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("Lebron")

print(random)

# リスト（インデックスで要素を取り出せる）
print(fruit2[0])
print(fruit2[1])
print(fruit2[2])
print(fruit2[3])

print(fruit2[3].replace("a","o"))

# リスト（リストはミュータブル(変更可能)）
colors = ["Red", "Green", "Blue"]
print(colors)
colors[1] = "Yellow"
print(colors)
colors[0] = ""
print(colors)

# リスト（リストの末尾の要素を取り除く）
item = colors.pop()
print(item)
print(colors)

# リスト（2つのリストを連結させる）
print(fruit2 + colors)

# リスト（リストにある要素が含まれているかどうか調べる）
print("Banana" in fruit2)
print("Yellow" not in colors)

# リスト（サイズ(要素の数)を取得）
print(len(fruit2))
print(len(colors))
print(len(vegetable))

# リスト（リストを使ったちょっとしたプログラム）

teams = ["GSW", "ATL", "PHI", "OKC"]

guess = input("NBAのチームの中で抽選！-> ")

if guess in teams:
	print("あたり！")
else:
	print("hazure")























