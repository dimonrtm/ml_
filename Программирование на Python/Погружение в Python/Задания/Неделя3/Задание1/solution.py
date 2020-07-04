class FileReader:
    def __init__(self,path):
        self.path=path
    def read(self):
        try:
            with open(self.path,"r") as read_file:
                result=read_file.read()
            return result
        except IOError:
            return ""
