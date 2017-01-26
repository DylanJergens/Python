def printList(value):
    print(value[0], end='')
    for i in range (1, len(value)):
        if i == (len(value) - 1):
          print(', and ' + value[i])
        else :
            print(', ' + value[i], end = '')

spam = ['apples', 'bananas', 'tofu', 'cats']
printList(spam)

          
        
