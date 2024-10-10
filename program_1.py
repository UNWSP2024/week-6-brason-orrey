import random

def randDice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

def main():
    rolls = []
    for _ in range(100):
        rolls.append(randDice())
    
    average_roll = sum(rolls) / len(rolls)
    
    print(f"The average of 100 dice rolls is: {round(average_roll, 2)}")

main()
