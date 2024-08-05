"""Class 'Character' that is basically the stats of the character
Saves everything"""

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

        self.exp += amount
        print(f"{self.name} just gained {self.exp} experience points")
        self.check_level_up()


    def check_level_up(self):
        """Check if exp grants a level up
        Increases the exp needed for a level up"""

        while(self.exp >= self.exp_next_level):
            self.exp -= self.exp_next_level
            self.level += 1
            self.exp_next_level *= 2.5 #multiplies the amount of exp needed tp go next level. 0/100 and so on
            self.level_up()

    
    def level_up(self):
        """Announces a level up
        Increases stats upon level up"""

        print(f"{self.name} has leveled up! {self.name.title()} is now {self.level}")
        
        self.health += 5
        self.mana += 5

    
    def update_strength(self, amount):
        """Updates strength manually
        Ensures health doesn't go below 0"""

        self.strength += amount
        self.health = max(0, self.health)

    
    def update_mana(self, amount):
        """Updates mana manually
        Ensures mana doesn't go below 0"""

        self.mana += amount
        self.mana = max(0, self.mana)


    def update_agility(self, amount):
        """Updates agility manually"""

        self.agility += amount

    
    def update_dexterity(self, amount):
        """Updates dexterity manually"""

        self.dexterity += amount

    
    def get_status(self):
        """Prints the characters status by printing a dictionary 
        of the attributes"""

        return {
            'Name' : self.name,
            'Level': self.level,
            'Exp': f'{self.exp} / {self.exp_next_level}',
            'Health': self.health,
            'Strength': self.strength,
            'Mana': self.mana,
            'Agility': self.agility,
            'Dexterity': self.dexterity
        }
    

    def save_to_file(self, filename):
        """Saves the current stats to a file"""
        data = self.get_status() 
        data['Exp to Next Level'] = self.exp_next_level

        with open(filename, 'w') as file:
            json.dump(data, file, indent = 4)
           
    @classmethod
    def load_from_file(cls, filename):
        """Loads character stats from file"""
        with open(filename, 'r') as file:
            data = json.load(file)
            character = cls(
                name = data['Name'],
                level = data['Level'],
                health = data['Health'],
                strength = data['Strength'],
                mana = data['Mana'],
                agility = data['Agility'],
                dexterity = data['Dexterity'],
                exp = int(data['Exp'].split(' / ')[0]),  # Extract the exp value from the string
                exp_next_level = data['Exp to Next Level']
            )
            return character