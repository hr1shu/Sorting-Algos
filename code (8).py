#Bubble sort algo
#Time Comp = o(n^2)


def bubble(arr,n):
    for i in range(0,n-1):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swapped = True
            if swapped == False:
                break
    return arr
                
if __name__ == "__main__":
    arr=[2,7,8,20]
    n = len(arr)
    print(bubble(arr,n))