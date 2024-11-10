# TODO Найдите количество книг, которое можно разместить на дискете
one_symbol_weight = 4  # Объем, который занимает один символ (в байтах)
number_of_symbols_on_line = 25  # Количество символов в строке
number_of_lines_on_page = 50  # Число строк на странице
number_of_pages_in_book = 100  # Количество страниц в книге
disk_capacity = 1.44  # Информационный объем дискеты (в мегабайтах)

book_weight = one_symbol_weight * number_of_symbols_on_line * number_of_lines_on_page * number_of_pages_in_book   # Объем, который занимает одна книга (в байтах)

book_weight_in_mb = book_weight / (1024 * 1024)  # Объем, который занимает одна книга (в мегабайтах)
number_of_books = round(disk_capacity / book_weight_in_mb)  # Количество одинаковых книг, которые можно поместить на дискету
print("Количество книг, помещающихся на дискету:", number_of_books)
