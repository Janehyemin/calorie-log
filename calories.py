import csv

calories = []


def read_csv(filename, column_num):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        rdr = csv.reader(f)
        next(rdr)
        for line in rdr:
            calories.append({
                'name': line[column_num[0]],
                '1quantity': line[column_num[1]],
                'kcal': float(line[column_num[2]])
            })


read_csv('OPENDATA_FOOD_1.csv', [2, 3, 4])
read_csv('OPENDATA_FOOD_2.csv', [3, 4, 5])
read_csv('OPENDATA_FOOD_3.csv', [2, 3, 4])


def find_food_list_by_name(name):
    food_list = []
    # 이름으로 찾기
    for c in calories:
        if name in c['name']:
            food_list.append(c)
    return food_list
