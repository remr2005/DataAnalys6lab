import csv
from dsmltf import knn_classify, k_neighbours_classify

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
    # датасеты приведенные в нужный формат
    data0 = [(i[:-1],i[-1]) for i in data]
    data1 = [(i[:-1],round(i[-1])) for i in data]
    # словарь с результатами
    dict0 = k_neighbours_classify(11,data0[:100])
    dict1 = k_neighbours_classify(11,data1[:100])
    # проценты точности?
    a0 = [dict0[i][0]/dict0[i][1] for i in range(1,12)]
    a1 = [dict1[i][0]/dict1[i][1] for i in range(1,12)]
    # лучшие k
    k0 = a0.index(max(a0))+1
    k1 = a1.index(max(a1))+1
    # Центральная Япония (34-39° с.ш., 136.5-142° в.д.)
    latitude, longitude = map(lambda x: float(x), input("Ведите широту и долготу ").split())
    print(knn_classify(k0,data0,(latitude,longitude)))
    print(knn_classify(k1,data1,(latitude,longitude)))    

if __name__ == "__main__":
    main()