# coding: UTF-8

# ファイルを開く（ファイル書き込み（+作成））
st = open("test1.txt", "w", encoding="utf-8")
st.write("PHI？優勝！！")
st.write("OKC優勝！")
st.close()

# ファイルを自動的に開く（閉じ忘れ防止）
with open("test2.txt","w", encoding="utf-8") as f:
	f.write("NEC優勝！")

# ファイルの読み出し
with open("test2.txt","r",encoding="utf-8") as f:
	print(f.read())

# ファイル読み出し時は、変数やコンテナに入れておくと良い
test3_list = []
with open("test3.txt","r",encoding="utf-8") as f:
	test3_list.append(f.read())

print(test3_list)

# CSVファイルの作成
import csv
with open("test.csv","w",newline="") as f:
	w = csv.writer(f, delimiter=",")
	w.writerow(["one", "two", "three"])
	w.writerow(["four", "five", "six"])

# CSVファイルの読み込み
with open("test.csv","r") as f:
	r = csv.reader(f, delimiter = ",")
	for row in r:
		print("|".join(row))


























