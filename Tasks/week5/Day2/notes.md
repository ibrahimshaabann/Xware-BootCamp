In Python, *args is used to pass an arbitrary number of arguments to a function. It's worth mentioning that the single asterisk( * ) is the most important element, the word arg is just a naming convention we can name it anything it will work as long as we have a ( * ) before it.

The *args parameter is helpful in tackling such programming issues. Using *args parameter gives the function ability to accepts any number of positional arguments

>> input
```python
def total_sum(*args):
    sum = 0
    for num in args:
        sum += num
    print("Sum :", sum)

total_sum(3, 4)
total_sum(3, 6, 7, 8,2)
total_sum(3, 7, 8,2)
total_sum(3, 8, 9)
```

>>output

``python
Sum : 7
Sum : 26
Sum : 20
Sum : 20

```


Using **kwargs In Python
Keyword arguments allow passing arguments as parameter names. In order to design a function which takes an arbitrary number of keywords arguments **kwargs in used as a parameter. It's worth noting that the double astrick(**) is the key element here kwargs is just a convention you can use any word.


>code

```python
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1, b=2, c="Some Text")
```
>output


```python
{'a': 1, 'b': 2, 'c': 'Some Text'}
```
