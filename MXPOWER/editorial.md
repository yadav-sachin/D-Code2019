# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MXPOWER)
[Contest](https://www.codechef.com/DCOD19TS/problems/MXPOWER)

\\\\\\\
Edit these :

*Author:* [Setter's name](https://www.codechef.com/users/author_nick)
*Tester:* [Tester's name](https://www.codechef.com/users/tester_nick)
*Editorialist:* [Editorialist's name](https://www.codechef.com/users/editorialist_nick)
\\\\\


# DIFFICULTY:
EASY

# PREREQUISITES:
Precomputation, Prefix-Sums
# PROBLEM:
Given a square matrix of integers find the maximum value which can be obtained by adding all the elements in a diamond in that matrix. Refer the figure given in the problem for a better idea. 
# QUICK EXPLANATION:
* Precompute the prefix-sums of all the diagonals from left-top to right-bottom as well as left-bottom to right-top.
* Now iterate over all the cells of the matrix, in each iteration consider that cell to be the centre of the diamond and find the maximum valued diamond corresponding to that cell using the calculated prefix sums of diagonals.
* So once we find the maximum corresponding to each centre the maximum value possible is maximum amongst all these calculated values.

# EXPLANATION:
* **Precomputation** : We need to find prefix-sums corresponding to all the diagonals from top-left to bottom-right as well as bottom-left to top-right as shown in the figure. There are $2N-1$ first kind of diagonals and $2N-1$ second kind of diagonals, so totally there are 4N-2 diagonals. Let us maintain 4 $N \times N$ matrices for easy understanding and let each of these represent the diagonals corresponding to the upper half triangle and lower half triangles. So precomp1_upper,  precomp1_lower, precomp2_upper and  precomp2_lower corresponding to red, blue, orange and yellow colours in the figure respectively. Now precomp1_upper[i][j] represents diagonal starting at cell matrix[1][i] and having length j. So starting with length one we can compute prefix sums of this matrix in $O(N^2)$,  similarily precompute for the remaining 3 matrices.


* Now as mentioned in the quick explanation iterate over each cell of the given matrix by considering matrix[i][j] as centre in each iteration and now find maximum value diamond corresponding to that centre. Now to compute for the cell matrix[4][5] in the figure, we initially can figure out the maximum size of diamond possible as $min(i,j,N-i+1,N-j+1)-1$. We start the 0 size diamond which is just the centre so compare the maximum till now with cell value and update maximum also assign this value calculated to a variable now for value[diamond of size 2]=value[diamond of size 1] + [(precomp1_upper[3][4] - precomp1_upper[3][2]) + (precomp1_upper[1][5] - precomp1_upper[1][3]) + (precomp2_upper[7][5] - precomp2_upper[7][3]) + (precomp2_lower[2][5] - precomp2_lower[2][3])] - [matrix[5][3] + matrix[6][4] + matrix[5][5] + matrix[4][4]]. We basically added the surrounding 4 diagonals and subracted the common corners once, as we have added them twice while adding diagonals. Similarily do this for all sizes and all possible centres.





# TIME COMPLEXITY:
* $O(N^3)$

\\\\\\\
Edit these :

# SOLUTIONS:

[details="Setter's Solution"]
indent whole code by 4 spaces
[/details]

[details="Tester's Solution"]
indent whole code by 4 spaces
[/details]

[details="Editorialist's Solution"]
indent whole code by 4 spaces
[/details]

\\\\\\\\\\\\\\\\\\\\\


