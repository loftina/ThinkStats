from __future__ import division
import random


def get_random(range):
    return int(random.random() * range)


def Monty_Hall(door_guess, switch=False):
    """"
    Takes a guess and whether the contestant wants to switch after
    the reveal or not. Returns True if the contestant won and False
    if they lost.
    """
    # the door where the prize is: doors 0 1 2
    correct_door = get_random(3)

    if correct_door == door_guess:
        if switch == False:
            return True
        else:
            return False
    elif switch == True:
        return True
    else:
        return False


def main():
    # Exercise 5.4
    do_not_switch = [Monty_Hall(get_random(3), switch=False) for _ in range(1000)]
    switch = [Monty_Hall(get_random(3), switch=True) for _ in range(1000)]
    print("Don't switch win percentage: {}% (1/3 in theory)".format(sum(do_not_switch)/len(do_not_switch)*100))
    print("Switch win percentage: {}% (2/3 in theory)".format(sum(switch)/len(switch)*100))

if __name__ == '__main__':
    main()
