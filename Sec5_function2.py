# coding: UTF-8

# タプル（色々）
my_tuple = tuple()	#空タプル
print(my_tuple)

my_tuple2 = ()			#空タプル
print(my_tuple)

why_not = ("R.Westbrook", 2008, True)		#オブジェクトは自由。カンマで区別。
print(why_not)

print(("se;f_taught",))		#要素が1つのタプルは、末尾にカンマをつける

print(why_not[0])			#インデックスで指定し、要素を抽出する

# 辞書（色々）
my_dict = dict()	#空辞書
print(my_dict)

my_dict2 = {}		#空辞書
print(my_dict2)	

nba_players = {"Westbrook":	"OKC",
						 "Lebron":			"CLE",
						 "Curry":			"GSW"}

print(nba_players)

nba_players["Embiid"] = "PHI"		#キーバリューペアの追加
print(nba_players["Embiid"])		#キーバリューペアの取り出し

print(nba_players)
del nba_players["Lebron"]			#キーバリューペアの削除
print(nba_players)

# 辞書を使ったプログラムの例

songs = {"ド": "ドーナツ",		"レ": "レモン",		"ミ": "みんな",		"ファ": "ファイト",
			   "ソ": "青い空",			"ラ":	"ラッパ",		"シ": "幸せ"}

kashi = input("音階を入力してください-> ")
if kashi in songs:
	print(songs[kashi])
else:
	print("お ま え は あ ほ か")

# コンテナ中のコンテナ（リストinリスト）
nba_players2 = []

okc = ["アダムス", "ロバーソン", "シェイ"]
was = ["ウォール", "ビール", "八村塁"]
sac = ["フォックス", "ボグダン", "バーンズ"]

nba_players2.append(okc)
nba_players2.append(was)
nba_players2.append(sac)

print(nba_players2)
okc = nba_players2[1]
print(okc)
print(nba_players2)
okc.append("ホーホーホ")
print(nba_players2)

# コンテナ中のコンテナ（タプルinリスト）
location = []

hyogo = ("近畿", "神戸")
okayama = ("中部", "岡山")

location.append(hyogo)
location.append(okayama)

print(location)

# コンテナ中のコンテナ（辞書inタプル）
birthday = {"大室璃紗": "1995/11/4", "掛橋沙耶香": "2001/11/27"}
birthday_list = [birthday]
print(birthday_list)
birthday_tuple = (birthday,)
print(birthday_tuple)

# コンテナ中のコンテナ（辞書のバリューに、[リスト]と(タプル)と{辞書}）
Ageo = {
			"ホームアリーナ": ("埼玉上尾", "京都"),
			"選手": ["吉野優理", "ジャジャサンティアゴ", "大室璃紗"],
			"事実": {"去年の成績": "3位", "今年の順位": "7位"}
			}

print(Ageo)
