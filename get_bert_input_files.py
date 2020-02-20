import utils
import random
from collections import defaultdict
from collections import Counter
import os
if __name__ == "__main__":
	CLEF_Loader = utils.CLEF_Loader()
	train, dev = CLEF_Loader.get_examples()
	path_outfiles = "bert_input_files"
	path_data = "clef2019-factchecking-task1/data/training/"
	block_set = set([x[0] for x in dev])
	train.extend(utils.ClaimBuster_Loader().get_examples(block_set=block_set))

	try:
		os.mkdir(path_outfiles)
	except:
		pass


	with open(os.path.join(path_outfiles, "train.txt"), "w") as outfile:
		for sentence, label in train:
			outfile.write(sentence + "\t" + str(label) + "\n")

	with open(os.path.join(path_outfiles, "dev.txt"), "w") as outfile:
		for sentence, label in dev:
			outfile.write(sentence + "\t" + str(label) + "\n")

	dev_fns = ["20161019_3pres.tsv", "20160414_9dem.tsv", "20180916_trump_miami.tsv", "20170928_trump_tax.tsv", "20182601_trump_world.tsv", "20160722_trump_acceptance.tsv", "20170228_trump_address.tsv"]
	for fn in dev_fns:
		with open(os.path.join(path_data, fn)) as infile:
			with open(os.path.join(path_outfiles, fn), "w") as outfile:
				for line in infile:
					line = line.strip().split("\t")
					outfile.write(line[2] + "\t" + line[3] + "\n")


	# get roberta input
	# bsub -W 2 -n 1 -R "rusage[mem=4096,scratch=8192]" -B -N python get_roberta_input.py

	#test tensorflow GPU
	# bsub -n 1 -R "rusage[mem=12800,ngpus_excl_p=1]" python test.py 

	# get bert input
	# bsub -W 2 -n 1 -R "rusage[mem=4096,scratch=8192]" python get_bert_input_files.py



