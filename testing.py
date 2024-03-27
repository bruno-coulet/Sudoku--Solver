import time
import statistics
from backtracking import Solver

class Test:
    def __init__(self):
        self.solver = Solver()

    def run_tests(self):

        # Create an instance of Solver with the specified file name
        input_file = Solver()
        
        # Ask user which file to test, how many times, which input
        algo_name = input("Entrez le nom du fichier à tester : ")

        execution_time = []
        minimum_time = float('inf')
    
        maximum_time = 0

        # Creates the markdown table
        table = "| Fichier testé | Nombre d'execution |  Temps le plus court | Temps le plus long | Temps moyen |\n"


        result = input_file.begin(algo_name)

        # there is a total_time
        if isinstance(result, float):
            execution_time.append(result)
            # Update mini and max times
            minimum_time = min(result, minimum_time)
            maximum_time = max(result, maximum_time)
            # Update table with current execution stats
            table += f"| {algo_name} | {result:.3f} ms | {result:.3f} ms | ---- |\n"
        else:
            # there is an error
            print("La solution de la grille n'a pas été trouvée")

        average_time = statistics.mean(execution_time)
        # Update the markdown table with the final results
        table += f"| {algo_name}  | {minimum_time:.3f} ms | {maximum_time:.3f} ms | {average_time:.3f} ms |\n"

        print(table)

# Exemple d'utilisation de la classe SudokuTester
if __name__ == "__main__":
    test = Test()
    test.run_tests()