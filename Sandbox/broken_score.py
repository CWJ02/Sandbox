import random
def main():
    score = float(input("Enter score: "))
    print(determine_status(score))

    random_score_result = random.randint(0,100)
    print("Random score: ",random_score_result)
    print(determine_status(random_score_result))

def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def determine_status(random_score_result):
    if random_score_result < 0 or random_score_result > 100:
        return "Invalid score"
    elif random_score_result >= 90:
        return "Excellent"
    elif random_score_result >= 50:
        return "Passable"
    else:
        return "Bad"

main()

