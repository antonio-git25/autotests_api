import logging
import platform
import sys


print(f'{platform.system()}, {platform.release()}')
print(sys.version)

logger = logging.getLogger("AUTOTEST")
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='myapp.log', level=logging.INFO)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger.addHandler(handler)

logger.debug("Это сообщение уровня DEBUG.")
logger.info("Это сообщение уровня INFO.")
logger.warning("Это сообщение уровня WARNING.")
logger.error("Это сообщение уровня ERROR.")
logger.critical("Это сообщение уровня CRITICAL.")