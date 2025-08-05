

import random
alarm = 0

guard_dialogue_unassuming = [
    "Guard: So bored tonight...\n",
    "Guard: I can't wait to go home.\n",
    "Guard: Man, I'm really hungry right now. How long until my break?\n"
]

guard_dialogue_sus = [
    "Guard: Huh? Did I hear something?\n",
    "Guard: Did that shadow just move?\n",
    "Guard: Alright, what was that?\n"
]
guard_dialogue_relieved = [
    "Guard: All clear.\n",
    "Guard: Guess it was nothing.\n",
    "Guard: I must be losing my mind.\n"
]

guard_dialogue_sudden = [
    "Guard: What the?\n",
    "Guard: Hey! Stop\n",
    "Guard: Consequences will never be the same!\n"
]

guard_dialogue_alert = [
    "Guard: Enemy spotted!\n",
    "Guard: Intruder!\n",
    "Guard: I need back up!\n"
]



def stealth_mission():
    print("You sneak through the hallway into darkness, you turn the corner, and ahead of you, you see a lone security guard. His back is turned to you, \n he is just standing there guarding the entrance to the other hallway. \n \n")
    print(random.choice(guard_dialogue_unassuming))

    print("How do you proceed?\n \n")
    print("1. Sneak up to his back and knock him out\n")
    print("2. Whistle and cause a distraction to lure him away from his position \n \n")

    action = input("Choose 1 or 2 \n")
    roll = random.randint(1,12)

    if action == "1":
        if roll > 2:
            print("You have successfully knocked out the guard")
        else:
            print("You hurt the guard, but he notices and fights back. \n")
            print(random.choice(guard_dialogue_sudden))
            
            while True:
                print("1. Attempt to knock the guard out again \n")
                print("2. Pull out your Five SeveN and shoot the guard \n")
                print("3. Run away to hide in the shadows \n \n")
                
                sub_action = input("Choose 1, 2, or 3 \n")
                roll = random.randint(1,5)
                
                if sub_action == "1":
                    if roll > 2:
                        print("You succeed in knocking the guard out.")
                    else:
                        print("The guard pushes you away and kills you.")
                    return
                
                elif sub_action == "2":
                    if roll > 2: 
                        print("You have successfully shot the guard and killed him")
                    else:
                        print("The guard shot and killed you as you were drawing your weapon")
                    return

                elif sub_action == "3":
                    if roll > 2:
                        print("You have successfully lost the guard, but he has reported an intruder.\n")
                        print(random.choice(guard_dialogue_alert))
                        print(f"Alarm level: {alarm + 1}")
                    else:
                        print("The guard shot you as you ran away, and you have been killed")
                    return
            
    elif action == "2":
        if roll > 2:
            print("The guard hears you, and proceeds into the shadowy hallway with you\n")
            print(random.choice(guard_dialogue_sus))

            print("1. Sneak around the guard into the entrance")
            print("2. Grab the guard and knock him out")

            sub_action1 = input("Choose 1 or 2")
            roll = random.randint(1,10)

            if sub_action1 == "1":
                if roll > 2:
                    print("You have successfully snuck around the guard and made it into the entrance unseen. \n")
            else:
                print("The guard has shot and killed you.")
        else:
            print("The guard didn't hear you. Try again or try to knock him out?")
        
                
            print("1. Try another whistle")
            print("2. Proceed down the hall to knock him out")
                
            sub_action = input("Choose 1 or 2")
            roll = random.randint(1,10)

            if sub_action == "1":
                if roll > 2:
                    print("You capture the guards attention, leading him down the hall \n \n")
                    print("1. Sneak around the guard into the entrance")
                    print("2. Grab the guard and knock him out")

                    sub_action2 = input("Choose 1 or 2")
                    roll = random.randint(1,8)

                    if sub_action2 == "1":
                        if roll > 2:
                            print("You have successfully made it past the guard and have entered through the entrance.")
                        else:
                            print("The guard turned around and caught you, alerted security and makes an attempt to apprehend you.\n")
                            print(f"Alarm level: (alarm + 1)\n\n")
                            print("1. You attempt to flee the scene and hide from the guard")
                            print("2. Attempt to take the guard out before causing anymore commotion")
                    

                            sub_action3 = input("Choose 1 or 2")
                            roll = random.randint(1,6)

                            if sub_action3 == "1":
                                if roll > 2:
                                    print("You successfully get away from the guard. However, guards are at high alert. Alarm level two.")
                                else:
                                    print("The guard has caught you and successfully apprehended you. Mission aborted")
                                    exit()

                            elif sub_action3 == "2":
                                if roll > 2:
                                    print("You have taken the guard out. However, the building is at high alert.")
                                    print(f"Alarm level: {alarm + 1}")
                                else:
                                    print("The guard shoots you as you make an attempt to take him down.")
                                    exit()
                    if sub_action2 == "2":
                        if roll > 2:
                            print("You end up knocking out the guard and you can proceed")
                        else:
                            print("The guard notices and calls for help and reports an intruder")


                else:
                    print("1. Sneak up to his back and knock him out\n")
                    print("2. Whistle and cause a distraction to lure him away from his position \n \n")
                        
                    action = input("Choose 1 or 2 \n")

    else:
        print("Invalid input. Try again.")

    # game loop

while True:
    stealth_mission()
    play_again = input("\nDo you want to play again? Yes/No \n")
    if play_again != "yes":
        print("Thanks for playing. \n")
        break






