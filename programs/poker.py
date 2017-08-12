

#  GIVENS
#  ------
#
#  1. You are given a deck of 50 cards that has numbered 
#     cards with ranks from 1 to 10 (5 of each card.)
#


#  2. A poker game is played using this deck between two
#     players.  Each poker hand will consist of 4 cards. 
#
#     The following are possible poker hands:
# 
#     - High card       - [4, 6, 9, 3] 4  9 is the high card . 
#     - One pair        - [2, 2, 7, 9] 3  Pair of 2's  [9, 7]
#     - Two pairs       - [5, 4, 5, 4] 2  Pair of 5's , pair of 4's 
#     - Three of a kind - [8, 8, 8, 1] 2  Three 8's  [1,]  
#     - Four of a kind  - [9, 9, 9, 9] 1  Four 9's 
#
#     If two hands are equal in terms of the above high-level poker hands,
#     then the remaining cards will dictate the winner.

#     [ 6, 6, 5, 3] = One pair [5, 3]
#     [ 6, 6, 9, 3] = One pair [9, 3]  --> Winner. 
#
#     For example, 3656 vs 6693.  Both hands have a single pair of 6's.
#     However, after the pair of 6's, we have the first hand with a 53 and
#     the second hand with a 93, thus the second hand is the winner.
#
#     If there are any questions regarding how hands should be compared,
#     please consult with the moderator.
#
#
#  CHALLENGE
#  ---------
#
#  Your challenge is to create a poker simulator, that will deal

#  hands to the two players from the deck and will determine which
#  player is the winner.
#
#  ADDITIONAL COMPARISON EXAMPLES
#  ------------------------------
#
#  4249 >  3132
#  4446 <  5553
#  4554 == 5544
#  9911 >  8877
#
import random
from random import shuffle

def card_generator():
    return [(x%10)+1for x in range(50)]
        
def shuffle_cards(cards=[]):
    shuffle(cards)

def find_hand_type(cards=[]):
    d_card={}
    for c in cards:
        if c not in d_card:
            d_card[c]=1
        else:
            d_card[c]+=1
    return {"type":sorted(d_card.values()),"skeys": sorted(d_card.items(), key=lambda tup: -tup[1])}

def compare_hands(hand_type_1={}, hand_type_2={}):
    if hand_type_1["type"] > hand_type_2["type"]:
        return ">"
    elif hand_type_1["type"] < hand_type_2["type"]:
        return "<"
    else:
        h_1= hand_type_1["skeys"]
        h_2= hand_type_2["skeys"]
        if h_1 > h_2:
            return ">"
        elif h_1 < h_2:
            return "<"
        else:
            return "="

def get_hand(cards=[], times=4):
    return [cards.pop() for x in range(times)]
        
def result_interpreter(logic, hand_1, hand_2):
    print " {0} {1} {2}".format(logic, hand_1, hand_2)

def simulator():
    cards=card_generator()
    shuffle_cards(cards)
    hand_1=get_hand(cards)
    hand_2=get_hand(cards)
    logic = compare_hands(find_hand_type(hand_1), find_hand_type(hand_2))
    result_interpreter(logic, hand_1, hand_2)

simulator()