from typing import List
from meal_base import Meal


class Dinner(Meal):
    menu = ["Steak", "Potatoes", "Wine", "Cake"]

    def validate(self) -> list:
        errors = []

        dessert_count = 0
        drink_count = 0
        for i in self.order:
            if i == "4":
                dessert_count += 1
            elif i == "3":
                drink_count += 1

        if dessert_count == 0:
            errors.append("Dessert is missing")
        
        if drink_count > 1:
            errors.append(self.menu[2] + " cannot be ordered more than once")
        
        return errors

    def __repr__(self):
        drink_count = 0
        for i in self.order:
            if i == "3":
                drink_count += 1
        
        output = "Steak, Potatoes, "

        if drink_count == 1:
            output += "Wine"
    
        output += "Water, Cake"
        
        return output
