#dataTypeStudy

###Types: 
-**integer(int)** ex: 2 ; 4 ; 5 ; 1322; 2313131;
-**string(str)** ex: "The quick brown fox jumps over the lazy dog” ; "oh" ; "i";
-**float(float)** ex: 1.0 ; 3.141592 ; 1.61803398875 ; 344422.43;


###Maths:
-**/** ----> used to divide a number by other, but returning a float number --> ex: 4/2 = 2.0;
-**//** ---> used to divide a number by other too, however returning a integer --> ex: 11//3 = 3;
-**%** ---> the percent symbol is used to return the remainder of the divide operation --> ex: 11%3 = 2;


###Convertion: 
--------------------------------/
>myBMI = 19.1932332
>myBMIinteger = int(myBMI)
--------------------------------/

###The len() function:
the len() function only works using string(str).
ex:
--------------------------------/
>>>text = "hello, world!"
>>>len(text)
13
--------------------------------/

and if another type is assigned...:
--------------------------------------------------/
>>>myBMI = 19.1932332
>>>len(myBMI)
*TypeError*: object of type 'float' has no len()
--------------------------------------------------/
...it returns a TypeError.

YET it has a solution. Convert. float to string:
--------------------------------------------------/
>>>myBMI = 19.1932332
>>>myBMIstr = str(myBMI)
>>>len(myBMIstr) --or len(str(myBMI)) if in prompt
10
--------------------------------------------------/

