def mergesort(arr):

    if arr.__len__()>1:

        midpoint = len(arr)//2
        left_arr = mergesort(arr[:midpoint])
        right_arr = mergesort(arr[midpoint:])
        i = j = k = 0
        ll=left_arr.__len__()
        rl=right_arr.__len__()
        while i<ll and j<rl:
            if left_arr[i]<right_arr[j]:
                arr[k]=left_arr[i]
                i+=1
            else:
                arr[k]=right_arr[j]
                j+=1
            k+=1
        while i<ll:
            arr[k]=left_arr[i]
            i+=1
            k+=1
        while j<rl:
            arr[k]=right_arr[j]
            j+=1
            k+=1
    return arr

print(mergesort([5,4,2,1]))

