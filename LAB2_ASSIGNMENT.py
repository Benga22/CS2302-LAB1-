# Course Name: CS2302
# Author: Olugbenga Iyiola ID:80638542
# Assignment 2
# Instructor: Olac Fuentes
# T.A.: Nath Anindita
# Date of last modification: 02/26/2018
# Purpose of program: Using recursion to draw interesting ﬁgures

# Importing packages needed for generating random numbers
import random

# Node Functions
class Node(object):
# Constructor
    def __init__(self,item, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev= prev

# List Functions
class List(object):
    # Constructor
    def __init__(self):
       self.head = None
       self.tail = None

#Returns empty list
def IsEmpty(L):
    return L.head == None

#Appends neew node to the tail of the list
def Append(L, x):
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
        L.prev=None
    else:
        L.tail.next = Node(x)
        L.tail.next.prev=L.tail
        L.tail = L.tail.next


def Print(L):
    # Prints list L's items in order using a loop
    if L is None:
        return
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line

# Add new node at the head of the list
def Prepend(L,x):
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        temp = Node(x)
        temp.next = L.head
        L.head = temp

#Returns the length of the list
def GetLength(L):
    temp=L.head
    count = 0
    while temp is not None:
         count +=1
         temp=temp.next
    return count

# Creates a copy of the list
def Copy(L):
    return L

#Returns element at a particular position  in the list
def ElementAt(L,i):
    if IsEmpty(L):
        return
    if(i <0 or i>= GetLength(L)):
        return
    count =0
    temp=L.head
    while temp is not None:
        if count == i:
            return temp.item
        count +=1
        temp=temp.next

# Builds a new list of random integers within specified range
def BuildList(n):
    L = List()
    for i in range(n):
        Append(L,random.randint(0,100))
    return L

# Returns element at middle position in the list for bubble sort
def MedianBubble(L):
    C = Copy(L)
    return ElementAt(C,GetLength(C)//2)

# Returns element at middle position in the list for merge sort
def MedianMerge(L):
    C = Copy(L)
    return ElementAt(C,GetLength(C)//2)

# Returns element at middle position in the list for quick sort
def MedianQuick(L):
    C = Copy(L)
    return ElementAt(C,GetLength(C)//2)

# Returns element at middle position in the list for modified quick sort
def MedianModQuick(L):
    C = Copy(L)
    return ElementAt(C,GetLength(C)//2)


# Bubble sort method which compares 2 consecutive list elements for every iteration
def BubbleSort(L):
    change = True  # boolean variable to optimize algorithm
    while change:
        t = L.head  # temporary variable for iteration
        change = False  # If there are no swaps iteration stops
        while t.next is not None:
            if t.item>t.next.item:  # Comparing the values of 2 consecutive nodes
                temp = t.item  # Swapping
                t.item = t.next.item
                t.next.item=temp
                change = True # true if there is a swap
            t=t.next

# Divides list into two halves, calls itself for the two halves and then merges the two sorted list.
def MergeSort(L):
    if GetLength(L) > 1:  # Checking if there is more than one node in list
        mid = GetLength(L)//2  # Getting middle position of list
        LeftList = List()  # Creating 2 lists to keep the two separate halve of original list
        RightList = List()
        counter = 0  # Counter the check when iterator is at the mid position  of list
        iterator = L.head  # temporary variable for iteration
        while iterator is not None:
            counter +=1  # Incrementing counter
            if counter <=mid:  # If condition to separate list into two halves
                if IsEmpty(LeftList):  # Appending to left list
                    LeftList.head = Node(iterator.item)
                    LeftList.tail = LeftList.head
                else:
                     LeftList.tail.next = Node(iterator.item)
                     LeftList.tail = LeftList.tail.next
                iterator = iterator.next
            else:
                if IsEmpty(RightList): # Appending to right list
                    RightList.head = Node(iterator.item)
                    RightList.tail = RightList.head
                else:
                    RightList.tail.next = Node(iterator.item)
                    RightList.tail = RightList.tail.next
                iterator = iterator.next
        MergeSort(LeftList)  # Recursive call on left list
        MergeSort(RightList)  # Recursive call on left list
        leftListHead = LeftList.head
        rightListHead = RightList.head
        mainListHead = L.head
        while leftListHead is not None and rightListHead is not None:  # Merging back list when both heads are not none
            if leftListHead.item < rightListHead.item:
                mainListHead.item = leftListHead.item
                leftListHead = leftListHead.next
                mainListHead = mainListHead.next
            else:
                mainListHead.item = rightListHead.item
                rightListHead = rightListHead.next
                mainListHead = mainListHead.next
        while leftListHead is not None:  # Merging back all the remaining items on the right list
            mainListHead.item = leftListHead.item
            leftListHead = leftListHead.next
            mainListHead = mainListHead.next
        while rightListHead is not None:  # Merging back all the remaining items on the right list
            mainListHead.item = rightListHead.item
            rightListHead = rightListHead.next
            mainListHead = mainListHead.next

        return L  # Return sorted list

#  Method returns pivot position for quicksort
def partition(L,Start,End):
    pivot = End.item  # stores item at the tail of the list as pivot
    previous = Start.prev  # stores previous node of current node
    iterator = Start  # Iterator to traverse list

    while iterator is not L.tail and iterator is not None:  # traversing list from head to penultimate node
        if iterator.item < pivot:  # keeping track of previous node of current
            if previous is None:
                previous = Start
            else:
                previous = previous.next  # Moving previous along with current
            temp = previous.item  # Swapping to move items greater than pivot to the right
            previous.item = iterator.item
            iterator.item = temp
        iterator = iterator.next
    if previous is None:
        previous = Start
    else:
        previous = previous.next  # Moving previous to the next to middle node
        temp2 = previous.item
        previous.item = End.item
        End.item = temp2
    return previous

# Recursive method which picks an element as pivot and partitions the given array around the picked pivot.
def quickSortRecur(L,Start,End):
    if End is not None and Start is not End and Start is not End.next:
        pivot= partition(L,Start,End)
        quickSortRecur(L,Start,pivot.prev)
        quickSortRecur(L,pivot.next,End)

# method calls the quicksort recursive method with head and tail of list as parameters
def  QuickSort(L):
        Start=L.head
        End= L.tail
        quickSortRecur(L,Start,End)
        return L

# Quicksort method with single recursive call, processing only the sublist where the median is known to reside
def QuickSortModified(Start, End):

    if (Start == End):  # Returns when there is only one node
        return
    newStart = Start  # variable to hold head of list
    newCurrent = newStart.next # Variable to hold node next to head of list

    # while newCurrent is not None
    while 1:
        if newStart.item < newCurrent.item:  # Comparing the items to check if there is need to swap
            temp = newCurrent.item
            newCurrent.item = newStart.item
            newStart.item = temp
        if newCurrent == End:
            break
        newCurrent = newCurrent.next  # Incrementing new current position if there is a swap

    temp1 = Start.item  #  Swapping
    Start.item = newCurrent.item
    newCurrent.item = temp1

    oldCurrent = newCurrent
    newCurrent = newCurrent.prev

    if newCurrent is not None:  # Checking if there need for recursion on left side
        if Start.prev is not newCurrent and newCurrent.next is not Start:
            QuickSortModified(Start, newCurrent)

    newCurrent = oldCurrent
    newCurrent = newCurrent.next

    if newCurrent is not None:  # Checking if there need for recursion on left side
        if newCurrent.prev is not End and End.next is not newCurrent:
            QuickSortModified(newCurrent, End)


L3=BuildList(11)
print('The original list for bubblesort is:', end=' ')
Print(L3)
print('The sorted list after bubblesort is:', end=' ')
BubbleSort(L3)
Print(L3)
print('The middle element  of the sorted list is:', end=' ')
print(MedianBubble(L3))
print()

L4=BuildList(11)
print('The original list for mergesort is:', end=' ')
Print(L4)
print('The sorted list after mergesort is:', end=' ')
MergeSort(L4)
Print(L4)
print('The middle element  of the sorted list is:', end=' ')
print(MedianMerge(L4))
print()

L5=BuildList(11)
print('The original list for quicksort is:', end=' ')
Print(L5)
#print('testing prvious element at: ')
#print(ElementAt(L5,4).prev.item)
print('The sorted list after quicksort is:', end=' ')
QuickSort(L5)
Print(L5)
print('The middle element  of the sorted list is:', end=' ')
print(MedianQuick(L5))
print()

L6=BuildList(11)
print('The original list for modified quicksort is:', end=' ')
Print(L6)
print('The sorted list after modified quicksort is:', end=' ')
QuickSortModified(L6.head,L6.tail)
Print(L6)
print('The middle element  of the sorted list is:', end=' ')
print(MedianModQuick(L6))
print()


