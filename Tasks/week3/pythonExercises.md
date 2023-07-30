# Exercises from codeforces

### <a href = "https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/C"> C. Simple Calculator
</a>
> Answer
```python
X, Y =  map(int, input().split())
print(f"{X} + {Y} = {X + Y}")
print(f"{X} * {Y} = {X * Y}")
print(f"{X} - {Y} = {X - Y}")

```

### <a href = "https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/K">K. Max and Min
</a>
> Answer
```python
arr = input().split()
max = int(arr[0])
min = int(arr[0])
for i in range(3):
    if int(arr[i]) >= max: max = int(arr[i])
    if int(arr[i]) <= min: min = int(arr[i])    

print(f"{min} {max}")

```
### <a href = "https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/F">F. Digits Summation</a>
> Answer
```python
str1, str2 = input().split()
print(f"{int(str1[-1]) + int(str2[-1])}")

```

### <a href = "https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Q">Q. Digits</a>
> Answer
```python
numOfInputs = int (input())   
arrOfNums = []
for i in range(0, numOfInputs):
    arrOfNums.append(input())

for f in range(0, len(arrOfNums)):
    numString = str(arrOfNums[f])
    newString = ""
    count = len(numString)
    for i in range (0, len(numString)): 
        count = count - 1
        newString = (newString + numString[count] + " ")
    print (newString) 
```

### <a href = "https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/S">S. Sum of Consecutive Odd Numbers
</a>
> Answer
```python
numOfInputs = int(input())

while numOfInputs > 0:
    startNum, endNum = map (int, input().split())
    if startNum < 0 or endNum < 0 : break
    if startNum > endNum : startNum, endNum = endNum, startNum
    sum = 0
    middleNum = startNum + 1

    while  middleNum < endNum:
        if middleNum % 2 != 0:
            sum += middleNum
        middleNum = middleNum + 1
    numOfInputs = numOfInputs - 1
    print(sum)   
```

### <a href = "https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/K">K. Divisors

</a>
> Answer
```python
inputNum = int(input())
counter = 1
while counter <= inputNum:
    if inputNum % counter == 0 : print(counter)
    counter = counter + 1
```
### <a href = "https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/J">J. Primes from 1 to n
 </a>
> Answer
```python
limit = int(input(""))
NumToBeChecked = 2
while (NumToBeChecked < limit):
    prime = True
    counter = 2
    while counter < NumToBeChecked:
        if NumToBeChecked % counter == 0 : 
            prime = False
            break
        counter = counter + 1
        # if prime means that if prime = true
    if prime  : 
        print (NumToBeChecked, end =" ")
    NumToBeChecked = NumToBeChecked +1
```
