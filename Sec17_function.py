# coding: UTF-8

# Pythonで正規表現を使う際にimpotrする標準ライブラリ: re
import re

l = "If you use Google Translate to read Japanese, I wonder if I should translate it into English before sending it."

# re.findall関数（一致したすべての部分をリストで返す）
matches1 = re.findall("it", l)
print(matches1)

# re.findall関数（3つ目の引数に re.IGNORECASE フラグを渡すと、大文字小文字の区別せず検索する）
matches2 = re.findall("if", l, re.IGNORECASE)
print(matches2)

# re.findall関数（3つ目の引数に re.MULTILINE フラグを渡すと、複数行のテキストを複数行として扱う）
zen = """Although never is
often better than
*right* now.
If the implementation is
hard to explain,
it's a bad idea.
If the implementation is
easy to explain,
it may be a good idea.
Namespaces are
one honking great
idea -- let's do
more of those!
"""

matches3 = re.findall("^If", zen, re.MULTILINE)
print(matches3)

# [abc]：a,b,cのいずれか1文字と一致する文字列を検索する
import re

name = "Oomuro Oozono"
matches4 = re.findall("oo[zm][ou][nr]o", name, re.IGNORECASE)
print(matches4)

# \d：数値と一致させる
Ageo = "#23 Risa Oomuro. #3 Santiago"
matches5 = re.findall("\d", Ageo, re.IGNORECASE)
print(matches5)

# *?：非貪欲な正規表現
t = "__one__ __two_ __three__ __four__ five____six__"
matches6 = re.findall("__.*?__", t,)
print(matches6)

# Mad Libsゲーム
text = """埼玉上尾メディックスの背番号23番の選手は、 __選手名__ 選手です。
__選手名__ は、身長 __数値__ __単位__と、埼玉上尾メディックスの選手の中でとても小さいですが、
ひとたびコートに立つと、存在感はとても大きいです。
__プレー1__ が特に上手で、最近は __プレー2__ も求められています。
"""

def mad_libs (mls):
	"""
	:param mls: 文字列で、ユーザーに入力してもらいたい単語(= hint)の部分は前後を2つのアンダースコアで挟んでください。hintの単語にはアンダースコアを含めないでください。__hint_hint__はダメです。__hint__はOKです。
	"""
	hints = re.findall("__.*?__",mls)
	if hints is not None:
		print(mls)
		for word in hints:
			question = "{}を入力してください。\n->".format(word)
			new = input(question)
			mls = mls.replace(word, new, 1)
			print("\n")
			mls = mls.replace("\n", " ")
			print(mls)
	else:
		print("引数 mls が無効です。")

mad_libs(text)

























