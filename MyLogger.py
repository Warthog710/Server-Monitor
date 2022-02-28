from pathlib import Path
from datetime import datetime

class Logger:
    def __write(self, level, message):
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day

        # Make sure the correct path exists
        Path(f'Logs/{year}/{month}').mkdir(parents=True, exist_ok=True)
        file_path = f'Logs/{year}/{month}/log_{day}.log'
        Path(file_path).touch(exist_ok=True)

        time = datetime.now().strftime('%H:%M:%S')

        with open(file_path, 'a') as log:
            log.write(f'{year}/{month}/{day} @{time} - {level} | {message}\n')

    def info(self, message):
        self.__write('INFO', message)

    def debug(self, message):
        self.__write('DEBUG', message)

    def warning(self, message):
        self.__write('WARNING', message)

    def error(self, message):
        self.__write('ERROR', message)
        