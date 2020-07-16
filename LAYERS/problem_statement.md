With the help of Sheska, Edward now has the research notes of Dr. Marcho. To prevent the secret of Philosopher stone falling into the wrong hands, Marcho has encoded the secret in the form of a list of triplets of numbers. Edward remembers that Dr. Marcho gave him a hint while he was leaving, "Sometimes you should try transmutation rectangles instead of circles, maybe they are better for making philosopher stones". Edward first thought it to be a joke, but he has got the hint now. He interprets each triplet as length, breadth and colour of rectangle centred at the origin. Given below is his interpretation to decode the numbers.
   
You are given $N$ rectangles of different dimensions and colours. Each of the rectangles has three properties, the colour $C_{i}$, the length $L_{i}$ and breadth $B_{i}$. The length $L$ and the breadth $B$ of these rectangles are even and all the rectangles are centred at the origin. The rectangles are placed one over the other. The rectangle $i$, is obscured by the rectangles $j$ if $j$ > $i$ , that is only the colour of the top rectangle is visible in the overlapping region.  
   
Edward believes that the ratio of the area of each colour in the final figure is pointing to some ratio of ingredients for making philosopher stone, which takes him more closer to the philosopher stone.
  
Given the colours and the dimensions of the rectangles, find out how many unit squares of each colour are visible in the final figure.


### Input:
- The first line contains $T$, the number of test cases. Then the test cases follow. 
- For each test case, the first line consists of $N$ (number of rectangles) and $C$ (the number of colours).
- For each test case, $N$ lines follows containing three integers $L_{i}$, $B_{i}$ and $C_{i}$. 



### Output:
For each test case, the output must contain a single line with $C$ integers representing the number of unit squares of each colour from $1$ to $C$ in the final figure.


### Constraints 
- $1 \leq T \leq 50$  
- $1 \leq N \leq 10^{5}$  
- $1 \leq C \leq 100$  
- $2 \leq L_{i} \leq 10^{9}$  
- $2 \leq B_{i} \leq 10^{9}$ 
- $L_{i}$ and $B_{i}$ are even 
- $1 \leq C_{i} \leq C$
- Sum of $N$ over all test cases doesn't exceed $10^{6}$

### Sample Input:
```
1
5 4
2 2 1
2 8 3
10 2 1
8 4 2
4 6 4
```
  

### Sample Output:
```
4 16 4 24
```

### EXPLANATION:   
![](https://codechef_shared.s3.amazonaws.com/download/HYC/External_contest_images/DCOD2019/image3.png =500x432)
    
In the above figure, Red is used for colour $4$,  Yellow for colour $3$, Blue for colour $2$ and Green for colour $1$.