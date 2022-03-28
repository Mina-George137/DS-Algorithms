
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

# ----------------------------------------------------------------------

def merge_sort(unsorted_list):
   if len(unsorted_list) <= 1:
      return unsorted_list
 # Find the middle point and devide it
   middle = len(unsorted_list) // 2
   left_list = unsorted_list[:middle]
   right_list = unsorted_list[middle:]

   left_list = merge_sort(left_list)
   right_list = merge_sort(right_list)
   return list(merge(left_list, right_list))

# Merge the sorted halves
def merge(left_half,right_half):
   res = []
   while len(left_half) != 0 and len(right_half) != 0:
      if left_half[0] < right_half[0]:
         res.append(left_half[0])
         left_half.remove(left_half[0])
      else:
         res.append(right_half[0])
         right_half.remove(right_half[0])
   if len(left_half) == 0:
      res = res + right_half
   else:
      res = res + left_half
   return res
# ----------------------------------------------------------------------

# Quick sort in Python
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)

