#!/usr/bin/python3
"""My first console - the command interpreter"""
import cmd
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def precmd(self, args):
        """method to preprocess the command input"""
        commands = ['create', 'show', 'update', 'all', 'destroy', 'count']
        if '.' in args and '(' in args and ')' in args:
            clss = args.split('.')
            comand = clss[1].split('(')
            arguments = comand[1].split(')')
            if clss[0] in storage.class_arb() and comand[0] in commands:
                args = comand[0] + ' ' + clss[0] + ' ' + arguments[0]
        return args

    def do_count(self, args):
        """Method to count instances"""
        count = 0
        for key, value in (storage.all()).items():
            clss = value.__class__.__name__
            if clss == args:
                count += 1
        print(count)

    def do_EOF(self, arg):
        """Type EOF to exit the command interpreter"""
        return True

    def do_quit(self, arg):
        """Type quit to exit the command interpreter"""
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
        """Prints the string representation of an instance base on
        the class name and id
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
                    clss = values.__class__.__name__
                    if arguments[1] == values.id and arguments[0] == clss:
                        print(values)
                        return
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
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
                    clss = values.__class__.__name__
                    if arguments[1] == values.id and arguments[0] == clss:
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

    def do_update(self, args):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        """
        if ',' in args:
            if '{' not in args:
                arg = args.split(',')
            else:
                arg = args.split(',', 1)
            class_id = arg[0].split()
            argu = ""
            argu += class_id[0] + f" {class_id[1]}"

            if '{' in arg[1]:
                argu += arg[1]
                arg = argu.split(" ", 2)

            else:
                argu += arg[1] + arg[2]
                arg = argu.split()
        else:
            arg = args.split()

        if not (args):
            print("** class name missing **")
            return
        if arg[0] not in storage.class_arb():
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        if len(arg) == 2:
            print("** attribute name missing **")
            return
        if len(arg) == 3 and '{' not in arg[2]:
            print("** value missing **")
            return
        if '{' not in arg[2]:
            for key, values in storage.all().items():
                if arg[1] == values.id:
                    setattr(values, arg[2], arg[3])
                    storage.save()
                    return
            print("** no instance found **")
        else:
            string = arg[2][1:-1]
            update_list = string.split(',')
            bol = 0
            for item in update_list:
                items = item.split(':')
                attr = items[0]
                val = items[1]
                for key, values in storage.all().items():
                    if arg[1] == values.id:
                        setattr(values, attr, val)
                        storage.save()
                        bol = 1
                        break
            if bol == 0:
                print("** no instance found **")
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
