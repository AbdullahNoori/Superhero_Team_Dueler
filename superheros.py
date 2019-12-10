import random

      
# Ability Class
class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage


    def attack(self):
        random_value = random.randint(2, 7)
        return random_value


    def add_ability(self, ability):
        ability = Ability("Grace Debugging", 50)
        hero = Hero("Grace Hopper", 200)
        hero.add_ability(ability)
        print(hero.abilities)

#Armor Class
class Armor:
    def __init__(self, name, max_block):
        self.name = name
        send.max_block = max_block
    pass

    def block(self):
        return random.randint(0, self.max_block)
    
#Class Hero
class Hero:
    def __init__(self, name, starting_health= 100):
        self.abilities: list()
        self.armors: list()
        self.name: name
        self.starting_health: starting_health
        self.current_health: starting_health
        self.death = 0
        self.kills = 0

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.num_deaths = num_deaths


    def defend(self, current_health):
       self.current_health = current_health 

    def armor(self, armor):
        self.armor = armor
            
    def defend(self, damage_amt):
        defense = self.defend()
        self.current_health -= damage - defense
     pass

     def is_alive(self):
           '''Return True or False depending on whether the hero is alive or not.
    '''
    # TODO: Check the current_health of the hero.
    # if it is <= 0, then return False. Otherwise, they still have health
    # and are therefore alive, so return True
    pass

 
    def fight(self, oppenent):
      '''Return True or False depending on whether the hero is alive or not.
  '''
  # TODO: Check the current_health of the hero.
  # if it is <= 0, then return False. Otherwise, they still have health
  # and are therefore alive, so return True
    pass 
   # TODO: Refactor this method to update the following:
        # 1) the number of kills the hero (self) has when the opponent dies.
        # 2) then number of kills the opponent has when the hero (self) dies
        # 3) the number of deaths of the opponent if they die    in the fight
        # 4) the number of deaths of the hero (self) if they die in the fight
    pass


#Ability Class
class Weapon(Ability):
    def attack(self, weapon):
        self.weapon = weapon
        pass

#Team Class
class Team:
    def __init__(self,name, add_hero, remove_hero, view_all_heroes):
        self.name = name
        self.add_hero = list()
        self.remove_hero = remove_hero()
        self.view_all_heroes = view_all_heroes

    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
        for hero in self.view_all_heroes:
            if hero in self.view_all_heroes == 

    def add_hero(self, hero):
        self.hero = hero.list()
        pass

    def stat(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{}" Kill/Deaths: {}.format(hero.name, kd))

    def revive_heroes(self):
    ''' Reset all heroes health to starting_health'''
        # TODO: for each hero in self.heroes,
        # set the hero's current_health to their starting_health
        pass

    def attack(self, other_team):

        living_heroes = list()
        living_opponents = lists()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_oppenents.append(hero)

        While len(living_heroes) > 0 and len(living_oppenents) > 0:
                    # TODO: Complete the following steps:
            # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
            # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
            # 3) update the list of living_heroes and living_opponents
            # to reflect the result of the fight
class Arena:
    def __init__(selfm, team_one, team_two):
            '''Instantiate properties'''
            self.team_one = team_one
            self.team_two = team_two

    
        # TODO: create instance variables named team_one and team_two that
        # will hold our teams

    def create_ability(self):
        '''Prompt for Ability information.
        return Abillity with values from user Input'''
        name = input("What is the ability name")
        max_damage = input("What is the maxthe ability?')

        return Ability(name, max_damage)



    

        


    
     


  

if __name__ == "__main__":
  
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)

        # self.damage_amt = damage_amt
    
        # for damages in self.damage_amt:
        #  
        #damage_amt -= max_damage()
        # return damage_amt
        # else 
        #     return max_damage

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())




#   '''Calculate the total block amount from all armor blocks.
#      return: total_block:Int

#   total_damage = 0
#         for ability in self.abilities:
#             total_damage += ability.attack()
#         return total_damage
#         total_damage = 0
#             for dam





#   '''   for damage in damage_amt
# #   # TODO: This method should run the block method on each armor in self.armor
#   random_value = random.randint(0, damage_amt)
#     return total_block



# def add_armor(self, armor):
#     self.armor = armors
    
# for abilitys in 







if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)



    # ability = Ability("Great Debugging', 50)
    # another_ability = ability('Smarty pants', 90)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add ability(another_ability)
    # print(my_hero.name)
    # print(my_name.current_health)






