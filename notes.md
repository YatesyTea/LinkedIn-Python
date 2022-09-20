# Purpose
This document is for all of the functions that I either wasn't aware of, or hadn't learnt in full.

# Chapter 4
## List Comprehensions
```python
myList = [1,2,3,4,5]
[2*item for item in myList] # This loops through all items in list and multiplies by 2

```

### With Filters
```python
[item for item in myList if item % 10 == 0] # Filters by divisible by 10
```
Could also replace %10==0 with %10<3 if you wanted every 0,1,2 ending number.

### With Functions (And On Strings)
```python
def cleanWord(word):
    return word.replace('.', '').lower() # note this is a chained function
# this means that we're using multiple functions at the same time in thsi case replace and lower case.
    ```
This can be chained with other examples above, keep in mind that readability is king.

## Dictionary Comprehensions
Need to go over again!

## Challenge Plan
Data Structure for different scribes

Data Structure:
* Name
* Starting Position (x,y) values
* Direction of Travel
* How Far It will Move

Funtion:
* Takes in data structure.
* Puts it on board.
* Sets Direction
* Travels baby!


