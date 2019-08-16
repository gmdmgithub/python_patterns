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

    print(f.closed)

if __name__ == "__main__":
    manage_file_class()