import logging
import os.path
import time

logging.basicConfig(level=logging.INFO, format='[%(asctime)s][%(name)s][%(levelname)s] %(message)s')
logger = logging.getLogger("GeneratorCore")
log_path = os.path.join("..", 'log')
log_file = os.path.join(log_path, 'laste.log')
if not os.path.isdir(log_path):
    os.mkdir(log_path)
handler = logging.FileHandler(log_file)
formatter = logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.addHandler(handler)


def close():
    handler.close()
    nowTime = time.strftime('%Y%m%d-%H%M%S')
    if os.path.isfile(log_file):
        os.rename(log_file, os.path.join(log_path, f"{nowTime}.log"))
