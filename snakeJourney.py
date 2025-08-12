#snake game

import sys
import time
import random

def getCharacter():
    character_map = {
        "A": "Knight",
        "B": "Wizard",
        "C": "Archer",
        "D": "Diety"
    }
    characterPick = input("Please choose a character:\n\nA: Knight\nB: Wizard\nC: Archer\nD: Diety\n\n").upper()
    return character_map.get(characterPick, "Unknown")

def monsterCheck(monsterHP):
    if monsterHP <= 0:
        print("The monster is defeated! Congratulations!\n\n")
        return True
    return False

def option():
    choice = input("\nA: Fight\nB: Act\nC: Item\nD: Run\n\n")
    return choice

def knightFight(knightStamina):
    print("\nSelect your move")
    print(f"Stamina left: {knightStamina}")
    fight = input("A: Heavy Slash\nB: Quick Slash\n\n")

    if fight.upper() == "A" and knightStamina >= 10:
        knightStamina -= 10
        damage = 10
        print("You used heavy slash!")
    elif fight.upper() == "B" and knightStamina >= 5:
        knightStamina -= 5
        damage = 8
    else:
        print("Not enough stamina or invalid choice. You wasted your turn!")
        damage = 0
        
    return damage, knightStamina

def wizardFight(mana):
    print("\nSelect your spell:")
    print(f"Mana available: {mana}")
    spell = input("A: Fireball (10 Mana, 15 Damage)\nB: Ice Shard (5 Mana, 8 Damage)\nC: Lightning Bolt (15 Mana, 20 Damage)\n\n")
    
    #selection of spells
    if spell.upper() == "A" and mana >= 10: 
        mana -= 10
        damage = 15
        print("You cast Fireball!")
    elif spell.upper() == "B" and mana >= 5:
        mana -= 5
        damage = 8
        print("You cast Ice Shard!")
    elif spell.upper() == "C" and mana >= 15:
        mana -= 15
        damage = 20
        print("You cast Lightning Bolt!")
    else:
        print("Not enough mana or invalid choice. You wasted your turn!")
        damage = 0
    
    return damage, mana

def archerFight(arrows):
    print("Select your move:")
    print(f"Arrows left: {arrows}")
    fight = input("A: Single fire (1 arrow)\nB: Triple Fire(3 arrows)\n\n")
    if fight.upper() == "A" and arrows >= 1:
        arrows -= 1
        damage = 15
        print("You fired an arrow!")
    elif fight.upper() == "B" and arrows >= 3:
        arrows -= 3
        damage = 45
        print("You fired three arrows!")
    else:
        print("Not enough arrows or invalid choice. You wasted your turn!")
        damage = 0

    return damage, arrows

def monsterStats(hp, attack):
    return hp, attack

def attackSystem(character, playerHP, monsterHP, monsterAttack, monsterName):
    mana = 30  
    mana_potions = 2  # stats 
    health_potions = 2
    arrows = 7
    quiver = 15
    knightStamina = 15

    print(f"The battle begins! Your HP: {playerHP}, {monsterName} HP: {monsterHP}")

    while monsterHP > 0 and playerHP > 0:
        choice = option()
        
        if choice.upper() == "A":
            if character == "Knight":
                damage, knightStamina = knightFight(knightStamina)
                monsterHP -= damage
                print(f"{monsterName} HP: {monsterHP}")
            elif character == "Wizard":
                damage, mana = wizardFight(mana)
                monsterHP -= damage
                print(f"{monsterName} HP: {monsterHP}")
            elif character == "Archer":
                damage, arrows = archerFight(arrows)
                monsterHP -= damage
                print(f"{monsterName} HP: {monsterHP}")
                
        elif choice.upper() == "B":
            monsterCheck(monsterHP)
        
        elif choice.upper() == "C": 
            if character == "Wizard":
                itemChoose = input("Choose your item!\nA: Health Potion\nMana Potion")
                if itemChoose.upper == "A":
                    if health_potions > 0 and playerHP < 20:
                        health_potions -= 1
                        health_potions = health_potions
                        playerHP += 10
                    elif playerHP >= 20:
                        print("You have full HP!")
                    else:
                        print("You don't have any HP potions left!")
                elif itemChoose.upper == "B":
                    if mana_potions > 0:
                        mana_potions -= 1
                        mana_potions = mana_potions
                        mana += 20
                        print("You used a mana potion! Mana restored by 20.")
                    else:
                        print("You are out of mana potions!")
                else:
                    print("Items not available!")
               
            elif character == "Archer":
                itemChoose = input("Choose your item!\nA: Health Potion\nB: Refill arrows")
                if itemChoose.upper == "A":
                    if health_potions > 0 and playerHP < 20:
                        health_potions -= 1
                        health_potions = health_potions
                        playerHP += 10
                    elif playerHP >= 20:
                        print("You have full HP!")
                    else:
                        print("You don't have any HP potions left!")
                elif itemChoose.upper == "B":
                        arrowAmount = 7
                        quiver -= arrowAmount
                        arrows += arrowAmount
                        quiver = quiver
                        arrows = arrows
                        print(f"You retrived {arrowAmount} arrows! You now have {arrows} arrows!")
                else:
                    print("Items are not available!")
            elif character == "Knight":
                itemChoose = input("Choose your item!\nA: Health Potion\nB: Recharge Stamina\n")
                if itemChoose.upper == "A":
                    if health_potions > 0 and playerHP < 20:
                        health_potions -= 1
                        health_potions = health_potions
                        playerHP += 10
                    elif playerHP >= 20:
                        print("You have full HP!")
                    else:
                        print("You don't have any HP potions left!")
                elif itemChoose.upper == "B":
                    knightStamina += 5
                else:
                    print("Items not available!")


        elif choice.upper() == "D":
            print(f"You ran away from the {monsterName}!")
            break

        else:
            print("Invalid option, please choose correctly.")
        
        if monsterHP <= 0:
            print(f"{monsterName} is defeated! Congratulations!")
            break

        # monster attacks the player
        randomNumber = random.randint(1, 3)

        if randomNumber == 1:
            playerHP -= monsterAttack
            print(f"The {monsterName} attacks you for {monsterAttack} damage!")
            print(f"Your HP: {playerHP}, {monsterName} HP: {monsterHP}")
        elif randomNumber == 2:
            playerHP -= (monsterAttack + 5)
            print(f"The {monsterName} did a super attack for {monsterAttack + 5} damage!")
            print(f"Your HP: {playerHP}, {monsterName} HP: {monsterHP}")
        elif randomNumber == 3:
            playerHP -= (monsterAttack - 5)
            print(f"The {monsterName} did a pathetic attack for {monsterAttack - 5} damage!")
            print(f"Your HP: {playerHP}, {monsterName} HP: {monsterHP}")

        if playerHP <= 0:
            print(f"You have been defeated by the {monsterName}! Game over.")
            sys.exit()  #ends the program
        
def quest1(character):
    completed = False
    print("You look around and find a woman who appears stressed. Great! Time for business.\nYou ask her what's wrong.\n'A hideous monster stole my baby... could you please help me find it?'")
    op1A = input("A: Yes\nB: No\n")
        
    if op1A.lower() == "a":
        print("'Thank you!!'\nYou head off..\nAs you leave the village, you wander the forest and suddenly spot a giant monster!\n'Mmm... yummy baby'\nYou quickly start a fight!\n\n")
        time.sleep(1)
        trollHP, trollAttack = monsterStats(10, 5)
        attackSystem(character, 20, trollHP, trollAttack, "Troll")
        completed = True
        return completed
    else:
        return completed
    print("After the defeat of this troll, you retrieve the baby.")
            
def quest2(character):
    print("You ask the bartender for a drink.\n'Here ya go Sonny.. you know, there's been a problem.")
    print("We've been having some issues with someone peeking their nose where it don't belong. You might snuffing that guy out?")
    op1 = input("A: Yes\nB: No\n")

    if op1.lower() == "a":
        print("Alright, take the trail through the woodsy forest and you'll find his home. Kill him.")
        time.sleep(1)
        print("You walk through the forest and find a house. Will you break through?")
        houseBreak = input("A: Yes\nB: No\n")
        if houseBreak.lower() == "a":
            print("You decide to break in the house... you suddenly hear crying and then a man in the shadows")
            time.sleep(1)
            print("\nStrange man: WHO'S HERE?! SHOW YOURSELF NOW!")
            time.sleep(1)
            print("You realize who this is. Time to kill.")
            time.sleep(1)
            strangeManHP, strangeManattack = monsterStats(20, 10)
            attackSystem(character, 20, strangeManHP, strangeManattack, "Strange Man")
        else:
            print("You decide not to..")

def quest3(character):
    print("No quest yet")


    
def main():
    print("Welcome to Snake Journey!")
    character = getCharacter()
    if character == "Unknown":
        print("Invalid character selection! Please restart the game.")
        return
    print("You have chosen", character)
    print("You arrive at a bar. What do you do?")
    op1 = input("A: Look around for quest givers\nB: Get a drink\nC: Talk to the weird man in the corner\n\n")
    if op1.upper() == "A":
        quest1Completed = quest1(character)
        if quest1Completed:
            time.sleep(1)
            print("You continue on your journey..")
    elif op1.upper() == "B":
        quest2(character)
    elif op1.upper() == "C":
        quest3(character)
    else:
        print("Invalid choice")
    

main()
