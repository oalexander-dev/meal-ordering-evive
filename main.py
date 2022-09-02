from cgitb import handler
import sys

from order_handler import OrderHandler

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Invalid usage. Should be: <Meal Name> 1,2,3,4")
        exit(1)
        
    mealName = sys.argv[1]
    orderItems = sys.argv[2]

    handler = OrderHandler(mealName, orderItems)
    valid = handler.validate__requirements()

    if valid:
        handler.print_order()
