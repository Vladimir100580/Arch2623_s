class User:
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()

    def __repr__(self):
        return f'User({self.name})'   # скопировав к код, мы сможем работать без ошибок


user = User('Спенглер')
print(user)
