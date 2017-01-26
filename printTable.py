def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in range (len(tableData)):
        for j in range (len(tableData[0])):
            if(len(tableData[i][j]) > colWidths[i]):
                colWidths[i] = len(tableData[i][j])
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(str(tableData[j][i]).rjust(colWidths[j]), end = ' ')
        print()
            
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
