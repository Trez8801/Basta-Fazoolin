# Come back later and find a way to convert the time from 24hour format to 12 hour format
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    def __repr__(self):
        return f'{self.name} is avaiable from {self.start_time} to {self.end_time}.'

    def calculate_bill(self, purchased_items):
        total = 0
        for i in purchased_items:
            if i in self.items:
                total += self.items[i]
        return 'The total comes out to ' + str(total)
    
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    
    def __repr__(self):
        return f'The location is {self.address}.'
    
    def avaiable_menus(self, time):
        available = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available.append(menu)
        return available

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

####################################### MENUS ##############################################
# Brunch Menu
brunch = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 
        'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 
        'orange juice': 3.50}
brunch_menu = Menu('Brunch', brunch, 1100, 1600)

# Early Bird
early_bird = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
            'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50,
            'mushroom ravioli (vegan)': 13.50, 'coffe': 1.50, 'espresso': 3.00}
early_bird_menu = Menu('Early Bird', early_bird, 1500, 1800)

#Dinner Menu
dinner = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00,
        'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50,
        'coffee': 2.00, 'espresso': 3.00}
dinner_menu = Menu('Dinner', dinner, 1700, 2100)

#Kids Menu
kids = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids_menu = Menu('Kids', kids, 1100, 1700)

#Arepa Menu
arepa = {'areapa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepa_menu =Menu('Arepa', arepa, 1000, 1600)
############################################################################################

#print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
#print(early_bird_menu.calculate_bill(['salumeria plate']))

flagship = Franchise('1232 West End Road', [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
newInstallment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])
arepas_place = Franchise('189 Fitzgerald Avenue', [brunch_menu, early_bird_menu, dinner_menu, kids_menu, arepa_menu])

business = Business("Basta Fazoolin' with my Heart", [flagship, newInstallment])
business2 = Business("Take a' Arepa", [arepas_place])




print(flagship.avaiable_menus(1700))

    