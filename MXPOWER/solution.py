for _ in range(int(input())):
	N = int(input())
	grid = [[int(i) for i in input().split()] for j in range(N)]
	gmain = [[0 for i in range(N+2)] for j in range(N+2)]
	gcross = [[0 for i in range(N+2)] for j in range(N+2)]
	for i in range(N):
		for d in range(N-i):
			i_ = i+d
			j_ = d
			gmain[i_][j_] = gmain[i_-1][j_-1] + grid[i_][j_]

	for j in range(1,N):
		for d in range(N-j):
			i_ = d
			j_ = j+d
			gmain[i_][j_] = gmain[i_-1][j_-1] + grid[i_][j_]

	for i in range(N):
		for d in range(i+1):
			i_ = i-d
			j_ = d
			gcross[i_][j_] = gcross[i_+1][j_-1] + grid[i_][j_]

	for j in range(1,N):
		for d in range(N-j):
			i_ = N-d-1
			j_ = j+d
			gcross[i_][j_] = gcross[i_+1][j_-1] + grid[i_][j_]

	mx = -10000000000000000000000000000000
	for i in range(N):
		for j in range(N):
			curr = 0
			for ll in range(min(i,j,N-j-1,N-i-1)+1):
				l = (i-ll),j
				r = (i+ll),j
				t = i,(j-ll)
				b = i,(j+ll)
				if(l==r and t==b and l==b):
					curr = grid[t[0]][t[1]]
				else:
					curr += grid[t[0]][t[1]] + grid[b[0]][b[1]] + grid[l[0]][l[1]] + grid[r[0]][r[1]]
					curr += gmain[r[0]-1][r[1]-1] - gmain[t[0]][t[1]] + gmain[b[0]-1][b[1]-1] - gmain[l[0]][l[1]] + gcross[l[0]+1][l[1]-1] - gcross[t[0]][t[1]] + gcross[b[0]+1][b[1]-1] - gcross[r[0]][r[1]]
				mx = max(mx,curr)
	print(mx)