import random

      
# Ability Class
class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage


    def attack(self):
        random_value = random.randint(2, 7)
        return random_value

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
    #Ability methods add to list
    def add_ability(self, ability):
        self.ability = ability 
        self.abilities.append(ability)
    #Attack method for hero
    def attack(self):
        total_damage = 0
        
        for ability in self.abilities:
            print(ability)
            total_damage += abliity.attack()
            return total_damage

    def add_armor(self, armor):
        self.armor = armor
        self.armors.append(armor)

    def add_death(self, num_deaths):
        self.num_deaths == num_deaths

    def defend(self, current_health):
        blocks = 0
        self.damage_amt == current_health 
        for blocks in self.armors:
            blocks += damage_amt.block()
            return blocks

    def take_damage(self, damage):
        #Confirms the amount of damage taken
        self.current_health -= damage

    def is_alive(self):
        #Checks if the Hero has health
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            if len(self.abilities) > 0 and len(oppenent.abilities) == 0:
                opppenent.take_damage(self.attack())

            elif len(opponent>abilites) > 0 and len(self.abilities) == 0:
                self.take_damage(self.attack)
            else:
                self.take_damage(self.attack())
                oppenent.take_damage(self.attack())

        if self.is_alive():
            print(f"{self.name} won!")
            opponent.add_death(1)
            self.add_kill(1)

        else:
            print(f"{opponent.name} won!")
            self.add_death(10)   
            opponent.add_kill(1)
            

    def add_weapon(self, weapon):
        self.weapon = weapon
        self.ablities.append(weapon)


    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths

#Ability Class
class Weapon(Ability):
    
    def attack(self):
        return random.randint(0, self.max_damage)

#Team Class
class Team:
    def __init__(self,name):
        self.name = name
        self.add_hero = list()

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
        self.heroes.append(hero)

    def stat(self):
        '''Print team statistics'''
        for hero in self.heroes:
        print("Your hero{}:".format(hero.name))
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
        name = input("What is the ability name?")
        max_damage = input("What is the max of the ability?')
        return Ability(name, max_damage)
        wf
    def create_weapon(self):
            '''Prompt user for Weapon information
            return Weapon with values from user input'''
        weapon_name = input("Create a new weapon...")
        max_damage = input("Max Damage.")
        return weapon(weapon_name, int(max_damage))

    def create_armor(self):e
        armor_name = input("Time to name your armor!")
        armor_block = input("Max Armor block")
        return armor(armor_name, int(armor_block)

    def create_hero(self):
         '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name - input("Hero's name:")
        hero = Hero(hero name)
        add_item = None 
        while add_item !+ "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3 Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1':
                ability = self.create_ability
                hero.add_ability(ability)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item =="3"
                armor = self.create_weapon()
                hero.add_armor(armor)
        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''

        team_Looney_Tune = input("How many Heroes are on your team?")
        
        if team_Looney_Tune != None:
            for _ in range(0, int(team_Looney_Tune)):
                hero - self. create_hero()
                self.team_one.add_hero(hero)

            else 
                team_Looney_Tune = input("Incorrect Input. Please enter a number:")
                return team_Looney_Tune

        def build_team_two(self):
            
            team_Disney = input("Select how many hereos are you on team 2")")

            if team_Disney != None:
                for _ in range(0, int(team_Disney)):
                    hero = self.create_hero()
                    self.two_add.add_hero(hero)
                else 
                    team_Disney = input("Sorry, incorrect input. Please enter a number:")

        def team_battle(self):
            #fight bewteen team_one and team_two
            self. team_one.attack(self.team_two):
        
        def show stats(self):
            print ("\nStats"):
            self.team_one.stats()
            self.team_two.stats()

            if len(self.team_one.currently_alive()) >0:
                print(self.team_pne.name + "wins")
            else:
                print(self.team_two.name + "wins")


    if __name__ == "__main__":
        game_is_running = True

        # Instantiate Game Arena
        arena = Arena()

        #Build Teams
        arena.build_team_one()
        arena.build_team_two()

        while game_is_running:

            arena.team_battle()
            arena.show_stats()
            play_again = input("Play Again? Y or N: ")

            #Check for Player Input
            if play_again.lower() == "n":
                game_is_running = False

            else:
                #Revive heroes to play again
                arena.team_one.revive_heroes()
                arena.team_two.revive_heroes()
    
