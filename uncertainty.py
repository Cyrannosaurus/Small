import random as rand
from typing import Callable, List, Tuple
# An experiment of an alternative Monty Hall problem
# In this version, we are given two envelopes with two slips
# of paper in each. One piece of paper is desirable, say a
# lottery ticket, while the others are worthless.

# Assuming we are the player, we are allowed to pick and open
# one of the envelopes, taking out exactly one slip of paper.

# We are asked whether we would like to switch our envelope
# upon seeing a non-desirable slip, or stay with the one 
# we had originally picked.


def stubborn(envelopes:List[tuple], choice:int, known:bool) -> int:
    """ Always keep the originally chosen envelope """
    # Already by inspection the function seems non-ideal as it does not make use of all the 
    # information available to it. This is only true if the given information is relevant.
    return choice

def reactive(envelopes:List[tuple], choice:int, known:bool) -> int:
    """ Switch chosen envelopes if we see a non-goal slip """
    if known == False:
        choice = switch(choice)
    return choice


def check_strategy(trials:list, strategy:Callable[[List[tuple],int,bool],int]) -> Tuple[int,int]:
    """ Run a simulation of the given strategy """
    num_won = 0
    for _, envelopes in enumerate(trials):
        num_won += int(play(strategy, envelopes))
    return (num_won, len(trials) - num_won)

def play(strategy:Callable[[List[tuple],int,bool],int], envelopes:List[tuple]) -> bool:
    """ Play a single game using the given strategy """
    envelopes = prepare_envelopes()
    choice = pick(envelopes)
    known = peek(envelopes, choice)
    choice = strategy(envelopes=envelopes, choice=choice, known=known)
    outcome = check_won(envelopes, choice)
    return outcome


def prepare_envelopes() -> List[tuple]:
    """ Return a randomly generated set of envelopes """
    choices = [0,0,0]
    choices.insert(rand.randint(0,3), 1)
    slot_1 = choices.pop(rand.randint(0,3))
    slot_2 = choices.pop(rand.randint(0,2))
    slot_3 = choices.pop(rand.randint(0,1))
    slot_4 = choices.pop(0)
    return [(slot_1, slot_2), (slot_3, slot_4)]


def pick(envelopes:List[tuple]) -> int:
    """ Randomly pick a envelope from the given list """
    choice = rand.randint(0,1)
    return choice
    
# 
def peek(envelopes:List[tuple], choice:int) -> bool:
    """ Returns true if the peeked object is the goal """
    return bool(rand.choice(envelopes[choice]))

def switch(choice:int) -> int:
    """ Get the other envelopes index """
    return int(not bool(choice))

def check_won(envelopes:List[tuple], choice:int) -> bool:
    """ Check for the goal slip """
    return any(envelopes[choice])
## One way we determine possibilities is looking at the past frequency
## How else can we determine possibilities?

def simulate(trials:int) -> None:
    ## Swap out reactive and stubborn to see how they compare
    envelopes = list()
    for i in range(trials):
        envelopes.append(prepare_envelopes())
    
    outcome = check_strategy(envelopes, reactive)
    print(f'The outcome for a reactive playstyle was {outcome[0]} wins and {outcome[1]} losses.')
    win_percent = (outcome[0] * 100) / trials
    print(f'This comes to a winning percentage of {win_percent:.2f}%.')
    print()
    outcome = check_strategy(envelopes, stubborn)
    print(f'The outcome for a stubborn playstyle was {outcome[0]} wins and {outcome[1]} losses.')
    win_percent = (outcome[0] * 100) / trials
    print(f'This comes to a winning percentage of {win_percent:.2f}%.')

if __name__ == '__main__':
    simulate(100000)
