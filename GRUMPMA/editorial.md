# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PROBLEMCODE)
[Contest](https://www.codechef.com/CONTESTCODE/problems/PROBLEMCODE)

*Author:* [Sachin Yadav](https://www.codechef.com/users/sachin_yadav)
*Tester:* [Kishen Gowda](https://www.codechef.com/users/tester_nick), [Taranpreet](https://www.codechef.com/users/tester_nick)
*Editorialist:* [Sachin Yadav](https://www.codechef.com/users/sachin_yadav)

# DIFFICULTY:
SIMPLE

# PREREQUISITES:
DP

# PROBLEM:
You are given an array $A$ of $N$ numbers. Given $M$, find the number of subsequences of length $K$ which satisfies the following property.  
For subsequence $seq$,    
 $$ seq[i] \% M = i \% M $$ 
,where $i$ is the **1-based index** of the subsequence.

# QUICK EXPLANATION:
We maintain an array of length of $K$, where the $i_{th}$ index stores the number of subsequences of length $i$ encountered till now which satisfies the given property. Initially the array is zero. Now at each array element we update the array accordingly. Finally arr[K] gives the answer.

# EXPLANATION:
We start here with initializing an array $L$ of length K, where the i_th index number would store the number of subsequences of length i encountered till now which satisfies the given property.
Intially it is set to zero.
Now we start iterating over the array and at every step we will update the array. 

Suppose we are at index j of array, and arr[j]%M=y.
So now I can append arr[j] to all subsequences of length j-1 $ \pm $

# ALTERNATE EXPLANATION:
Could contain more or less short descriptions of possible other approaches.

# SOLUTIONS:

[details="Setter's Solution"]
C++1
[/details]

[details="Tester's Solution"]
indent whole code by 4 spaces
[/details]

[details="Editorialist's Solution"]
indent whole code by 4 spaces
[/details]