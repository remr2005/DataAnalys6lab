import csv

# спарсим данные с csv файла
def load_dataset() -> list:
    res = []
    with open("usgs_japan_1968_2018.csv", "r") as f:
        for row in csv.reader(f,delimiter=','):
            try:
                # будем добавлять только широту, долготу и магнитуду
                res.append([float(row[1]),float(row[2]),float(row[4])])
            except:
                continue
    return res
        
def main():
    data = load_dataset()

if __name__ == "__main__":
    main()