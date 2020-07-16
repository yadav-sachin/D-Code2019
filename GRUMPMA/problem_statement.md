After the death of their mother, Alphonse and Edward now live with Pinako and Winry.     
Pinako is worried about their obsession with Alchemy, that they don't give attention to their studies.
   
So to improve their maths solving ability, every day she gives a mathematical problem for the boys to solve. They can go out to practice Alchemy only after they have solved the problem.
Help them by solving the given problem, so that they can go early today for their Alchemy practice.    
      
You are given an array $A$ of $N$ numbers. Given $M$, find the number of subsequences of length $K$ which satisfies the following property.  
For subsequence $seq$,    
 $$ seq[i] \% M = i \% M $$ 
,where $i$ is the **1-based index** of the subsequence.     
As the output may be very large, answer the result in $1000000007$ modulo form.     
       
**PS**: We also proposed the idea of making a look-alike clone through alchemy and keeping it in front of the study table. But it seems impossible to convince Edward to make a clone of his exact same height, not taller than him. So solving the problem for him was a better choice.   
  

### Input:
- The first line contains $T$, the number of test cases. Then the test cases follow. 
- For every test case, the first line contains $N$, $K$ and $M$.
- For every test case, the second line contains $N$ integers $A_{i}$ ( $1 \leq i \leq N$).


### Output:
For every test case output a line containing the number of subsequences of length $K$ satisfying the given property.


### Constraints 
- $1 \leq T \leq 100$  
- $1 \leq N \leq 10^{4}$  
- $1 \leq K \leq N$  
- $\lceil \frac{K}{100}\rceil \leq M \leq  100\times K$    
- $0 \leq A_{i} \leq 10^{9}$    


### Sample Input:
```
1
12 4 3
4 5 6 7 1 4 6 9 0 0 10 2
```

### Sample Output:
```
8
```


### EXPLANATION:  
The subsequences of length $4$, satisfying the given criteria are $[4, 5, 6, 7]$, $[4, 5, 6, 10]$, $[4, 5, 6, 10]$, $[4, 5, 6, 1]$, $[4, 5, 9, 10]$ ,$[4, 5, 6, 4]$ , $[4, 5, 0, 10]$ and $[4, 5, 0, 10]$. This accounts for the total $8$ subsequences.

