from .world import World
import time
from .kbhit import KBHit


def main():
    filename=input("**** Welcome to the Game of Life! **** \n type in file name for grid configuration or hit enter for random. \n ")
    if filename == '':
        size=input('Enter desired board size: \n')
    else: 
        filename='projects/gameoflife/'+filename+'.txt'
        with open(filename,'r') as fh:
            size=len(fh.readline().partition(','))
    if size == '': size=10
    world=World(int(size),filename)

    speed_input=input('Enter Desired Simulation Speed From 1-10, \n type man for frame by frame: ')
    loop=True
    k=KBHit()
    if speed_input == '':
        speed_input=20
        print('You found a cheat code!')
        time.sleep(.5)
    if speed_input != 'man':
        time_step=float(speed_input)**-1
        while loop:
            loop=world.progress()
            time.sleep(time_step)
            if k.kbhit(): break
    else:
        while loop:
            if k.getch() == '\n':
                loop=world.progress()
                print('Hit enter to continue, or Q to quit')
            elif k.getch() == 'q':
                loop=False
    print('Hit enter to play again or anything else to quit \n')
    if k.getch() == '\n':
        main()
            
            




if __name__ == '__main__':
    main()
    


    
