cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }

def get_shop_list_by_dishes(dishes, person_count):
  dict_shop = {}
  quantity_early = 0
  for dish in dishes:
    for ingridient in cook_book[dish]:
      if dict_shop.get(ingridient['ingredient_name']) != None:
        quantity_early = dict_shop[ingridient['ingredient_name']]['quantity']
      dict_shop[ingridient['ingredient_name']] = {'measure': ingridient['measure'], 'quantity': ingridient['quantity'] * person_count + quantity_early}
  return dict_shop

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

print(get_shop_list_by_dishes(dishes, person_count))