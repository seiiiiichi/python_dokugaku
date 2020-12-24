# coding: UTF-8

# Q1
print("Q1：文字列\"カミュ\"に含まれるすべての文字を1文字ずつ出力しよう。")
Kamyu = "カミュ"
print(Kamyu[0])
print(Kamyu[1])
print(Kamyu[2])

# Q2
print("""Q2：2つの文字列を入力させるプログラムを書こう。
その文字列をそれぞれ別の文字列の2つの箇所に穴埋めした新しい文字列を作ろう。
\"私は昨日[入力1]を書いて、[入力2]に送った！\"　そして、それを出力しよう。""")

print("誰に何を書いた？")
who = input("誰に？ ->")
what = input("何を？ ->")

print("私は昨日{}を書いて、{}に送った！".format(what, who))

# Q3
print("Q3：文法的には正しい文章を書いた文字列\"aldous Huxley was born in 1894.\"の先頭をメソッドを使って大文字にしよう。")

letter = "aldous huxley was born in 1894.".capitalize()
print(letter)

# Q4
print("Q4：文字列\"どこで？　だれが？　いつ？\"をメソッドで分割して、[\"どこで？\", \"だれが？\", \"いつ？\"]のようなリストにしよう。")

nani = "どこで？　だれが？　いつ？"
print(nani.split("　"))

# Q5
print\
("""Q5：リスト[\"The\", \"fox\", \"jumped\", \"over\", \"the\", \"fence\", \".\"]の文字列を
正しい英文になるように連結しよう。単語と単語の間は空白が必要ですが、最後のピリオドの前には空白は不要です。文字列を要素に持つリストを1つに連結するメソッドがあることを忘れずに！""")

fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
fox = fox[0:-2] + "."
print(fox)

# Q6
print("文字列\"A screaming comes across the sky.\"に含まれるすべての\"s\"をどる記号に置き換えた文字列を作ろう。")

print("A screaming comes across the sky.".replace("s","$"))

# Q7
print("メソッドを使って、\"Hemingway\"の中で最初に\"m\"が出現するインデックスを調べよう。")

print("Hemingway".index("m"))

# Q8
print("Q8：好きな本のセリフを探して、Pythonの文字列にしよう。ただし、クォートが含まれているセリフを選ぶこと。")

print("僕の趣味は地雷踏みじゃないよ。\"空中散歩\"さ。地雷を踏むのは、空中に飛び上がるのに、それが一番手っ取り早いからさ。")

# Q9
print("""Q9；文字列を\"+\"で結合して\"three three three\"という文字列を作ろう。
また、\"*\"を使って同じ文字列を作ろう。""")

print("three" + "three" + "three")
print("three" * 3)

# Q9
print("文字列\"四月の晴れた寒い日で、時計がどれも十三時をうっていた。\"をスライスして、「、」の前までの部分文字列を作ろう。")

remon = "四月の晴れた寒い日で、時計がどれも十三時をうっていた。"
print(remon[:11])






