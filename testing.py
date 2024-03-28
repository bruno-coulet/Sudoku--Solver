import time, os, statistics, sys
from backtracking import Backtracking
from BruteForce import BruteForce

class Testing:
    '''Tests either brute force or backtracking'''
    def __init__(self):

        self.algorithm_name = input('Quel méthode voulez-vous utiliser, "bruteforce" ou "backtracking" : ')
        if self.algorithm_name.lower() == 'bruteforce':
            self.solver = BruteForce()
        elif self.algorithm_name.lower() == 'backtracking':
            self.solver = Backtracking()
        else:
            raise ValueError("Méthode invalide. Veuillez choisir 'BruteForce' ou 'Backtracking'.")

         

    def run_tests(self):
        input_folder = "input"
        algo_names = [file for file in os.listdir(input_folder) if file.endswith(".txt")]

        # Gets the script name
        script_name = os.path.basename(sys.argv[0])

        # Creates the markdown table
        table = "| Fichier testé | Grille testée | Temps d'exécution  |\n"
        table += "| -------------- | ------------- | ----------------- |\n"

        # Initialize variables for calculating min, max, and average time
        execution_times = []

        for algo_name in algo_names:
            print(f"Testing de {algo_name}...")
            file_path = os.path.join(input_folder, algo_name)
            execution_time = self.solver.begin(file_path)
            # Update table with current execution stats
            table += f"| {self.algorithm_name}  |  {algo_name}   | {execution_time:.3f} ms |\n"
                        
            if execution_time is not None:
                execution_times.append(execution_time)

            # if None:
            #     print(f"Pas de solution trouvée pour {algo_name}.\n")
                
        if execution_times:
            # Calculate min, max, and average times
            minimum_time = min(execution_times)
            maximum_time = max(execution_times)
            average_time = statistics.mean(execution_times)

            # Update the markdown table with the final results
            table += f"\nTemps le plus court : {minimum_time:.3f} ms\n"
            table += f"Temps le plus long : {maximum_time:.3f} ms\n"
            table += f"Temps moyen : {average_time:.3f} ms\n"

        print(table)
        return table


if __name__ == "__main__":
    test = Testing()
    table = test.run_tests()

   # creates README.md to store the table
    try:
        with open("README.md", "w") as readme_file:
            readme_file.write(table)
        print("Le fichier README.md a été créé avec succès.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la création du fichier README.md : {e}")