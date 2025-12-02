names = []
name = 'What is your name '
names.append(name)





quiz = [
    "What is the capital of France? ",
    "How many continents are there? ",
    "What color do you get when you mix red and white? "
]

answers = ['Paris', '7','Pink']
def score_master():
    score = 0
    for q in range(len(quiz)):
        print(quiz[q])
        answer = input()
        
        if answer.title() == answers[q]:
                print('Right answer')
                print()
                score += 1
                continue
        else:
                print('Wrong answer')
                continue
    return score

print(score_master())


