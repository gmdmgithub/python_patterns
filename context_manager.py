## context manager with class
class OpenFile():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        print("init done")

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print("just open")
        return self.file
    def __exit__(self,exit_type, exit_val, traceback):
        self.file.close()
        print("file closed")

def manage_file_class():
    with OpenFile("test.txt","w") as f:
        f.write("This is sample line")

    print(f.closed) #is file closed?

############# using the function  ##################

from contextlib import contextmanager

def open_file_with_function_context_manager():
    
    @contextmanager
    def open_file(file,mode):
        try:
            f = open(file,mode)
            yield f
        except e:
            print(e)
        finally:
            f.close()

    with open_file("test.txt","a") as f:
        f.write("\nhi there now we append with function context manager!")

    print(f.closed) #is file closed?


import os

def print_dirlist_with_function_context_manager():
    
    @contextmanager
    def change_dir(destination):
        try:
            cwd = os.getcwd()
            os.chdir(destination)
            yield
        except Exception as e: #any
            print(e)
        finally:
            os.chdir(cwd)#back to original dir
    
    with change_dir("test"):
        print(os.listdir())
    with change_dir("thread"):
        print(os.listdir())


#################

if __name__ == "__main__":
    # first on class case
    #manage_file_class()
    #now with function
    #open_file_with_function_context_manager()
    print_dirlist_with_function_context_manager()


