"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def phone_sold(stock):
    sum_of_all_sold = 0
    number_of_all_sold = 0
    for all_sold_of_one_phone in stock:
        sum_of_sold_one_phone = 0
        number_of_sold_one_phone = 0
        for sold in all_sold_of_one_phone['items_sold']:
            sum_of_sold_one_phone += sold
            number_of_sold_one_phone += 1
        number_of_all_sold += number_of_sold_one_phone    
        sum_of_all_sold += sum_of_sold_one_phone
        average_sold_one_phone = round(sum_of_sold_one_phone / number_of_sold_one_phone, 1)
        print(f'Среднее количество продаж по {all_sold_of_one_phone["product"]}: {average_sold_one_phone}')
        print(f'Суммарное количество продаж по {all_sold_of_one_phone["product"]}: {number_of_sold_one_phone}')

    print(f'Количество всех продаж: {number_of_all_sold}')
    average_sold = round(sum_of_all_sold / number_of_all_sold, 2)
    print(f'Среднее количество всех продаж: {average_sold}')
    

def main():
    stock = [
             {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
             {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
             {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
    phone_sold(stock)
   


if __name__ == '__main__':
    main()