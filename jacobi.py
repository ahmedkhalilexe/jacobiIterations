import numpy as np
def Jacobi():
    #Jacobi iterations main function
    matrixA = getMatrixA()
    n = np.size(matrixA, 0)
    vecterB = getVecterB(n)
    toelrence = float(input('Enter the tolerance: '))
    maxIterations = int(input('Enter the maximum number of iterations: '))
    x = np.zeros(n, dtype=float)
    xPrime = np.zeros(n, dtype=float)
    iterations = 0
    #check if matrix is diagonally dominant
    if checkDiagDom(matrixA) == False:
        #make the matrix diagonally dominant
        matrixA, vecterB = makeDiagDom(matrixA, vecterB)
    #looping through the iterations
    while iterations < maxIterations:
        #looping throgth the rows
        for i in range(n):
            sum = 0
            #looping through the columns
            for j in range(n):
                #checks if we are not in a diagonal element
                if j != i:
                    #calculate the sum of the elements Ai,j * Xj
                    sum = sum + matrixA[i, j] * x[j]
            #calculate the new value of Xi Bi - sum / Aii (diagonal element)
            xPrime[i] = (vecterB[i] - sum) / matrixA[i, i]
        #check if the new solution is within the tolerance
        if np.linalg.norm(xPrime - x) < toelrence:
            #print the solution
            printSolution(xPrime)
            return 
        #update the solution for next iteration
        x = xPrime.copy()
        iterations = iterations + 1
    #no solution found within the maximum number of iterations
    print('No solution found within the maximum number of iterations.')
    printSolution(xPrime)
    return

def checkDiagDom(matrixA):
    n = len(matrixA)
    #looping through the rows
    for i in range(n):
        sum = 0
        #looping through the columns
        for j in range(n):
            #checks if we are not in a diagonal element
            if j != i:
                #calculate the sum of the absulote elements Ai,j
                sum = sum + abs(matrixA[i, j])
        #checks if the diagonal element is less than the sum of the absulote elements
        if abs(matrixA[i, i]) < sum:
            print('Matrix is not diagonally dominant.')
            return False
    return True

def makeDiagDom(matrixA, vecterB):
    n = len(matrixA)
    tempMatrix = []
    tempVector = []
    for i in range(n):
        maxIndexInRow = getMaxIndexInRow(matrixA[i])
        if maxIndexInRow != i:
            tempMatrix = np.copy(matrixA[i])
            tempVector = np.copy(vecterB[i])
            matrixA[i] = np.copy(matrixA[maxIndexInRow])
            vecterB[i] = np.copy(vecterB[maxIndexInRow])
            matrixA[maxIndexInRow] = tempMatrix.copy()
            vecterB[maxIndexInRow] = tempVector.copy()
    print("new matrix: ", matrixA)
    print("new b is: ", vecterB)
    return matrixA, vecterB

def getMaxIndexInRow(row):
    n = len(row)
    maxValueIndex = 0
    for i in range(n):
        sum = 0
        for j in range(n):
            if j != i:
                #calculate the sum of the absulote elements Ai,j
                sum = sum + abs(row[j])
        if abs(row[i]) > sum:
            maxValueIndex = i
    return maxValueIndex

def printSolution(x):
    n = len(x)
    #looping through the solution x = [x1,x2,...,xn]
    for i in range(n):
        print('x' + str(i + 1) + ' = ' + str(x[i]))

def getMatrixA():
    n = int(input('Enter the size of the matrix: '))
    matrixA = np.zeros((n, n), dtype=float)
    #looping through the rows
    for i in range(n):
        #looping through the columns
        for j in range(n):
            #gets input from the user for each element
            matrixA[i, j] = input('Enter a' + str(i + 1) + str(j + 1) + ': ')
    return matrixA

def getVecterB(n):
    vecterB = np.zeros(n, dtype=float)
    #looping through the vecterB B=[b1,b2,...,bn]
    for i in range(n):
        #gets input from the user for each element
        vecterB[i] = input('Enter b' + str(i + 1) + ': ')
    return vecterB

Jacobi()

