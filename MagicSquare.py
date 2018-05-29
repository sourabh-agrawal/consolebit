'''
This program is written by sourabh agrawal
problem:- 
	Basically it is a magic square problem
	Magic square problem is a problem in which we have to generate a matrix whose size is given by user and then the sum of matrix(it can be either sum of elements 	of any rows, some of elements of any column, some of diagonal elements) is a same number

Instructions:-
	This will work for odd dimension square matrix of any size
	size is being taken from the user, it can go large as per your need
	sum is also get prints along with the matrix on the screen
'''

# !/usr/bin/python3
matrix = []  # matrix is global matrix where the grid will get stored
no = 1  # no is used to get the max no that stored in grid


# This method will initialize the grid of size 'size' by 0
def initialize(size):
    global matrix
    matrix = []
    for j in range(size):
        temp = []
        for i in range(size):
            temp.append(0)
        matrix.append(temp)


# This method will print the grid with lpad with 0 so that the matrix will look in readable format
def printgrid(size):
    global matrix
    s = int(len(str(no)))
    for j in range(size):
        for i in range(size):
            t = str(matrix[j][i]).zfill(s)
            print(t, end=" ")
        print("")


# This method is used to calculate the magic square and store it in matrix
'''
Algorithm being used in grid method is:
1. 	take the size of the matrix from the user
2.	initialize the matrix of 'size' with 0
	we will fill the elements of the matrix with number "1 to size^2"
	initially take no=1
3.	select the mid element(position->(i,j) i =0th row and j=size//2 th column) of first row and rewrite it with no which is 1
4.	now make duplicate copy of i and j and store them in k, l respectively
5.	while no<size**2
		increment the value of no
		decrement the value of k(go one row up. so if the current row is 4 then go to 3rd row)
		increment the value of l(go one column right. so, if the current column is 3rd then go for 4th column)
			if 
				the element at (k,l) is 0 then rewrite it with current value of no
			else		 
				go for the element which is below the current element, so make use of i, j whose value represent the position of element on which last change was 					performed. so row = i+1 and column = j
				and then change the value of k, l accordingly
'''


def grid(size):
    global no
    no = 1
    global matrix
    i, j = 0, size // 2
    k, l = i, j
    matrix[i][j] = no
    while no < size ** 2:
        no += 1
        k -= 1
        l += 1
        if k < 0:
            k = size - 1
        if l > size - 1:
            l = 0
        if matrix[k][l] is 0:
            matrix[k][l] = no
            i, j = k, l
        else:
            matrix[i + 1][j] = no
            k = i + 1
            l = j
    calsum(size)


# This method is used to calculate the sum of magic square
def calsum(size):
    global matrix
    sum_rowwise = 0
    sum_colwise = 0
    sum_diagwise = 0
    for i in range(size):
        sum_colwise += matrix[i][0]         #calculating sum of elements of first column
        sum_rowwise += matrix[0][i]         #calculating sum of elements of first row
        sum_diagwise += matrix[i][i]        #calculating sum of diagonal
    # print("\nAs you can see the sum is %d" % sum)
    print("rowwise sum %d" % sum_rowwise)
    print("colwise sum %d" % sum_colwise)
    print("diagwise sum %d" % sum_diagwise)


def main():
    global matrix
    size = 1
    while size:
        size = int(input("\nEnter the size of the grid\t"))
        if size % 2 != 0:
            initialize(size)
            grid(size)
            printgrid(size)
            choice = int(input("\npress 0 to quit or any other no to continue\t"))
            if choice is 0:
                break
        else:
            print("\nEven no are not allowed")
            choice = int(input("\npress 0 to quit or any other no to continue\t"))
            if choice is 0:
                break


if __name__ == '__main__': main()
