#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def close(self):
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        self.close()
        print()
        quit()

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print('** class name missing **')
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print('** class doesn\'t exist **')

    def do_show(self, arg):
        if not arg:
            print('** class name missing **')
            return
        instance = arg.split()
        if len(instance) == 1:
            print('** instance id missing **')
            return
        try:
            Base_id = f'{instance[0]}.{instance[1]}'
            print(storage.all()[Base_id])
        except Exception:
            print("** no instance found **")

    def do_destroy(self, arg):
        if not arg:
            print('** class name missing **')
            return
        
        instance = arg.split()
        if len(instance) == 1:
            print('** instance id missing **')
            return
        try:
            Base_id = f'{instance[0]}.{instance[1]}'
            del(storage.all()[Base_id])
        except Exception:
            print('** no instance found **')

    def do_all(self, arg):
        if not arg:
            instance_list = []
            instance_str = ""
            i = 0
            length_storage = len(storage.all())
            for instance in storage.all():
                instance_str += f'{storage.all()[instance]}'
                if instance_str.endswith("}") and i < length_storage - 1:
                    instance_str += ", "
                i += 1
            instance_list.append(instance_str)
            print(instance_list)
            return 
        try:
            name_class = eval(arg).__name__
        except Exception:
            print('** class doesn\'t exist **')
        else:
            instance_list = []
            instance_str = ""
            length_storage = len(storage.all())
            i = 0
            for instance in storage.all():
                if instance.startswith(name_class + "."):
                   instance_str += f'{storage.all()[instance]}'
                   if instance_str.endswith("}") and i < length_storage - 1:
                    instance_str += ", "
                i += 1
            instance_list.append(instance_str)
            print(instance_list)
            return



if __name__ == '__main__':
    HBNBCommand().cmdloop()
