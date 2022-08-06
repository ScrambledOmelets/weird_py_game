import time

def scream():
    print('you\'re still in the dark')
    print('what do you do?')
    print('1 - look for a light')


    while True:

        choice = input('>>')
        #i might have to make choice a global variable so that i can determine which function i need to call next

        #using try and exceptions stops the program from crashing if someone enters a non number
        try:
            if int(choice) == 1:
                print('you feel around, your hand brushing against something weird.')
                time.sleep(0.5)
                print('you feel around the object further')
                time.sleep(1.5)
                print('it\'s a small furry ball you feel')
                break
            else:
                print('enter either 1, 2, or 3:')
        except:
            print('You must either a whole number 1, 2, or 3:')

    #gonna treat this one different since it only has one option?
    #return choice

def ball():
    print('the ball is furry and weird')
    print('you roll it in between your fingers, and some hairs rub off')
    time.sleep(1.5)
    print('it\'s kind of grossing you out...')