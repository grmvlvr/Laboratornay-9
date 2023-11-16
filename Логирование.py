#подключаем модули, random - генерирует случайные числа, logging - 
import random
import logging

#Создаем лог при помощи функции basicConfig и передаем функции название файла и уровень логирования
logging.basicConfig(filename='bochki.log', level=logging.INFO)

def main():
    while True:
        try:
            n = int(input("Введите количество бочонков: ")) #Запрашиваем количество бочонков
            if n <= 0:
                raise ValueError # Вызываем обработку исключений
            break
        #Описываем обработку исключений
        except ValueError:
            print("Пожалуйста, введите число больше 0.")
            logging.error("Ошибка: введено число меньше нуля")
    #Создание последовательности бочонков
    bochki = list(range(1, n + 1))
    #Перемешивание значений
    random.shuffle(bochki)

    
    for bochkis in bochki:
        #Запрашиваем у пользователя вытянуть бочонок 
        input("Нажмите Enter, чтобы вытянуть следующий бочонок: {}".format(bochkis))
        #Логируем номер вытянутого бочонка
        logging.info("Вытянут бочонок: {}".format(bochkis))

    #Вывод
    print("Бочонки закончились!!!")

if __name__ == "__main__":
    main()
