import time, os, statistics, sys
from backtracking import Backtracking

class Testing:
    def __init__(self):
        self.solver = Backtracking()

    def run_tests(self):
        input_folder = "input"
        grid_names = [file for file in os.listdir(input_folder) if file.endswith(".txt")]

        # Gets the script name
        script_name = os.path.basename(sys.argv[0])

        # Creates the markdown table
        table = "| Fichier testé | Grille testée | Temps d'exécution  |\n"
        table += "| -------------- | ------------- | ----------------- |\n"

        # Initialize variables for calculating min, max, and average time
        execution_times = []

        for grid_name in grid_names:
            print(f"Testing de {grid_name}...")
            file_path = os.path.join(input_folder, grid_name)
            execution_time = self.solver.begin(grid_name, file_path)
            # Update table with current execution stats
            table += f"| {script_name}  |  {grid_name}   | {execution_time:.3f} ms |\n"
                        
            if execution_time is not None:
                execution_times.append(execution_time)

            # if None:
            #     print(f"Pas de solution trouvée pour {grid_name}.\n")
                
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

   # Tentative d'écriture du contenu de la variable table dans le fichier README.md
    try:
        with open("README.md", "w") as readme_file:
            readme_file.write(table)
        print("Le fichier README.md a été créé avec succès.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la création du fichier README.md : {e}")