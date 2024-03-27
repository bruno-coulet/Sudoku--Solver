import time, os
from backtracking import Solver

class Test:
    def __init__(self):
        self.solver = Solver()

    def run_tests(self):
        input_folder = "input"
        algo_names = [file for file in os.listdir(input_folder) if file.endswith(".txt")]

        for algo_name in algo_names:
            print(f"Test de {algo_name}...")
            file_path = os.path.join(input_folder, algo_name)
            execution_time = self.solver.begin(algo_name, file_path)

            if None:
                print(f"Pas de solution trouvée pour {algo_name}.\n")

if __name__ == "__main__":
    test = Test()
    test.run_tests()
