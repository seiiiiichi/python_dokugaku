# coding: UTF-8
import random,time

def hangman(word):
	"""
	Returns:
	:param word: プレーヤーに当ててもらいたい単語
	:return: 
	"""
	# 変数宣言
	wrong = 0		# まちがいの回数をカウントする変数
	stages = ["",
					"___________               ",
					"|          |             ",
					"|          |             ",
					"|          ◯          ",
					"|        / | \         ",
					"|        ／ ＼         ",
					"|                         ",
					]						# プレーヤーが間違えるたびに、1行に1つずつ表示する
	rletters = list(word)			# 変数wordを1文字ずつ分解して、リストにしたもの
	board = ["_"] * len(word)	# 変数wordの文字数分のアンダースコアをリストで保持する
	win = False						# プレーヤーの勝敗を保持する変数
	
	print("ハングマンへようこそ！")
	print(" ".join(board))
	time.sleep(2)
	# ゲームをプレー
	while wrong < len(stages) - 1:
		print("")
		
		# プレーヤーが文字を入力
		msg = "1文字予想してね💙💚💛"
		char = input(msg + "\n-> ")
		
		# 入力された文字があるかないかを判定
		if char in rletters:
			cind = rletters.index(char)		# 答えの文字列の中で、当てられた文字のインデックスを格納する
			board[cind] = char				# アンダースコアの中で、当てられた文字は開ける
			rletters[cind] = '$'					# 答えの文字列の中で、当てられた文字は"$"に置き換える。2重に開くことを避けるため
		else:
			wrong += 1							# プレーヤーが間違えた場合、wrong変数をインクリメント
		
		# 文字が開くかどうかを出力
		print(" ".join(board))					# 現在開いている文字を出力。それ以外はアンダースコアを出力
		e = wrong + 1							# ハングマンの絵をどこまで出力するかを決めるための変数。wrong変数 + 1の値を格納する
		print("\n".join(stages[0:e]))		# ハングマンの絵を改行で分けながら、e変数の値までスライスして表示する
		
		# 文字がすべて開けば、プレーヤーの勝利
		if "_" not in board:
			print("You win!!!")
			print(" ".join(board))
			win = True
			break
	
	# プレーヤーが負けて whileループを抜けた場合
	if not win:
		print("\n".join(stages[0:wrong+1]))
		print("You lose!!!ll\n正解は「{}」".format(word))

# 答えの単語リスト
answer_list = ["great", "downtown", "spectacular", "fucking", "sync", "michael", "spring", "priority", "protocol"]

# 答えの単語リストからランダムに、答えを選択
answer = answer_list[random.randint(0,8)]

# ハングマンの実行
hangman(answer)





























