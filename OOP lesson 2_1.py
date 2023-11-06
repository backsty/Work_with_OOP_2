import os
from pprint import pprint

path = os.path.join(os.getcwd(), 'task.txt')
with open(path, 'r', encoding='utf-8-sig') as recipes:
    cook_book = {}
    for string in recipes:
        dish = string.strip()
        ingredients_kol = int(recipes.readline().strip())
        lst_book = []
        for item in range(ingredients_kol):
            ingredient_name, quantity, measure = recipes.readline().strip().split('|')
            lst_book.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[dish] = lst_book
        recipes.readline() # Прописываем для чтения пустой строки, иначе у нас итерация будет
        # останавливаться и не считывать все позиции
pprint(cook_book, sort_dicts=False, width=100)


"""Создаём функцию для получения информации о покупках исходя из заказов и кол-ва покупателей"""


def get_shop_list_by_dishes(dishes, number_of_buyers):
    shopping_dict = {}
    for dish_ in dishes:
        for ingredient in cook_book[dish_]:
            ingredient_list = dict([(ingredient['ingredient_name'],
                                 {'quantity': int(ingredient['quantity']) * number_of_buyers,
                                  'measure': ingredient['measure']})])
            # Производим проверку если блюдо заказано повторно, то увеличиваем список
            # Иначе если блюдо ещё не заказывали добавляем ингредиенты в список покупок
            if shopping_dict.get(ingredient['ingredient_name']):
                merger = (int(shopping_dict[ingredient['ingredient_name']]['quantity']) +
                          int(ingredient_list[ingredient['ingredient_name']]['quantity']))
                shopping_dict[ingredient['ingredient_name']]['quantity'] = merger
            else:
                shopping_dict.update(ingredient_list)
    return shopping_dict


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2), sort_dicts=False, width=100)






