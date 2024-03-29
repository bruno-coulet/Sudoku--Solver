from Visuel.Screen import Screen
class MainBacktracking(Screen):
    def __init__(self):
        Screen.__init__(self)
        
    def running(self):
        self.run()

main = MainBacktracking()
main.running()