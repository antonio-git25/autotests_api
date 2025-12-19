import logging
from datetime import date
import time


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    file_name = f"inner_logs/myapp_{date.today()}_{time.strftime('%H%M%S')}.log"
    logging.basicConfig(filename=file_name, level=logging.INFO)

    # Создаем обработчик, который будет выводить логи в консоль
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    # Задаем форматирование лог-сообщений: включаем время, имя логгера, уровень и сообщение
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)  # Применяем форматтер к обработчику

    # Добавляем обработчик к логгеру
    logger.addHandler(handler)

    return logger