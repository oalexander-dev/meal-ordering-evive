from order_handler import OrderHandler


def test_simplebreakfast(capsys):
    handler = OrderHandler("Breakfast", "1,2,3")
    handler.validate__requirements()
    handler.print_order()

    output = capsys.readouterr()

    assert(output.out.strip()) == "Eggs, Toast, Coffee"
