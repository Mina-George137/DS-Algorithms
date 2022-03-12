def selection_sort(a):
   sortedFlag = False #To avoid sorting if it is already sorted
   for i in range(len(a)-1):
       if not sortedFlag:
           sortedFlag = True
           min = i
           for j in range(i+1,len(a)):
               if (a[j]<a[min]):
                    min =j
                    sortedFlag = False
           a[i], a[min] = a[min], a[i]

def insertion_sort(a) :
    for i in range(len(a)):
        temp = a[i]
        j = i
        while j > 0 and temp < a[j-1]:
            a[j] = a[j-1]
            j -= 1
        a[j] = temp

def bubble_sort(a):
    sortFlag = False
    passes = 1
    while passes< len(a) and not sortFlag:
        sortFlag = True
        for j in range(len(a)-passes):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                sortFlag = False
        passes += 1
