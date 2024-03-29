from VisuelBruteForce.Screen import Screen

class MainBruteForce(Screen):
    def __init__(self):
        Screen.__init__(self)
        
    def running_Brute_force(self):
        self.run()

main = MainBruteForce()
main.running_Brute_force()