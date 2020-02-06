

#TESTNG FOR SIMPLE CALCULATION
'''num1 = int(input('Enter first number: '))
operator = input(Please type operation you would like to complete:
        + for addition
        - for subtraction
        * for multiplication
        / for division
        = for result
        )
num2 = int(input('Enter second number: '))
        
def operation():
    if operator == '+':
        print('{} + {} = '.format(num1, num2), end = ' ')
        print(num1 + num2)
        
    elif operator == '-':
        print('{} - {} = '.format(num1, num2), end='')
        result = num1 - num2
        return result
        
    elif operator == '*':
        result = '{} * {} ='.format(num1, num2)
        return result

        
    elif operator == '/':
        return '{} / {} = '.format(num1, num2)

    else:
        print('Type a valid operator.')
    

if __name__ == '__main__':
    math = operation()
    print(math, end='')'''


#PROMPT FOR CALCULTE AGAIN 
from calculator import operation

Again = input('''Do you want to calculate again: 
        y for yes
        n for no
        ''')

def again(): 
    if Again == 'y':
        calculate_again = operation()
        return calculate_again
    
    else:
        print('Goodbye')

if __name__ == '__main__':
    again()



