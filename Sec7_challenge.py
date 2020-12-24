# coding: UTF-8

# Q1
print("""Q1：次のリストの要素をそれぞれ出力しよう。
[\"ウォーキング・デッド\", \"アントラージュ\", \"ザ・ソプラノズ\", \"ヴァンパイア・ダイアリーズ\"]""")

eigas = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for eiga in eigas:
	print(eiga)

# Q2
print("Q2：25から50までの数値をそれぞれ出力しよう。")
for i in range(25,51):
	print(i)

# Q3
print("Q3：チャレンジ1のリストの要素をそれぞれ、インデックス値と一緒に出力しよう。")
for i, eiga in enumerate(eigas):
	print("{}:{}".format(i, eiga))

# Q4
print("""Q4：無限ループする数字当てプログラムを書こう。
ユーザーに文字を入力してもらい、qが入力されたら終了、数字が入力されたら正解かどうか判定しよう。
正解の数値はプログラム内にいくつかリストで持たせておいて、
ユーザーが入力した数字がそのどれかと一致したら「正解」、一致しなかったら「不正解」と表示しよう。
もし数字かq以外の文字が入力されたら、「数字を入力するか、qで終了します」と表示しよう。""")

correct_list = [3,6,3,6,434,6,76,334,25,78,9,42,1,4]
print("数字当てクイズ。")
while True:
	user_answer = input("数字を入力してください。「q」を入力すれば終了します。\n->")
	if user_answer == "q":
		print("なんや、終わんのかい。")
		break
		
	try:
		user_answer = int(user_answer)
	except ValueError:
		print("数字を入力するか、qで終了します。")
		continue
	if user_answer in correct_list:
		print("すごいな！あるで！")
	else:
		print("ちゃうで。やり直して。")

# Q5
print("""Q5：2つのリストに含まれるすべての数字の組み合わせで掛け算しよう。
1つ目のリストは[8, 19, 148, 4]、2つ目のリストは[9, 1, 33, 83]で、
それぞれ掛け算した結果は新しいリストに格納しよう。""")

list1 = [8,19, 148, 4]
list2 = [9, 1, 33, 83]
times = []

for i in list1:
	for j in list2:
		times.append(i * j)
print(times)


















