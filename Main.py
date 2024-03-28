from Visuel.Screen import Screen
class Main(Screen):
    def __init__(self):
        Screen.__init__(self)
        
    def running(self):
        self.run()

main = Main()
main.running()