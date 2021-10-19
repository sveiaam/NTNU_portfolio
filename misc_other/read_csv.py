#Bygget for TFY4165 lab 2
def read_csv(filename):
	import pandas as pd
	import numpy as np
	data = filename
	x1 = pd.read_csv(data)  # importerer dokument
	x2 = pd.DataFrame.as_matrix(x1)  # Importert materiale til np.array
	x3 = np.delete(x2, 0, 0)  # Skreller bort det øverste laget med tekst
	x4 = x3.astype(np.float)  # Gjør string om til float
	return x4
