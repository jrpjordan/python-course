# How to define a function, and also default values
def greet_user(username='user', age=20):
    print(f"Hello {username.title()}, I am {age} year old!")

# Calling function
greet_user('JoseR', 34)

# We can break the order of the arguments
greet_user(age=34, username="joser")


# Functions returning values and optional value, in this example middle name is marked as optional
def get_formatted_name(first_name, last_name, middle_name=''): # we must move optional parameters to the end
    full_name = f"{first_name} {last_name}"

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# We can also return dictionaries to enhace the power of the function
def get_game(title, price, platform=''):
    game = {'title': title, 'price': price, 'platform': platform}
    return game

game = get_game('dragon ball', 54.99, 'ps4')

# when you pass a list as a parameter, list can be modified

# arbitrary number of arguments
def make_pizza(*toppings):
    print(toppings)

make_pizza('mushrooms', 'green peppers', 'extra cheese')


# arbitrary keyword arguments
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('alber', 'einstein', location='princeton', field='physics')
print(user_profile)