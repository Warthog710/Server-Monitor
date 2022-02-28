import enum

from Email import EmailSender
from MyLogger import Logger

class RaidStates(enum.Enum):
    drive_failure = 0
    raid_safe = 1

class MonitorRaid:
    def __init__(self):
        self.__email = EmailSender()
        self.__logger = Logger()

    #? Monitors a mdadm raid by reading /proc/mdstat
    def monitor(self):
        self.__logger.info('Checking raid status...')

        with open('/proc/mdstat', 'r') as status:
            status_text = status.read()

        raid_status = self.get_raid_status(status_text)

        # If a drive has failed send a warning
        if raid_status == RaidStates.drive_failure:
            failed_drives = self.get_failed_drives(status_text)
            self.__logger.warning(f'Detected failed drives! {failed_drives}')
            self.__email.send_raid_failure_warning(status_text, failed_drives)
        else:
            self.__logger.info('Detected no issues.')
    
    def get_raid_status(self, status):
        raid_status = RaidStates.raid_safe

        if '(F)' in status:
            raid_status = RaidStates.drive_failure

        return raid_status

    def get_failed_drives(self, status):
        failed_drives = []

        # Iterate over the status to find all failed drives
        for string in status.split():
            if '(F)' in string:
                failed_drives.append(string[:3])

        return failed_drives
           