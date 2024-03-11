with open('recepies.txt', 'r', encoding='utf-8') as f:
    ingr_file = f.read()

def make_cook_book(file):
    list_ingr = file.split('\n')
    list_ingr.append('')
    def formating(splitted_list):
        format_ingr = []
        iter_list = []
        for ind, line in enumerate(splitted_list):
            if line != '':
                iter_list += [line]
            else:
                format_ingr.append(iter_list)
                iter_list = []
        return format_ingr

    def add_dish(format_list):
        cook_book = {}
        for i in format_list:
            cook_book[i[0]] = []
            comfr = cook_book[i[0]]
            for ingr in i[2:]:
                dict_ingr = {}
                list_ingr = ingr.split(' | ')
                dict_ingr['ingridient'] = list_ingr[0]
                dict_ingr['quantity'] = list_ingr[1]
                dict_ingr['measure'] = list_ingr[2]
                comfr.append(dict_ingr)
        return cook_book
    
    format_ingr = formating(list_ingr)
    cook_book_in_func = add_dish(format_ingr)
    return cook_book_in_func

cook_book = make_cook_book(ingr_file)

def get_shop_list_by_dishes(list_dishes, quantity_people=1):
    shop_dict = {}
    for dish in list_dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                x = int(ingr['quantity']) * quantity_people
                name_ingr = ingr['ingridient']
                if name_ingr not in shop_dict:
                    shop_dict[name_ingr] = {'quantity': x, 'measure': ingr['measure']}
                else:
                    shop_dict[name_ingr]['quantity'] += x
    return shop_dict
