# Assignment Operators

This type of operators assign values to variables or variables to variables.

## Assignment:

- **`=`** ----> assign a value to a variable or a variable to a variable.

_ex:_ 

```python
x = 10
y = 5
aux = x
x = y
y = aux
print(x, y)
```
> OUTPUT: 5, 10

## Addition Assignment:

- **`+=`** ----> add and assign it in the same time.

_ex:_ 

```python
x = 10
y = 5
x += y
print(x)
```
> OUTPUT: 15

It is same as `x = x + y`


## Subtraction Assignment:

- **`-=`** ----> subtract one number by another and assign it in the same time.

_ex:_ 

```python
x = 10
y = 5
x -= y
print(x)
```
> OUTPUT: 5

It is same as `x = x - y`


## Multiplication Assignment:

- **`*=`** ----> multiply a number by another and assign it in the same time.

_ex:_ 

```python
x = 10
y = 5
x *= y
print(x)
```
> OUTPUT: 50

It is same as `x = x * y`


## Division Assignment:

- **`/=`** ----> divide a number by other, but returning a float number and assign it in the same time.

_ex:_ 

```python
x = 10
y = 5
x /= y
print(x)
```
> OUTPUT: 2.0


- **`//=`** ---> divide a number by other too. However, returning a integer and assign it in the same time.

_ex:_ 

```python
x = 10
y = 5
x //= y
print(x)
```
> OUTPUT: 2


- **`%=`** ---> return the remainder of the divide operation between the given numbers and assign it in the same time.

_ex0:_ 

```python
x = 10
y = 5
x %= y
print(x)
```
> OUTPUT: 0


_ex1:_ 

```python
x = 13
y = 5
x %= y
print(x)
```
> OUTPUT: 3


## Exponentiation Assignment:

- **`**=`** ----> exponentiate a number to another and assign it in the same time.

_ex:_ 

```python
x = 2
y = 3
x = x ** y
print(x)
```
> OUTPUT: 8



