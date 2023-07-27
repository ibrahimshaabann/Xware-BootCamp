# Python Basics :muscle:

`Create two variables x = 10, y = 20 and swap them in two ways`
### First way
```python
x = 10
y = 20
temp = 0
print("\nBefore Switching:")
print("\tx = ", x)
print("\ty = ", y )


print("\nAfter Switching:")
temp = x
x = y
y = temp
print("\tx = ", x)
print("\ty = ", y, "\n\n" )
```

### Second Way :flushed:
```python
x, y = y, x   

```
___
`Guessing game Problem`
**The user will enter a number in the range from zero to 10 and tell him if the number he entered is smaller or larger than the random number**
 
 
```python
 import random

numToBeGuessed = random.randint(1,10)
print(type(numToBeGuessed))
print("\t\nTry to guess a number and we will tell you if the number you've entered is smaller or larger than the specified number")
enterdNumber = int(input("\t\nGuess a number: "))

while enterdNumber != numToBeGuessed :
    if enterdNumber > numToBeGuessed:
        print("\n\t TRY AGAIN! Your NUMBER IS LARGER \n")
        enterdNumber = int(input("\t\nGuess Again: "))

    
    elif enterdNumber < numToBeGuessed:
        print("\n\t TRY AGAIN! Your NUMBER IS SMALLER \n")
        enterdNumber = int(input("\t\nGuess Again: "))


print("\n\t CPNGRATULATIONS !!!! YOU GOT THE CORRECT NUMBER \n")
```
___

### Ways of Printing in python and for loop
```python
for i in range(10):
    print("S" + str(i)) # -> First way
    print (f"Hello {i * i}") # f-string way
```
___
### lists and pass keyword
```python
dates = [2002, 2003, 2004]
N = len(dates)
for i in range(N):
    pass #you want to create for loop and implement it lated so id does not cause error, use pass
    print(dates[i])
```



















