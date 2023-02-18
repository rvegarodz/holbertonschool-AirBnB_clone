#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        self.close()
        quit()
    
    def close(self):
        return True
    
    def do_EOF(self, arg):
        'EOF command to exit the program'
        self.close()
        print()
        quit()
    
    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()