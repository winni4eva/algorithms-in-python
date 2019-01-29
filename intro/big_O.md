# Big O Notations => Order Of ()

- definition: Measures how a computer algorithm scales as the amount of data increases. 
- How will the an algorithm behave when handling a 15 element array comapred to a 150,000 element array
- NB: Its not always a measure of speed but a measure of how a computer algorithm scales
- For example lets say we have the formula 
- 45n^3 + 20n^2 + 19 = ? let n = 1 => ans = 84 ; Our goal here is to find the algorithm that has the largest impact on our answer
- lets increase n to 2
- 45n^3 + 20n^2 + 19 = ? let n = 2 => ans = 459 ;
- lets increase n to 10
- 45n^3 + 20n^2 + 19 = ? let n = 10 => ans = 47,019 ;
- If we analyze all the components of this eqn we would quickly realise that 
- 45n^3 when n = 10; equals 45,000, making 20n^2 and 19 almost virrelevant with regards to the result of the equation
- Even the 45 here does not matter compared to the [n^3]
- We can summarise all this and say the above equation has the order of O(N^3), because it has the largest impact on our equation
- We'll discus
- Order of O(1), O(N), O(N^2), O(log N), O(n log N)