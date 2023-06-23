print("First Question")
array=[1,2,3,4,5,6]
result=sum(array)
print ("sum of the array is", result)
print("Second Question")
str = "Hi everyone"   
print ("The original string  is : ",str)   
reverse_String = ""    
count = len(str) 
while count > 0:   
    reverse_String += str[ count - 1 ] 
    count = count - 1  
print ("The reversed string is : ",reverse_String)
print ("Question 3")
def isPalindrome(s):
    return s == s[::-1]
  
  

s = "racecar"
ans = isPalindrome(s)
  
if ans:
    print("Yes")
else:
    print("No")
print("question 4")
def Maximum(arry, n):
  max = arry[0]
  for i in range(1, n):
        if arry[i] > max:
            max = arry[i]
  return max
 
arry = [10, 324, 45, 90, 9808]
n = len(arry)
Ans = Maximum(arry, n )
print("maximum in given array ", Ans)
print("Question 5")

my_list = [1, 2, 3, 1, 2, 4, 5, 4 ,6, 2]
print("List Before ", my_list)
temp_list = []

for i in my_list:
    if i not in temp_list:
        temp_list.append(i)

my_list = temp_list

print("List After removing duplicates ", my_list)
print("Question 6")
num = 2


if num > 1:
   
    for i in range(2, int(num/2)+1):
        
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

print("Question 7")    
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x,countX(lst,x)))
 

    

