# /* coding: utf-8 * /

import csv

with open('Leetspeak_dict.csv') as f:
    d = dict(filter(None, csv.reader(f)))

print(d)
