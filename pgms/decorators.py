def outer(m):
	mes = m
	def inner(mes):
		print mes
	return inner(mes)
aa = outer()
