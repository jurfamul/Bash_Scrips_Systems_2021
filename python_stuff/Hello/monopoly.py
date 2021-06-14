#!/user/bin/python3
import random
import pprint as pp
import json

#Global variables
BOARD_SIZE = 40

class Player:
    def __init__(self, human=False, name="bot"):
        self.human = human
        self.name = name
        self.money = 1500
        self.position = 0
        self.property = []
        self.monopolies = []   # stores the group color of a player's monopolies
        self.num_railroads = 0
        self.num_turns = 1
        self.bankrupt = False

    def roll_dice(self):
        firstroll = random.randint(1, 6)
        secondroll = random.randint(1, 6)
        extraturn = False

        if firstroll == secondroll:
            extraturn = True

        return firstroll, secondroll, extraturn

    def move(self, spaces):
        tempMove = self.position + spaces

        if tempMove > BOARD_SIZE :
            tempMove = tempMove - BOARD_SIZE

            if self.num_turns <= 20:
                self.money = self.money + 100
                pp.pprint("You passed go. you get $100. You have ${0}.".format(self.money))
            else :
                pp.pprint("You passed go but got no money.")
        elif tempMove == BOARD_SIZE:
            tempMove = 0
            if self.num_turns <= 20:
                self.money = self.money + 200
                pp.pprint("You landed on go. you get $200. You have ${0}.".format(self.money))
            else:
                pp.pprint("You landed on go but got no money.")

        self.position = tempMove
        return self.position

    def check_for_monopoly(self, group):
        group_count = 0
        for prop in self.property:
            if group == prop['group']:
                group_count = group_count + 1

        if group == "utility" or group == "brown" or group == "darkblue":
            if group_count == 2:
                self.monopolies.append(group)
                pp.pprint("{0} has a monopoly over the {1} properties!".format(self.name, group))
        elif group == "white":
            self.num_railroads = group_count
            if group_count == 4:
                self.monopolies.append(group)
                pp.pprint("{0} has a monopoly over the railroads!".format(self.name))
        else:
            if group_count == 3:
                self.monopolies.append(group)
                pp.pprint("{0} has a monopoly over the {1} properties!".format(self.name, group))

    def buy_property(self, new_property):
        new_property['owner'] = self
        self.property.append(new_property)
        self.money = self.money - new_property['cost']

        new_prop_group = new_property['group']
        self.check_for_monopoly(new_prop_group)

    def add_money(self, cash):
        self.money = self.money + cash

    def transfer_property(self, other_player):
        for prop in self.property:
            self.property.remove(prop)
            print("setting owner of {0} to {1}.".format(prop['name'], other_player.get_name()))
            prop['owner'] = other_player.get_name()
            other_player.property.append(prop)
            new_prop_group = prop['group']
            other_player.check_for_monopoly(new_prop_group)

    def release_property(self):
        for prop in self.property:
            self.property.remove(prop)
            print("setting owner of {0} to None.".format(prop['name']))
            prop['owner'] = None

    def pay_rent(self, other_player, rent):
        if self.money > rent:
            self.money = self.money - rent
            other_player.add_money(rent)
            print("{0} payed {1} ${2} for rent".format(self.name, other_player.get_name(), rent))
        else:
            print("{0} can not afford to pay the rent to {1} and goes bankrupt."
                  .format(self.name, other_player.get_name()))
            other_player.add_money(self.money)
            self.money = 0
            self.transfer_property(other_player)
            self.bankrupt = True

    def pay_tax(self, tax):
        if self.money > tax:
            print("{0} pays ${1} in taxes.".format(self.name, tax))
            self.money = self.money - tax
        else:
            print("Player {0} can not pay ${1} in taxes and goes bankrupt.".format(self.name, tax))
            self.money = 0
            self.release_property()
            self.bankrupt = True

    def update_turn_count(self, turn):
        self.num_turns = turn

    def get_name(self):
        return self.name

    def get_space(self):
        return self.position

    def get_cash(self):
        return self.money

    def get_num_railroads(self):
        return self.num_railroads

    def has_monopoly(self, group):
        return group in self.monopolies

    def is_human(self):
        return self.human

    def is_bankrupt(self):
        return self.bankrupt

    def __str__(self):
        return "Player name: {0}, cash: {1}, {2} properties owned, {3} monopolies controlled."\
            .format(self.name, self.money, len(self.property), len(self.monopolies))


class Game():
    def __init__(self, numPlayers):
        self.numPlayers = numPlayers
        self.players = []
        self.numTurns = 1
        self.board = [
            {'name': 'Go', 'cost': 0, 'location': 0, 'type': 'pass', 'base_rent': 0, 'group': 'go'},
            {'name': 'Mediterranean Avenue', 'cost': 60, 'location': 1, 'type': 'property', 'base_rent': 2, 'group': 'brown',
             'owner': None},
            {'name': 'Community Chest', 'cost': 0, 'location': 2, 'type': 'chest', 'base_rent': 0,
                'group': 'chill'},
            {'name': 'Baltic Avenue', 'cost': 60, 'location': 3, 'type': 'property', 'base_rent': 4, 'group': 'brown',
                'owner': None},
            {'name': 'Income Tax', 'cost': 0, 'location': 4, 'type': 'tax', 'base_rent': 100,
                'group': 'tax'},
            {'name': 'Reading RR', 'cost': 200, 'location': 5, 'type': 'railroad', 'base_rent': 25, 'group': 'white',
                'owner': None},
            {'name': 'Oriental Avenue', 'cost': 100, 'location': 6, 'type': 'property', 'base_rent': 6,
                'group': 'blue', 'owner': None},
            {'name': 'Chance', 'cost': 0, 'location': 7, 'type': 'chance', 'base_rent': 0,
                'group': 'chill'},
            {'name': 'Vermont Avenue', 'cost': 100, 'location': 8, 'type': 'property', 'base_rent': 6, 'group': 'blue',
                'owner': None},
            {'name': 'Connecticut Avenue', 'cost': 120, 'location': 9, 'type': 'property', 'base_rent': 8,
                'group': 'blue', 'owner': None},
            {'name': 'Jail', 'cost': 0, 'location': 10, 'type': 'chest', 'base_rent': 0,
                'group': 'chill'},
            {'name': 'St. Charles', 'cost': 140, 'location': 11, 'type': 'property', 'base_rent': 10, 'group': 'purple',
                'owner': None},
            {'name': 'Electric Company', 'cost': 150, 'location': 12, 'type': 'utility', 'base_rent': 1,
                'group': 'utility', 'owner': None},
            {'name': 'States Avenue', 'cost': 140, 'location': 13, 'type': 'property', 'base_rent': 10, 'group': 'purple',
                'owner': None},
            {'name': 'Virginia Avenue', 'cost': 160, 'location': 14, 'type': 'property', 'base_rent': 12,
                'group': 'purple', 'owner': None},
            {'name': 'Pennsylvania RR', 'cost': 200, 'location': 15, 'type': 'railroad', 'base_rent': 25,
                'group': 'white', 'owner': None},
            {'name': 'St. James', 'cost': 180, 'location': 16, 'type': 'property', 'base_rent': 14, 'group': 'orange',
                'owner': None},
            {'name': 'Community Chest', 'cost': 0, 'location': 17, 'type': 'chest', 'base_rent': 0,
                'group': 'chill'},
            {'name': 'Tennessee Avenue', 'cost': 180, 'location': 18, 'type': 'property', 'base_rent': 14,
                'group': 'orange', 'owner': None},
            {'name': 'New York', 'cost': 200, 'location': 19, 'type': 'property', 'base_rent': 16, 'group': 'orange',
                'owner': None},
            {'name': 'Free Parking', 'cost': 0, 'location': 20, 'type': 'parking', 'base_rent': 0,
                'group': 'chill'},
            {'name': 'Kentucky Avenue', 'cost': 220, 'location': 21, 'type': 'property', 'base_rent': 18, 'group': 'red',
                'owner': None},
            {'name': 'Chance', 'cost': 0, 'location': 22, 'type': 'chance', 'base_rent': 0,
                'group': 'chill'},
            {'name': 'Indiana Avenue', 'cost': 220, 'location': 23, 'type': 'property', 'base_rent': 18, 'group': 'red',
                'owner': None},
            {'name': 'Illinois Avenue', 'cost': 240, 'location': 24, 'type': 'property', 'base_rent': 20, 'group': 'red',
                'owner': None},
            {'name': 'B&O RR', 'cost': 200, 'location': 25, 'type': 'railroad', 'base_rent': 25, 'group': 'white',
                'owner': None},
            {'name': 'Atlantic Avenue', 'cost': 260, 'location': 26, 'type': 'property', 'base_rent': 22,
                'group': 'yellow', 'owner': None},
            {'name': 'Ventnor Avenue', 'cost': 260, 'location': 27, 'type': 'property', 'base_rent': 22,
                'group': 'yellow', 'owner': None},
            {'name': 'Water Works', 'cost': 150, 'location': 28, 'type': 'utility', 'base_rent': 1,
                'group': 'utility', 'owner': None},
            {'name': 'Marvin Gardens', 'cost': 280, 'location': 29, 'type': 'property', 'base_rent': 24, 'group': 'yellow',
                'owner': None},
            {'name': 'Go To Jail!', 'cost': 0, 'location': 30, 'type': 'gotojail', 'base_rent': 0,
                'group': 'chill'},
            {'name': 'Pacific Avenue', 'cost': 300, 'location': 31, 'type': 'property', 'base_rent': 26, 'group': 'green',
                'owner': None},
            {'name': 'North Carolina', 'cost': 300, 'location': 32, 'type': 'property', 'base_rent': 26, 'group': 'green',
                'owner': None},
            {'name': 'Community Chest', 'cost': 0, 'location': 33, 'type': 'chest', 'base_rent': 0,
                'group': 'chill'},
            {'name': 'Pennsylvania Avenue', 'cost': 320, 'location': 34, 'type': 'property', 'base_rent': 28,
                'group': 'green', 'owner': None},
            {'name': 'Short Line', 'cost': 200, 'location': 35, 'type': 'railroad', 'base_rent': 25, 'group': 'white',
                'owner': None},
            {'name': 'Chance', 'cost': 0, 'location': 36, 'type': 'chance', 'base_rent': 0,
                'group': 'chill'},
            {'name': 'Park Place', 'cost': 350, 'location': 37, 'type': 'property', 'base_rent': 35, 'group': 'darkblue',
                'owner': None},
            {'name': 'Luxury Tax', 'cost': 0, 'location': 38, 'type': 'tax', 'base_rent': 75,
                'group': 'tax'},
            {'name': 'Boardwalk', 'cost': 400, 'location': 39, 'type': 'property', 'base_rent': 50, 'group': 'darkblue',
                'owner': None}
            ]

    def addplayers(self):
        count = 1
        while count <= self.numPlayers :
            isHuman = None
            playerName = ""

            while isHuman == None:
                isHumanInput = input("player {0}, enter 'h' for human or 'b' for bot: ".format(count))

                if isHumanInput == 'h' :
                    isHuman = True
                    playerName = input("Enter player name: ")
                elif isHumanInput == 'b' :
                    isHuman = False
                    playerName = "bot{0}".format(count)
                else:
                    print("Invalid entry detected. Please try again.")

            newPlayer = Player(isHuman, playerName)
            self.players.append(newPlayer)
            count = count + 1

    @staticmethod
    def offer_property(current_space, current_player):
        prop_cost = current_space['cost']
        if prop_cost < current_player.get_cash():
            if current_player.is_human():

                phase_complete = False
                while not phase_complete:
                    buy_prop = input("Would you like to buy {0} (y/n)? (cost: ${1}, you have ${2}): "
                                     .format(current_space['name'], prop_cost, current_player.get_cash()))
                    if buy_prop == 'y':
                        pp.pprint("player {0} is purchasing {1} for ${2}"
                                  .format(current_player.get_name(), current_space['name'], prop_cost))
                        current_player.buy_property(current_space)
                        phase_complete = True
                    elif buy_prop == 'n':
                        pp.pprint("player {0} is not purchasing {1}"
                                  .format(current_player.get_name(), current_space['name']))
                        phase_complete = True
                    else:
                        pp.pprint("Invalid input. Please try again.")
            else:
                pp.pprint("player {0} is purchasing {1} for ${2}"
                          .format(current_player.get_name(), current_space['name'], prop_cost))
                current_player.buy_property(current_space)
        else:
            pp.pprint("You can not afford {0}. (cost: {1}, you have ${2})"
                      .format(current_space['name'], prop_cost, current_player.get_cash()))

    def take_turn(self, current_player):
        current_space = self.board[current_player.get_space()]

        pp.pprint("Player {0}, it's your turn! (cash: {1}, location: {2} ({3})"
                  .format(current_player.get_name(), current_player.get_cash(),
                          current_player.get_space(), current_space['name']))

        if current_player.is_human() :
            input("Press enter to roll dice, {0}".format(current_player.get_name()))

        rolls = current_player.roll_dice()
        total = rolls[0] + rolls[1]
        pp.pprint("The first die rolls {0}, the second die rolls {1}, the total roll is {2}".format(rolls[0], rolls[1], total))
        has_extra_turn = rolls[2]

        if has_extra_turn :
            pp.pprint("You rolled doubles! you get an extra turn.")

        current_space = self.board[current_player.move(total)]
        c_space_group = current_space['group']
        c_space_type = current_space['type']
        pp.pprint("player {0} landed on {1}.".format(current_player.get_name(), current_space['name']))

        if c_space_group == 'chill' or c_space_group == 'go':
            pass
        elif c_space_group == 'tax':
            current_player.pay_tax(current_space['base_rent'])
        else:
            if c_space_type == "property":
                if current_space['owner'] == None :
                    self.offer_property(current_space, current_player)
                else:
                    owner = current_space['owner']
                    if current_player != owner:
                        rent = current_space['base_rent']
                        group = current_space['group']
                        print("{0} is owned by {1}.".format(current_space['name'], owner.get_name()))

                        if owner.has_monopoly(group):
                            rent = rent * 2
                            print("Bad news: They have a monopoly here. Rent is doubled.")

                        current_player.pay_rent(owner, rent)
                    else:
                        print("Player {0} already owns {1}.".format(current_player.get_name(), current_space['name']))
            elif c_space_type == "railroad":
                if current_space['owner'] == None:
                    self.offer_property(current_space, current_player)
                else:
                    owner = current_space['owner']
                    if current_player != owner:
                        rent = current_space['base_rent']
                        group = current_space['group']
                        print("{0} is owned by {1}.".format(current_space['name'], owner.get_name()))

                        if owner.has_monopoly(group):
                            rent = 200
                            print("Bad news: They have a monopoly here. fairs are $200.")
                        else:
                            num_rail = owner.get_num_railroads()

                            if num_rail == 3:
                                rent = 100
                                print("They own a {0} railroads. fairs are ${1}.".format(num_rail, rent))
                            elif num_rail == 2:
                                rent = 50
                                print("They own a {0} railroads. fairs are ${1}.".format(num_rail, rent))
                            elif num_rail == 1:
                                print("They own a {0} railroads. fairs are ${1}.".format(num_rail, rent))

                        current_player.pay_rent(owner, rent)
                    else:
                        print("Player {0} already owns {1}.".format(current_player.get_name(), current_space['name']))
            elif c_space_type == "utility":
                if current_space['owner'] == None :
                    self.offer_property(current_space, current_player)
                else:
                    owner = current_space['owner']
                    if current_player != owner:
                        group = current_space['group']
                        rent = total
                        print("{0} is owned by {1}.".format(current_space['name'], owner.get_name()))

                        if owner.has_monopoly(group):
                            print("Bad news: They have a monopoly on utilities.")
                            print("The rent is 10 times your total roll of {0}.".format(rent))
                            rent = rent * 10
                        else:
                            print("The owner only owns this utility.")
                            print("The rent is 4 times your total roll of {0}".format(rent))
                            rent = rent * 4

                        current_player.pay_rent(owner, rent)
                    else:
                        print("Player {0} already owns {1}.".format(current_player.get_name(), current_space['name']))

        pp.pprint(str(current_player))
        if current_player.is_human():
            input("Press enter to end turn.")

        print("")
        return has_extra_turn

    def play(self):
        self.addplayers()
        while self.numPlayers > 1 :
            for player in self.players:
                if not player.is_bankrupt():
                    player.update_turn_count(self.numTurns)
                    has_turn = True
                    count_extra_turns = 0
                    while has_turn and count_extra_turns < 3:
                        has_turn = self.take_turn(player)
                        if has_turn:
                            count_extra_turns = count_extra_turns + 1

                    if player.is_bankrupt():
                        self.players.remove(player)
                        self.numPlayers = self.numPlayers - 1
            self.numTurns = self.numTurns + 1
        print("Congratulations Player {0}. You win!".format(self.players[0].get_name()))

    #Testing functions
    def printplayers(self):
        for player in self.players :
            pp.pprint(str(player))


def main():
    numPlayers = None

    while numPlayers == None :
        numInput = input("How many players (1-4): ")

        if numInput == '1' or numInput == '2' or numInput == '3' or numInput == '4' :
            numPlayers = int(numInput)
        else :
            print("Invalid number of players entered. Try again")

    newGame = Game(numPlayers)
    newGame.play()


if __name__ == "__main__" :
    main()
