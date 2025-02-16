from tabulate import tabulate
import sys
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 2 and not ( ".csv" in sys.argv[1] ):
    sys.exit("Not a CSV file")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1]) as file:
        menu = csv.reader(file)
        print(tabulate(menu, headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
