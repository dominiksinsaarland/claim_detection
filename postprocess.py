import sys
import os
predictions = []
with open(os.path.join(sys.argv[2], sys.argv[1])) as infile:
	for line in infile:
		predictions.append(line.strip())

i = 1
with open(os.path.join(sys.argv[2], sys.argv[1]), "w") as outfile:
	for pred in predictions:
		outfile.write(str(i) + "\t" + pred + "\n")
		i += 1


