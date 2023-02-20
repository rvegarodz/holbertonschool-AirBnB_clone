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
            return

    def do_show(self, arg):
        if not arg:
            print('** class name missing **')
            return
        instance = arg.split()
        if len(instance) == 1:
            print('** instance id missing **')
            return
        Base_id = f'{instance[0]}.{instance[1]}'
        try:
            if storage.all()[Base_id]:
                pass
        except Exception:
            print('** class doesn\'t exist **')
        try:
            print(storage.all()[Base_id])
        except Exception:
            print("** no instance found **")
            return

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
            return

    def do_all(self, arg):
        if not arg:
            instance_list = []
            instance_str = ""
            for instance in storage.all():
                instance_str = f'{storage.all()[instance]}'
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
            for instance in storage.all():
                if instance.startswith(name_class + "."):
                   instance_str = f'{storage.all()[instance]}'
                instance_list.append(instance_str)
            print(instance_list)
            return
    
    def do_update(self, arg):
        if not arg:
            print('** class name missing **')
            return
        if arg:
            """Something pass"""
            input_args = arg.split()
            if len(input_args) == 1:
                print("** instance id missing **")
                return
            elif len(input_args) == 2:
                print("** attribute name missing **")
                return
            elif len(input_args) == 3:
                print("** value missing **")
                return
            else:
                """ Verifying and assiging class_name"""
                try:
                    class_name = eval(input_args[0]).__name__
                except Exception:
                    print('** class doesn\'t exist **')
                    return
                Base_id = f'{class_name}.{input_args[1]}'
                try:
                    if storage.all()[Base_id]:
                        pass
                except Exception:
                    print("** no instance found **")
                    return
                """ Verifying and assiging atrb_name"""
                Obj = storage.all()[Base_id]
                if input_args[2] not in ['id', 'created_at', 'updated_at']:
                    new_attr = {str(input_args[2]): input_args[3]}
                    Obj.__dict__.update(new_attr)
                    Obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
