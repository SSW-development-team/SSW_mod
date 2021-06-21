import re
# ステートのキーと値を入力すると、各言語用に変換してくれる
# 例：「STATE_1:0 "コルシカ"」→「state_1_def:0 "コルシカ", state_1_fra:0 "コルシカ", state_1_ger:0 "コルシカ"」
lang_keys = set(["def"])
lang_keys=lang_keys.union(set(input("言語キーのリストを,で区切って入力してください(例：fra,ger,...)\n").split(",")))
print("ステート名のキーバリューリスト（改行区切り）を入力してください。終わったらendと入力してください\n例\n STATE_1:0 \"コルシカ\"\n STATE_2:0 \"ラティウム\"")
f = open("state_names_output.txt","w")
f.write("l_english:\n")
import re
while True:
    i = input(">")
    if i == "end":
        f.close()
        break
    for lang_key in lang_keys:
        key = re.sub(r' STATE_(\d+):(\d) "(\w+)"', r' state_\1_LANG_KEY:\2 "\3"', i)
        key=key.replace("LANG_KEY",lang_key)
        print(key)
        f.write(key + "\n")
