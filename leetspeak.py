# /* coding: utf-8 */

import csv

# 辞書ファイル読み込み


with open('Leetspeak_dict.csv') as f:
    ls_dict = dict(filter(None, csv.reader(f)))

# リートスピークに変換


def cvrt_text(data):
    list_data = list(data)
    converted_data = []

    for i in list_data:
        converted_data += ls_dict[i]

    output_text = ''.join(converted_data)

    return output_text

# 本体プログラム


print("変換したい英数字を入力してください")
raw_input = input().upper()
output = cvrt_text(raw_input)

print("\n変換前: {} \n変換後: {}".format(raw_input, output))
