from meal_base import Meal


class Breakfast(Meal):
    menu = ["Eggs", "Toast", "Coffee"]

    def validate(self):
        side_count = 0
        for i in self.order:
            if i == "2":
                side_count += 1

        if side_count > 1:
            self.handle_error(self.menu[1] + " cannot be ordered more than once")

    def __repr__(self):
        drink_count = 0
        for i in self.order:
            if i == "3":
                drink_count += 1
        
        output = "Eggs, Toast"

        if drink_count > 0:
            output += ", Coffee"
    
        if drink_count > 1:
            output += "(" + str(drink_count) + ")"
        
        return output
