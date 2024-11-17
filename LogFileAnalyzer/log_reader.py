
class LogFileReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def __iter__(self):
        try:
            self.file = open(self.file_name, "r")
            return self
        except FileNotFoundError:
            print(f"Error: File '{self.file_name}' not found.")
            raise

    def __next__(self):
        line = self.file.readline()
        if line:
            return line.strip()
        else:
            self.file.close()
            raise StopIteration
