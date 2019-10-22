#this code is free and can be used by anyone

from random import randint

import random

import time







def battle():


    health = 100

    ehealth = 100

    count = 0

    exp = 0

    heal = 5

    print ("If you heal, you'll get 10 hp back! But you can only use it 5 times!")

    attack = False
    while attack == False:
        print ("")
        print ("")
        time.sleep(0.2)
        choice = input ("What do you wish to do. FLEE OR ATTACK OR HEAL?\n      ;").lower()


        if choice == ("attack"):
            ehit=random.randint(0,35)
            ehealth = ehealth - ehit
            time.sleep(0.7)
            print ("")
            print ("You have hit",ehit)
            print ("")
            time.sleep(0.7)
            print ("The enemys health is",ehealth)
            hit=random.randint(0,35)
            health = health - hit
            print ("")
            time.sleep(0.7)
            print ("The enemy has hit you",hit)
            print ("")
            time.sleep(0.7)
            print ("Your health is now",health)
            time.sleep(3.5)
            count = count + 1
            if count == 1:
                attack = True
        attack = False





        if choice == ("heal"):
            if heal > 0:
                health = health + 10
                time.sleep(0.7)
                print ("")
                print ("Your health is now",health)
                heal = heal - 1
                print ("")
                print ("You have",heal,"health potions left!")
        if choice == ("heal"):
            if heal < 1:
                print ("")
                print ("You don't have any more potions!")
                health = health + 0


        if choice == ("flee"):
            print("\nYou have left the battle!")
            break

        if health < 1:
            health = min
            print ("")
            time.sleep(0.8)
            print ("You have lost!!")
            break

        if ehealth < 1:
            health = min
            exp = random.randint (0,15)
            print ("")
            time.sleep(0.3)
            exp = exp + exp
            print ("")
            print ("")
            print ("You have won! You recieved",exp,"experience!")
            break


battle()
