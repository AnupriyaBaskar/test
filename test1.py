# Reverse the given string

a = input("Enter the string: ")                 # "codecode" 
result = ""

if len(a)>=1 and len(a)<=100:
    for i in range(0,len(a)):
        result = a[i] + result                 # adding the letter one by one
    print(result)
else:
    print("Enter a string having length greater than 1")

# Prime no 

number = int(input("Enter the no: "))
count = 0

for i in range(2,number):
    if number%i==0:
        count += 1                      # using count method if count > 1 then it is not a prime no

if count>0:
    print("No")

else:
    print("Yes")

# reverse the no

number = int(input("Enter the number: "))

temp = number

reversed_no = 0
if number>=1 and number<=10000:
    while temp>0:
         m = temp%10
         reversed_no = reversed_no*10 + m
         temp = temp//10
    print(reversed_no)
else:
    print("Enter a no greater than zero or less than 10000")

# Arrange the array in such a way it forms largest number


def getlargeno(arr):
    for i in range(len(arr)):
        # convert to a string
        arr[i] = str(arr[i])
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):

            # using comparision method to find which combination is greater

            if arr[j]+arr[i] > arr[i]+arr[j] :   
                arr[i] , arr[j] = arr[j] , arr[i]
    result = "".join(arr)
    return f"The largest number formed is {result}"
    

    

a = getlargeno([1,34,3,98,9,76,45,4])
print(a)
    

#  Maximum and minumum in a array

def getmax_min(arr):
    min_no = arr[0]
    max_no = arr[0]  
    for i in range(0,len(arr)):    # [ 54, 546, 548 , 60]
        if arr[i] < min_no:
            min_no = arr[i]
        if arr[i]> max_no:
            max_no = arr[i]
    return f"Maximum no = {max_no}, Minimum no = {min_no}" 

result = getmax_min([54,546,2,548,6,4])

print(result)



