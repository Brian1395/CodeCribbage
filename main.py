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
##        1 = ACE
##        2-10 = Card according to value
##        11 = JACK
##        12 = QUEEN
##        13 = KING        

import player1 as P1
import player2 as P2
import random
import copy

def cardValue(card):
    val = int(card[1:len(card)])
    if(val > 10):
        return 10
    return val


def checkStraight(c): 
    nums = []
    straight_cards = 0
    fifteen_check = 0
    for x in c:
        nums.append(x[1:len(x)])
        fifteen_check += int(x[1:len(x)])

    if(fifteen_check == 15):
        straight_cards = 2
        
    try:
        if(abs(nums[-1] - nums[-2]) == 1):
            if((nums[-2] - nums[-3]) == (nums[-1] - nums[-2])):
                straight_cards += 3;
            else:
                return(straight_cards)
        else:
            return(straight_cards)
    except:
        return(straight_cards)

    i = 0
    while(i < len(nums) - 3):
        if((nums[-(i-1)] - nums[-i]) == (nums[-i] - nums[-(i+1)])):
            straight_cards += 1
        else:
            return(straight_cards)
                
    
    
def checkPTS(cards_played):
    pts = 0;
    try: #Could use ifs but I decided to spice things up a bit
        if(cards_played[-1] == cards_played[-2]):
            pts = 2;
    except:
        return(0)
    try:
        if((cards_played[-1] == cards_played[-2]) and (cards_played[-3] == cards_played[-2])):
            pts = 6
    except:
        for x in cards_played:
            fifteen_check += int(x[1:len(x)])
        if(fifteen_check == 15):
            pts += 2
        return(pts)

    stpts = checkStraight(cards_played)
    
    if(stpts > 0):
        pts = stpts
        return(pts)
    
    try:
        if((cards_played[-1] == cards_played[-2]) and (cards_played[-3] == cards_played[-2]) and (cards_played[-3] == cards_played[-4])):
            pts =12
    except:
        return(pts)
        
    return(0)

def countHand(hand):
    hand.append(turned_card)
    print(hand)
    nums = []
    pts = 0
    for x in hand:
        nums.append(int(x[1:len(x)]))

    #Pairs
    counted_nums = []
    for i in nums:      
        pairs = 0
        if i not in counted_nums:
            for u in nums:
                if(i == u):
                    pairs += 1
            if(pairs == 2):
                pts += 2
                counted_nums.append(i)
            elif(pairs == 3):
                pts += 8
                counted_nums.append(i)
            elif(pairs == 4):
                pts += 12
                counted_nums.append(i)
    #Straights
    straight_nums = sorted(nums)
    print(straight_nums)
    pos = 0
    for i in straight_nums:
        x = 0

        if(pos > 2):
            x = -1
        #print(x)

        double = 0
        while(x >= 0):
            
                
            if(straight_nums[x + 1 + pos] - straight_nums[x + pos] == 1):
                print(straight_nums[x + 1 + pos])
                print(straight_nums[x + pos])
                x += 1
            elif(straight_nums[x + 1 + pos] == straight_nums[x + pos]):
                double += 1
                x += 1
            else:
                if(x - double > 1):
                    print("Straight of %d cards" %(x+1 - double))
                    pts += (x+1 - double) * (double + 1)
                    pos = 100
                x = -1
            if(x >= 4 - pos):
                if(x - double > 1):
                    print("Straight of %d cards" %(x+1 - double))
                    pts += (x+1 - double) * (double + 1)
                    pos = 100
                x = -1
        pos += 1

    

    #Fifthteens (doesn't work yet)
##    for w in hand:
##        for h in hand:
##            if(cardValue(w) + cardValue(h) == 15):
##                pts += 2
##                print("15 with %s len 2" %w) 
##    for a in hand:
##        for b in hand:
##            for c in hand:
##                if(cardValue(a) + cardValue(b) + cardValue(c) == 15 and not (a == b or a == c or b == c)):
##                    pts += 2
##                    print("15 with %s %s len 3" %(a,b))
##    for a in hand:
##        for b in hand:
##            for c in hand:
##                for d in hand:
##                    if(cardValue(a) + cardValue(b) + cardValue(c) == 15 and not (a == b or a == c or a == d or b == c or b == d or c == d)):
##                        pts += 2
##                        print("15 with %s %s len 4" %(a,b))

    #Flush
    suit = hand[0][0]
    flush = True
    for s in hand:
        if(suit != s[0]):
            flush = False

    if flush:
        pts += 5

    elif(hand[0][0] == hand[1][0] == hand[2][0] == hand[3][0]):
        pts += 4

    print("Pts: ",pts)
    return(pts)          

##turned_card = "H5"
##hand = ["D3","D4","D5","D6"]
##countHand(hand)

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
        plr1_crib = not plr1_crib #Other person has crib
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
        crib2 = P2.deckProcess(not plr1_crib,player2_hand,pts2,pts1)
        
        #TODO: Check for valid crib return
        
        #Processes crib
        crib = crib1 + crib2
        print("CRIB: ", crib)
        del player1_hand[player1_hand.index(crib1[0])]
        del player1_hand[player1_hand.index(crib1[1])]
        del player2_hand[player2_hand.index(crib2[0])]
        del player2_hand[player2_hand.index(crib2[1])]

        #Flip card
        num = random.randint(0,len(deck)-1)
        turned_card = deck[num]
        
        if(turned_card[1:len(turned_card)] == 11): #Checks if Jack was flipped
            if(plr1_crib):
                pts1 += 2
            else:
                pts2 += 2

        #Actual card playing phase
        played_cards = []
        played_cards_tot = 0
        player1_counthand = copy.deepcopy(player1_hand)
        player2_counthand = copy.deepcopy(player2_hand)
        while((len(player1_hand) > 0 and len(player2_hand) > 0) and ((pts1 < 121) and (pts2<121))):
            card1 = "NA"
            card2 = "NA"
            if(plr1_crib):
                while(played_cards_tot < 31 and (card1 != "GO" and card2 != "GO")):
                    card2 = P2.playCard(player2_hand,played_cards,pts2,pts1)
                    if(card2 != "GO"):
                        played_cards.append(card2)
                        played_cards_tot += cardValue(card2)
                        del player2_hand[player2_hand.index(card2)]
                        pts2 += checkPTS(played_cards)
                    if(card2 == "GO" and card1 == "GO"):  #This allows pts if player 1 called go last round
                        card2 == "NA"
                    card1 = P1.playCard(player1_hand,played_cards,pts1,pts2)
                    if(card1 != "GO"):
                        played_cards.append(card1)
                        played_cards_tot += cardValue(card1)
                        del player1_hand[player1_hand.index(card1)]
                        pts1 += checkPTS(played_cards)
                    print(played_cards)
                    print(played_cards_tot)
                if(played_cards_tot == 31):
                    if(card1 == "GO"):
                       pts2 += 2
                       played_cards = []
                       played_cards_tot = 0
                    else:
                       pts1 += 2
                       played_cards = []
                       played_cards_tot = 0
                else:
                    if(card2 == "GO"):
                        pts1 += 1
                        played_cards = []
                        played_cards_tot = 0
                    else:
                        pts2 += 1
                        played_cards = []
                        played_cards_tot = 0
            else:
                while(played_cards_tot < 31 and (card1 != "GO" and card2 != "GO")):
                    card1 = P1.playCard(player1_hand,played_cards,pts1,pts2)
                    if(card1 != "GO"):
                        played_cards.append(card1)
                        played_cards_tot += cardValue(card1)
                        del player1_hand[player1_hand.index(card1)]
                        pts2 += checkPTS(played_cards)
                    if(card2 == "GO" and card1 == "GO"):  #This allows pts if player 2 called go last round
                       card1 == "NA"
                    card2 = P2.playCard(player2_hand,played_cards,pts2,pts1)
                    if(card2 != "GO"):
                        played_cards.append(card2)
                        played_cards_tot += cardValue(card2)
                        del player2_hand[player2_hand.index(card2)]
                        pts2 += checkPTS(played_cards)
                    print(played_cards)
                    print(played_cards_tot)
                if(played_cards_tot == 31):
                   if(card1 == "GO"):
                       pts2 += 2
                       played_cards = []
                       played_cards_tot = 0
                   else:
                       pts1 += 2
                       played_cards = []
                       played_cards_tot = 0
                else:
                   if(card1 == "GO"):
                       pts2 += 1
                       played_cards = []
                       played_cards_tot = 0
                   else:
                       pts1 += 1
                       played_cards = []
                       played_cards_tot = 0
            
            print("Pl: %d" %pts1)
            print("P2: %d" %pts2)
        if((pts1 < 121) and (pts2<121) and not plr1_crib):    
            pts1 += countHand(player1_counthand)
        elif((pts1 < 121) and (pts2<121)):
            pts2 += countHand(player2_counthand)
        if((pts1 < 121) and (pts2<121) and plr1_crib):    
            pts1 += countHand(player1_counthand)
            pts1 += countHand(crib)
        elif((pts1 < 121) and (pts2<121)):
            pts2 += countHand(player2_counthand)
            pts2 += countHand(crib)
        print("Pl: %d" %pts1)
        print("P2: %d" %pts2)
        #Checks pts in hands
##        if(plr1_crib):
            
            
        #pts1 = 121 #Just here to end loop for testing purposes
    game += 1
