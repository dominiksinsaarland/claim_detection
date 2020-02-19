from sklearn.linear_model import SGDClassifier

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV

from sklearn.pipeline import Pipeline
import re

import os
import argparse

text_clf = Pipeline([
     ('vect', CountVectorizer(max_df = 0.5 , min_df=3, ngram_range=(1,2), lowercase=False)),
     ('tfidf', TfidfTransformer(sublinear_tf=True)),
     ('clf', SGDClassifier(loss='hinge', penalty='l2',
                           alpha=1e-5, random_state=42,
                           max_iter=500, tol=None, class_weight="balanced")),
 ])




import utils
import random
from collections import defaultdict
from collections import Counter
if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("--train_set", default="CLEF_2019", type=str, help="path to pages of the Wikipedia dump")
	parser.add_argument("--include_ClaimRank_data", default="no", type=str, help="path to pages of the Wikipedia dump")
	parser.add_argument("--include_ClaimBuster_data", default="no", type=str, help="path to pages of the Wikipedia dump")
	parser.add_argument("--include_MultiFC_data", default="no", type=str, help="path to pages of the Wikipedia dump")
	args = parser.parse_args()
	CLEF_Loader = utils.CLEF_Loader()
	if args.train_set == "CLEF_2019":
		train, dev = CLEF_Loader.get_examples()
	elif args.train_set == "CLEF_2018":
		train, dev = CLEF_Loader.get_clef2018_train_set()
	elif args.train_set == "ClaimRank":
		train, dev = CLEF_Loader.get_clef2018_train_set()
		block_set = set([x[0] for x in dev])
		claimrank_data = utils.ClaimRank_Loader().get_examples(block_set=block_set)
		train = claimrank_data

	elif args.train_set == "ClaimBuster":
		train, dev = CLEF_Loader.get_clef2018_train_set()
		block_set = set([x[0] for x in dev])
		train = utils.ClaimBuster_Loader().get_examples(block_set=block_set)
		print (len(train))
		print (Counter([x[1] for x in train]))

	"""
	elif args.train_set == "MultiFC":
		train, dev = CLEF_Loader.get_clef2018_train_set()
		block_set = set([x[0] for x in dev])
		train = utils.MultiFC_Loader().get_examples(block_set=block_set)
	"""
	
	if args.include_ClaimRank_data == "yes":
		print (len(train))
		print (len(set([x[0] for x in train])))
		# some of the data in the ClaimRank dataset is part of the dev set of CLEF2018, be careful to not include such instances
		block_set = set([x[0] for x in dev])
		claimrank_data = utils.ClaimRank_Loader().get_examples(block_set=block_set)
		"""
		claimrank_set = set([x[0] for x in claimrank_data])
		clef_set = set([x[0] for x in train])

		c, n = 0,0
		label_diffs = defaultdict(int)
		for i in claimrank_data:
			if i[0] in clef_set:
				for j in train:
					if j[0] == i[0]:
						if i[1] != j[1]:
							c += 1
							#print ("text", i[0], "----- claimrank label", i[1],  "-------- clef label",j[1])
							#input("")
							label_diffs[str(i[1]) + " -> " + str(j[1])] += 1
							if j[1] == 1 and i[1] == 0:
								print (i[0])
								input("")
						else:
							n += 1
		print (c, n, label_diffs)
		input("")
		"""		
		#train.extend(claimrank_data)
		"""
		print (train[:5])
		print (claimrank_data[:5])
		print (np.shape(train))
		print (np.shape(claimrank_data))
		print (set([x[1] for x in claimrank_data]))
		input("")
		"""
		print (len(train))
		print (len(set([x[0] for x in train])))


		train.extend(claimrank_data)
	if args.include_ClaimBuster_data == "yes":
		print (len(train))
		print (len(set([x[0] for x in train])))

		block_set = set([x[0] for x in dev])
		train.extend(utils.ClaimBuster_Loader().get_examples(block_set=block_set))
		print (len(train))
		print (len(set([x[0] for x in train])))
		print (Counter([x[1] for x in train]))


	if args.include_MultiFC_data == "yes":
		block_set = set([x[0] for x in dev])
		train.extend(utils.MultiFC_Loader().get_examples(block_set=block_set))
		print (len(train))
		print (len(set([x[0] for x in train])))



	"""
	print (len(train))
	print (len(set([x[0] for x in train])))
	block_set = set([x[0] for x in dev])
	train.extend(utils.ClaimRank_Loader().get_examples(block_set=block_set))
	print (len(train))
	print (len(set([x[0] for x in train])))
	"""
	"""
	a,b = set(train), set(dev)
	print ("length intersection", len(a.intersection(b)))

	# problem: our dev set partially overlaps with ClaimRank data AND with ClaimBuster data, thus we should not include it

	train.extend(utils.ClaimRank_Loader().get_examples())
	a,b = set(train), set(dev)
	print ("length intersection", len(a.intersection(b)))



	train.extend(utils.ClaimBuster_Loader().get_examples())
	a,b = set(train), set(dev)
	print ("length intersection", len(a.intersection(b)))
	print (len(dev), len(b))

	input("")
	"""

	#train_data, train_target = [re.sub("\d+", "#", x[0]) for x in train], [x[1] for x in train]

	train_data, train_target = [x[0] for x in train], [x[1] for x in train]
	text_clf.fit(train_data, train_target)

	all_dev_set, dev_fns, path_data = CLEF_Loader.get_dev_examples()

	outpath = "baseline_predictions"
	try:
		os.mkdir(outpath)
	except:
		pass

	print (len(all_dev_set), len(dev_fns))
	for examples, dev_fn in zip(all_dev_set, dev_fns):
		predicted = text_clf.decision_function([x[0] for x in examples])
		i = 1
		with open(os.path.join(outpath, dev_fn), "w") as outfile:
			for pred in predicted:
				# format(0.1, '.20f')
				outfile.write(str(i) + "\t" + format(pred, '.10f') + "\n")
				#outfile.write(str(i) + "\t" + str(pred) + "\n")
				i += 1

	print (",".join([os.path.join(path_data, fn).strip("clef2019-factchecking-task1/") for fn in dev_fns]))
	print (",".join([os.path.join("..", outpath, fn) for fn in dev_fns]))



	# cd clef2019-factchecking-task1/
	# PYTHONPATH="." python3 scorer/main.py --gold_file_path="data/training/20161019_3pres.tsv,data/training/20160414_9dem.tsv,data/training/20180916_trump_miami.tsv,data/training/20170928_trump_tax.tsv,data/training/20182601_trump_world.tsv,data/training/20160722_trump_acceptance.tsv,data/training/20170228_trump_address.tsv" --pred_file_path="../baseline_predictions/20161019_3pres.tsv,../baseline_predictions/20160414_9dem.tsv,../baseline_predictions/20180916_trump_miami.tsv,../baseline_predictions/20170928_trump_tax.tsv,../baseline_predictions/20182601_trump_world.tsv,../baseline_predictions/20160722_trump_acceptance.tsv,../baseline_predictions/20170228_trump_address.tsv" 
