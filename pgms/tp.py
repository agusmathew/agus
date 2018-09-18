def bomberMan(n, grid):	
	b=[]
	for i in grid:
		a=list(i)
		b.append(a)
	for j in range(1,n+1):
		if j == 1:
			
			print 5555555555555
			for k in range(len(b)):
				for l in range(len(b[0])):
					b[k][l].replace('0','1')

		elif not j%2:
			print b
			for k in range(len(b)):
				for l in range(len(b[0])):
					b[k][l].replace('1','2')
					b[k][l].replace('.','0')
					
		else:
			for k in range(len(b)):
				for l in range(len(b[0])):
					if b[k][l] == '2':
						b[k,l] = '.'
						b[k+1,l] = '.'
						b[k,l+1] = '.'
						b[k-1,l] = '.'
						b[k,l-1] = '.'
					b[k][l].replace('0','1')
					b[k][l].replace('1','2')
	kl = ["".join(n) for n in b]
	return kl
rcn = raw_input().split()

r = int(rcn[0])

c = int(rcn[1])

n = int(rcn[2])

grid = []

for _ in xrange(r):
	grid_item = raw_input()
	grid.append(grid_item)

result = bomberMan(n, grid)
print result,n,grid