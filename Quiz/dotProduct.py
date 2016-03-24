def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    dotProduct = 0
    for i in range(len(listA)):
        dotProduct += listA[i] * listB[i]
    return dotProduct 