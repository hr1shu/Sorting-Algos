#Insertion Sort algo

def insertion(arr,n):
    for i in range(n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key
    return arr
        
        
if __name__ == "__main__":
    arr = [8, 3, 7, 4, 1]
    n = len(arr)
    print(insertion(arr,n))