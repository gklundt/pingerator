import logging
import datetime
import subprocess
import time


def wait(interval):
    time.sleep(interval)


if __name__ == '__main__':

    logging.basicConfig(filename='pingerator.log', level=logging.INFO)

    ping_process = subprocess.Popen(["ping", "-t", "-i", "100", "www.google.com"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:

        logging.info(datetime.datetime.now())
        line = ping_process.stdout.readline().decode()
        if not line:
            logging.info('No output')
            wait(5)
            continue
        x = line.strip()
        logging.info(x)
        print(x)
        wait(5)
