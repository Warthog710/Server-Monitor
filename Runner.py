import schedule

from time import sleep

# Custom classes
from Raid import MonitorRaid

MONITOR_RAID = True

def monitor():
    if MONITOR_RAID:
        schedule.every().hour.at(':30').do(MonitorRaid().monitor)

    while True:
        schedule.run_pending()

        # Sleep until the next task
        sleep_time = schedule.idle_seconds()
        sleep(sleep_time)

if __name__ == '__main__':
    monitor()