from breakfast import Breakfast


class OrderHandler:
    items_ordered = []
    meal_name = ""
    meal_handler = any

    def __init__(self, meal: str, items: str):
        self.meal_name = meal
        self.items_ordered = items.split(',')

    def validate__requirements(self):
        if self.meal_name == "Breakfast":
            handler = Breakfast(self.items_ordered)

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
            self.handle_error(handler.menu[0] + " cannot be ordered more than once")
        
        handler.validate()

    def print_order(self):
        if self.meal_name == "Breakfast":
            handler = Breakfast(self.items_ordered)
        print(handler)

    def handle_error(self, message: str):
        print("Unable to process: " + message)
        exit(1)
