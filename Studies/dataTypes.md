# Data Type

## Types: 

### Numeric Types:
- **integer(`int`)** ex: 2 ; 4 ; 5 ; 1322; 2313131;

- **float(`float`)** ex: 1.0 ; 3.141592 ; 1.61803398875 ; 344422.43;

### Text Types:
- **string(`str`)** ex: "The quick brown fox jumps over the lazy dog” ; "oh" ; "i";


## Convertion: 

It is possible to convert some types to others. In this example `float` is converted to `int`:

```python
myBMI = 19.1932332
myBMIinteger = int(myBMI)
```

> OUTPUT: 19


## The `len()` function:

the `len()` function only works using `str` ~~and colections such as lists, tuples, dictionaries and arrays, but this is a introduction... so pretend you didn´t read this, please.~~

_ex:_
```python
text = "hello, world!"
print(len(text))
```
> OUTPUT: 13


and if another type is assigned...:

```python
myBMI = 19.1932332
len(myBMI)
```

> OUTPUT: _*TypeError*: object of type 'float' has no len()_

...it returns a _**`TypeError`**!_



YET it has a solution. _Convert. `float` to `string`:_

```python
myBMI = 19.1932332
myBMIstr = str(myBMI)
print(len(myBMIstr)) #or print(len(str(myBMI))) 
```
> OUTPUT: 10


## The `type()` function: 

the `type()` function is used to get the data type of any object:

```python
x = "Hello"
print(type(x))
```
> OUTPUT: <class 'str'>











