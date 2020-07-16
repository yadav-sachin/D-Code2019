Edward Elric is chasing after Scar. To stop Edward, Scar creates $N$ barriers in the way. Given the height of Edward is $H$, he can duck by $Y_{1}$ and can jump by height $Y_{2}$. There are barriers of two types namely $t$ = 1 and $t$  = 2. The barriers of type 1 start from a height $X$ above the ground while the barriers of type 2 start from the ground and extend up to the height $X$ above the ground. Edward has an alchemic life force of $L$, and whenever he can't pass a barrier by bending or jumping (considered passed even when the barrier just touches him), he uses Alchemy to break the barrier. However, this costs him a single alchemic life force.  
If after breaking a barrier no life force is left, Edward gets completely exhausted, unable to pass that barrier.   
How many barriers can Edward cross?   

**Warning**: Don't call him a pipsqueak if his height is too short. 

![](https://codechef_shared.s3.amazonaws.com/download/HYC/External_contest_images/DCOD2019/problem1.png =500x500)
             
### Input:

- The first line contains $T$, the number of test cases. Then the test cases follow. 
- For each test case, the first line contains five integers $N$, $H$, $Y_{1}$, $Y_{2}$ and $L$.
- The next $N$ lines, each contain two integers $t_{i}$ and $X_{i}$ for the $i^{th}$ barrier.
  
### Output:
For each test case print a single line containing the number of barriers Edward can pass.
  
### Constraints 
- $1\leq T\leq100$   
- $1\leq N\leq10^{3}$    
- $2 \leq H\leq10^{3}$   
- $1\leq Y_{1}< H$   
- $1\leq Y_{2}\leq10^{3}$    
- $1\leq L\leq N$    
- $1\leq X_{i}\leq 10^{3}$ 
  
### Sample Input:
```
3
6 5 1 2 3
2 2
2 1
1 10
2 8
2 4
1 2
1 4 2 5 1
2 6
6 5 1 2 3
2 2
2 1
1 10
2 8
2 4
1 6
```
  
### Sample Output:
```
5
0
6
```