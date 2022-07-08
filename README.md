# **AirBnB clone - The console :snake:**

![AirBnB Clone](https://github.com/Robert-octavo/holbertonschool-AirBnB_clone/blob/master/img-readme/arb.png)

## Concepts

For this project, we expect you to look at these concepts:

* [Python packages](https://intranet.hbtn.io/concepts/66)
* [AirBnB clone](https://intranet.hbtn.io/concepts/74)

# Background Context
Welcome to the AirBnB clone project! 

Before starting, please read the [**AirBnB**](https://intranet.hbtn.io/rltoken/bw70gxOl1RHBKFAWAR2Y3w) concept page.

## **First step: Write a command interpreter to manage your AirBnB objects.**

This is the first step towards building your first full web application: the **AirBnB clone**. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

* put in place a parent class (called *BaseModel*) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (*User, State, City, Place…*) that inherit from *BaseModel*
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

## **What’s a command interpreter?**

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

# Resources
## **Read or watch:**

* [Python abstract classes](https://intranet.hbtn.io/rltoken/5Dv7z90qa94hYqtPRCe_wA)
* [cmd module](https://intranet.hbtn.io/rltoken/7dj8WbEE01SwPY2Qxy_Ixg)
* [Packages concept page](https://intranet.hbtn.io/concepts/66)
* [uuid module](https://intranet.hbtn.io/rltoken/xJhjt-mMAchNu5WOb2X6DQ)
* [datetime](https://intranet.hbtn.io/rltoken/aEuCrtCn7p5xaYbNRM8ccQ)
* [unittest module](https://intranet.hbtn.io/rltoken/XfOae8zIhTiKYFMTF98qLg)
* [args/kwargs](https://intranet.hbtn.io/rltoken/jQd3P_uSO0FeU6jlN-z5mg)
* [Python test cheatsheet](https://intranet.hbtn.io/rltoken/WPlydsqB0PG0uVcixemv9A)

Python Unit Tests

* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the **unittest module**
* All your test files should be python files (extension: .py)
* All your test files and folders should start by test_
* Your file organization in the tests folder should be the same as your project
* e.g., For *models/base_model.py*, unit tests must be in: *tests/test_models/test_base_model.py*
* e.g., For *models/user.py*, unit tests must be in: *tests/test_models/test_user.py*
* All your tests should be executed by using this command: **python3 -m unittest** discover tests
* You can also test file by file by using this command: *python3 -m unittest tests/test_models/test_base_model.py*
* All your modules should have a documentation *(python3 -c 'print(__import__("my_module").__doc__)')*
* All your classes should have a documentation *(python3 -c 'print(__import__("my_module").MyClass.__doc__)')*
* All your functions (inside and outside a class) should have a documentation *(python3 -c 'print(__import__("my_module").my_function.__doc__)'* and *python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')*
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

# **More Info**
## Execution

Your shell should work like this in interactive mode:


    $ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit

    (hbnb) 
    (hbnb) 
    (hbnb) quit
    $


But also in non-interactive mode: (like the Shell project in C)



    $ echo "help" | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb) 
    $
    $ cat test_help
    help
    $
    $ cat test_help | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb) 
    $


All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

## Installation :hammer_and_wrench:
Clone the repository and run the console.py
```
$ git clone https://github.com/Robert-octavo/holbertonschool-AirBnB_clone.git
```

## Usage :wrench:

|   **Method**   |   **Description**   |
| -------------- | --------------------- |
|[create](./console.py) | Creates object of the given class |
|[show](./console.py) | shows an instance in dict form|
|[all](./console.py) | shows all the instances in string representation |
|[update](./console.py) | Updates an instance based on the class name and id by adding or updating attribute |
|[destroy](./console.py)| Deletes an instance based on the class name and id |
|[count](./console.py)| Retrieve the number of instances of a class |
|[help](./console.py)| Prints information about a specific command of the console|
|[quit/ EOF](./console.py)| Exit the console |

###### Examples

```
./console.py
(hbnb) create User
bb4f4b81-7757-460b-9263-743c9ea6fef6
(hbnb) show User bb4f4b81-7757-460b-9263-743c9ea6fef6
[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106)}
(hbnb) all User
["[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106)}"]
(hbnb) update User bb4f4b81-7757-460b-9263-743c9ea6fef6 name Betty
['User', 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'name', 'Betty']
(hbnb) all User
["[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'name': 'Betty', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106)}"]
(hbnb) destroy User bb4f4b81-7757-460b-9263-743c9ea6fef6
(hbnb) all User
[]
(hbnb) show User
** instance id missing **
(hbnb)

```

###

```
./console.py
(hbnb) User.create
*** Unknown syntax: User.create
(hbnb) User.create()
e6ee5344-04ef-454d-84e4-ba6fc613f1b4
(hbnb) User.all()
["[User] (e6ee5344-04ef-454d-84e4-ba6fc613f1b4) {'id': 'e6ee5344-04ef-454d-84e4-ba6fc613f1b4', 'updated_at': datetime.datetime(2019, 11, 13, 17, 14, 1, 963404), 'created_at': datetime.datetime(2019, 11, 13, 17, 14, 1, 963373)}"]
(hbnb) User.show()
** instance id missing **
(hbnb) User.show(e6ee5344-04ef-454d-84e4-ba6fc613f1b4)
[User] (e6ee5344-04ef-454d-84e4-ba6fc613f1b4) {'id': 'e6ee5344-04ef-454d-84e4-ba6fc613f1b4', 'updated_at': datetime.datetime(2019, 11, 13, 17, 14, 1, 963404), 'created_at': datetime.datetime(2019, 11, 13, 17, 14, 1, 963373)}
(hbnb) User.update("e6ee5344-04ef-454d-84e4-ba6fc613f1b4", "name", "Betty")
['User', '"e6ee5344-04ef-454d-84e4-ba6fc613f1b4"', '"name"', '"Betty"']
(hbnb) User.all()
['[User] (e6ee5344-04ef-454d-84e4-ba6fc613f1b4) {\'"name"\': \'"Betty"\', \'id\': \'e6ee5344-04ef-454d-84e4-ba6fc613f1b4\', \'updated_at\': datetime.datetime(2019, 11, 13, 17, 14, 1, 963404), \'created_at\': datetime.datetime(2019, 11, 13, 17, 14, 1, 963373)}']
(hbnb) User.destroy(e6ee5344-04ef-454d-84e4-ba6fc613f1b4)
(hbnb) User.all()
[]
(hbnb) quit

```
### Authors :fountain_pen:
* Sebastian García - @SebasGTX1 - sebas-0202@hotmail.es
* Robert Ortega - @Robert-octavo - robert.ortega.octavo@gmail.com

### Acknowledgements :raised_hands:
To all the peers that contribuited with their knowledge


