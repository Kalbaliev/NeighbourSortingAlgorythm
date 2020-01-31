import random


class SortingAlgorythm:

    def __init__(self):
        self.generateMatrix()
        sorted_array=self.sortFunc(self.unsorted_array,self.n,self.m)

        all_list=[]
        counter=0
       
        print("\n----------- ",self.n,"x",self.m,"Matrix --------------")
        print("------------ SORTED ARRAY --------------\n")
        for i in range(self.n):
            inner_list=[]
            for j in range(self.m):
                inner_list.append(sorted_array[counter])
                counter+=1
            all_list.append(inner_list)
            
            print(all_list[i])

        print("\n********************* THANKS A LOT !**************************\n")
    def generateMatrix(self):
        self.n = random.randint(1, 10)
        self.m = random.randint(1, 10)
        self.unsorted_array=list(range(1,(self.n*self.m)+1))

    def sortFunc(self,arr,n,m):
        for i in range((n*m)-1):
            if abs(arr[i]-arr[i+1])==1:
                if i+1!=n*m-1:
                    arr.insert(i+1,arr[n*m-1])
                    arr.pop()   
                else:
                    arr.insert(0,arr[n*m-1])
                    arr.pop()
        return arr



obj = SortingAlgorythm()