class Potion():
	def __init__(self, potion_name):
		self.name = potion_name
		self.description = None
	def get_potion_description(self, potion_description):
		self.description = potion_description
	def set_potion_description(self):
		return self.description
	def describe_item(self)
		print(self.description)