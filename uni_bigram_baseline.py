from sklearn.linear_model import SGDClassifier

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV

from sklearn.pipeline import Pipeline


import os

text_clf = Pipeline([
     ('vect', CountVectorizer(max_df = 0.5 , min_df=2, ngram_range=(1,2), lowercase=False)),
     ('tfidf', TfidfTransformer(sublinear_tf=True)),
     ('clf', SGDClassifier(loss='hinge', penalty='l2',
                           alpha=1e-5, random_state=42,
                           max_iter=300, tol=None, class_weight="balanced")),
 ])




import utils
import random
CLEF_Loader = utils.CLEF_Loader()
train, dev = CLEF_Loader.get_examples()
a,b = set(train), set(dev)
print ("length intersection", len(a.intersection(b)))

# problem: our dev set partially overlaps with ClaimRank data AND with ClaimBuster data, thus we should not include it

"""
train.extend(utils.ClaimRank_Loader().get_examples())
a,b = set(train), set(dev)
print ("length intersection", len(a.intersection(b)))

train.extend(utils.ClaimBuster_Loader().get_examples())
a,b = set(train), set(dev)
print ("length intersection", len(a.intersection(b)))
print (len(dev), len(b))

input("")
"""

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
	predicted = text_clf.predict([x[0] for x in examples])
	i = 1
	with open(os.path.join(outpath, dev_fn), "w") as outfile:
		for pred in predicted:
			outfile.write(str(i) + "\t" + str(pred) + "\n")
			i += 1

print (",".join([os.path.join(path_data, fn).strip("clef2019-factchecking-task1/") for fn in dev_fns]))
print (",".join([os.path.join("..", outpath, fn) for fn in dev_fns]))



# cd clef2019-factchecking-task1/
# PYTHONPATH="." python3 scorer/main.py --gold_file_path="data/training/20161019_3pres.tsv,data/training/20160414_9dem.tsv,data/training/20180916_trump_miami.tsv,data/training/20170928_trump_tax.tsv,data/training/20182601_trump_world.tsv,data/training/20160722_trump_acceptance.tsv,data/training/20170228_trump_address.tsv" --pred_file_path="../baseline_predictions/20161019_3pres.tsv,../baseline_predictions/20160414_9dem.tsv,../baseline_predictions/20180916_trump_miami.tsv,../baseline_predictions/20170928_trump_tax.tsv,../baseline_predictions/20182601_trump_world.tsv,../baseline_predictions/20160722_trump_acceptance.tsv,../baseline_predictions/20170228_trump_address.tsv" 
