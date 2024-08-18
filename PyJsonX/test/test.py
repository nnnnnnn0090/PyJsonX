import PyJsonX
import os

with open(f"{os.path.dirname(os.path.abspath(__file__))}/example.pyjsonX", 'r', encoding="utf-8") as file:
    print(PyJsonX.execute(file.read()))