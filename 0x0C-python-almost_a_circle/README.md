# Python - Almost a circle :page_with_curl: 0x0C-python-almost_a_circle

## About this project:
In this project i learnt,practiced and reviewed everything i have learnt in python's
object-oriented programming, by connecting classesto represent rectangles and squares.
I learnt and practiced:
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is `args` and how to use it
- What is `kwargs` and how to use it
- How to handle named arguments in a function

The following function tools were used in creating all the classes and testing its functionality:
- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file
- `args`/`kwargs`
- JSON and CSV
- serialization/deserialization
## Task files descriptions
### Classes:
* [models](models) - folder containing all the classes and corresponding subclass
  * [base.py](models/base.py) - Contains the base class `Base`
  * [rectangle.py](models/rectangle.py) - Contains the class `Rectangle`, a subclass of `Base`
  * [square.py](models/square.py) - Contains the class `Square`, a subclass of `Rectangle`

### Tests:
* [tests](tests) - folder containing the test models
  * [test_models](tests/test_models) - Folder containing test files for the classes
    * [test_base.py](tests/test_models/test_base.py) - Contains all tests pertaining to class `Base`
    * [test_rectangle.py](tests/test_models/test_rectangle.py) - Contains all tests pertaining to class `Rectangle`
    * [test_square.py](tests/test_models/test_square.py) - Contains all tests pertaining to class `Square`
