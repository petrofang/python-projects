''' Introduction to Python - CIS177G: Final Project

Giles Cooper 2023 - MIT License

So basically I've been working on a game I just call "dungeon" for now,
aspirationally it's a Multi-User Dungeon, but I haven't gotten to the 
Multi- or even the -User aspects quite yet. I'm still framing out the 
basic mechanics and combat of players and monsters, then the game world
and moving around in it. Some of the work I've done already is beyond 
the scope of this final project, so I've stripped out a lot of it. 
Also, the game is divided into a half dozen modules (so far) which I've
brought all into this single module for convenience, at cost of clarity.  
'''
from random import random
from time import sleep
import pickle   # this module converts objects into binary
                # which can be saved to file

mobile_list = {} # it's a list but it's actually a dictionary.
monster_types = ['kobold',
                'goblin', 
                'orc', 
                'zombie', 
                'giant spider', 
                'owlbear', 
                'vampire', 
                'beholder', 
                'mind-flayer', 
                'dragon',
                ]
PROMPT='\n  > '

def d20_roll(): return (int(1+(random()*20//1)))

class Mobile(): 
    ''' a mobile (living, moving entity)
    
    base class for many other types of creature, including players.
    '''
    id=1
    def __init__(self, name:str='monster', hit_points:int=10, attack:int=1, defense:int=0):
        self.id=Mobile.id
        Mobile.id+=1
        self.name=name
        self.hit_points=hit_points
        self.attack=attack
        self.defense=defense
        self.dead=False
        # add the mobile to the dictionary of active mobiles (no subclasses though)
        if type(self)==Mobile: mobile_list[self.id]=self 
        print(f'{self} arrives on the scene.')

    def die(self):
        ''' how to die (a psuedo-deconstructor)'''
        if not self.dead:
            print(f'{self} hits the ground... DEAD')
            self.dead=True
    
    def __str__(self):
        return self.name

    def fight(self, other): 
       fight(self, other)

class PlayerCharacter(Mobile): # PlayerCharacter has 4 non-dunder methods, 2 of them inherited
    ''' a player-character.'''
    def __init__(self, name:str='adventurer', hit_points:int=100, attack=10, defense=5) -> None:
        super().__init__(name, hit_points, attack, defense)
        self.id=self.name # player names are unique, we we can use that as their ID...
                     # using Mobile.id would cause problems when we load characters
                     # from file later on, when we reload the game
    def save(self):
        ''' save a player-character to file '''
        with open(f"./{self.name}.player", "wb") as f: 
            pickle.dump(self, f)
            print(f'{self} saved to file')
    
    def level_up(self):
        ''' ding! grats.'''
        self.attack+=1
        self.defense+=1
        print(f'{self} has leveled up.')
        print(f'attack:{self.attack}')
        print(f'defense:{self.defense}')
  
def load_player(player_name:str=None) -> PlayerCharacter:
    ''' load a player-character from file. '''
    if player_name == None: 
        player_name=input('What player name would you like to load?' + PROMPT)

    try:
        with open(f"./{player_name}.player", "rb") as f: 
            player = pickle.load(f)
            print(f'{player} has been loaded from file.')

    except FileNotFoundError:
        print(f'No playerfile located for {player_name}')
        player=None

    except pickle.UnpicklingError:
        print(f'Error loading {player_name}\'s file. ')
        player=None
    
    return player

def monster_generator():
    ''' generate a monster'''
    for index,each in enumerate(monster_types):
        print(f' {index+1:<3}| {each}')
    try:
        monster_type=int(input('Which type of monster did you want to summon?'+PROMPT))
        if monster_type < 1 or monster_type > 10:
            raise ValueError
    except TypeError:
        print(f'that was not one of the choices. pick a number between 1 and 10.')
        monster_generator()
    else:
        Mobile(monster_types[monster_type-1], monster_type*10, monster_type*2, monster_type*1)
        # very rudimentary but gets the job done for our purposes

def new_player(name=None) -> PlayerCharacter:  
    ''' generate a new player-character object '''
    print(" --- New character generation ---")
    if name==None: 
        name='adventurer'
        name=input(f'What is you name, {name}?{PROMPT}')
    sleep(1)
    if name=='': name='adventurer' # user did not pick a name, so default adventurer
    try: # check if the player name already exists by trying to open their file
        f = open(f'{name}.player', 'rb')
        f.close()
        if name !='adventurer' and name!='': print('That name is already taken.')
        # if so, just return a default adventurer 
        player=PlayerCharacter()
    except FileNotFoundError: # ie, there is not already a player file of that name
        print(f'Very well, {name}...')
        player=PlayerCharacter(name)
        sleep(1)
    player.save()
    return player

def fight(me:Mobile, them:Mobile):
    ''' engage in combat against a Mobile'''
    if them.dead: pass # cannot kill that which has no life
    else:
        me_roll=d20_roll()
        them_roll=d20_roll()
        print(f'{me} makes an attack at {them}!')
        sleep(2)
        print(f'{me}\'s attack: {me.attack}')
        print(f'{them}\'s defense: {them.defense}')
        sleep(1)
        print(f'{me}\'s d20: {me_roll}.')
        print(f'{them}\'s d20: {them_roll}')
        sleep(2)
        # TODO: hit/miss and damage/armor as seperate rolls (add depth)
        damage = me_roll + me.attack - them_roll - them.defense
        if damage > 0:
            sleep(1)
            print(f'damage = ({me_roll} + {me.attack}) - ({them_roll} + {them.defense})')
            sleep(1)
            if me_roll < 20: 
                print("It's a hit!")
            else: 
                print(" ** CRITICAL STRIKE! **  damage doubled!") 
                damage *= 2
            print(f'{damage} damage done to {them}!')
            them.hit_points-=damage
            print(f'{them} remaining HP: {max(0, them.hit_points)}')
        else:
            print("Swing and a miss!")

        # if HP are depleted, they die; if not, they attack back.   
        if them.hit_points <= 0:
            them.die()
            mobile_list.pop(them.id, None) # remove the dead from the mobile list
            print(f'{me} is victorious!')
            if isinstance(me, PlayerCharacter):
                me.level_up() 
            if isinstance(them, PlayerCharacter):
                print(f"{them.name.upper()} HAS DIED... GAME OVER!")
                quit()
        else: 
            fight(them, me)

def show_monster_list():
### python 3.12 f-string:
#   print(f'{'-'*5}+{'-'*20}')
    print(f'{"-"*5}+{"-"*20}')
    for key, mob in mobile_list.items():
            print(f' {key:<5} | {mob.name}')

def show_stats(mobile:Mobile):
    # TODO: complete function stub
    print(f'  {mobile.name} (ID: {mobile.id})')
    print(f'HP: {mobile.hit_points}')
    print(f'attack: {mobile.attack}')
    print(f'defense: {mobile.defense}')

def size_up(them:Mobile):
    # this would be a great opportunity to implement operator overloading
    # for __lt__ and __gt__ for instantiations of the Mobile class
    my_level = me.attack + me.defense + (me.hit_points // 10)
    their_level = them.attack + them.defense + (them.hit_points // 10)
    if my_level > their_level + 10: print(f'You will almost certainly defeat {them} in battle.')
    elif my_level > their_level: print(f'You could probably defeat {them} in battle.')
    elif my_level < their_level - 10: print(f'{them} is going to wreck you! I want to see this!')
    elif my_level < their_level: print(f'{them} might defeat you in battle.')
    elif my_level == their_level: print(f'You are evenly matched with {them}, could go either way.')
    
def main():
  while True:
    print('---------- MAIN MENU ----------')
    print(' 1) View the monster list')  # 'user can PRINT the collection'
    print(' 2) View a monster\'s stats')# 'user can SEARCH' based on monster ID     
    print(' 3) View player\'s stats')   #  player can view their own stats
    print(' 4) Summon a monster')       # 'user can ADD an object to the collection'
    print(' 5) Size up a monster')      #  user can compare monster stats to player stats
    print(' 6) Fight a monster')        # 'user can REMOVE a particular object (or die trying!)
    print(' 7) Save and quit')          # 'use a class method' to save player to file
    user_input=input(PROMPT)
    if user_input=='1':
        show_monster_list()
    if user_input=='2':
        show_monster_list()
        try: 
            which_monster=int(input('which monster\'s stats would you like to view?'+PROMPT))
            show_stats(mobile_list[which_monster])
        except: 
            print(f'Not found. Choose a monster number from the list or generate more.')
    if user_input=='3':
        show_stats(me)
    if user_input=='4':
        monster_generator()
    if user_input=='5':
        show_monster_list()
        try: 
            size_up(mobile_list[int(input('Which monster would you like to size up?'+PROMPT))])
        except: pass # hmmmmmm
    if user_input=='6':
        show_monster_list()
        try:
            me.fight(mobile_list[int(input('Which monster would you like to fight?'+PROMPT))])
        except: raise # hmm... what was the exception though?
    if user_input=='7':
        if not me.dead: 
            print(f'restoring {me} to full health...')
            me.hit_points=100
            me.save()
        quit()
    sleep(2)

if __name__=="__main__": 
    # first, get the player's character... 
    me=None
    while me==None:
        print(' (N)ew player')
        print(' (L)oad player')
        user_input=input(PROMPT)
        if user_input.upper()=='N': 
            me=new_player()
        if user_input.upper()=='L': 
            me=load_player()
            sleep(1)

    # then, generate some monsters:
    monster_generator()
    while True:
        another=input('Summon another monster? Y/N' + PROMPT)
        if another.upper() == "Y":
            monster_generator()
        else: break
    sleep(0.6)
    if len(mobile_list) < 3: # that's it? weak
        print('    Some more monsters join the party:') 
        sleep(0.3)
        Mobile('sickly kobold',5)
        sleep(0.3)
        Mobile('red goblin',23,4,1)
        sleep(0.3)
        Mobile('gelatinous cube',40,5,5)
        sleep(0.3)
        Mobile('mimic',50,10,0)
        sleep(0.3)
        Mobile('wraith',60,8,0)
        sleep(0.3)
        Mobile('dragonkin', 80,10,10) 
        sleep(0.3)
    Mobile('Smaug, the Great Dragon', 120,20,10)
    sleep(0.5)

    # okay let's enter the main game loop now:
    main()