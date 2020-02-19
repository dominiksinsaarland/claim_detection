import utils
import random
from collections import defaultdict
from collections import Counter

if __name__ == "__main__":
	CLEF_Loader = utils.CLEF_Loader()
	train, dev = CLEF_Loader.get_examples()
	with open("train_clef_2019.txt", "w") as outfile:
		for sentence, label in train:
			outfile.write(sentence + "\t" + str(label) + "\n")

	with open("dev_clef_2019.txt", "w") as outfile:
		for sentence, label in train:
			outfile.write(sentence + "\t" + str(label) + "\n")

