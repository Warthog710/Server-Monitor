import schedule

from time import sleep, time_ns

# Custom classes
from Raid import MonitorRaid
from MyLogger import Logger

MONITOR_RAID = True

def monitor():
    logger = Logger()

    if MONITOR_RAID:
        schedule.every().hour.at(':30').do(MonitorRaid().monitor)

    while True:
        logger.info('Running scheduled tasks...')
        start = time_ns()
        schedule.run_pending()
        end = time_ns()
        logger.info(f'Finished scheduled tasks. Time Elapsed={(end - start) / 1e6}ms')

        # Sleep until the next task
        sleep_time = schedule.idle_seconds()
        logger.info(f'Sleeping until the next scheduled task(s) in {sleep_time} seconds...')
        sleep(sleep_time)

if __name__ == '__main__':
    monitor()