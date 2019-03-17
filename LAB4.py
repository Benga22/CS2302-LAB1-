# Course Name: CS2302
# Author: Olugbenga Iyiola ID:80638542
# Assignment 4
# Instructor: Olac Fuentes
# T.A.: Nath Anindita / Maliheh Zargaran
# Date of last modification: 03/16/2019
# Purpose of program: Binary Search Trees

# Importing packages needed for generating random numbers
import math

# This class is used to create objects of B Trees
class BTree(object):
    # Constructor
    def __init__(self, item=[], child=[], isLeaf=True, max_items=5):
        self.item = item
        self.child = child
        self.isLeaf = isLeaf
        if max_items < 3:  # max_items must be odd and greater or equal to 3
            max_items = 3

        #if max_items < 2:  # max_items must be odd and greater or equal to 3
        #  max_items = 2
        if max_items % 2 == 0:  # max_items must be odd and greater or equal to 3
           max_items += 1
        self.max_items = max_items


# Method is used to find the correct index position of child
def FindChild(T, k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree
    for i in range(len(T.item)):
        if k < T.item[i]:  # checks for correct index position of the child
            return i
    return len(T.item)


#  Method is used to insert item into non-leaf nodes
def InsertInternal(T, i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T, i)  # Inserting leaf nodes
    else:
        k = FindChild(T, i)  # Returns correct position of child
        if IsFull(T.child[k]):  # Checking if node is full
            m, l, r = Split(T.child[k])  # returns middle node, left and right subtrees respectively
            T.item.insert(k, m)  # Inserts middle node of child in the parent node
            T.child[k] = l  # pointing the node to its left child
            T.child.insert(k + 1, r)  # pointing the node to its right child
            k = FindChild(T, i)  # Finding the position of the child of the current node after split.
        InsertInternal(T.child[k], i)  # Recursive call


#  Method is used to split full nodes
def Split(T):
    # print('Splitting')
    # PrintNode(T)
    mid = T.max_items // 2  # Getting middle position of node
    if T.isLeaf:  # If it is a leaf node
        leftChild = BTree(T.item[:mid])  # Creates left child with array elements from 1st to index before mid
        rightChild = BTree(T.item[mid + 1:])  # Creates right child with array elements from index after mid to last
    else:  # If it is not a leaf node
        leftChild = BTree(T.item[:mid], T.child[:mid + 1], T.isLeaf)  # Creates left child with array elements from
                                                                    # 1st to index before mid and points the splitted
                                                                    # node to its left child
        rightChild = BTree(T.item[mid + 1:], T.child[mid + 1:], T.isLeaf) # Creates right child with array elements from
                                                                    #  index after mid to last and points the splitted
                                                                    # node to its right child
    return T.item[mid], leftChild, rightChild  # Returns mid node, left and right children of splitted node


# Method is used to insert into leaf nodes
def InsertLeaf(T, i):
    T.item.append(i)  # appending the item
    T.item.sort()  # sorting the item  after appending


# Method is used to check if node is full using the variable max_items from the constructor
def IsFull(T):
    return len(T.item) >= T.max_items


# Method is used to insert items into nodes
def Insert(T, i):
    if not IsFull(T):  # Checking if node is full
        InsertInternal(T, i)  # Inserting into non-leaf nodes
    else:
        m, l, r = Split(T)  # Splitting if node is full
        T.item = [m]  # Inserting item in mid position of node
        T.child = [l, r] # Inserting left and right items which points to corresponding children
        T.isLeaf = False  # Setting boolean to false since node has children
        k = FindChild(T, i)  # Finding index position of child
        InsertInternal(T.child[k], i)  # Recursive call


#  Method is used to search item in a B Tree
def Search(T, k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T, k)], k) # Recursive call with appropriate child


# Method Prints items in tree in ascending order
def Print(T):
    if T.isLeaf:
        for t in T.item:
            print(t, end=' ')  # Printing leaf node items
    else:
        for i in range(len(T.item)):  # Printing non-leaf node items
            Print(T.child[i])  # Recursive call on node's children
            print(T.item[i], end=' ')  # Printing items of current node
        Print(T.child[len(T.item)])  # Recursive call on last child of node


# Method Prints items and structure of B-tree
def PrintD(T, space):
    if T.isLeaf:
        for i in range(len(T.item) - 1, -1, -1):  # Printing leaf node items from last to first
            print(space, T.item[i])
    else:  # Printing non leaf node items from last to first with space to separate depths
        PrintD(T.child[len(T.item)], space + '   ')
        for i in range(len(T.item) - 1, -1, -1):
            print(space, T.item[i])
            PrintD(T.child[i], space + '   ')


# Method is used to find height of tree
def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])  # Increment by one for every next child


#  Method extracts items in B-tree into a sorted list
def BTreeToSorted(T, SortedList):
    if T.isLeaf:
        for i in range(len(T.item)):
            SortedList.append(T.item[i])  # Appending leaf node items into list
    else:
        for i in range(len(T.item)):
            BTreeToSorted(T.child[i], SortedList)  # Recursive call on children to append their items
            SortedList.append(T.item[i])  # Appending current node items
        BTreeToSorted(T.child[-1],SortedList)  # Recursive call to append items of node's last child
    return SortedList


#  Method is used to find minimum element in tree at a given depth d
def MinimumAtDepthD(T,d):
    if d ==0:  # Checking if depth is 0 which will be the needed depth
        return T.item[0]
    if T.isLeaf:
        return -math.inf  # Returning infinity is depth is not in tree or valid
    else:
        return MinimumAtDepthD(T.child[0],d-1)  # Recursive call using pointer to first child of node


#  Method is used to find maximum element in tree at a given depth d
def MaximumAtDepthD(T,d):
    if d ==0:  # Checking if depth is 0 which will be at the needed depth
        return T.item[-1]
    if T.isLeaf:
        return -math.inf  # Returning infinity is depth is not in tree or valid
    else:
        return MaximumAtDepthD(T.child[-1],d-1)  # Recursive call using pointer to last child of node


#  Method is used get the number of nodes at a give depth
def NumberOfNodesAtD(T,d):
    count = 0  # Counter to count nodes
    if d==0:  # Checking if depth is 0 which will be at the needed depth
        return 1
    else:
        for i in range(len(T.child)):
              count+=NumberOfNodesAtD(T.child[i],d-1)  # counting number of node at given depth
    return count


#  Method is used to print all items in tree at a given depth
def PrintItemsAtD(T,d):
    if d==0:  # Checking if depth is 0 which will be at the needed depth
        for i in range(len(T.item)):
            print(T.item[i], end= ' ')  # Printing node items at given depth
    else:
        for i in range(len(T.item)):
            PrintItemsAtD(T.child[i],d-1)  # Recursive on node's children
        PrintItemsAtD(T.child[-1],d-1)  # Recursive on node's last child


#  Method is used to get the number of nodes in the tree that are full
def FullNodes(T):
    count = 0  # Counter to count full nodes
    if not T.isLeaf:
        for c in T.child:
            count += FullNodes(c)
    if len(T.item) == T.max_items:
        count += 1  # Incrementing by 1 for every full node
    return count

#  Method is used to get number of leaves in the tree that are full
def NumOfFullLeaves(T):
    count =0
    if T.isLeaf and len(T.item)==T.max_items:  # Checking if leaf is full
        return 1
    else:
        for i in range(len(T.child)):
            count += NumOfFullLeaves(T.child[i])  # Recursive call to on nodes children
    return count

#  Method is used get the depth at which a given key, k is found
def FindDepth(T,k):
    if k in T.item:  # Checking if key is in node
        return 0
    if T.isLeaf:  # returning -1 if k is not in tree
        return -1
    if k > T.item[-1]:  # Checking k is greater that last item of node
        d = FindDepth(T.child[-1], k)  # recursive call on last child of node
    else:
        for i in range(len(T.item)):
            if k < T.item[i]:  # Checking  for correct index of node's child where k can be found
                d = FindDepth(T.child[i],k)  # Recursive call on node's children
                break  # Break out of loop if k is found
    if d == -1:
        return -1  # This will return -1 when k is not in tree
    return d + 1  # Returning depth


# Building BTree from a list
L = [4,7,8,9,11,12,13,15,16,17,24,27,28,30,33,34,37,40,42,50]
T = BTree()
for i in L:
    Insert(T, i)  # Inserting list items in list

#  Performing different operations on the BTree
print('*********THE HEIGHT OF THE TREE***********')
print('The height is: ',  height(T))
print('******************************************')
print('*********EXTRACTION OF BTREE***********')
PrintD(T,'')
SortedList = []
sortedList=BTreeToSorted(T,SortedList)
print('The sorted list is: ')
for i in SortedList:
    print(i,end = ' ')
print()
print('*******************************************')
print('******MINIMUM ELEMENT AT DEPTH D***********')
print('Minimum element at depth 0 is: ',MinimumAtDepthD(T,0))
print('Minimum element at depth 1 is: ',MinimumAtDepthD(T,1))
print('Minimum element at depth 2 is: ',MinimumAtDepthD(T,2))
print('*******************************************')
print('******MAXIMUM ELEMENT AT DEPTH D***********')
print('Maximum element at depth 0 is: ',MaximumAtDepthD(T,0))
print('Maximum element at depth 1 is: ',MaximumAtDepthD(T,1))
print('Maximum element at depth 2 is: ',MaximumAtDepthD(T,2))
print('*******************************************')
print('******NUMBER OF NODES AT DEPTH D***********')
print('Number of nodes at depth 0 is: ',NumberOfNodesAtD(T,0))
print('Number of nodes at depth 1 is: ',NumberOfNodesAtD(T,1))
print('Number of nodes at depth 2 is: ',NumberOfNodesAtD(T,2))
print('*******************************************')
print('******PRINTS ITEMS AT DEPTH D***********')
print('Element at depth 0 is: ', )
PrintItemsAtD(T,0)
print()
print('Elements at depth 1 are: ',)
PrintItemsAtD(T,1)
print()
print('Elements at depth 2 are: ', )
PrintItemsAtD(T,2)
print()
print('*******************************************')
print('*****NUMBER OF FULL NODES IN TREE *********')
print('The number of full nodes in tree is: ', FullNodes(T))
print('*******************************************')
print('*****NUMBER OF FULL LEAVES IN TREE *********')
print('The number of leaves that are full: ',NumOfFullLeaves(T))
print('*******************************************')
print('********DEPTH OF KEY IN TREE **************')
print('The depth  of 16 is: ', FindDepth(T,16))
print('The depth  of 8 is: ', FindDepth(T,8))
print('The depth  of 4 is: ', FindDepth(T,4))
print('*******************************************')