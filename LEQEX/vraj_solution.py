from collections import defaultdict
for _ in range(int(input())):
	N = int(input())
	ddmn = defaultdict(int)
	ddmx = defaultdict(int)
	C_l = [1<<(int(i)-1) for i in input().split()]
	C_lx = [0 for i in range(len(C_l)+1)]
	for i in range(len(C_l)):
		C_lx[i] = C_lx[i-1] ^ C_l[i]
	ddmn[0] = -1
	for i in range(len(C_lx)-1):
		if C_lx[i] not in ddmn:
			ddmn[C_lx[i]] = i
		ddmx[C_lx[i]] = i
	tset = [1<<j for j in range(30)]
	mxl = 0
	for i in ddmx:
		for j in tset:
			target = i^j
			if target in ddmn:
				mxl = max(mxl,(ddmx[i] - ddmn[target])//2)
	print(mxl)