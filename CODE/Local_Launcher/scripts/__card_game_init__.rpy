default selectcard = -1
default selectenemycard = -1
default currentpage = 0
#Shown Cards is a integer for how many cards should be hidden
#
#Sudden Death is where when there is draw then a new round will begin
#Where you take all card of you color up in you hand
#
#Reverse is where the take over is reverse so instead of > it is <
#
#Dobelt_number
# Rules(Shown Cards, Sudden Death, Reverse, Dobelt_number)
default standard_rules = [0, False, False, False]

default playercolor_rgb = Color((2, 106, 185, 255))
default enemycolor_rgb = Color((219, 0, 0, 255))


default table_cards = [[None for x in range(0,3)] for y in range(0,3)]

#Special Cards

default card_bird = Card( imagepath="images/cards/087001_hr1.png",
                            topvalue = 4,
                            bottomvalue = 2,
                            rightvalue = 2,
                            leftvalue = 1,
                            title="Bird",
                            description = "Its a bird.")

default card_fireball = Card( imagepath="images/cards/087006_hr1.png",
                            topvalue = 2,
                            bottomvalue = 1,
                            rightvalue = 3,
                            leftvalue = 3,
                            title="Fireball",
                            description = "Its a Fireball.")

default card_snail = Card( imagepath="images/cards/087008_hr1.png",
                            topvalue = 7,
                            bottomvalue = 1,
                            rightvalue = 4,
                            leftvalue = 4,
                            title="Spike Snail",
                            description = "Its a snail with spikes.")

default card_chicken = Card( imagepath="images/cards/087085_hr1.png",
                            topvalue = 1,
                            bottomvalue = 2,
                            rightvalue = 3,
                            leftvalue = 3,
                            title="Giant Chicken",
                            description = "Its an oversized chicken.")

default card_monster = Card( imagepath="images/cards/087012_hr1.png",
                            topvalue = 2,
                            bottomvalue = 2,
                            rightvalue = 5,
                            leftvalue = 5,
                            title="Monster",
                            description = "Its a Monster.")

default card_goldie = Card( imagepath="images/cards/Goldie.jpg",
                            topvalue = 5,
                            bottomvalue = 2,
                            rightvalue = 5,
                            leftvalue = 4,
                            title="Goldie",
                            description = "Its a Goldfish.")
                    
default card_Goldie2 = Card( imagepath="images/cards/Goldie2.jpg",
                            topvalue = 5,
                            bottomvalue = 2,
                            rightvalue = 5,
                            leftvalue = 4,
                            title="Goldie",
                            description = "Its a Goldfish.")

default card_milo = Card( imagepath="images/cards/Milo.jpg",
                            topvalue = 5,
                            bottomvalue = 2,
                            rightvalue = 5,
                            leftvalue = 1,
                            title="Milo",
                            description = "Its a Good boy.")

default card_milo2 = Card( imagepath="images/cards/Milo2.jpg",
                            topvalue = 5,
                            bottomvalue = 2,
                            rightvalue = 5,
                            leftvalue = 1,
                            title="Milo2",
                            description = "Continues to be a Good Boy.")

default card_stanley = Card( imagepath="images/cards/Stanley.jpg",
                            topvalue = 5,
                            bottomvalue = 2,
                            rightvalue = 3,
                            leftvalue = 5,
                            title="Stanley",
                            description = "Just the cutest little ball of Evil")

default card_stanley2 = Card( imagepath="images/cards/Stanley2.jpg",
                            topvalue = 5,
                            bottomvalue = 2,
                            rightvalue = 3,
                            leftvalue = 5,
                            title="Stanley2",
                            description = "A murderous force of Evil for you heart to behold.")

default card_aflac = Card( imagepath="images/cards/Aflac.jpg",
                            topvalue = 3,
                            bottomvalue = 7,
                            rightvalue = 4,
                            leftvalue = 2,
                            title="Aflac",
                            description = "Aflac is a duck.")

default card_aflac2 = Card( imagepath="images/cards/Aflac2.jpg",
                            topvalue = 3,
                            bottomvalue = 7,
                            rightvalue = 4,
                            leftvalue = 2,
                            title="Aflac2",
                            description = "Aflac is a duck.")

default card_charlie = Card( imagepath="images/cards/Charlie.jpg",
                            topvalue = 2,
                            bottomvalue = 5,
                            rightvalue = 7,
                            leftvalue = 2,
                            title="Charlie",
                            description = "Charlie is a Horse.")

default card_charlie2 = Card( imagepath="images/cards/Charlie2.jpg",
                            topvalue = 2,
                            bottomvalue = 5,
                            rightvalue = 7,
                            leftvalue = 2,
                            title="Charlie2",
                            description = "Charlie is a Horse.")

default card_chirp = Card( imagepath="images/cards/Chirp.jpg",
                            topvalue = 3,
                            bottomvalue = 7,
                            rightvalue = 0,
                            leftvalue = 4,
                            description  = "Chirp is a cricket.",)

default card_chirp2 = Card( imagepath="images/cards/Chirp2.jpg",
                            topvalue = 3,
                            bottomvalue = 7,
                            rightvalue = 0,
                            leftvalue = 4,
                            description  = "Chirp is a cricket.",)

default card_clara = Card( imagepath="images/cards/Clara.jpg",
                            topvalue = 2,
                            bottomvalue = 5,
                            rightvalue = 9,
                            leftvalue = 5,
                            title="Clara",
                            description = "Clara is a mouse.")

default card_clara2 = Card( imagepath="images/cards/Clara2.jpg",
                            topvalue = 2,
                            bottomvalue = 5,
                            rightvalue = 9,
                            leftvalue = 5,
                            title="Clara2",
                            description = "Clara is a mouse.")

default card_cordell = Card( imagepath="images/cards/Cordell.jpg",
                            topvalue = 5,
                            bottomvalue = 2,
                            rightvalue = 7,
                            leftvalue = 9,
                            title="Cordell",
                            description = "Cordell is a sheep.")

default card_cordell2 = Card( imagepath="images/cards/Cordell2.jpg",
                            topvalue = 5,
                            bottomvalue = 2,
                            rightvalue = 7,
                            leftvalue = 9,
                            title="Cordell2",
                            description = "Cordell is a sheep.")

default card_dilly = Card( imagepath="images/cards/Dilly.jpg",
                            topvalue = 3,
                            bottomvalue = 7,
                            rightvalue = 7,
                            leftvalue = 6,
                            title="Dilly",
                            description = "Dilly is a Duck.")

default card_dilly2 = Card( imagepath="images/cards/Dilly2.jpg",
                            topvalue = 3,
                            bottomvalue = 7,
                            rightvalue = 7,
                            leftvalue = 6,
                            title="Dilly2",
                            description = "Dilly is a Duck.")

default card_goliath = Card( imagepath="images/cards/Goliath.jpg",
                            topvalue = 3,
                            bottomvalue = 7,
                            rightvalue = 7,
                            leftvalue = 3,
                            title="Goliath",
                            description = "Goliath is a wolf.")
default card_goliath2 = Card( imagepath="images/cards/Goliath2.jpg",
                            topvalue = 3,
                            bottomvalue = 7,
                            rightvalue = 7,
                            leftvalue = 3,
                            title="Goliath2",
                            description = "Goliath is a wolf.")

default card_gwltney = Card( imagepath="images/cards/Gwltney.jpg",
                            topvalue = 3,
                            bottomvalue = 7,
                            rightvalue = 5,
                            leftvalue = 6,
                            title="Gwltney",
                            description = "Gwltney is a rhino.")
default card_gwltney2 = Card( imagepath="images/cards/Gwltney2.jpg",
                            topvalue = 3,
                            bottomvalue = 7,
                            rightvalue = 5,
                            leftvalue = 6,
                            title="Gwltney2",
                            description = "Gwltney is a rhino.")
default card_hector = Card( imagepath="images/cards/Hector.jpg",
                            topvalue = 2,
                            bottomvalue = 5,
                            rightvalue = 4,
                            leftvalue = 4,
                            title="Hector",
                            description = "Hector is a girraffe.")
default card_hector2 = Card( imagepath="images/cards/Hector2.jpg",
                            topvalue = 2,
                            bottomvalue = 5,
                            rightvalue = 4,
                            leftvalue = 4,
                            title="Hector2",
                            description = "Hector is a girraffe.")

default card_jackson = Card( imagepath="images/cards/Jackson.jpg",
                            topvalue = 2,
                            bottomvalue = 5,
                            rightvalue = 0,
                            leftvalue = 2,
                            title="Jackson",
                            description = "Jackson is a swan.")
default card_jackson2 = Card( imagepath="images/cards/Jackson2.jpg",
                            topvalue = 2,
                            bottomvalue = 5,
                            rightvalue = 0,
                            leftvalue = 2,
                            title="Jackson2",
                            description = "Jackson is a swan.")
default card_michael = Card( imagepath="images/cards/Michael.jpg",
                            topvalue = 3,
                            bottomvalue = 7,
                            rightvalue = 0,
                            leftvalue = 5,
                            title="Michael",
                            description = "Michael is a cardinal.")
default card_michael2 = Card( imagepath="images/cards/Michael2.jpg",
                            topvalue = 3,
                            bottomvalue = 7,
                            rightvalue = 0,
                            leftvalue = 5,
                            title="Michael2",
                            description = "Michael is a cardinal.")
default card_Olivia = Card( imagepath="images/cards/Olivia.jpg",
                            topvalue = 2,
                            bottomvalue = 5,
                            rightvalue = 8,
                            leftvalue = 2,
                            title="Olivia",
                            description = "Olivia is a Ostrige.")
default card_Olivia2 = Card( imagepath="images/cards/Olivia2.jpg",
                            topvalue = 2,
                            bottomvalue = 5,
                            rightvalue = 8,
                            leftvalue = 2,
                            title="Olivia2",
                            description = "Olivia is a Ostrige.")
default card_Peacky = Card( imagepath="images/cards/Peacky.jpg",
                            topvalue = 5,
                            bottomvalue = 2,
                            rightvalue = 7,
                            leftvalue = 2,
                            title="Peacky",
                            description = "Peacky is a peacock.")
default card_Peacky2 = Card( imagepath="images/cards/Peacky2.jpg",
                            topvalue = 5,
                            bottomvalue = 2,
                            rightvalue = 7,
                            leftvalue = 2,
                            title="Peacky2",
                            description = "Peacky is a peacock.")
default card_robin = Card( imagepath="images/cards/Robin.jpg",
                            topvalue = 3,
                            bottomvalue = 7,
                            rightvalue = 2,
                            leftvalue = 5,
                            title="Robin",
                            description = "Robin is a bird.")
default card_robin2 = Card( imagepath="images/cards/Robin2.jpg",
                            topvalue = 3,
                            bottomvalue = 7,
                            rightvalue = 2,
                            leftvalue = 5,
                            title="Robin2",
                            description = "Robin is a bird.")
default card_rocky = Card( imagepath="images/cards/Rocky.jpg",
                            topvalue = 3,
                            bottomvalue = 7,
                            rightvalue = 2,
                            leftvalue = 4,
                            title="Rocky",
                            description = "Rocky is a pitbull.")
default card_rocky2 = Card( imagepath="images/cards/Rocky2.jpg",
                            topvalue = 3,
                            bottomvalue = 7,
                            rightvalue = 2,
                            leftvalue = 4,
                            title="Rocky2",
                            description = "Rocky is a pitbull.")
default card_squaky = Card( imagepath="images/cards/Squaky.jpg",
                            topvalue = 3,
                            bottomvalue = 7,
                            rightvalue = 7,
                            leftvalue = 5,
                            title="Squaky",
                            description = "Squaky is a raven.")

### For testing and place holding purposes ### 
default card_back = Card( imagepath="images/cards/start.jpeg",
                            topvalue = 0,
                            bottomvalue = 0,
                            rightvalue = 0,
                            leftvalue = 0,
                            title="Back",
                            description = "Back of the card.")

### Deck must hold 10 cards change cards to basic ai card sets later for each opponent, also later when webhook integration is done set this to sync with the server

default enemy_deck = [card_goldie, card_Goldie2, card_milo, card_milo2, card_stanley]


### Unlocked cards are the cards that are available to the player and will be used to create the deckbuilder portion if deckbuilder is fully added 
default unlocked_cards = [card_goldie, card_Goldie2, card_milo, card_milo2, card_stanley]


### PLAYER Deck must hold 10 cards
default playerdeck = [card_goldie, card_Goldie2, card_milo, card_milo2, card_stanley]

####### Rulesets for later

#####    default card_rule_reverse = CardGameRule(name="Reverse", description="Instead of a higher number, you need to have the lowest number to take over a card.", icon="images/cardgame/rule_reverse.webp")
#####    default card_rule_hidden = CardGameRule(name="Hidden", description="The hidden rule means that a certain amount of cards in your enemies deck will be hidden.", icon="images/cardgame/rule_hidden.webp")

default cards_basic = [card_monster, card_chicken, card_snail, card_fireball, card_bird]

default cards_realm = [card_monster, card_chicken, card_snail, card_fireball, card_bird, card_goldie, card_Goldie2, card_milo, card_milo2, card_stanley, card_stanley2]

default cards_all = list(cards_realm) #+ list(insert card array here for more card types) 

default opponent_first_deck = [card_monster.clone(), card_chicken.clone(), card_snail.clone(), card_fireball.clone(), card_bird.clone()]



init python:
    def card_exist(unlockedlist, cardobj):
        for elm in unlockedlist:
                if cardobj.title == elm.title:
                    return True
        return False
    replace_index = 0
    new_deck = []
    def create_random_deck(min, max, card_pool):
        new_deck = []
        smalles_func = lambda elm1, elm2 : elm1.get_total_value() > elm2.get_total_value()
        gretest_func = lambda elm1, elm2 : elm1.get_total_value() < elm2.get_total_value()
        temp_pool = []
        temp_pool.extend(card_pool)
        for card in range(0,5):
            random_choice = renpy.random.choice(temp_pool)

            new_deck.append(random_choice)
            del temp_pool[temp_pool.index(random_choice)]

        while min > get_deck_score(new_deck) or max < get_deck_score(new_deck):
            replace_index = 0
            if get_deck_score(new_deck) < min:
                replace_index = find_index_func(temp_pool, smalles_func)
            else:
                replace_index = find_index_func(temp_pool, gretest_func)


            replace_index = clamp(replace_index,0,4)
            random_choice = renpy.random.choice(temp_pool)

            temp_pool.append(new_deck[replace_index])
            new_deck[replace_index] = (random_choice)
            del temp_pool[temp_pool.index(random_choice)]

        return new_deck
    def find_index_func(seq, func):
        func_index = 0
        for i in range(0, len(seq)):
            if func(seq[func_index], seq[i]):
                func_index = i
        return func_index

    def get_deck_score(deck):
        score = 0
        for card in deck:
            score += card.get_total_value()
        return score

    def get_image_size(image):
        myDisplayable = im.Image(image)
        myRender = renpy.render(myDisplayable, 800, 600, 0, 0)
        sizes = myRender.get_size()
        x = sizes[0]
        y = sizes[1]

        return (x,y)

    def get_hex_string(red, green, blue, alpha=1.0):
        red = str(hex( int( math.ceil( red*255))))[2:]
        if not len(red) == 2:
            red = "0"+red
        green = str(hex(int(math.ceil( green * 255))))[2:]
        if not len(green) == 2:
            green = "0"+green
        blue = str(hex(int(math.ceil( blue * 255))))[2:]
        if not len(blue) == 2:
            blue = "0"+blue
        alpha = str(hex(int(math.ceil( alpha * 255))))[2:]
        if not len(alpha) == 2:
            alpha = "0"+alpha

        return "#" + red + green + blue + alpha

    def get_hex_string_tuple(color):
        return get_hex_string(color[0], color[1], color[2], color[3])

    def get_rgb_tuple(hex):
        rgb = get_rgb_list(hex)
        return tuple(rgb)

    def get_rgb_list(hex):
        hex = hex.lstrip('#')
        hex_len = len(hex)
        rgb = list(int(hex[i:i + hex_len // 3], 16) for i in range(0, hex_len, hex_len // 3))
        if len(rgb) < 4:
            rgb.append(255) # Add alpha
        return rgb

    def get_width(image):
        return get_image_size(image)[0]

    def get_height(image):
        return get_image_size(image)[1]

    def reset_table_cards():
        global table_cards

        for y in range(0,3):
            for x in range(0,3):
                table_cards[x][y] = None
        return

    def check_winner(player_deck):
        global table_cards
        playerpoints = len(player_deck)

        for y in range(0,3):
            for x in range(0,3):
                if table_cards[x][y] and table_cards[x][y].playercard:
                    playerpoints += 1
        if playerpoints > 5:
            return "win"
        elif playerpoints == 5:
            return "draw"
        else:
            return "loss"

    def update_table(x, y, reverse, dobelt_number):
        global table_cards
        if reverse:
            take_over = lambda a, b : a < b
        else:
            take_over = lambda a, b : a > b


        if not y == 0 and not table_cards[x][y-1] == None and take_over(table_cards[x][y].topvalue, table_cards[x][y-1].bottomvalue):
            table_cards[x][y-1].playercard = table_cards[x][y].playercard

        if not y == 2 and not table_cards[x][y+1] == None and take_over(table_cards[x][y].bottomvalue, table_cards[x][y+1].topvalue):
            table_cards[x][y+1].playercard = table_cards[x][y].playercard

        if not x == 0 and not table_cards[x-1][y] == None and take_over(table_cards[x][y].leftvalue, table_cards[x-1][y].rightvalue):
            table_cards[x-1][y].playercard = table_cards[x][y].playercard

        if not x == 2 and not table_cards[x+1][y] == None and take_over(table_cards[x][y].rightvalue, table_cards[x+1][y].leftvalue):
            table_cards[x+1][y].playercard = table_cards[x][y].playercard

        if dobelt_number:
            dobelt_found = []
            if not y == 0 and not table_cards[x][y-1] == None:
                if table_cards[x][y].topvalue == table_cards[x][y-1].bottomvalue:
                    dobelt_found.append([x,y-1])

            if not y == 2 and not table_cards[x][y+1] == None:
                if table_cards[x][y].bottomvalue == table_cards[x][y+1].topvalue:
                    dobelt_found.append([x,y+1])

            if not x == 0 and not table_cards[x-1][y] == None:
                if table_cards[x][y].leftvalue == table_cards[x-1][y].rightvalue:
                    dobelt_found.append([x-1,y])


            if not x == 2 and not table_cards[x+1][y] == None:
                if table_cards[x][y].rightvalue == table_cards[x+1][y].leftvalue:
                    dobelt_found.append([x+1,y])

            if len(dobelt_found) > 1:
                for card in dobelt_found:
                    table_cards[card[0]][card[1]].playercard = table_cards[x][y].playercard


################################################################################################

        ### ADD FUNCTION TO SEND CURRENT TABLE TO SERVER HERE ####
        ## Potentially Mirror code to ensure that the server has the correct values
        #    def table_push(ip, player_id, player_name):
        #    try:
        #        data = {
        #            "player_id": player_id,
        #            "player_name": player_name
        #        }
        #        response = requests.post(f"http://{ip}/register", json=data)
        #        return response.status_code == 200
        #    except:
        #        return False
import json
import requests  # Assuming you will use requests for POST requests (if not using Socket.IO for all communication)

# Function to send game state to the server
def table_push(ip, player_id, player_name, player_hand, current_turn, player_score):
    try:
        # Define the game state data to be sent to the server
        game_state = {
            "player_id": player_id,  # Player's ID
            "player_name": player_name,  # Player's Name
            "cards_in_hand": [card.to_dict() for card in player_hand],  # Cards in hand
            "current_turn": current_turn,  # Whose turn it is
            "score": player_score  # Current score
        }

        # Send the game state to the server via POST request
        response = requests.post(f"http://{ip}/register", json=game_state)

        # Check if the request was successful
        if response.status_code == 200:
            print("Game state successfully sent to the server.")
            return True
        else:
            print(f"Failed to send game state: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error while sending game state: {e}")
        return False

# Fallback function for local mode
def initialize_local_game_data():
    # Placeholder function for local mode (you can replace with your actual local setup)
    print("Initializing local game data...")
    return {"player_hand": [], "current_turn": None, "player_score": 0}

# Example of how to use this function in your game logic
def card_game_init():
    player_id = 1  # Example player ID
    player_name = "Player1"  # Example player name
    player_hand = []  # Example player hand (replace with actual data)
    current_turn = 1  # Example current turn
    player_score = 100  # Example score

    # Server IP - use the correct IP address of your server
    server_ip = "127.0.0.1"  # Assuming the server is running locally for now

    # Call the table_push function to send the game state
    success = table_push(server_ip, player_id, player_name, player_hand, current_turn, player_score)

    if not success:
        print("Failed to push data to the server. Running in local mode.")
        local_game_data = initialize_local_game_data()  # Assuming you have this function
        print("Running in local mode.")

# Running the initialization
card_game_init()

################################################################################################


    def add_card_to_deck(title):
            for card in unlocked_cards:
                if title == card.title:
                    card.copies += 1

    class CardGameRule(object):
        def __init__(self, **kwargs):
            self.name = None
            self.description = None
            self.icon = None
            self.__dict__.update(**kwargs)

    class Card(object):
        sizes = (320, 480)

        def __init__(self, **kwargs):
            self.playercard = True
            self.textcolor = "{color=#ffffff}"
            self.copies = 0
            self.description = "Description"
            self.title = "Title"
            self.imagepath = "images/cards/card.webp"
            self.backside = "images/cards/start.jpeg"

            self.topvalue = 0
            self.bottomvalue = 1
            self.rightvalue = 2
            self.leftvalue = 3
            self.__dict__.update(**kwargs)

        def get_image(self, backside=False):
            return self.backside if backside else self.imagepath

        ######Border Finally working!



        def get_border(self):
            if self.playercard:
                return Transform("images/cards/border.webp", matrixcolor=TintMatrix(playercolor_rgb))
            return Transform("images/cards/border.webp", matrixcolor=TintMatrix(enemycolor_rgb))

        def get_title(self):
            return self.textcolor+self.title+"{/color}"
        def get_amount(self):
            return self.textcolor+"amount: " + str(self.copies+1)+"{/color}"
        def get_totalvalue(self):
            return self.textcolor+str(self.topvalue+self.bottomvalue+self.leftvalue+self.rightvalue)+"{/color}"
        def get_total_value(self):
            return self.topvalue+self.bottomvalue+self.leftvalue+self.rightvalue

        def get_description(self):
            return self.textcolor+self.description+"{/color}"

        def clone(self):
            return Card(title = self.title,imagepath=self.imagepath, topvalue=self.topvalue, bottomvalue=self.bottomvalue, rightvalue=self.rightvalue, leftvalue=self.leftvalue, playercard = self.playercard)

        def get_ai_score(self, table_of_cards, reverse, dobelt_number):
            high_score = -1000
            position = (0,0)
            wallscore = 3
            getcardscore = 12
            if reverse:
                score_func = lambda a : 10 - a
                take_over = lambda a, b : a < b
            else:
                score_func = lambda a : a
                take_over = lambda a, b : a > b

            for y in range(0,3):
                for x in range(0,3):
                    score = 0
                    if table_cards[x][y] == None:
                        if not y == 0 and not table_cards[x][y-1] == None and table_cards[x][y-1].playercard:
                            if take_over(self.topvalue, table_cards[x][y-1].bottomvalue):
                                score += getcardscore
                            else:
                                score += score_func(self.topvalue)
                        else:
                            score += wallscore

                        if not y == 2 and not table_cards[x][y+1] == None and table_cards[x][y+1].playercard:
                            if take_over(self.bottomvalue, table_cards[x][y+1].topvalue):
                                score += getcardscore
                            else:
                                score += score_func(self.bottomvalue)
                        else:
                            score += wallscore

                        if not x == 0 and not table_cards[x-1][y] == None and table_cards[x-1][y].playercard:
                            if take_over(self.leftvalue, table_cards[x-1][y].rightvalue):
                                score += getcardscore
                            else:
                                score += score_func(self.leftvalue)
                        else:
                            score += wallscore

                        if not x == 2 and not table_cards[x+1][y] == None and table_cards[x+1][y].playercard:
                            if take_over(self.rightvalue, table_cards[x+1][y].leftvalue):
                                score += getcardscore
                            else:
                                score += score_func(self.rightvalue)
                        else:
                            score += wallscore

                        if dobelt_number:
                            dobelt_found = []
                            if not y == 0 and not table_cards[x][y-1] == None:
                                if self.topvalue == table_cards[x][y-1].bottomvalue:
                                    dobelt_found.append(table_cards[x][y-1])

                            if not y == 2 and not table_cards[x][y+1] == None:
                                if self.bottomvalue == table_cards[x][y+1].topvalue:
                                    dobelt_found.append(table_cards[x][y+1])

                            if not x == 0 and not table_cards[x-1][y] == None:
                                if self.leftvalue == table_cards[x-1][y].rightvalue:
                                    dobelt_found.append(table_cards[x-1][y])


                            if not x == 2 and not table_cards[x+1][y] == None:
                                if self.rightvalue == table_cards[x+1][y].leftvalue:
                                    dobelt_found.append(table_cards[x+1][y])

                            if len(dobelt_found) > 1:
                                for card in dobelt_found:
                                    if card.playercard:
                                        high_score += getcardscore

                        if score > high_score:
                            high_score = score
                            position = (x, y)


            return [high_score, position]
