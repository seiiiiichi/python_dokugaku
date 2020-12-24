# coding: UTF8

# mathモジュールをインポート
import math
# pow(x,y) -> xのy乗を返す。
print(math.pow(2,3))

# randomモジュール
import random
# randint(x,y) -> 整数xとyの間の整数をランダムに返す。
print(random.randint(1,8))

# statisticsモジュール
import statistics
numbers = [3,6,2,24,54,7,283,392,279,9,39,54,2,2]
# mean(x) -> 整数のリストxから平均値を返す。
print(statistics.mean(numbers))
# median(x) -> 整数のリストxから中央値を返す。
print(statistics.median(numbers))
# mode(x) -> 整数のリストxから最頻値を返す。
print(statistics.mode(numbers))

# keywordモジュール
import keyword
# iskeyword(x) -> xがPythonのキーワードかどうかをチェックする。TrueかFalseを返す。
print(keyword.iskeyword("for"))
print(keyword.iskeyword("Lebron"))














