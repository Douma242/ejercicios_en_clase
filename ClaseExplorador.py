class Explorer(object):
	def __init__(self, nombre, tabs, url):
		self.nombre = nombre
		self.tabs= []
		self.urls= []
	

	def agregar_tab(self, nombres, url):
		self.tabs.append(nombres)
		self.urls.append(url)

	def mostrartabs(self):
		for i in range (0, len(self.tabs)):
			return self.tabs[i]
	
	def eliminartab(self, nombres):
		self.tabs.pop(nommbres+1)
		self.urls.pop(nommbres+1)

	def eliminartodas(self):
		self.tabs= False


