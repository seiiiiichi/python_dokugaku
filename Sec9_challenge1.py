# coding: UTF-8
import time

# Q1
print("Q1：コンピューターにある何かのファイルをPythonで開いて、コンテンツを出力しよう。")
import os
os

with open("Sec8_function1.txt","r") as f:
	print(f.read())

time.sleep(1)
# Q2
print("Q2：何か質問するプログラムを書こう。入力された回答をファイルに書き出そう。")

with open("Sec9_challenge2_answer.txt","w",encoding="utf-8") as f:
	answer = input("誕生日は？\n->")
	f.write(answer)

time.sleep(1)
# Q3
print("""Q3：リストのリストに含まれている要素をCSVファイルに書き出そう。データは次の通り:
[[\"Top Gun\", \"Risky Business\", \"Minority Report\"], [\"Titanic\", \"The Revenant\", \"Inception\"], [\"Training Day\", \"Man of Fire\", \"Flight\"]]
データの各要素はCSVの1行となり、その1行に含まれる各要素がカンマで区切られるように書き出そう。""")

import csv

movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man of Fire", "Flight"]]
with open("Sec9_challenge3.csv","w",newline="") as f:
	w = csv.writer(f,delimiter = ",")
	w.writerow(movies[0])
	w.writerow(movies[1])
	w.writerow(movies[2])

with open("Sec9_challenge3.csv","r") as f:
	r = csv.reader(f, delimiter = ",")
	for row in r:
		print(row)

time.sleep(1)
# Q4
print("""Q4：チャレンジ3を日本語で同じようにやってみよう。
たとえば、\"Top Gun\"を\"トップガン\"のように日本語に置き換えて、CSVファイルに書き出そう。""")

movies = [["トップガン", "リスキービジネス", "マイノリティレポート"], ["タイタニック", "リベナント", "インセプション"], ["トレーニングデイ", "炎の男", "フライト"]]
with open("Sec9_challenge4.csv","w",newline="") as f:
	w = csv.writer(f,delimiter = ",")
	w.writerow(movies[0])
	w.writerow(movies[1])
	w.writerow(movies[2])

with open("Sec9_challenge4.csv","r") as f:
	r = csv.reader(f, delimiter = ",")
	for row in r:
		print(row)



















