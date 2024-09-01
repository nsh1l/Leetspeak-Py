import csv

def main():
    w = input("変換したい英数字を入力してください: ").upper()
    with open('dict.csv') as f:
        ls = dict(filter(None, csv.reader(f)))
    print(w.translate(str.maketrans(ls)))

if __name__ == '__main__':
    main()