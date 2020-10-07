# creating empty list 
list1 = [] 
  
# asking number of elements to put in list 
num = int(input("Enter number of elements in list: ")) 
  
# iterating till num to append elements in list 
for i in range(1, num + 1): 
    ele = input("Enter elements: ")
    list1.append(ele) 

list1.sort()
      
# print maximum element 
print("Largest element is:", list1[-1]) 
