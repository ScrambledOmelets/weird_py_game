import time

def room():
    print('you\'re in the strange white room')
    print('what do you do?')
    print('1 - look around', '2 - cry', '3 - do nothing', sep='\n')

    #logic
  

    while True:

        choice = input('>>')
        #i might have to make choice a global variable so that i can determine which function i need to call next

        #using try and exceptions stops the program from crashing if someone enters a non number
        try:
            if int(choice) == 1:
                print('room looks weird. its white and stuff')
                looper = False
            elif int(choice) == 2:
                print('You cry like a baby...')
                time.sleep(1.5)
                print('Achieving nothing')
                #for main logic
              
            elif int(choice) == 3:
                print('You sit there doing nothing like an idiot...')
                time.sleep(1.5)
                print('What is wrong with you?')
                #for main logic
                break
            else:
                print('enter either 1, 2, or 3:')
        except:
            print('You must either a whole number 1, 2, or 3:')

    return choice

#idk i guess i would have any extra modules here for this story branch
#assuming that all 3 choices have the same outcome