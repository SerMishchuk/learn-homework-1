"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
def check_string (one_str, two_str):
    if type(one_str) is not str or type(two_str) is not str:
        return '0'
    elif one_str == two_str:
        return '1'
    elif len(one_str) >= len(two_str)and two_str != 'learn':
        return '2'
    elif one_str != two_str and two_str == 'learn':
        return '3'
   
one_str = 'test_test'
two_str = 'learn'
print(check_string(one_str, two_str))
    
    
if __name__ == "__main__":
    main()
