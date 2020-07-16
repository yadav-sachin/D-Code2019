In the nation of Amestris, people use transmutation circles for Alchemy, but in different regions of the world people have come up with different methods to harness the power of Alchemy.
In the nation of Creta, people use transmutation figures in the shape of Diamond for Alchemy. Refer to the figure below for Diamond shape.

Elric brothers come to Creta to learn this form of Alchemy. For this Alchemy, the energy from the earth is used to deconstruct and reconstruct. Now Edward is standing on a piece of land, which can be considered a grid of dimensions $N \times N$. For every block of land, the energy it provides in Alchemy is given as $E_{ij}$.
The power of transmutation from a diamond figure is the sum of the energies ( $E_{ij}$ ) of the blocks included in the transmutation diamond.   
  
Given that the diamond figure must lie inside the grid, find the maximum power that can be generated from any diamond transmutation figure.

![](https://codechef_shared.s3.amazonaws.com/download/HYC/External_contest_images/DCOD2019/problem3.png)   

The above figure shows a few diamonds of different sizes that can be formed in the grid.


### Input:
- The first line contains $T$, the number of test cases. Then the test cases follow. 
- For each test case, the first line contains $N$.
- Then $N$ lines follow. The $j^{th}$ integer in the $i^{th}$ line is $E_{ij}$.


### Output:
For each test case, print a single line answering the maximum power from a diamond in the grid.


### Constraints 
- $1\leq T\leq 100$  
- $ 1 \leq N \leq 100$  
- $| E_{ij} | \leq 10^{9}$


### Sample Input:
```
3
1
-5
2
-1 1
1 1
3
-10 5 -50
26 -1 10
0 6 45
```

### Sample Output:
```
-5
1
46
```