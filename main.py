from cgitb import handler
import sys

from order_handler import OrderHandler

if __name__ == "__main__":
    mealName = sys.argv[1]
    orderItems = sys.argv[2]

    handler = OrderHandler(mealName, orderItems)
    handler.validate__requirements()
    handler.print_order()
