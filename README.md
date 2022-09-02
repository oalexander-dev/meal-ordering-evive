# Meal Ordering Application

This is a command-line based Python application which implements the meal ordering
specification for Evive. The `main.py` file is the main driver for the program. The
`order_handler.py` file contains the main driver class which defines the procedure
for handling an order input. The `breakfast.py`, `lunch.py`, and `dinner.py` files
contain the classes which extend the class found in `meal_base.py` to implement 
rules and food items specific to each meal. They have a common interface for the order
handler to work with.

## Installation

Run the following commands to download this source code and install the dependencies
required to run tests. 

**Python3, pip, and virtualenv must be installed on your machine before this step**

**These are the commands for the Linux operating system. They are slightly different on Windows**

```sh
git clone https://github.com/oalexander-dev/meal-ordering-evive.git
cd ./meal-ordering-evive
python3 -m virtualenv venv 
. venv/bin/activate
pip install -r requirements.txt
```

## Usage 

For common use, run the following in the command line. The meal name and item order can be changed,
but should follow the same format.

```sh
python3 main.py Breakfast 1,2,3
```

To run the test suite, run the following commands. The tests are located in `test_order_handler.py`.

```sh 
pytest
```