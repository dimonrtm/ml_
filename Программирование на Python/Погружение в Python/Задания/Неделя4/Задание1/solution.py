import os
import tempfile
import uuid

class File:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            open(file_path, "w").close()

    def read(self):
        with open(self.file_path) as f:
            return f.read();

    def write(self, new_str):
        with open(self.file_path, "w") as f:
            return f.write(new_str)

    def __add__(self, file):
        new_str = self.read() + file.read()
        new_file = File(os.path.join(tempfile.gettempdir(),str(uuid.uuid4().hex)))
        new_file.write(new_str)
        return new_file

    def __str__(self):
        return self.file_path

    def __iter__(self):
        self.f = open(self.file_path)
        return self

    def __next__(self):
         line = self.f.readline()
         if not line:
             self.f.close()
             raise StopIteration
         return line



