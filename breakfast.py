from meal_base import Meal


class Breakfast(Meal):
    menu = ["Eggs", "Toast", "Coffee"]

    def validate(self) -> list:
        errors = []

        side_count = 0
        for i in self.order:
            if i == "2":
                side_count += 1

        if side_count > 1:
            errors.append(self.menu[1] + " cannot be ordered more than once")
        
        return errors

    def __repr__(self):
        drink_count = 0
        for i in self.order:
            if i == "3":
                drink_count += 1
        
        output = "Eggs, Toast, "

        if drink_count == 0:
            output += "Water"

        elif drink_count == 1:
            output += "Coffee"
    
        else:
            output += "Coffee(" + str(drink_count) + ")"
        
        return output
