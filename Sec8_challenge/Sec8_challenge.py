# coding: UTF-8
import time

# Q1
print("Q1：statisticsモジュールの別の関数を呼んでみよう。")
import statistics
numbers = [3824,285,60,2,4,0,4284,4,4,20529]

print("pvariance：母分散")
print(statistics.pvariance(numbers))

print("pstdev：標本")
print(statistics.pstdev(numbers))

time.sleep(2)
# Q2
print("""Q2：cubedという名前のモジュールを作って関数を1つ書こう。
関数は1つの数値を引数として受け取り、渡された数値を3乗して返そう。
このモジュールを他のモジュールからインポートして関数を呼び出そう。""")
import cubed
number = input("3乗したい値を入力してください。\n->")
print(cubed.pow3(int(number)))