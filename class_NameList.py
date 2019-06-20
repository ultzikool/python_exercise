class NameList(list):
	def __init__(self, a_name):
		list.__init__([])
		self.name = a_name

johnny = NameList("John Paul Jones")

johnny.append("Bass Player")
johnny.extend(["Composer","Arranger","Musician"])

for attr in johnny:
	print(johnny.name + " is a " + attr + ".")