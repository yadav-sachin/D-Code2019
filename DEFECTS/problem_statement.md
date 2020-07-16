Greed has an invincible shield due to which the attacks of Edward would not work on him. But Edward being a prodigy has caught onto the flaws in Greed's shield. The shield is made up of the same fundamental element, by which all other life forms are formed, Carbon.
  
He observed that Greed's shield can be represented as a grid of carbon clusters with $N$ rows and $M$ columns. Each block on the grid represents the orientation of the carbon cluster, either $0$ or $1$.
In each move, Edward uses alchemy on a given carbon cluster and reverses the orientation of the clusters by flood filling on the chosen carbon cluster (diagonal filling is not allowed). If the initial orientation was $1$, now the orientation will be $0$ and vice-versa.

Now he selects a block in the shield and performs this move on it repetitively until the entire shield carbon clusters have a single orientation, either $1$ or $0$. The block from which it takes the minimum number of moves to make all clusters of same orientation is the weakest point of the shield.
Find the minimum number of moves to make all clusters of same orientation given that you have the freedom to choose any cluster to start from in the beginning.


### Input:
- The first line contains $T$, the number of test cases. Then the test cases follow. 
- For each test case, the first line contains $N$ and $M$.
- For each test case, $N$ lines follow, containing $M$ integers ($0$ or $1$) depicting the orientation of that cluster.


### Output:
For each test case print a single line answering the minimum number of moves required to make the complete shield of single orientation.


### Constraints 
- $1\leq T\leq 10$  
- $1 \leq N,M \leq 50$


### Sample Input:
```
3
6 6
0 0 0 1 1 1
0 0 0 1 1 0
0 0 0 0 0 0
1 1 1 1 1 1
1 1 0 0 0 0
1 1 1 0 0 0
4 3
1 1 1
1 1 1
1 1 1
1 1 1
2 4
0 0 0 0
1 1 1 1
```

### Sample Output:
```
2
0
1
```