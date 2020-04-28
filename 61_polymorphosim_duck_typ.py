class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")
class notepad :
    def execute(self):
        print("spell check")
        print("Convention check")
        print("Compiling")
        print("Running")
class Laptop:
    def code(self,ide):
        ide.execute()
ide=Pycharm()
ide1 = notepad()
lap1 =Laptop()
lap1.code(ide)
lap1.code(ide1)
