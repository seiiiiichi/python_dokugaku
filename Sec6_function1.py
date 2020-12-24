# coding: UTF-8

# 文字列もイテラブル
hito = "しんぶんし"
print(hito[0])
print(hito[1])
print(hito[2])
print(hito[3])
print(hito[4])

# マイナスインデックス
print(hito[-1])
print(hito[-2])
print(hito[-3])
print(hito[-4])
print(hito[-5])

# 「+」で文字列を連結
print("I" + " love" +" you")

# 「*」で文字列を連続表示
print("ピザ" * 10)

# 文字列を全て大文字にする
print("trust the process".upper())

# 文字列を全て小文字にする
print("Life Goes ON...".lower())

#文字列の先頭を大文字にする
print("i was born to love you.".capitalize())

# 書式化（「{}」の部分を置き換えるメソッド）
print("こんにちは、{}".format("赤ちゃん"))

name = input("誰に会いましたか？\n->")
print("こんにちは、{}".format(name))

year_born = "1997"
print("{}は、{}年に生まれました。".format(name, year_born))

# 文字列の分割、結合

print("埼玉上尾が負けたんだ。2セットもリードしてたんだぜ！".split("。"))

first_alphabet = "abc"
gattai = "+".join(first_alphabet)
print(gattai)

win_the_championship = ["GSW", "blew", "a", "3-1", "lead", "."]
print(" ".join(win_the_championship))

# 空白除去（文字列の最初と最後だけ）
space = "                      俺yade  "
print(space.strip())

# 置換
name = "Seiichi Enomoto"
print(name.replace("i","o") + name.replace("o","x"))

# 文字列を検索
print("animals".index("a"))
try:
	print("animals".index("z"))
except:
	print("Not found.")

# 包含
print("Cat" in "Cat in the hat.")
print("Bat" in "Cat in the hat.")
print("like" not in "I Like you.")

# エスケープ文字
print("What the spel is \"polish\"?")

# スライス
kaidotakeru = ["チーム・バチスタの栄光", "ナイチンゲールの沈黙",
						 "ジェネラル・ルージュの凱旋", "イノセントゲリラの祝祭",
						 "アリアドネの弾丸", "ケルベロスの肖像", "カレイドスコープの箱庭"]
print(kaidotakeru[2:4])

shiratorikeisuke = "厚生労働省医療過誤死関連中立的第三者機関設置推進準備室室長"
print(shiratorikeisuke[0:10])
print(shiratorikeisuke[10:30])
print(shiratorikeisuke[:15])
print(shiratorikeisuke[25:])
print(shiratorikeisuke[:])