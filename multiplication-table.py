stcol = int(input("Input start table column: "))
etcol = int(input("Input end table column: "))
strow = int(input("Input start table row: "))
etrow = int(input("Input end table row: "))
columns = range(stcol,(etcol+1)) 
rows = range(strow,(etrow+1))
for x in columns: # loop through the column range
	print('\nTABLE ' + str(x))
	for y in rows: # loop through the row range
		product = x * y 
		print(str(x) + " x " + str(y) + " = " + str(product))