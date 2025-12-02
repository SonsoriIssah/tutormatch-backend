name = input('What is your name: ').title()
print()


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
final_score = score_master()
if final_score >= 2:
    print(f'{name}, you pass with {final_score} marks')
else:
    print(f'{name}, you fail with {final_score} marks')

