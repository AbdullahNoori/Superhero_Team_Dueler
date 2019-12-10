import random

      
# Ability Class
class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage


    def attack(self):
        random_value = random.randint(2, 7)
        return random_value


    # def add_ability(self, ability):
    #     ability = Ability("Grace Debugging", 50)
    #     hero = Hero("Grace Hopper", 200)
    #     hero.add_ability(ability)
    #     print(hero.abilities)

#Armor Class # creates defense for hero characters
class Armor:
    def __init__(self, name, max_block):
        self.name = name
        send.max_block = max_block

    def block(self):
        random.randint(0, self.max_block)
        return random_value
    
#Class Hero
class Hero:
    def __init__(self, name, starting_health= 100):
        self.name = name
        self.starting_health: starting_health
        self.current_health: starting_health
        self.abilities: list()
        self.armors: list()
        self.deaths = 0
        self.kills = 0
    
    def add_ability(self, ability):
        self.ability = ability 
        self.abilities.append(ability)

    def attack(self):
        total _damage = 0
        for ability in self.abilities:
            print(ability)
            total_damage += abliity.attack()
            return total_damage

    def add_armor(self, armor)
        self.armor = Armor


    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.num_deaths == num_deaths

    def defend(self, current_health):
       self.current_health == current_health 

    def armor(self, armor):
        self.armor == armor
            
    def defend(self, damage_amt):
        defense == self.defend()
        self.current_health -= damage - defense
     pass

     def is_alive(self):
           '''Return True or False depending on whether the hero is alive or not.
     
    '''
        if current_health in hero <= 0:
            return False 
        elif current_health >= 0:
            return True

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
    def attack(self):
        return random.randint(0, self.max_damage)

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
        for hero in self.heros:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes = append(hero)

    def stat(self):
        '''Print team statistics'''
        for hero in self.heroes:
            print(Your hero{}:".format(hero.name))
            print("{}" Kill/Deaths: {}.format(hero.name, hero.deaths))

    def revive_heroes(self):
    ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        self.other_team = other_team
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_oppenents.append(hero)

        While len(living_heroes) > 0 and len(living_oppenents) > 0:
            random_hero = hero.choice(living_heroes)
            random_opponent = random.choice(living_heroes)
            random_hero.fight(random_oppenent)

            if random_hero.is_alive():
                living_oppenents.remove(random_oppenents)
            else: living_heroes.remove(random_hero)

    def currently_alive(self):
        currently_alive = []
        for hero in self.heroes:
            if hero.is_alive == True:
                currently_alive.append(hero)
            return currently_alive

                    # TODO: Complete the following steps:
            # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
            # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
            # 3) update the list of living_heroes and living_opponents
            # to reflect the result of the fight
class Arena:
    def __init__(self, team_one, team_two):
            '''Instantiate properties'''
            self.team_one = team_one
            self.team_two = team_two
            self.team_Looney_Tune = input( "What is the name of the first team?")
            self.team_Disney = input("What is the name of the second team?")
            self.team_one = Team(self.team_Looney_Tune)
            self.team_two = Team(self.team_Disney)
    
    def create_ability(self):
        '''Prompt for Ability information.
        return Abillity with values from user Input'''
        name = input("What is the ability name")
        max_damage = input("What is the max of the ability?')
        return Ability(name, max_damage)
        

    def create_weapon(self):
            '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # TODO: This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.
        pass


    def create_armor(self):
             '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor object.
        #  return the new armor object with values set by user.
        pass
    

    def cerate_hero(self):
         '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name - input("Hero's name:")
        hero = Hero(hero_name)
        add_item =="1":
        TODO add an ability to the hero
        elif add_item == "3":
           #TODO add an armor to the hero
        return hero  


    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # TODO: This method should allow a user to create team one.
        # 1) Prompt the user for the name of the team
        # 2) Prompt the user for the number of Heroes on the team
        # 3) Instantiate a new Team object,
        # using the team name obtained from user input
        # 4) use a loop to call self.create_hero() for the number
        # of heroes the user specified the team should have,
        # and then add the heroes to the team.
        pass

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # TODO: This method should allow a user to create team two.
        # 1) Prompt the user for the name of the team
        # 2) Prompt the user for the number of Heroes on the team
        # 3) Instantiate a new Team object,
        # using the team name obtained from user input
        # 4) use a loop to call self.create_hero() for the number
        # of heroes the user specified the team should have,
        # and then add the heroes to the team.
        pass
    
    def team_battel(self):
             '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        pass



        


    
     


  

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






