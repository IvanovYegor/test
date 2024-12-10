# TODO Напишите функцию для поиска индекса товара
def search_items(items_list, find_item):
    for index, item in enumerate(items_list):
        if item == find_item:
            return index
    return None
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
search_items_list = ['банан', 'груша', 'персик']
for item in search_items_list:
    index_item = search_items(items_list, item)
    if index_item is not None:
        print(f"Первое вхождение товара '{item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{item}' не найден в списке.")

