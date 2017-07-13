from operator import attrgetter

class User:

	def __init__(self, name, user_id):
		self.name = name
		self.user_id = user_id

	def __repr__(self):
		return self.name + ": " + str(self.user_id)

Users = [
	User('Bucky', 43),
	User('Faiz', 5),
	User('Sagar', 321),
	User('Theta', 312),
	User('Tuna', 212)
]

for user in Users:
	print(user)

print('------------')
for user in sorted(Users, key=attrgetter('name')):
	print(user)

print('------------------')

for user in sorted(Users, key=attrgetter('user_id')):
	print(user)