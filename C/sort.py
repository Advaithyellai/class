from random import randint
from datetime import datetime

Algorithms = ["bubble", "quick", "selection", "insertion", "merge"] #"all"
Algorithm = "all"
lenarr = 997

def main(arr, alg):
    start = datetime.now()
    print("-------------------")
    print("Algorithm: ", alg)
    # print("Before sorting:", arr)
    if alg == "all":
        for a in Algorithms:
            main(arr, a)
        exit()
    elif alg == "bubble": bubble(arr)
    elif alg == "selection": selection(arr)
    elif alg == "quick": arr = quick(arr)
    elif alg == "insertion": insertion(arr)
    elif alg == "merge": arr = merge(arr)
    else:
        raise ValueError("Wrong Algorithm.\n'%s' Algorithm does not exist." %(Algorithm))
    
    # print("After sorting:", arr)
    
    end = datetime.now()
    print("Time taken: ", (end-start).total_seconds())

    if (arr == sorted(arr)) and (len(arr) == lenarr): print("The sorting is successful")
    else: exit("You are a failure")
    print("-------------------")

def bubble(arr):
    # time complexity = O(n^2)
    for j in range(lenarr-1, 0, -1):
        for i in range(j):
            if arr[i] > arr[i+1]: arr[i], arr[i+1] = arr[i+1], arr[i]

def selection(arr):
    # time complexity = O(n^2)
    for i in range(lenarr):
        minval = None
        for j in range(i, lenarr):
            if (not minval) or (arr[j] < minval[0]):
                minval = [arr[j], j]
        arr[minval[1]] = arr[i]
        arr[i] = minval[0]

def merge_pile(larr, rarr):
    ans = []
    
    lenla = len(larr)
    lenra = len(rarr)
    
    i = j = 0
    
    while (i < lenla) and (j < lenra):
        if larr[i] < rarr[j]:
            ans.append(larr[i])
            i += 1
        else:
            ans.append(rarr[j])
            j += 1

    while i < lenla:
        ans.append(larr[i])
        i += 1
    
    while j < lenra:
        ans.append(rarr[j])
        j += 1

    return ans

def merge(arr2, left=0, right=lenarr):
    sa = arr2
    if left+1 < right:
        mid = (left+right)//2
        la = merge(arr[left:mid], left, mid)
        ra = merge(arr[mid:right], mid, right)
        sa = merge_pile(la, ra)
    return sa

def quick(arr):
    pivot = arr[-1]
    less = []
    more = []
    i = 0
    for ele in arr:
        if (ele == pivot) and (i == 1): less.append(ele)
        elif (ele == pivot): i = 1
        elif ele < pivot: less.append(ele)
        elif ele > pivot: more.append(ele)
    if len(less) > 1: less = quick(less)
    if len(more) > 1: more = quick(more)
    return less+[pivot]+more

def insertion(arr):
    for i in range(1, len(arr)):
        j = i
        while (j>0) and (arr[j] < arr[j-1]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

arr = [randint(0, 10000) for j in range(lenarr)]
main(arr, Algorithm)