from distutils.log import error
from breakfast import Breakfast
from dinner import Dinner
from lunch import Lunch


class OrderHandler:
    items_ordered = []
    meal_name = ""
    meal_handler = any

    def __init__(self, meal: str, items: str):
        self.meal_name = meal
        self.items_ordered = items.split(',')

        if self.meal_name == "Breakfast":
            handler = Breakfast(self.items_ordered)
        elif self.meal_name == "Lunch":
            handler = Lunch(self.items_ordered)
        elif self.meal_name == "Dinner":
            handler = Dinner(self.items_ordered)
        else:
            print("Invalid meal name. Make sure it is capitalized")
            exit(1)
        
        self.meal_handler = handler

    def validate__requirements(self):
        errors = []

        # Each meal requires exactly one main and at least one side
        main_count = 0
        side_count = 0
        for i in self.items_ordered:
            if i == "1":
                main_count += 1
            elif i == "2":
                side_count += 1
        
        if main_count == 0:
            errors.append("Main is missing")
        
        if side_count == 0:
            errors.append("Side is missing")
        
        if main_count > 1:
            errors.append(self.meal_handler.menu[0] + " cannot be ordered more than once")
        
        meal_errors = self.meal_handler.validate()

        for e in meal_errors:
            errors.append(e)
        
        if len(errors) != 0:
            error_output = "Unable to process: " + errors[0]
            
            for i, e in enumerate(errors):
                if i == 0:
                    continue
                error_output += ", " + e.lower()
            
            print(error_output)
            exit(1)

    def print_order(self):
        print(self.meal_handler)
