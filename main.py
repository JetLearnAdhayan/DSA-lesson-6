array = [12,3,45,6,9,10,23]

print(array)

def merge_sort(array):
    if len(array)>1:
        m = len(array)//2
        L = array[:m]
        R = array[m:]
        merge_sort(L)
        merge_sort(R)
        # i - left element of array
        # j - right element of array 
        # k - merged array index
        i = j = k = 0 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j = j+1

            k = k+1
        while i < len(L):
            array[k] = L[i]
            i += 1 
            k += 1        

        while j  < len(R):
            array[k] = R[j]
            j+=1
            k+=1     

def print_array(array):
    for x in range(len(array)):
        print(array[x], end = "  ")


merge_sort(array) 
print("Sorted List")
print_array(array)


    
