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
   return a

def merge_sort(unsorted_list,threshold):
   if len(unsorted_list) <= 1:
      return unsorted_list
   if len(unsorted_list) <= threshold:
      return selection_sort(unsorted_list)
   else:
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

def hybird_sort(a,threshold):
   if len(a) < 2:
      return a

   if len(a) <= threshold:
      return selection_sort(a)

   else:
      return merge_sort(a,threshold)