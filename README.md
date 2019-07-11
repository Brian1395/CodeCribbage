# Cribbage
This is a game where 2 people code players to play against each other in a simulated game of cribbage

How to play:
Each player makes 2 functions named "deckProcess" and "playCard" and puts them in a .py file titled player1 or player2

deckProcess:
    is passed(crib,                 hand,       your pts,   opponent pts)
             (bool(true if yours),  array(6),   int,        int)
    returns(cards to put in crib)
           (array(2))
            
playCard:
    is passed(hand,         played cards,   your pts,   opponent pts)
             (array(1-4),   array(0-7),     int,        int)          
    returns(card to play)
           (str)

All cards are sent in the format:
    str[0] = char that says suit:
        D = Diamonds
        H = Hearts
        S = Spades
        C = Clubs
    str[1,len(str) - 1] = int that says value:
        0 = KING
        1 = ACE
        2-10 = Card according to value
        11 = JACK
        12 = QUEEN
