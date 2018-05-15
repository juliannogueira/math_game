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
    answer_one = input()

    if answer_one == 'YES' or answer_one == 'Yes' or answer_one == 'yes':
        print('\nAwesome! I will give you a fun math quiz!\nIt consists of (3) questions.')
        break

    elif answer_one == 'NO' or answer_one == 'No' or answer_one == 'no':
        print('Okay! Have a nice day! Enter anything to quit.')
        input()
        exit()

    else:
        print('I did not quite understand that! Forgive me! Please enter \'yes\' or \'no\'.')




#The next block of code will hold the first math question.

print('You are only given (1) chance to answer each question correctly. So, just get it right.')

print('\nHere is the first question: ', end = '')
print('What is 2 + 2 ? Please enter a number.')
answer_two = input()

if answer_two == '4':
    print('You got it! Amazing!')

else:
    terminator()




#This block of code holds the second math question.

print('\nHere is the next question: ', end = '')
print('What is ((4*2) + 8)/4 ? Please enter a number.')
answer_three = input()

if answer_three == '4':
    print('It is true! You do like math!')
else:
    terminator()




#Here is the third and final question.

print('\nHere is the final question: ', end = '')
print('How do you spell \'4\' ? Please use capital letters.')
answer_four = input()

if answer_four == 'FOUR':
    print('Wow! You did fantastic!')
    print('\nEnter anything to quit.')
    input()
    print('Goodbye.')
    exit()

elif answer_four == 'Four' or answer_four == 'four':
    print('You were so close, but so far...')
    terminator()

else:
    terminator()