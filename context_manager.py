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
        f = open(file,mode)
        yield f
        f.close()

    with open_file("test.txt","a") as f:
        f.write("\nhi there now we append with function context manager!")

    print(f.closed) #is file closed?

#################

if __name__ == "__main__":
    # first on class case
    #manage_file_class()
    #now with function
    open_file_with_function_context_manager()


