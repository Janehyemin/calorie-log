class FoodLog:
    def __init__(self, date, meal_time, food_name, portion, calorie):
        self.date = date
        self.meal_time = meal_time
        self.food_name = food_name
        self.portion = portion
        self.calorie = calorie

    def __str__(self):
        return '날짜 : %s / 구분 : %s / 음식 : %s / 양 : %s / 칼로리 : %s' % (
            self.date,
            self.meal_time,
            self.food_name,
            self.portion,
            self.calorie
        )


def create_food_log(food_logs):
    date = input('날짜는? ')
    meal_time = input('아침, 점심, 저녁, 간식? ')
    food_name = input('뭐먹? ')
    portion = input('몇 인분? ')
    calorie = input('칼로리 멍미? ')

    food_log = FoodLog(date, meal_time, food_name, portion, calorie)
    food_logs.append(food_log)


def read_food_log(food_logs):
    for log in food_logs:
        print(log)


def delete_food_log(food_logs):
    del food_logs[-1]


if __name__ == '__main__':
    food_logs = []

    while True:
        user_input = input('뭐할까? 입력하려면 입력이라고 말해? ')
        if user_input == '입력':
            create_food_log(food_logs)
        elif user_input == '조회':
            read_food_log(food_logs)
        elif user_input == '삭제':
            delete_food_log(food_logs)
            read_food_log(food_logs)
