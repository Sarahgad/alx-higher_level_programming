#!/usr/bin/python3
def pascal_triangle(n):
    lists = []*n
    for i in range (n):
        lists.append([0]*i)
        
    for list in lists: 
        list.insert(0,1)
        if len(list) > 1:
            list[-1] = 1
    for i in range(2, n):
        for j in range(1, i):
            lists[i][j] = lists[i-1][j-1] + lists[i-1][j]
    return lists


    
    
def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
     print_triangle(pascal_triangle(5))