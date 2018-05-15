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
print('What is 2 + 2? Please enter a number.')
answer_two = input()

if answer_two == '4':
    print('You got it!')

else:
    terminator()

    