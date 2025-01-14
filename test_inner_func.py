def test_function():
    def inner_function():
        print('я в области видимости функции', test_function.__name__)

    inner_function()


#inner_function()  #// здесь ошибка тк эта функция (локальная) не определена
test_function()
