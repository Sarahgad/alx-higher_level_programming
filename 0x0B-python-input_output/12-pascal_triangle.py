#!/usr/bin/python3
def pascal_triangle(n):
    list = [[]]

    for i in range (n):
        list += [[1]]
        for i in range(n - (n - i)):
            list  += [list[i - 1] + list[i - 2]]
        return list
    
def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
