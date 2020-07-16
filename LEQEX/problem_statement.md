"Humankind cannot gain anything without first giving something in return. To obtain, something of equal value must be lost. That is alchemy's first law of Equivalent Exchange. In those days, we really believed that to be the world's one, and only truth."
                                  -- Alphonse Elric
                                      
Now, here we have an equivalent exchange law for triangles which states that two right-angled isosceles triangles of the same colour can be made into a square of the same colour using Alchemy.
  
You are given $N$ right-angled isosceles triangles in which the two equal sides have a length of $1$ unit. The $i^{th}$ of which is described by $C_{i}$, the colour of the triangle.
To create a tower we choose a subarray of length ( $2k+1$, $k\geq0$ ), such that it forms $k$ pairs of triangles with the same colour. Then the two triangles in a pair are joined using Alchemy (following the law of equivalent exchange for triangles) to form squares and these squares are placed one upon other. The last triangle is placed as a roof to the tower. This results in a tower of the height of $k$.
Find the maximum height of the tower that can be formed. 


### Input:
- The first line contains $T$, the number of test cases. Then the test cases follow. 
- For every test case, the first line contains $N$.
- For every test case, the second line contains $N$ integers $C_{i}$ ( $1 \leq i \leq N$).


### Output:
For every test case output a line containing the maximum height of the tower that can be formed.



### Constraints   
- $1 \leq T \leq 100$  
- $1 \leq N \leq 10^{5}$  
- $1 \leq C_{i} \leq 30$ 
- Sum of $N$ over all test cases doesn't exceed $5\times 10^{5}$ 




### Sample Input:
```
4
14
5 4 2 2 3 2 1 3 2 7 4 9 9 9
3
1 2 1
3
1 1 1
5
1 2 3 4 1
```

### Sample Output:
```
3
1
1
0
```

### EXPLANATION:  
- #$1$: The subarray $[2, 2, 3, 2, 1, 3, 2]$ results in a tower of height $3$.
- #$2$: The subarray $[ 1, 2, 1 ]$ results in a tower of height $1$.
- #$3$: The subarray $[ 1, 1, 1 ]$ results in a tower of height $1$. 
- #$4$: The subarrays $[ 1 ]$, $[ 2 ]$ , $[ 3 ]$, $[ 4 ]$ and $[ 1 ]$ all results in a tower of height $0$.
    
![](https://codechef_shared.s3.amazonaws.com/download/HYC/External_contest_images/DCOD2019/problem2.png =500x500)

The above tower is possible by subarray $[2, 2, 3, 2, 1, 3, 2]$ resulting in a height of $3$ in test case $1$.


