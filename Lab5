# Author: Olugbenga Iyiola ID:80638542
# Assignment 5
# Instructor: Olac Fuentes
# T.A.: Nath Anindita / Maliheh Zargaran
# Date of last modification: 03/08/2019
# Purpose of program: Binary Search Trees


# # Importing packages needed for Binary Search Tree and Hash Table Implementation
import time
import statistics
import numpy as np
import matplotlib.pyplot as plt

# BST Class
class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):
        self.item = item  # Objects content
        self.left = left   # pointer to  objects left child
        self.right = right  # pointer to objects right child

# Word Embed Class
class wordEmbed(object):

    # Constructor
    def __init__(self, item, arrays = np.arange(0, dtype=np.float) ):
        self.item = item  # Objects content
        self.arrays = arrays  # Objects content

# Hash table class
class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self, size):
        self.size = size
        self.num_items = 0  #  Counts number of items in hash table
        self.item = []
        for i in range(size):
            self.item.append([])

#  Method reads text file, creates and returns table of an word embed object
def CreateTable():
    Table = []
    f = open('glove.6B.50d.txt',encoding='utf-8-sig')  # Reading text file
    for line in f:  # Loop to traversal
        line = line.rstrip('\n')  # Removing the space character after each read line
        splittedArray = line.split(' ')  # Creating array from text file with a delimeter
        stringword = splittedArray[0]  # The first element of the array is the word
        arrays = np.arange(0, dtype=np.float)  # Creating numpy array for the embeddings
        for i in range(1,len(splittedArray)):
            arrays= np.append(arrays,splittedArray[i])  # Appending the embeddings

        myWord = wordEmbed(stringword,arrays)  # Creating an object that has word and array as items
        Table.append(myWord)

    return  Table

 # Method reads text file, finds words embeddings and calculate similarity between 2 words
def CreateNewTable(T):
    Table = []
    f = open('LISTB.txt', encoding='utf-8')  # Reading text file
    for line in f:
        line = line.rstrip('\n')  # Removing the space character after each read line
        splittedArray = line.split(' ')  # Creating array from text file with a delimeter

        stringword1 = splittedArray[0]  # Variable with line's first word
        stringword2 = splittedArray[1]  # Variable with line's second word
        Embedding1 = CreateEmbedding(T,stringword1)  # Variable with line's first word embeddings
        Embedding2 = CreateEmbedding(T,stringword2)  # Variable with line's second word embeddings
        DotProduct = np.dot(Embedding1,Embedding2)  # Dot product of the embeddings
        Magnitude1 = CreateMagnitude(Embedding1)  # Magnitude of first word embeddings
        Magnitude2 = CreateMagnitude(Embedding2)  # Magnitude of second word embeddings
        Similarities = DotProduct/(Magnitude1*Magnitude2)  # Similarity between two word
        print('Similarity ', '[',stringword1,',', stringword2,']', ' = ', Similarities)

    return  Table

#  Method returns embedding of input string
def CreateEmbedding(T,stringword):
    foundWord = FindIterativeBST(T, stringword)  # Finding word inside BST
    if foundWord == -1:
        print('Item not found')
    else:
        embeddings1 = foundWord.arrays  # Variable to store embeddings of word
        embeddings12 = np.array(embeddings1, dtype=np.float)  # Converting embeddings from string to float
        return embeddings12

#  Method retuns magnitude of input word
def CreateMagnitude(Embedding):
    return abs(np.linalg.norm(Embedding))  # Returning magnitude of word


# Method reads text file, finds words embeddings and calculate similarity between 2 words
def CreateNewTable2(H):
    Table = []
    f = open('LISTB.txt', encoding='utf-8')  # Reading text file
    for line in f:
        line = line.rstrip('\n')  # Removing the space character after each read line
        splittedArray = line.split(' ')  # Creating array from text file with a delimeter

        stringword1 = splittedArray[0]  # Variable with line's first word
        stringword2 = splittedArray[1]  # Variable with line's second word
        Embedding1 = CreateEmbedding2(H,stringword1)  # Variable with line's first word embedding
        Embedding2 = CreateEmbedding2(H,stringword2)  # Variable with line's second word embedding
        DotProduct = np.dot(Embedding1,Embedding2)  # Dot product of the embeddings
        Magnitude1 = CreateMagnitude(Embedding1)  # Magnitude of first word embeddings
        Magnitude2 = CreateMagnitude(Embedding2)  # Magnitude of second word embeddings
        Similarities = DotProduct/(Magnitude1*Magnitude2)  # Similarity between 2 words
        print('Similarity ', '[',stringword1,',', stringword2,']', ' = ', Similarities)
    return  Table

#  Method returns embedding of input string
def CreateEmbedding2(H,stringword):
    foundWord = FindC(H, stringword)  # Finding word inside Hash table
    if foundWord == -1:
        print('Item not found')
    else:
        embeddings1 = foundWord.arrays  # Variable to store embeddings of word
        embeddings12 = np.array(embeddings1, dtype=np.float)  # Converting embeddings from string to float
        return embeddings12

#  Method retuns magnitude of input word
def CreateMagnitude(Embedding):
    return abs(np.linalg.norm(Embedding))   # Returning magnitude of word

#  Method constructs binary search tree
def InsertBST(T, newItem):
    if T == None:
        T = BST(newItem)  # Create root if tree is empty
    elif T.item.item> newItem.item:
        T.left = InsertBST(T.left, newItem)  # Insert as left child if current item > new item
    elif T.item.item < newItem.item:
         T.right = InsertBST(T.right, newItem)  # Insert ad right child if current item < new item
    else:
        print('value already in list')  # Do not insert if item is already in tree
    return T

#  Method is used to find nodes of a BST
def FindIterativeBST(T,k):
    if T is None or T.item.item ==k:  # Checking if node's item is same as given string
        return T.item  # Return node if true
    while T is not None:  # Checking if node is not none
        if T.item.item>k:  # Checking if node's item is greater than given string
            T=T.left  # Move left if true
        elif T.item.item < k:  # Checking if node's item is lesser than given string
            T=T.right  # Move right if true
        else:
            return T.item  # Returning node
    print('Item not found')
    exit()
    return None

# Inserting nodes inside has table
def InsertHash(H, k, l):
    # Inserts k in appropriate bucket (list)
    # Does nothing if k is already in the table
    check = loadFactor(H)  # Checking value of load factor
    if check > 1:  # Checking if load factor is greater than 1
        newSizeHash=Resize(H)  # Creating new hash table with double size
        for i in range(len(H.item)):  # Traversing hash table
            for j in H.item[i]:
                b = h(j.item, len(newSizeHash.item))  # Getting new buckets for old items of hash table
                newSizeHash.item[b].append([j])  # Appending the old items to the new hash table
                newSizeHash.num_items += 1  # Incrementing num items for every item inserted in hash table
        b = h(k.item, len(newSizeHash.item))  # Getting buckets for new items of hash table
        newSizeHash.item[b].append([k])  # Appending the new item to the new hash table
        newSizeHash.num_items +=1  # Incrementing num items for every item inserted in hash table
        return newSizeHash
    else:
         b = h(k.item, len(H.item))  # Getting bucket for item
         H.item[b].append([k])  # Appending item in the bucket of the hash table
         H.num_items+=1  # Incrementing num items for every item inserted in hash table
         return H

#  Getting Hash values of strings
def h(s, n):
    r = 0
    for c in s:
        r = (r * n + ord(c)) % n  # computing unicode of list modulus hash table size
    return r

#  Method is used to find nodes of a hash table
def FindC(H, k):
    # Returns bucket (b) and index (i)
    # If k is not in table, i == -1
    b = h(k, len(H.item))  # Getting bucket for item
    for i in range(len(H.item[b])):
        if H.item[b][i][0].item == k:  # Comparing node's item with given string
            return H.item[b][i][0]  # Returning node
    print('Item not found')
    exit()
    return -1

# Returning hash table load factor
def loadFactor(H):
        return H.num_items/len(H.item)  # total hash table items divided by hash table size

# Resizing hash table to double its size plus 1
def Resize(H):
    newSize = ((H.size)*2) +1
    newH = HashTableC(newSize)
    return newH  # Returning new bigger hash table


def DeleteC(H, k):
    # Returns k from appropriate list
    # Does nothing if k is not in the table
    # Returns 1 in case of a successful deletion, -1 otherwise
    b = k % len(H.item)
    try:
        H.item[b].remove(k)
        return 1
    except:
        return -1

# Method returns total number of nodes in a BSt
def NumberOfNodes(T):
    if T is None:
        return 0
    else:
        return 1+ NumberOfNodes(T.left)+ NumberOfNodes(T.right)  # Incrementing counter for every visited node

#  Method is used to find standard deviation of the length of the hash table lists
def ListStandardDeviation(H):
    StandardDeviationTable = []  # list to store length of the lists in the hash table
    for i in range(len(H.item)):  # traversing the hash table
        StandardDeviationTable.append(len(H.item[i]))  # Appending the table list lengths to the list
    SD = statistics.stdev(StandardDeviationTable)  # Computing the standard deviation
    return  SD

# Method is used to find height of BST
def height(T):
    if T is None:
        return -1;
    hleft = height(T.left)  # gets height of left tree
    hright = height(T.right)  # gets height of right tree
    if hleft > hright:  # returns the greater of right and left trees
        return 1 + hleft
    return 1 + hright

#  Method returns percentage of list that is empty
def EmptyList(H):
    counter =0  # Counter to counter number of positions in table
    for i in range(len(H.item)):  # traversing hash table
        for j in H.item[i]:
            counter +=1  # Incrementing for every position
    percentEmpty= ( H.num_items/counter)/100  # number of items divided capacity of hash table
    return percentEmpty

# Method is used to display graph of a BST
def Draw_Trees(T, ax, center, width, length):
   # if T is None:
    #    return
    #  Printing items for leaves
    if T is not None:
         if T.left is None and T.right is None:
            #plt.text(center[1, 0], center[1, 1], T.item.item, bbox={"boxstyle": "circle", "color": "grey"})
            ax.text(center[1, 0], center[1, 1], T.item.item, size=7.5, ha="center", va="center",
                    bbox=dict(facecolor='w', boxstyle="circle"))

         #  Printing items for left children of BST

         if T.left is not None:
            center[0, 0] = center[1, 0] - width
            center[0, 1] = center[1, 1] - length
            ax.plot(center[:, 0], center[:, 1], color='k' )
           # plt.text(center[1, 0], center[1, 1], T.item.item, bbox={"boxstyle": "circle", "color": "grey"})

            ax.text(center[1, 0], center[1, 1], T.item.item, size=7.5, ha="center", va="center",
                    bbox=dict(facecolor='w', boxstyle="circle"))

            center1= np.array([[center[0,0], center[0,1]],[center[0,0], center[0,1]],[center[0,0], center[0,1]]])
            Draw_Trees(T.left,ax, center1, width/2, length)

    #  Printing items for right children of BST
         if T.right is not None:
            center[2, 0] = center[1, 0] + width
            center[2, 1] = center[1, 1] - length
            ax.plot(center[:, 0], center[:, 1], color='k')
           # plt.text(center[1, 0], center[1, 1], T.item.item, bbox={"boxstyle": "circle", "color": "grey"})
            ax.text(center[1, 0], center[1, 1], T.item.item, size=7.5, ha="center", va="center",
                    bbox=dict(facecolor='w', boxstyle="circle"))

            center2 = np.array([[0, 0], [center[2, 0], center[2, 1]], [center[2, 0], center[2, 1]]])
            Draw_Trees(T.right, ax, center2, width / 2, length)


#Code to test the functions above'''plt.close("all")
orig_center = np.array([[0,0],[0,0],[0,0]])
width = 50
length = 100
fig, ax = plt.subplots()

#  Implementation of both BST and Hash table
print('Choose table implementation')
choice = int(input('Type 1 for binary search tree or 2 for hash table with chaining: '))

if choice == 1:
    print('Choice: ', choice)
    print('Building binary search tree')
    start = time.perf_counter_ns() # start time of creating BST
    Table = CreateTable()  # Creating BST

    T = None
    for a in Table:
        T = InsertBST(T, a)  # Inserting word embed object inside BST

    end = time.perf_counter_ns()  # End time of creating BST
    runningTimeBSTtable = end - start

    print('Binary Search Tree stats: ')
    print('Number of nodes: ', NumberOfNodes(T))  # Total number of nodes in BST
    print('Height: ',height(T))  # Height of BST
    print('Running time for binary search tree construction: ',runningTimeBSTtable, ' nanoseconds')
    print('Reading word file to determine similarities')
    #Draw_Trees(T, ax, orig_center, width, length / height(T))
    start1 = time.perf_counter_ns()  # Start time
    CreateNewTable(T)  # Creating new list and finding similarities of words
    end1 = time.perf_counter_ns()
    runningTimeBSTtable1 = end1 - start1
    print()
    print('Running time for binary search tree query processing: ', runningTimeBSTtable1, ' nanoseconds')


elif  choice==2:

    print('Choice: ', choice)
    print('Building hash table with chaining')
    start2 = time.perf_counter_ns()  # Start time of creating hash table
    TableHash = CreateTable()

    H = HashTableC(60601)
    InitialSizeHash = len(H.item)
    for a in TableHash:
        myHashT = InsertHash(H, a, len(a.item))  # Inserting word embed object inside hash table

    end2 = time.perf_counter_ns()
    runningTimeBSTtable2 = end2 - start2

    print('Hash table stats: ')
    print('Initial table size: ', InitialSizeHash)
    print('Final table size: ', len(myHashT.item))
    print('Load factor: ', loadFactor(myHashT))
    print('Percentage of empty lists: ',EmptyList(myHashT))
    print('Standard deviation of the lengths of the lists: ', ListStandardDeviation(myHashT))
    print('Running time for hash table construction: ', runningTimeBSTtable2, ' nanoseconds')
    print()
    print('Reading word file to determine similarities')
    print('Word similarities found: ')
    start3 = time.perf_counter_ns()
    CreateNewTable2(myHashT)   # Creating new list and finding similarities of words
    end3 = time.perf_counter_ns()
    runningTimeBSTtable3 = end3 - start3
    print()
    print('Running time for hash table query processing: ', runningTimeBSTtable3, ' nanoseconds')

'''ax.set_aspect(1.0)
ax.axis('off')
plt.show()  # Displaying figure
fig.savefig('squares.png')
print()
print()
print('**********************************')'''
