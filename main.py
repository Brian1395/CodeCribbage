##Each player makes 2 functions named "deckProcess" and "playCard"
##and puts them in a .py file titled player1 or player2
##
##deckProcess:
##    is passed(crib,                 hand,       your pts,   opponent pts)
##             (bool(true if yours),  array(6),   int,        int)
##    returns(cards to put in crib)
##           (array(2))
##            
##playCard:
##    is passed(hand,         played cards,   your pts,   opponent pts)
##             (array(1-4),   array(0-7),     int,        int)          
##    returns(card to play)
##           (str)
##    OR returns "GO" if no card can be played
##
##All cards are sent in the format:
##    str[0] = char that says suit:
##        D = Diamonds
##        H = Hearts
##        S = Spades
##        C = Clubs
##    str[1,len(str) - 1] = int that says value:
##        0 = KING
##        1 = ACE
##        2-10 = Card according to value
##        11 = JACK
##        12 = QUEEN
        

import player1 as P1
import player2 as P2
import random
import copy

def cardPlayed(card,


games = 1
game = 0
while (game < games) :
    pts1 = 0
    pts2 = 0
    deck_b = []

    #Makes a deck
    i = 1
    while(i < 53): 
        if(i< 14):
              z = 'H' + str(i)
        elif(i< 27):
              z = 'S' + str(i - 13)
        elif(i< 40):
              z = 'D' + str(i - 26)
        elif(i< 53):
              z = 'C' + str(i - 39)
        deck_b.append(z)
        i += 1
        
    #Decides who starts crib
    start_plr = random.randint(1,2)
    plr1_crib = True #These will get inverted anyways
    if (start_plr == 1):
        plr1_crib = False

    #Actual Rounds
    while((pts1 < 121) and (pts2<121)): 
        #Set-up
        plr1_crib = !plr1_crib #Other person has crib
        deck = copy.deepcopy(deck_b) #Makes a new deck so the base one isn't ruined
        player1_hand = []
        player2_hand = []

        #Deals hands
        for c in range(0,6):
            num = random.randint(0,len(deck)-1)
            player1_hand.append(deck[num])
            del deck[num]
        for c in range(0,6):
            num = random.randint(0,len(deck)-1)
            player2_hand.append(deck[num])
            del deck[num]

        crib1 = P1.deckProcess(plr1_crib,player1_hand,pts1,pts2)
        crib2 = P2.deckProcess(!plr1_crib,player2_hand,pts2,pts1)

        #TODO: Check for valid crib return
        
        #Processes crib
        crib = crib1 + crib2
        del player1_hand[crib1[0]]
        del player1_hand[crib1[1]]
        del player2_hand[crib2[0]]
        del player2_hand[crib2[1]]

        played_cards = []
        played_cards_tot = 0
        while(len(played_cards) < 8):
            if(plr1_crib):
                while(played_cards_tot < 31 and (card1 != "GO" and card2 != "GO")):
                   card2 = P2.playCard(player2_hand,played_cards,pts2,pts1)
                   if(card2 != "GO"):
                       played_cards.append(card2)
                       del player2_hand[card2]
                   if(card2 == "GO" and card1 == "GO"):  #This allows pts if player 1 called go last round
                       card2 == "NA"
                   card1 = P1.playCard(player1_hand,played_cards,pts1,pts2)
                   if(card1 != "GO"):
                       played_cards.append(card1)
                       del player1_hand[card1]
                if(played_cards_tot = 31):
                   if(card1 == "GO"):
                       pts2 += 2;
                   else:
                       pts1 += 2;
                else:
                   if(card2 == "GO"):
                       pts1 += 1;
                   else:
                       pts2 += 1;
            else:
                while(played_cards_tot < 31 and (card1 != "GO" and card2 != "GO")):
                   card1 = P1.playCard(player1_hand,played_cards,pts1,pts2)
                   if(card1 != "GO"):
                       played_cards.append(card1)
                       del player1_hand[card1]
                   if(card2 == "GO" and card1 == "GO"):  #This allows pts if player 2 called go last round
                       card1 == "NA"
                   card2 = P2.playCard(player2_hand,played_cards,pts2,pts1)
                   if(card2 != "GO"):
                       played_cards.append(card2)
                       del player2_hand[card2]
                if(played_cards_tot = 31):
                   if(card1 == "GO"):
                       pts2 += 2;
                   else:
                       pts1 += 2;
                else:
                   if(card1 == "GO"):
                       pts2 += 1;
                   else:
                       pts1 += 1;
        
        pts1 = 121 #Just here to end loop for testing purposes
    game += 1
