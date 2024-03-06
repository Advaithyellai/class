from datetime import datetime
import numpy

SORTING_ALGS = ["Bubble", "Merge", "Insertion", "Shell", "Selection",\
                "Counting", "Radix", "Tim"]
RUN_ALL_ALGS = True
ALGORITHM = "Counting"
ALARM = False

def Main(alg_name, ul):
    if alg_name == "Bubble":
        ol = bubble_sort(ul)
    elif alg_name == "Merge":
        ol = merge_sort(ul)
    elif alg_name == "Insertion":
        ol = insertion_sort(ul)
    elif alg_name == "Shell":
        ol = shell_sort(ul)
    elif alg_name == "Selection":
        ol = selection_sort(ul)
    elif alg_name == "Counting":
        ol = counting_sort(ul)
    elif alg_name == "Radix":
        ol = radix_sort(ul)
    elif alg_name == "Tim":
        ol = tim_sort(ul)
    else:
        exit("Please input the correct algorithm name.")
    
    return ol

def bubble_sort(array):
    while True:
        l = []
        for ele in array: l.append(ele)
        for i in range(len(array)-1, 0, -1):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
        if l == array: break
    return array

def merge_sort(array):
    half = len(array)//2
    if half == 0: return array

    left_side = merge_sort(array[:half])
    right_side = merge_sort(array[half:])

    merged_list = left_side+right_side
    merged_list = bubble_sort(merged_list)
    return merged_list

def insertion_sort(array):
    for i in range(len(array)):
        j = i-1
        ele = array[i]
        while j >= 0:
            if ele > array[j]: break
            array[j+1], array[j] = array[j], ele
            j -= 1
    return array

def shell_sort(array):
    l = [[], [], []]
    one_third = len(array)//3
    
    for i in range(3):
        for j in range(one_third):
            l[i].append(array[3*j+i])
    
    if len(array)-3*one_third == 1:
        l[0].append(array[-1])
    elif len(array)-3*one_third == 2:
        l[0].append(array[-1])
        l[1].append(array[-2])
    
    l1 = insertion_sort(l[0])
    l2 = insertion_sort(l[1])
    l3 = insertion_sort(l[2])
    
    order_l = []
    
    for k in range(len(array)):
        if k%3==0: order_l.append(l1[k//3])
        elif k%3==1: order_l.append(l2[k//3])
        else: order_l.append(l3[k//3])
    
    return insertion_sort(order_l)

def selection_sort(array):
    order_l = []
    for i in range(len(array)):
        smallest_ele = None
        for ele in array:
            if smallest_ele == None or ele < smallest_ele:
                smallest_ele = ele
        array.remove(smallest_ele)                
        order_l.append(smallest_ele)
    return order_l

def counting_sort(array):
    minimum = None
    maximum = None
    
    for ele in array:
    
        if minimum == None or ele < minimum: minimum = ele
        if maximum == None or ele > maximum: maximum = ele
    
    count = []
    counter = 0
    
    for i in range(minimum, maximum):    
        if i in array:
            
            for ele in array:
                if ele == i: counter += 1
    
        count.append(counter)
    
    sorted_list = []
    count.insert(0, 0)
    count.pop(-1)
    
    for ele in count:
        if ele != 0: ele -= 1

    for i in range(len(count)):
        if len(sorted_list) == 0 or sorted_list.index(sorted_list[-1]) < i:
    
            if i == len(count)-1:    
                for j in range(count[i], len(array)):
                    sorted_list.append(maximum)
    
            elif count[i] != count[i+1]:
    
                for j in range(count[i], count[i+1]):
                    sorted_list.append(minimum+i)
    
    return sorted_list

def radix_sort(array):
    max_val = max(array)
    c = True
    k = 0
    while c == True:
        for i in range(len(array)):
        
            j = i-1
            ele = array[i]
            
            while j >= 0:
                if len(str(ele)) <= k: a = 0
                else: a = int(str(ele)[-(k+1)])

                if len(str(array[j])) <= k: b = 0
                else: b = int(str(array[j])[-(k+1)])

                if a < b:
                    array[j+1], array[j] = array[j], ele
                    j -= 1
                else: break
        if max_val/(10**k) < 10: break
        k += 1

    return array

def tim_sort(array):
    onethird = len(array)//3
    
    first_third = insertion_sort(array[:onethird])
    second_third = insertion_sort(array[onethird:2*onethird])
    
    last_third = insertion_sort(array[2*onethird:])
    two_third = bubble_sort(first_third+second_third)
    
    return bubble_sort(last_third+two_third)

a = tuple(numpy.random.randint(0, 10000, 1000))
sorted_list = sorted(list(a))

print()
print()
print()

print("------------------------------------------------------------")
print("Original Unordered List -", list(a))
print("Sorted List -", sorted_list)
print("------------------------------------------------------------")
print()

if RUN_ALL_ALGS == True:
    fastest_time = None
    best_algorithm = None
    for alg in SORTING_ALGS:
        
        start_time = datetime.now()

        unordered_list = list(a)
        ordered_list = Main(alg, unordered_list)

        end_time = datetime.now()
        
        time_taken = end_time-start_time
        if not fastest_time or time_taken < fastest_time:
            fastest_time = time_taken
            best_algorithm = alg

        print()
        print("------------------------------------------------------------")
        print("Algorithm -", alg)
        print("------------------------------------------------------------")
        print("Sorted -", sorted_list == ordered_list)
        print("Time Taken -", time_taken)
        print("------------------------------------------------------------")
        print()

        if sorted_list != ordered_list: ALARM = True

else:
    
    start_time = datetime.now()

    unordered_list = list(a)
    ordered_list = Main(ALGORITHM, unordered_list)

    end_time = datetime.now()

    print()
    print("------------------------------------------------------------")
    print("Algorithm -", ALGORITHM)
    print("------------------------------------------------------------")
    print("Sorted -", sorted_list == ordered_list)
    print("Ordered List -", ordered_list)
    print("Time Taken -", end_time - start_time)
    print("------------------------------------------------------------")
    print()

print()
print("Fastest Time:", time_taken)
print("Fastest Algorithm:", best_algorithm)
print()

if ALARM == True:
    raise ArithmeticError("The program sucks since it is not sorting correctly")
