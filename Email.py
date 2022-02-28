import os
import yagmail

from dotenv import load_dotenv

class EmailSender:
    def __init__(self):
        load_dotenv()

        self.__email_password = os.getenv('GMAIL_APP_PASSWORD')
        self.__email_from = os.getenv('EMAIL_FROM')
        self.__email_to = os.getenv('EMAIL_TO')

        self.__html_code_style = ' '.join([
            'font-family: Consolas,"courier new";',
            'background-color: #f1f1f1;',
            'padding: 2px;'
        ])

    def send_email(self, subject, content):
        with yagmail.SMTP(self.__email_from, self.__email_password) as mail:
            mail.send(self.__email_to, subject, content)

    def send_raid_failure_warning(self, raid_status, failed_drives):

        subject = 'URGENT - Raid Drive Failure'
        content = f'The following drive(s) have failed in your array: <strong>{",".join(failed_drives)}</strong>\n\n'
        content += f'<code style="{self.__html_code_style}">{raid_status}</code>'

        self.send_email(subject, content)