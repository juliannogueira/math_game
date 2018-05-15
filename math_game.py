#This initial block of code simply asks the user if she or he likes math. The answer will dictate whether to continue the program
#or not.

while True:

    print('Hello! Do you like math?')
    answer_one = input()

    if answer_one == 'YES' or answer_one == 'Yes' or answer_one == 'yes':
        print('Awesome! I will give you a fun math quiz!\nIt will consist of (3) questions')
        break

    elif answer_one == 'NO' or answer_one == 'No' or answer_one == 'no':
        print('Okay! Have a nice day! Enter anything to quit.')
        input()
        exit()

    else:
        print('I did not quite understand that! Forgive me! Please enter \'yes\' or \'no\'.')
