class Explorer(object):
	def __init__(self, nombre):
		self.nombre = nombre
		self.tabs= []
	

	def agregar_tab(self, nombres):
		self.tabs.append(nombres)

	def mostrartabs(self):
		for i in range (0, len(self.tabs)):
			return self.tabs[i]
	def eliminartab(self, nombres):
		self.tabs.pop(nommbres)

	def eliminartodas(self):
		self.tabs=


