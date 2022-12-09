import random
help = """
 help - напечатать справку по программе.
 add - добавить задачу в список.
 show - напечатать все добавленные задачи.
 random - добавлять случайную задачу на дату Сегодня."""

RANDOM_TASKS = ["Погладь котэ", "Cожги дом", "Купи змею"]
tasks = {

}

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
    print("Задача", task, "на", date, "добавлена")

run = True
print("Привет, я ToDo. Если ты пользуешься первый раз, то введи команду help")
while run:
    command = input("Введите команду: ")
    if command == "help":
        print(help)
    elif command == "show":
        date = input("Введите дату для отображения списка задач: ")
        if date in tasks:
                for task in tasks[date]:
                    print('-', task)
        else:
            print("Такой даты нет. Все ваши задачи")
            print("-", tasks)
    elif command == "add":
        date = input("Введите дату для добавления задачи: ")
        task = input("Введите задачу: ")
        add_todo(date, task)
    elif command == "random":
        task = random.choice(RANDOM_TASKS)
        add_todo("Сегодня", task)
    else:
        print("Неизвестная команда")
        break
print("До свидания!")

