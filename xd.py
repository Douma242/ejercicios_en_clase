def maximo(l1):
	if len(l1) == 1:
		return l1[0]
	sl1= l1[1:]
	smax= maximo(sl1)
	if l1[0] > smax:
		return	l1[0]
	return	smax	