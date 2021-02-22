#Selection Sort algo
#Time Comp: o(n^2)

def selectSort(arr,n):
    for i in range(n):
        min_ind = i
        for j in range(i+1,n):
            if arr[j]<arr[min_ind]:
                min_ind = j
        arr[min_ind],arr[i] = arr[i],arr[min_ind]
    return arr
    
if __name__ == "__main__":
    arr=[2,70,8,20]
    n = len(arr)
    print(selectSort(arr,n))