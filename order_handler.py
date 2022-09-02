from breakfast import Breakfast


class OrderHandler:
    items_ordered = []
    meal_name = ""
    meal_handler = any

    def __init__(self, meal: str, items: str):
        self.meal_name = meal
        self.items_ordered = items.split(',')
        if self.meal_name == "Breakfast":
            handler = Breakfast(self.items_ordered)
            self.meal_handler = handler

    def validate__requirements(self):
        # Each meal requires exactly one main and at least one side
        main_count = 0
        side_count = 0
        for i in self.items_ordered:
            if i == "1":
                main_count += 1
            elif i == "2":
                side_count += 1
        
        if main_count == 0:
            self.handle_error("Main is missing")
        
        if side_count == 0:
            self.handle_error("Side is missing")
        
        if main_count > 1:
            self.handle_error(self.meal_handler.menu[0] + " cannot be ordered more than once")
        
        self.meal_handler.validate()

    def print_order(self):
        print(self.meal_handler)

    def handle_error(self, message: str):
        print("Unable to process: " + message)
        exit(1)
