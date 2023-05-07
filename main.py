import re


def find_good_numbers(string):
    pattern = r"\d{2,4}\\\d{2,5}"
    good_numbers = []
    for match in re.findall(pattern, string):
        first, second = match.split('\\')
        good_numbers.append(f"{first.zfill(4)}\\{second.zfill(5)}")
    return good_numbers


def get_result_task_1():
    print("введите число строк:")
    x = int(input())
    rows = []
    for row in range(x):
        rows.append(r'' + str(input()))
    # rows = [r"Адрес 5467\456. Номер", r"405\549", r"Тестовый текст 17\234 для поиска номеров 567\12345"]
    for row in rows:
        for num in find_good_numbers(row):
            print(num)


def add_atms(k, distances):
    for i in range(k):
        q = distances.index(max(distances))
        distances[q] = distances[q] // 2
        distances.insert(q + 1, distances[q])
    return distances


def get_result_task2():
    print('Введите сколько банкоматов уже есть (n):')
    n = int(input())
    print('Введите сколько банкоматов нужно поставить (k):')
    k = int(input())
    L = []
    for i in range(n):
        print(f' Расстояние от {i+1} до следующего банкомата (L):')
        L.append(int(input()))
    # k = 3
    # L = [100, 180, 50, 60, 150]
    result = add_atms(k, L)
    print(result)


def concatenate_numbers(str_list):
    sorted_list = sorted(str_list, reverse=True, key=lambda x: x + x[0])
    return ''.join(sorted_list)


def get_result_task3():
    print("Введите колличество чисел:")
    count = int(input())
    nums = []
    for i in range(count):
        nums.append(input())
    # nums = ['11', '234', '005', '89']
    print(concatenate_numbers(nums))


if __name__ == '__main__':
    print('Задача 1')
    get_result_task_1()
    print('Задача 2')
    get_result_task2()
    print('Задача 3')
    get_result_task3()
