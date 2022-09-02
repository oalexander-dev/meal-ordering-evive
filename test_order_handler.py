from order_handler import OrderHandler


def use_handler(meal, items):
    handler = OrderHandler(meal, items)
    valid = handler.validate__requirements()
    if valid:
        handler.print_order()

# TESTING BREAKFAST HANDLER AND COMMON FUNCTIONALITY
def test_simple_breakfast(capsys):
    use_handler("Breakfast", "1,2,3")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Eggs, Toast, Coffee"

def test_backwards_input_breakfast(capsys):
    use_handler("Breakfast", "2,3,1")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Eggs, Toast, Coffee"

def test_multiple_drink_breakfast(capsys):
    use_handler("Breakfast", "1,2,3,3,3")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Eggs, Toast, Coffee(3)"

def test_missing_side_breakfast(capsys):
    use_handler("Breakfast", "1")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Unable to process: Side is missing"

def test_missing_main_breakfast(capsys):
    use_handler("Breakfast", "2,3")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Unable to process: Main is missing"

def test_missing_side_and_drink_breakfast(capsys):
    use_handler("Breakfast", "3,3")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Unable to process: Main is missing, side is missing"

def test_no_drink_breakfast(capsys):
    use_handler("Breakfast", "1,2")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Eggs, Toast, Water"

def test_duplicate_main_breakfast(capsys):
    use_handler("Breakfast", "1,1,2")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Unable to process: Eggs cannot be ordered more than once"

def test_duplicate_main_no_side_breakfast(capsys):
    use_handler("Breakfast", "1,1")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Unable to process: Side is missing, eggs cannot be ordered more than once"


# TESTING LUNCH RULES
def test_simple_lunch(capsys):
    use_handler("Lunch", "1,2,3")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Sandwich, Chips, Soda"

def test_no_drink_lunch(capsys):
    use_handler("Lunch", "1,2")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Sandwich, Chips, Water"

def test_missing_side_lunch(capsys):
    use_handler("Lunch", "1")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Unable to process: Side is missing"

def test_missing_main_lunch(capsys):
    use_handler("Lunch", "2,3")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Unable to process: Main is missing"

def test_duplicate_main_lunch(capsys):
    use_handler("Lunch", "1,1,2")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Unable to process: Sandwich cannot be ordered more than once"

def test_duplicate_side_lunch(capsys):
    use_handler("Lunch", "1,2,2,2")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Sandwich, Chips(3), Water"

def test_empty_lunch(capsys):
    use_handler("Lunch", "")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Unable to process: Main is missing, side is missing"


# TESTING DINNER RULES
def test_simple_dinner(capsys):
    use_handler("Dinner", "1,2,3,4")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Steak, Potatoes, Wine, Water, Cake"

def test_no_drink_dinner(capsys):
    use_handler("Dinner", "1,2,4")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Steak, Potatoes, Water, Cake"

def test_missing_side_dinner(capsys):
    use_handler("Dinner", "1,4")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Unable to process: Side is missing"

def test_missing_main_dinner(capsys):
    use_handler("Dinner", "2,3,4")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Unable to process: Main is missing"

def test_duplicate_main_dinner(capsys):
    use_handler("Dinner", "1,1,2,4")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Unable to process: Steak cannot be ordered more than once"

def test_duplicate_side_missing_dessert_dinner(capsys):
    use_handler("Dinner", "1,2,2,2")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Unable to process: Potatoes cannot be ordered more than once, dessert is missing"

def test_no_dessert_dinner(capsys):
    use_handler("Dinner", "1,2,3")
    output = capsys.readouterr()
    assert(output.out.strip()) == "Unable to process: Dessert is missing"