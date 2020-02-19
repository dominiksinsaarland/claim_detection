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
		for sentence, label in dev:
			outfile.write(sentence + "\t" + str(label) + "\n")


	# bsub -W 2 -n 1 -R "rusage[mem=4096,scratch=8192]" -B -N python get_roberta_input.py

	#test tensorflow GPU
	# bsub -n 1 -R "rusage[mem=12800,ngpus_excl_p=1]" python test.py 



