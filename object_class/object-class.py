class Info:
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return self.value

	def new_object(self, new_value):
		return self.__class__(new_value)


info1 = Info("value1")
print(dir(info1))
print(type(info1))
print(info1)

info2 = info1.new_object("value2")
print(dir(info2))
print(type(info2))
print(info2)