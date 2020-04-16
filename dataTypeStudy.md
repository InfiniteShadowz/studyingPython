# dataTypeStudy

## Types: 
- **integer(`int`)** ex: 2 ; 4 ; 5 ; 1322; 2313131;

- **string(`str`)** ex: "The quick brown fox jumps over the lazy dog” ; "oh" ; "i";

- **float(`float`)** ex: 1.0 ; 3.141592 ; 1.61803398875 ; 344422.43;


## Maths:

- **`/`** ----> used to divide a number by other, but returning a float number --> ex: 4/2 = 2.0;

- **`//`** ---> used to divide a number by other too, however returning a integer --> ex: 11//3 = 3;

- **`%`** ---> the percent symbol is used to return the remainder of the divide operation --> ex: 11%3 = 2;


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


