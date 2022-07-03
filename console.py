#!/usr/bin/python3
"""Console"""

from ast import Store
import cmd
from click import argument, prompt
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Command Interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Type EOF to exit the command interpreter"""
        return True

    def do_quit(self, arg):
        """Type Exit to exit the command interpreter"""
        return True

    def emptyline(self):
        """Do not execute nothing """
        pass

    def do_create(self, args):
        """Creates a new Instance"""
        if not (args):
            print("** class name missing **")
        elif args not in storage.class_arb():
            print("** class doesn't exist **")
        else:
            ins = storage.class_arb()[args]()
            ins.save()
            print(ins.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the
        class name and id
        Exmaple: (hbnb) show User a8d30b54-af4d-401e-ba78-4c11c8294264
        """
        if not (args):
            print("** class name missing **")
        else:
            """Split args to get the class name(user) and the id(user_id)"""
            arguments = args.split(' ')
            if len(arguments) != 2:
                print("** instance id missing **")
            elif arguments[0] not in storage.class_arb():
                print("** class doesn't exist **")
            else:
                for key, values in storage.all().items():
                    if arguments[1] == values.id:
                        print(values)
                        return
                print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        Exmaple: (hbnb) destroy User a8d30b54-af4d-401e-ba78-4c11c8294264
        """
        if not (args):
            print("** class name missing **")
        else:
            """Split args to get the class name(user) and the id(user_id)"""
            arguments = args.split(' ')
            if len(arguments) != 2:
                print("** instance id missing **")
            elif arguments[0] not in storage.class_arb():
                print("** class doesn't exist **")
            else:
                for key, values in storage.all().items():
                    if arguments[1] == values.id:
                        del storage.all()[key]
                        storage.save()
                        return
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name
        """
        arg = args.split(' ')
        if arg[0] not in storage.class_arb() and arg[0]:
            print("** class doesn't exist **")
        else:
            my_obj_list = []
            for key, values in storage.all().items():
                if values.__class__.__name__ == arg[0] or not arg[0]:
                    my_obj_list.append(str(values))
            print(my_obj_list)
            return

    def do_updated(self, args):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
