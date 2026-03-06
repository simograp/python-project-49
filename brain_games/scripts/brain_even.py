import prompt
import random
print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')
print('Answer "yes" if the number is even, otherwise answer "no".')
count = 3
while count > 0:
    number = random.randint(1, 100)
    print('Question: ',number)
    answer = ''
    your_answer = ''
    if number%2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    print('Your answer: ', your_answer)
    your_answer = input()
    if your_answer == answer:
        print('Correct!')
        count = count - 1
    else:
        print(f'{your_answer} is wrong answer ;(. Correct answer was {answer}')
        print(f'Let\'s try again, {name}')
        count = 3
print(f'Congratulations, {name}')
