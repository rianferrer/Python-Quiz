#Ferrer, Marion Caryl R.
#3ITD
#IT ELEC2C - PRELIM - MA 2 - FUNCTION

from random import sample
import sys


def quiz_remarks(right_ans):
    if (right_ans < 1):
        return 'U It\'s time to think of what should be your priority.'
    elif (0 < right_ans < 2):
        return 'F It won\'t bite you if you take interest in learning the course.'
    elif (1 < right_ans < 4):
        return 'D You fail! Exert effort in your studies.'
    elif (3 < right_ans < 6):
        return 'C+ Satisfactory, at least'
    elif (5 < right_ans < 8):
        return 'B+ Very Good, aim higher!'
    elif (7 < right_ans < 9):
        return 'A+ Excellent! Keep up the good work.'
    
def compute_score():
    print('Welcome to ITELEC2C Quiz.')
    print('This quiz has 8 questions and are answerable only by true or false.')
    print('Answer the questions by typing T or F ONLY.')

    Qs = ['\nPython is a high-level programming language. ',
          '\nPython is not case-sensitive. ',
          '\nComments in Python starts with asterisk (*). ',
          '\nUsers can do multiple assignments in Python. ',
          '\ncomplex is a Text data type. ',
          '\nisLower() method returns a lowercased string. ',
          '\nupper() method returns a uppercased string. ',
          '\nYou don\'t need to import a method to use it. '
          ]
          
    As= ['T',
         'F',
         'F',
         'T',
         'F',
         'F',
         'T',
         'F'
         ]

    #initialize right_ans
    right_ans = 0
    #randomize the list by zip method
    value = list(zip(Qs, As))
    #shows 8 questions
    score = sample(value, 8)

    #for loop for questions + score with try/except and nested if-else
    for i in score:
        print(i[0])
        try:
            while True:
                user_answer = input('Answer (T/F): ')
                if user_answer.isalpha():
                    if user_answer.lower() == i[1].lower():
                        right_ans += 1
                        print('Correct answer.', right_ans, ' point/s')
                        break
                    else:
                        print('Wrong answer.', right_ans, ' point/s')
                        break
                else:
                    print('Enter correct value! T or F only.')
                    user_answer
        except Exception as e:
            print(e)

    #prints the score & remarks of the user
    remarks = quiz_remarks(right_ans)
    print('\n{}/8 correct answers'.format(right_ans))
    print(remarks)

compute_score()


while True:
    try_again = input('Retake the test? Y/N: ')
    
    if try_again == 'Y':
        compute_score()
    elif try_again == 'N':
        print('\nHope you had fun with answering the test.')
        print('Made by: Ferrer, Marion Caryl R. | 3ITD')
        sys.exit()
    else:
        try_again
