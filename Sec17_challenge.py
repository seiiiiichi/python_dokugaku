# coding: UTF-8

# Q3
print("Q3：Pythonのreモジュールを使って、何かの文字の後に o が2回登場する単語に一致する正規表現を書こう。そして、\"The ghost that says boo haunts the loo\"の文中にある boo や loo に一致するか試そう。")

import re

print("")

string = "She looks like Risa Oomuro. But sometimes She looks likes Momoko Oozono."

print(string)
check1 = re.findall(".oo.*?[ .]", string, re.IGNORECASE)
print(check1)

print("")

text = "The ghost that says boo haunts the loo"
print(text)
check2 = re.findall(".oo", text, re.IGNORECASE)
print(check2)