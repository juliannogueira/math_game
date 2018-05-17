#These variables will hold the math questions.
question_one = 'What is 2 + 2 ? Please enter a number.'

question_two = 'What is ((4*2) + 8)/4 ? Please enter a number.'

question_three = 'How do you spell \'4\' ? Please use capital letters.'




#This function will be used to terminate the program if a user answers a question incorrectly.

def terminator():
    print('\nThat is incorrect.')
    print('The program will be terminated in:')
    for counter in range(1,7):
        print('...' + str(6 - counter))
    print('Goodbye.')
    exit()




#This initial block of code simply asks the user if she or he likes math. The answer will dictate whether to continue the program
#or not.

print('Hello! Do you like math?')

while True:
    like_math = input()

    if like_math == 'YES' or like_math == 'Yes' or like_math == 'yes':
        print('\nAwesome! I will give you a fun math quiz!\nIt consists of (3) questions.')
        break

    elif like_math == 'NO' or like_math == 'No' or like_math == 'no':
        print('Okay! Have a nice day! Enter anything to quit.')
        input()
        exit()

    else:
        print('I did not quite understand that! Forgive me! Please enter \'yes\' or \'no\'.')




#The next block of code will hold the first math question.

print('You are only given (1) chance to answer each question correctly. So, just get it right.')

print('\nHere is the first question: ', end = '')
print(question_one)
answer_one = input()

if answer_one == '4':
    print('You got it! Amazing!')

else:
    terminator()




#This block of code holds the second math question.

print('\nHere is the next question: ', end = '')
print(question_two)
answer_two = input()

if answer_two == '4':
    print('It is true! You do like math!')
else:
    terminator()




#Here is the third and final question.

print('\nHere is the final question: ', end = '')
print(question_three)
answer_three = input()

if answer_three == 'FOUR':
    print('Wow! You did fantastic!')
    print('\nEnter anything to quit.')
    input()
    print('Goodbye.')
    exit()

elif answer_three == 'Four' or answer_three == 'four':
    print('You were so close, but so far...')
    terminator()

else:
    terminator()