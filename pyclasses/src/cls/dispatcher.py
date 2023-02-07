
from src.cls.printer import printer

class Dispatcher:
        def __init__(self):
                self.bucket = []
                self.printer = printer()

        def send(self, object):
                self.bucket.append(object)

        def show(self):
                return self.bucket

        def run(self):
                for i in self.bucket:
                        self.printer.printTxt(i)

class Postman:
        def __init__(self):
                self.bucket = []
                self.sent = 0
                self.printer = printer()
        def send(self, object, dis_class:Dispatcher):
                dis_class.send(object)
                print(dis_class.show())
        def check(self, dis_class:Dispatcher):
                return dis_class.show()

