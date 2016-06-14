def maximo(l1):
	if l1[0:]<=l1[1:]:
		return l1[max()]
	return l1[0]*maximo(l1[0+1])