"""Class 'Character' that is basically the stats of the character
Saves everything"""
#Made by @unearthlydeath on Github

import json

class Character:
    """Prints and updates stats of character"""

    def __init__(self, name, level, health, strength, mana, agility, dexterity, exp, exp_next_level):
        """Initialize attributes"""

        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
        self.mana = mana
        self.agility = agility
        self.dexterity = dexterity
        self.exp = exp
        self.exp_next_level = exp_next_level


        


    def update_exp(self, amount):
        """Updates the amount of exp"""

        print(f"{self.name} just gained {amount} experience points")
        self.exp += amount
        self.check_level_up()


    def check_level_up(self):
        """Check if exp grants a level up
        Increases the exp needed for a level up"""

        while(self.exp >= self.exp_next_level):
            self.exp -= self.exp_next_level
            self.level += 1
            self.exp_next_level *= 2 #multiplies the amount of exp needed tp go next level. 0/100 and so on
            self.level_up()

    
    def level_up(self):
        """Announces a level up
        Increases stats upon level up"""

        print(f"{self.name} has leveled up! {self.name.title()} is now level {self.level}")
        self.health += 5
        self.mana += 2


    def update_health(self, amount):
        """Updates health manually"""

        self.health += amount

    
    def update_strength(self, amount):
        """Updates strength manually"""

        self.strength += amount


    
    def update_mana(self, amount):
        """Updates mana manually"""
     
        self.mana += amount


    def update_agility(self, amount):
        """Updates agility manually"""

        self.agility += amount

    
    def update_dexterity(self, amount):
        """Updates dexterity manually"""

        self.dexterity += amount

    
    def get_status(self):
        """Returns character's status as a dictionary"""
        return {
            'Name': self.name,
            'Level': self.level,
            'Exp': f'{self.exp} / {self.exp_next_level}',
            'Health': self.health,  
            'Mana': self.mana,  
            'Strength': self.strength,
            'Agility': self.agility,
            'Dexterity': self.dexterity
        }
    

    def save_to_file(self, filename):
        """Saves the current stats to a file"""
        data = self.get_status()
        data['Exp to Next Level'] = self.exp_next_level

        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
                print(f"Data saved to {filename}")
        except OSError as e:
            print(f"Error saving to file: {e}")

           
    @classmethod
    def load_from_file(cls, filename):
        """Loads character stats from file"""
        with open(filename, 'r') as file:
            data = json.load(file)
            character = cls(
                name = data['Name'],
                level = data['Level'],
                health = data['Health'],
                mana = data['Mana'],
                strength = data['Strength'],
                agility = data['Agility'],
                dexterity = data['Dexterity'],
                exp = int(float(data['Exp'].split(' / ')[0])),  # Extract the exp value from the string
                exp_next_level = data['Exp to Next Level']
            )
            return character
