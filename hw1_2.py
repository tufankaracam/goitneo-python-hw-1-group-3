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
