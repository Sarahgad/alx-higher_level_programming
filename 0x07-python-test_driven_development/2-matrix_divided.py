#!/usr/bin/python3
def matrix_divided(matrix, div):
    newMatrix = []
    newElement = [] 
    if not isinstance(div, (int, float)):
        raise TypeError ("div must be a number")
    if div == 0:
        raise ZeroDivisionError ("division by zero")
    
    for element in matrix:
        if not isinstance(matrix, list) or not isinstance(element,list):
            raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")

        if not len(element) == len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for num in element:
            if not isinstance (num, (int, float)):
                raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
        newElement = [round(num / div, 2) for num in element]
        newMatrix.append(newElement)
    return newMatrix
