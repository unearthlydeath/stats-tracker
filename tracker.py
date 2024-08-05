"""Gets information about monsters killed
Returns and loads updated/saved stats
Made by @unearthlydeath on Github"""

from stats import Character
import os


def exp_calc():
    """"Calculates the amount of exp gained"""
    total_exp = 0
    while True:

        monster_type = input("\nMonster type. Enter q to exit: ")

        if(monster_type == 'q'):
            break

        monst_level = int(input("What level: "))
        amt_killed = int(input("Amount killed: "))

        if monster_type == 'goblin':
            if (monst_level == 1):
                exp = amt_killed * 10
            elif monst_level == 2:
                exp = amt_killed * 20
            elif monst_level == 3:
                exp = amt_killed * 30
        elif (monster_type == 'elite goblin'):
            if (monst_level == 1):
                exp = amt_killed * 15
            elif monst_level == 2:
                exp = amt_killed * 25
            elif monst_level == 3:
                exp = amt_killed * 35
        elif (monster_type == 'hobgoblin'):
            if (monst_level == 1):
                exp = amt_killed * 35
            elif monst_level == 2:
                exp = amt_killed * 45
            elif monst_level == 3:
                exp = amt_killed * 60
      
        total_exp += exp
    

    return total_exp


def update_stats(Character):
    """Updates stats based on user input"""

    while True:
        stat_to_update = input("\nWhich stat would you like to update? (health, mana, strength, agility, dexterity, done): ").lower()
        if(stat_to_update == 'done'):
            break
        amount = int(input(f"Enter the amount to update {stat_to_update} by: "))

        if(stat_to_update == 'health'):
            Character.update_health(amount)

        elif(stat_to_update == 'mana'):
            Character.update_mana(amount)

        elif(stat_to_update == 'strength'):
            Character.update_strength(amount)

        elif(stat_to_update == 'agility'):
            Character.update_agility(amount)

        elif(stat_to_update == 'dexterity'):
            Character.update_dexterity(amount)
        
        else:
            print("Invalid stat. Please try again.")
        
        print(f"Updated {stat_to_update} by {amount} points.")



#Define file name for saving/loading stats
filename = 'Character_Stats.json'


#load the file if it exists otherwise creates a new file with initial stats
if(os.path.exists(filename)):
    MC = Character.load_from_file(filename)
    print(MC.get_status())
else:
    MC = Character(
        name = 'character_name', #change to your character's name
        level = 1,
        health = 10,
        strength = 3,
        mana = 3,
        agility = 5,
        dexterity = 5,
        exp = 0,
        exp_next_level = 100)


#starts the program
enter = input("\nStart program (y/n)?: ")
if (enter == 'n'):
    print("Goodbye")
else:
    #updates the exp
    earned_exp = exp_calc()
    MC.update_exp(earned_exp)

    #updates the attributes
    update_stats(MC)

    #print current stats
    status = MC.get_status()
    print("\n",status)

    #save the stats
    MC.save_to_file(filename)
