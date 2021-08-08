#frequency distribution, bin mean,boundary distribution
def equifreq(arr1,m):
     a=len(arr1)
     n=int(a/m)
     for i in range(0,m):
         arr=[]
         brr=[]
         for j in range(i*n,(i+1)*n):
             if(j>=a):
                 break
             arr=arr+[arr1[j]]
             brr=brr+[arr1[j]]
         print("frequency of bin ",i+1)
         print(arr)
         mean_of_brr=sum(brr)/len(brr)
         for p in range(0,len(brr)):
             brr[p]=mean_of_brr
         print("bin mean of bin ", i+1)
         print(brr)

         for q in range(0,len(arr)):
             t1=abs(arr[0]-arr[q])
             t2=abs(arr[len(arr)-1]-arr[q])
             if (t1>=t2):
                     arr[q] = arr[len(arr) - 1]
             else:
                    arr[q] = arr[0]
         print("boundary distribution of bin ", i+1)
         print(arr)
equifreq([4,8,15,21,21,24,25,28,34],3)