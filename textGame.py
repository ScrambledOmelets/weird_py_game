def main():
    intro()

def intro():
    print('Last night you went to bed in your house.')
    print('You now find yourself awake in a strange environment.', 'What do you do?', sep='\n')

    #options
    print('1 - blink your eyes')
    print('2 - scream for help')

    #option logic
    #guess im just doing it in this function
    while True:

        choice = input()
        #using try and exceptions stops the program from crashing if someone enters a non number
        try:
            if int(choice) == 1:
                print('insert what the person does')
            elif int(choice) == 2:
                print('insert what person does again')
                break
            else:
                print('enter either 1 or 2:')
        except:
            print('You must either a whole number 1 or 2:')

#dunders
if __name__ == '__main__':
    main()