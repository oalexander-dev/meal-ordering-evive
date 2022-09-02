from meal_base import Meal


class Lunch(Meal):
    menu = ["Sandwich", "Chips", "Soda"]

    def validate(self) -> list:
        errors = []

        drink_count = 0
        for i in self.order:
            if i == "3":
                drink_count += 1

        if drink_count > 1:
            errors.append(self.menu[2] + " cannot be ordered more than once")
        
        return errors

    def __repr__(self):
        side_count = 0
        drink_count = 0
        for i in self.order:
            if i == "2":
                side_count += 1
            elif i == "3":
                drink_count += 1
        
        output = "Sandwich"

        if side_count == 1:
            output += ", Chips"
        elif side_count > 1:
            output += ", Chips(" + str(side_count) + ")"
    
        if drink_count == 0:
            output += ", Water"
        else:
            output += ", Soda"
        
        return output
