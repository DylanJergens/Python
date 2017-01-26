def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(str(number))
    else:
        number = (3 * number) + 1
    return number

def output():
    print ('Please enter a number.')
    value = int(input())
    num = collatz(value)
    while num != 1:
        num = collatz(num)
    print('The preceding numbers are the collatz sequence for ' + str(value))
    print('Would you like to try another integer?')
    print('Type y/n:')
    answer = input()
    while answer != 'y' and answer != 'n':
        print('Type y/n:')
        answer = input()
    if answer == 'n':
        print('Thanks for playing')
    return answer
    
print('This program runs the collatz sequence on a given number.')    
answer2 = output()
while(answer2 == 'y'):
    answer2 = output()

    
    


