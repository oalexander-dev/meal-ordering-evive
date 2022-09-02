class Meal:
    order = []

    def __init__(self, items):
        self.order = items
    
    def handle_error(self, message: str):
        print("Unable to process: " + message)
        exit(1)