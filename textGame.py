#allows me to use sleep so stuff is delayed like those old games
import time
import storyBranch1 as br1
import storyBranch2 as br2





def main():
    
    #this works fine as well
    #the functions just return strings lol
    decision1 = intro()
    decision2 = 0

    if decision1 == '1':
        print("")
        time.sleep(1.5)
        decision2 = br1.room()
        
    elif decision1 == '2':
        print('')
        time.sleep(1.5)
        decision2 = br2.scream()
        time.sleep(1.5)
        print('')
        br2.ball()
    

#works fine
def intro():
    print('Last night you went to bed in your house.')
    print('You now find yourself awake in a strange environment.', 'What do you do?', sep='\n')

    #options
    print('1 - blink your eyes')
    print('2 - scream for help')

    #option logic
    #guess im just doing it in this function
    #apparently using try and except cancles the while looping forever

    while True:

        choice = input('>>')
        #i might have to make choice a global variable so that i can determine which function i need to call next

        #using try and exceptions stops the program from crashing if someone enters a non number
        try:
            if int(choice) == 1:
                print('You blink your eyes, only to have your pitch black environment replaced with a bright white one.')
                #looper = False
                break
            elif int(choice) == 2:
                print('You scream at the top of your lungs.')
                time.sleep(1.5)
                print('No one seems to hear you though.')
                #for main logic
                #looper = False
                break
            else:
                print('enter either 1 or 2:')
        except:
            print('You must either a whole number 1 or 2:')
    
    #allows for me to do logic in main
    #i hope
    return choice

#making story branches in other files i guess

#dunders
if __name__ == '__main__':
    main()