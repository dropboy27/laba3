

def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    while True:
        user_input = input()

        if not user_input:
            continue

        if user_input == "exit":
            print("Выход")
            break


if __name__ == "__main__":
    main()
