#This initial block of code simply asks the user if she or he likes math. The answer will dictate whether to continue the program
#or not.

while True:

    print('Hello! Do you like math?')
    answer_one = input()

    if answer_one == 'YES' or answer_one == 'Yes' or answer_one == 'yes':
        print('\nAwesome! I will give you a fun math quiz!\nIt will consist of (3) questions')
        break

    elif answer_one == 'NO' or answer_one == 'No' or answer_one == 'no':
        print('Okay! Have a nice day! Enter anything to quit.')
        input()
        exit()

    else:
        print('I did not quite understand that! Forgive me! Please enter \'yes\' or \'no\'.')




#The next block of code will hold the first math question.

print('You will only be given (1) chance to get each question correct. So, just answer correctly.\n')

print('Here is the first question: ', end = '')
print('What is 2 + 2? Please enter a number.')
answer_two = input()

if answer_two == '4':
    print('You got it!')

else:
    print('\nThat is incorrect.')
    print('Program is being terminated in...')
    for counter in range(1, 7):
        print(6 - counter)
    print('Goodbye.')
    exit()
    