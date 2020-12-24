# coding: UTF-8

#shuffleメソッドを利用する
from random import shuffle
import time

# Card クラス
class Card:
	
	# スート
	suits = ["spades", "hearts", "diamonds", "clubs"]
	
	# 値（リストのインデックスを値と揃えるためにNoneを2つ入れる）
	values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
	
	def __init__ (self, v, s):
		""""スートも値も整数値"""
		self.value = v
		self.suit = s
	
	# x <= y の演算ができるようになる特殊メソッド
	def __lt__ (self, c2):
		if self.value <= c2.value:
			return True
		else:
			return False
		return False
	
	# x >= y の演算ができるようになる特殊メソッド
	def __gt__ (self, c2):
		if self.value >= c2.value:
			return True
		else:
			return False
		return False
	
	# print関数にインスタンスオブジェクトを与えた時の出力
	def __repr__ (self):
		v = self.values[self.value] + " of " + self.suits[self.suit]
		return v

# Deckクラス
class Deck:
	def __init__ (self):
		self.cards = []
		# カード（値, スート）の登録。2-14までの値と、0-3のスート
		for i in range(2,15):
			for j in range(4):
				self.cards.append(Card(i, j))
	
		shuffle(self.cards)
	
	# cardsリストから要素を1つ削除して、その値を返す。リストが空ならNoneを返す。
	def rm_card(self):
		if len(self.cards) == 0:
			retrun
		return self.cards.pop()

# Playerクラス
class Player:
	def __init__ (self, name):
		#ゲームで何回勝ったか
		self.wins = 0
		# そのときプレーヤーが持っているカードを格納する
		self.card = None
		# プレーヤーの名前
		self.name = name

# Gameクラス
class Game:
	def __init__ (self):
		self.deck = Deck()
		name1 = input("プレーヤー1の名前\n->")
		name2 = input("プレーヤー2の名前\n->")
		self.player1 = Player(name1)
		self.player2 = Player(name2)
	
	# ラウンド終了時に呼び出す
	def wins(self, winner):
		print("このラウンドは{}が勝ちました。".format(winner))
	
	# カードドロー時に呼び出す
	def draw(self, player1_name, player1_card, player2_name, player2_card):
		print("{}は{}、{}は {}を引きました。".format(player1_name, player1_card, player2_name, player2_card))
	
	# 勝ったプレーヤーか、引き分けたかを返す
	def winner(self, player1, player2):
		if player1.wins > player2.wins:
			return "{}の勝利！".format(player1.name)
		if player1.wins < player2.wins:
			return "{}の勝利！".format(player2.name)
		return "引き分け！"
	
	# ゲームの開始
	def play_game(self):
		cards = self.deck.cards
		print("戦争(War)を始めます。🤗")
		
		while len(cards) >= 2:			# デッキのカード枚数が2枚以上ならループ
			# ゲームを終了する？
			response = input("q で終了、それ以外のキーでPlay：")
			if response == 'q':
				break
			
			# プレーヤーの登録
			player1_name = self.player1.name
			player2_name = self.player2.name
			
			# カードドロー
			player1_card = self.deck.rm_card()
			player2_card = self.deck.rm_card()
			self.draw(player1_name, player1_card, player2_name, player2_card)
			
			# 対戦結果を処理
			if player1_card > player2_card:
				self.player1.wins += 1
				self.wins(self.player1.name)
			else:
				self.player2.wins += 1
				self.wins(self.player2.name)
		
		# ゲーム終了時の処理
		print("ゲーム終了。{}".format(self.winner(self.player1, self.player2)))

game = Game()
game.play_game()















