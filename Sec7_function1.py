# coding: UTF-8

# forループ（文字を1つずつ）
name = "Ted"
for character in name:
	print(character)

# forループ（10回表示）
for i in range(10):
	print(name)

# forループ（リストを1つずつ）
shows = ["GOT", "Narcos", "Vice"]
for show in shows:
	print(show)

# forループ（タプルを1つずつ）
nec = ("SarinaKoga", "YukaSawada", "ManamiKojima")
for player in nec:
	print(player)

# forループ（辞書のキーを取り出す）
volley_player = {"SaitamaAgeo": "RisaOomuro",
			  "ToreyAllows": "MayuIshikawa",
			  "HitachiRiverle": "MiyuKubota",
		}
for team in volley_player:
	print(team)

# forループ（リストの中身を変更できる_けどめんどくさいやり方）
tv = ["Yohukashi", "Kanjamu", "Kuronikuru"]
i = 0
for show in tv:
	new = tv[i]
	new = new.upper()
	tv[i] = new
	i += 1
	print(tv)
print(tv)

# forループ（インデックス変数値を自動的に用意してくれる）
lal = ["LeBron", "Anthony", "Bron"]
for i, new in enumerate(lal):
	new = lal[i]
	new = new.upper()
	lal[i] = new
print(lal)

# forループ（forループの中で、リストの要素を加工し、別のリストに要素を追加する）
phi = ["hoford", "Shimeiken"]
okc = ["furgason", "danny"]
trade = []

for player in phi:
	player = player.upper()
	trade.append(player)

for assett in okc:
	assett = assett.upper()
	trade.append(assett)

print(trade)

# forループ（range関数）
for i in range(1,11):
	print(i)

# whileループ
x =10
while x > 0:
	print("{}".format(x))
	x -= 1
print("Happy Birthday!!")

# break文
question = ["What is your name?",
				   "What is your fav. color?",
				   "What is your quest?"]

n = 0
while True:
	print("Type q to quit.")
	answer = input(question[n] + "\n->")
	if answer == "q":
		break
	n = (n+1) % 3

# continue文
print("continue文(for文)")
for  i in range(1,6):
	if i ==3:
		continue
	print(i)

print("continue文(continue文)")
i = 1
while i <= 5:
	if i == 3:
		i += 1
		continue
	print(i)
	i += 1

# 入れ子のループ
print("入れ子のループ")
for i in range(1,3):
	print(i)
	for letter in ["a", "b", "c"]:
		print(letter)

list1 = [1,2,3,4]
list2 = [5,6,7]
added = []

for i in list1:
	for j in list2:
		added.append(i * j)
print(added)

while input("y or n?\n->") != "n":
	for i in range(0,2):
		print(i)
