from datetime import datetime,timedelta

def get_birthdays_per_week(users):
    now = datetime.now().date()
    delta_next_week = 7 -  now.weekday()
    next_week_start = now + timedelta(days=delta_next_week) 
    next_week_end = next_week_start + timedelta(days=6)

    birthdays = {}

    current_date = next_week_start

    while (current_date <=next_week_end):
        birthdays[current_date.strftime('%A')]=[]
        current_date+=timedelta(days=1)

    for user in users:
        birthday = datetime(now.year,user['birthday'].month,user['birthday'].day).date()
        if next_week_start <=birthday <=next_week_end:
            birthdays[birthday.strftime('%A')].append(user['name']) 
            
    
    result = ''

    for k,v in birthdays.items():
        if len(v) > 0:
            names = ', '.join(v)
            result+=f'{k}: {names}\n'

    return result





def add_contact(args,contacts):
    if len(args)==2:
        contacts[args[0]]=args[1]
        return 'Contact added.'
    else:
        return 'Invalid command!'
  
def change_contact(args,contacts):
    if len(args)==2:
            if args[0] in contacts:
                contacts[args[0]]=args[1]
                return 'Contact updated.'
            else:
                return 'Contact not found!'
    else:
        return 'Invalid command!'
              
def show_phone(args,contacts):
    if len(args)==1:
        if args[0] in contacts:
            return contacts[args[0]]
        else:
            return 'Contact not found!'

def show_all(contacts):
    return '\n'.join([f'{k}: {v}' for k,v in contacts.items()])

def parseCommands(input):
    if input=='':
        return '',[]
    
    cmd,*args = input.strip().lower().split()
    return cmd,args

def main():
    print('Welcome to the Contact Assistant!')
    contacts = {}
    while(True):
        cmd,args = parseCommands(input('>'))
        #print(f'cmd : {cmd} | commands : {args}')
        if cmd == 'hello':
            print('How can I help you?')
        elif (cmd =='close' or cmd =='exit'):
            print('Good bye!')
            break
        elif cmd =='phone':
            print(show_phone(args,contacts))
        elif cmd =='add':
            print(add_contact(args,contacts))
        elif cmd =='change':
            print(change_contact(args,contacts))
        elif cmd =='all':
            print(show_all(contacts))
        else:
            print('Invalid command.')

if __name__ == '__main__':
    main()
