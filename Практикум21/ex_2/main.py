from solution import ShoppingBasket
from code_info import code_data


def menu() -> None:
    """
    Main interactive menu function for the shopping basket application.

    Provides a command-line interface for users to manage their shopping basket,
    including loading data, adding/removing products, viewing basket contents,
    and browsing available products.

    The menu displays the following options:
        1. Load products from file
        2. Add a product by barcode
        3. Delete a product by barcode
        4. Show current basket contents
        5. Show all available products with details
        0. Exit the application

    Returns:
        None
    """
    filename = input('Введите название файла: ')
    basket = ShoppingBasket(filename)
    basket.load()
    flag = True

    while flag:
        print('\n1. Загрузить товары')
        print('2. Добавить товар')
        print('3. Удалить товар')
        print('4. Показать корзину')
        print('5. Показать доступные товары')
        print('0. Выход')

        choice = input('Выбор: ')

        match choice:
            case '1':
                basket.load()
                print('Данные загружены')

            case '2':
                code = input("Штрих-код: ")
                try:
                    basket.add_product(code)
                except ValueError as e:
                    print(e)

            case '3':
                code = int(input("Штрих-код для удаления: "))
                basket.delete_product(code)

            case '4':
                basket.show()

            case '5':
                print("\nДоступные товары:\n")

                for code, data in code_data.items():
                    print(f"Штрих-код: {code}")
                    print(f"Название: {data['name']}")
                    print(f"Цена: {data['price']}")
                    print(f"Страна: {data['country']}")
                    print("-" * 30)

            case '0':
                flag = False


if __name__ == "__main__":
    menu()
