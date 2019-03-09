# Course Name: CS2302
# Author: Olugbenga Iyiola ID:80638542
# Assignment 3
# Instructor: Olac Fuentes
# T.A.: Nath Anindita / Maliheh Zargaran
# Date of last modification: 03/08/2019
# Purpose of program: Binary Search Trees

# Importing packages needed for generating random numbers
import numpy as np
import matplotlib.pyplot as plt
import math

# BST Class
class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

# Method to insert BST nodes in a tree
def Insert(T, newItem):
    if T == None:
        T = BST(newItem)  # Create root if tree is empty
    elif T.item > newItem:
        T.left = Insert(T.left, newItem)  # Insert as left child if current item > new item
    elif T.item < newItem:
         T.right = Insert(T.right, newItem)  # Insert ad right child if current item < new item
    else:
        print('value already in list')  # Do not insert if item is already in tree
    return T

# Method to print BST in order of root, left child and right child
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        print(T.item, end=' ')
        InOrder(T.left)
        InOrder(T.right)

# Method returns height of BST
def height(T):
    if T is None:
        return -1;
    hleft = height(T.left)  # gets height of left tree
    hright = height(T.right)  # gets height of right tree
    if hleft > hright:  # returns the greater of right and left trees
        return 1 + hleft
    return 1 + hright

# Method to sort native list in ascending order
def sortList(A):
    swapped =True
    j=0
    for j in range(len(A)):
        swapped = False
        for i in range(len(A)-1):
             if A[i]>A[i+1]:
                temp = A[i]
                A[i]=A[i+1]
                A[i+1]=temp
                swapped=True
    return A

# Iterative method to search for BST items
def FindIterative(T,k):
    if T is None or T.item ==k:
        return T
    while T is not None:
        if T.item>k:
            T=T.left  # Keep moving left if current item > key
        elif T.item < k:
            T=T.right  # Keep moving right if current item < key
        else:
            return T.item  # Returns current item if it is equals key
    return print('Item not found!')

# Method builds a balanced BST from a sorted list
def BalancedBST(T, Start, End):
    if T is None or len(T) == 0 or Start > End:
        return None
    mid = (Start + End)//2  # The middle item is used as root for every recursive call
    Root = BST(T[mid])

    Root.left = BalancedBST(T,Start,mid-1)  # Recursive call on left BST
    Root.right = BalancedBST(T,mid+1, End)  # Recursive call on right BST

    return Root

# Method extracts elements of BST into a sorted list
def ExtractToSorted(T,B,i):
    if T is None:
        return i
    i = ExtractToSorted(T.left,B,i)  # keeping track of array index
    B[i]= T.item  # filling list with BST item
    i+=1  # Incrementing index
    i = ExtractToSorted(T.right,B,i)  # keeping track of array index
    return i

# Method prints elements in a BST  ordered by depth
def PrintByDepth(T, level):

    if T is None:
        return 0
    if level ==0:
        print('keys at depth', level, ': ', T.item)
    if T.left is not None and T.right is not None:
            print('keys at depth',level+1,': ',T.left.item, ' ',T.right.item)
    if T.right is None and T.left is not None:
            print('keys at depth', level+1, ': ', T.left.item)
    if T.left is None and T.right is not None:
            print('keys at depth', level+1, ': ', T.right.item)

    downlevel = PrintByDepth(T.left,level + 1)  # Recursive call on BST left side
    if (downlevel != 0):
        return downlevel

    downlevel = PrintByDepth(T.right,level + 1)  # Recursive call on BST right side
    return downlevel

# Method is used to display graph of a BST
def Draw_Trees(T, ax, center, width, length):
    if T is None:
        return
    #  Printing items for leaves
    if T.left is None and T.right is None:
        plt.text(center[1, 0], center[1, 1], T.item, bbox={"boxstyle": "circle", "color": "grey"})

    #  Printing items for left children of BST
    if T.left is not None:
        center[0, 0] = center[1, 0] - width
        center[0, 1] = center[1, 1] - length
        ax.plot(center[:, 0], center[:, 1], color='k', )
        plt.text(center[1, 0], center[1, 1], T.item, bbox={"boxstyle": "circle", "color": "grey"})

        center1= np.array([[0,0],[center[0,0], center[0,1]],[center[0,0], center[0,1]]])
        Draw_Trees(T.left,ax, center1, width/2, length)

    #  Printing items for right children of BST
    if T.right is not None:
        center[2, 0] = center[1, 0] + width
        center[2, 1] = center[1, 1] - length
        ax.plot(center[:, 0], center[:, 1], color='k')
        plt.text(center[1, 0], center[1, 1], T.item, bbox={"boxstyle": "circle", "color": "grey"})

        center2 = np.array([[0, 0], [center[2, 0], center[2, 1]], [center[2, 0], center[2, 1]]])
        Draw_Trees(T.right, ax, center2, width / 2, length)


#Code to test the functions above'''plt.close("all")
orig_center = np.array([[0,0],[0,0],[0,0]])
width = 50
length = 100
fig, ax = plt.subplots()
T = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42]
for a in A:
    T = Insert(T, a)

# TESTING FOR NUMBER 2 - ITERATIVE SEARCH
print(FindIterative(T,1300))
print()
print(FindIterative(T,10))
print()

# TESTING FOR NUMBER 3 - BALANCED BST
sortedA = sortList(A)
BBST = BalancedBST(sortedA, 0, len(sortedA)-1)
Draw_Trees(BBST, ax,orig_center,width, length/height(T))

# TESTING FOR NUMBER 4 - EXTRACTING INTO SORTED BST
B=[70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42]
T2 = None
for b in B:
    T2 = Insert(T2, b)
print('***********ORIGINAL T2 BST**********')
InOrder(T2)
print()
print('**********EXTRACTED A***************')
ExtractToSorted(T2,B,0)
for i in A:
    print(i, end=' ')
print()
print()

# TESTING FOR NUMBER 5
print('*************************************')
PrintByDepth(T, 0)

# TESTING FOR NUMBER 1
#Draw_Trees(T, ax,orig_center,width, length/height(T))

ax.set_aspect(1.0)
ax.axis('off')
plt.show()  # Displaying figure
fig.savefig('squares.png')
print()
print('**********************************')


