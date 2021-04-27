# String Replacer by Y式植林装置
# ファイル内部の文字列に高度な置換を適応します
import re

NUM_LEFT = 1


def replaceStr(m: re.Match):
    s: str = m.group(0)  # x=15 だとすれば、15が入る
    num = int(s)
    num += NUM_LEFT
    return str(num)


with open("ssw_UKR.txt", "r+") as f:
    buf = ""
    for line in f.readlines():
        buf += line+"\n"
    pattern = re.compile(r"\s?=\s?(\d+)")
    buf = pattern.sub(replaceStr, buf)
    f.write(buf)
