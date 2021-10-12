


class CellPhone:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.model = "iPhone"
        self.contacts = {
            "Sarah" : 540-497-3223,
            "Dan" : 540-497-5432,
            "Bryce" : 540-497-8956
        }
        self.message_from = []
        self.messages = []
        self.vibrate = False
    
    def recieve_text(self, name, message):
        print(f'{name} sent you a Message. It reads {message} ')
        self.messages.append(message)
        self.message_from.append(name)

    def vibrate_toggle(self):
        if self.vibrate == False:
            self.vibrate = True
            print('Your phone is now on Vibrate')
        elif self.vibrate == True:
            self.vibrate = False
            print('Your phone is off vibrate now!')
    
    def send_text(self, contact_name, message):
        print(f'Sending your message to {contact_name}. \nMessage reading; {message}; was sent.')


    
