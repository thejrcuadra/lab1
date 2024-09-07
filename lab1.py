def main():    
    print('''What simple mathematic operation would you like to do?
        
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division''')

    choice = int(input('> '))
    while choice > 4 or choice < 1:
        choice = int(input('Enter a valid choice'))

    print('Enter your first number.')
    num1 = int(input("> "))
    print('Enter your second number.')
    num2 = int(input('> '))

    if choice == 1:
        num3 = num1 + num2
        print(num1, ' + ', num2, ' = ', num3)
    elif choice == 2:
        num3 = num1 - num2
        print(num1, ' - ', num2, ' = ', num3)
    elif choice == 3:
        num3 = num1 * num2
        print(num1, ' * ', num2, ' = ', num3)
    else:
        num3 = num1 / num2
        print(num1, ' / ', num2, ' = ', num3)

clear = 'c'
while clear.lower() == 'c':
    main()
    clear = input('Enter [c] to clear and rerun program')


# I want you to see how I initially went about this prompt.
# I initially tackled that prompt as the user only having one input
# for the entire mathematical operation having (3 + 7) as an input, for example.
# Me over-complicating things will be a common thread during the semester :) 


#def main():
#    print('This is a calculator simulator. Input a simple operation as you would with a calculator.')
#    userInput = input('> ')
#    userInput = validation(userInput)
#    while userInput == 'ERROR':
#        print('An error has been found. Please enter a valid input.')
#        userInput = input('> ')
#        userInput = validation(userInput)
#    i = 0
#    if '+' in userInput:
#        for x in userInput:
#            if

#def validation(uI):
#    validCharacters = ['+', '-', '*', '/']
#    index = 0
#    for x in uI:
#        if uI[index].isdigit() or uI[index] in validCharacters or uI[index].isspace():
#            index += 1
#            continue
#        elif uI[index] not in validCharacters:
#            return 'ERROR'
#        elif uI == '':
#            return 'ERROR'
#        else:
#            return 'ERROR'

#    return uI
        

#yes = 'y'
#while yes.lower() == 'y':
#    main()
#    yes = input('Enter [y] to rerun program.')