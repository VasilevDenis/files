import os
from pprint import pprint


def txt_to_dict(file):
    cook_book = {}
    full_path = os.path.join(os.getcwd(), file)
    with open(full_path) as f:
        text = f.read()
        blocks = text.split('\n\n')
        for block in blocks:
            dish = block.split('\n')
            cook_book[dish[0]] = []
            for elem in dish[2:]:
                ingredient_name, quantity, measure = elem.split(' | ')
                ingredient = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
                cook_book[dish[0]].append(ingredient)
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = txt_to_dict('files/recepies.txt')
    all_ingredients = {}
    for dish in dishes:
        ingredients_param = cook_book[dish]
        for elem in ingredients_param:
            ingredient_name = elem['ingredient_name']
            if ingredient_name not in all_ingredients.keys():
                all_ingredients[ingredient_name] = {'quantity': int(elem['quantity']) * person_count,
                                                    'measure': elem['measure']}
            else:
                all_ingredients[ingredient_name]['quantity'] += int(elem['quantity']) * person_count
    return all_ingredients


def file_union(files):
    files_dict = {}
    for file in files:
        full_path = os.path.join(os.getcwd(), file)
        with open(full_path) as f:
            lines = f.readlines()
            files_dict[len(lines)] = (lines, os.path.basename(file))
    with open('files/swap_file.txt', 'w') as write_file:
        all_lines = ''
        for key in sorted(files_dict.keys()):
            all_lines += files_dict[key][1] + '\n'
            all_lines += str(key) + '\n'
            all_lines += f'{"".join(files_dict[key][0])}\n'
        write_file.write(all_lines)


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
file_union(['files/file_1.txt', 'files/file_2.txt', 'files/file_3.txt'])
