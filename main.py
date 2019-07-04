from calories import find_food_list_by_name

FILE_NAME = 'log.data'


class FoodLog:
    def __init__(self, date, meal_time, food_name, portion, calorie):
        self.date = date
        self.meal_time = meal_time
        self.food_name = food_name
        self.portion = portion
        self.calorie = calorie

    def __str__(self):
        return f'날짜 : {self.date} / 구분 : {self.meal_time} / 음식 : {self.food_name} / ' \
            f'양 : {self.portion} / 칼로리 : {self.calorie}'

    def to_csv(self):
        return f'{self.date},{self.meal_time},' \
            f'{self.food_name},{self.portion},{self.calorie}'

    @staticmethod
    def from_csv(line):
        line = line.split(',')
        return FoodLog(*line)


def create_food_log(food_logs):
    date = input('날짜는? ')
    meal_time = input('아침, 점심, 저녁, 간식? ')
    food_name = input('뭐먹? ')

    # TODO: 숫자가 아닌 게 들어왔을 때 예외처리
    portion = int(input('몇 인분? '))
    # calorie = input('칼로리 멍미? ')

    food_list = find_food_list_by_name(food_name)

    # TODO: 첫 번째 말고 정확하게 고르기 OR 고르게 하기
    # TODO: 못 찾았을 때 처리
    calorie = food_list[0]['kcal'] * portion
    food_name = food_list[0]['name']

    food_log = FoodLog(date, meal_time, food_name, portion, calorie)
    food_logs.append(food_log)


def read_food_log(food_logs):
    for log in food_logs:
        print(log)


def delete_food_log(food_logs):
    del food_logs[-1]


def load_from_file():
    result = []
    try:
        with open(FILE_NAME, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                result.append(
                    FoodLog.from_csv(line.split('\n')[0])
                )
    except FileNotFoundError:
        pass

    return result


def store_to_file(food_logs):
    with open(FILE_NAME, 'w') as f:
        for idx in range(len(food_logs)):
            f.write(food_logs[idx].to_csv())
            if idx != len(food_logs) - 1:
                f.write('\n')


if __name__ == '__main__':
    food_logs = load_from_file()

    while True:
        user_input = input('뭐할까? 입력하려면 입력이라고 말해? ')
        if user_input == '입력':
            create_food_log(food_logs)
            store_to_file(food_logs)
        elif user_input == '조회':
            read_food_log(food_logs)
        elif user_input == '삭제':
            delete_food_log(food_logs)
            store_to_file(food_logs)
            read_food_log(food_logs)
