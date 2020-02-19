import csv
import os
from collections import Counter
class CLEF_Loader:
	def __init__(self, path_data="clef2019-factchecking-task1/data/training"):
		self.dev_fns = ["20161019_3pres.tsv", "20160414_9dem.tsv", "20180916_trump_miami.tsv", "20170928_trump_tax.tsv", "20182601_trump_world.tsv", "20160722_trump_acceptance.tsv", "20170228_trump_address.tsv"]
		self.path_data = path_data
		self.train_fns_CLEF2018 = ["20160926_1pres.tsv", "20161005_vice_pres.tsv", "20161010_2pres.tsv"]
	def get_examples(self):
		train_set, dev_set = [], []
		for filename in os.listdir(self.path_data):
			with open(os.path.join(self.path_data, filename)) as infile:
				for line in infile:
					# format is line_number, speaker, sentence, label
					nr, speaker, sentence, label = line.strip().split("\t")
					if filename in self.dev_fns:
						dev_set.append((sentence, int(label)))
					else:
						train_set.append((sentence, int(label)))
		return train_set, dev_set


	def get_clef2018_train_set(self):
		train_set, dev_set = [], []
		for filename in os.listdir(self.path_data):
			with open(os.path.join(self.path_data, filename)) as infile:
				for line in infile:
					# format is line_number, speaker, sentence, label
					nr, speaker, sentence, label = line.strip().split("\t")
					if filename in self.dev_fns:
						dev_set.append((sentence, int(label)))
					elif filename in self.train_fns_CLEF2018:
						train_set.append((sentence, int(label)))
		return train_set, dev_set


	def get_dev_examples(self):
		all_dev_set = []
		for filename in self.dev_fns:
			with open(os.path.join(self.path_data, filename)) as infile:
				dev_set = []
				for line in infile:
					# format is line_number, speaker, sentence, label
					nr, speaker, sentence, label = line.strip().split("\t")
					if filename in self.dev_fns:
						dev_set.append((sentence, int(label)))
			all_dev_set.append(dev_set)
		return all_dev_set, self.dev_fns, self.path_data


class ClaimRank_Loader:
	def __init__(self, path_data="claim-rank/data/transcripts_all_sources"):
		self.path_data=path_data

	def get_examples(self, block_set = None):
		train_set = []
		for filename in os.listdir(self.path_data):
			with open(os.path.join(self.path_data, filename)) as csvfile:
				csvreader = csv.reader(csvfile, delimiter="\t")
				next(csvreader)
				for row in csvreader:
					# format is: ID      Speaker ALL     CT      ABC     CNN     WP      NPR     PF      TG      NYT     FC      Text
					if block_set is not None:
						if row[-1] not in block_set:
							if int(row[2]) != 0:
								is_claim = 1
							else:
								is_claim = 0
							#print (row[-1], is_claim)
							#input("")


							train_set.append((row[-1], is_claim))
		return train_set


class ClaimBuster_Loader:
	def __init__(self, path_data="claim_buster_data/crowdsourced.csv"):
		self.path_data=path_data

	def get_examples(self, block_set = None):
		train_set = []
		with open(self.path_data, 'r') as csvfile:
			csvreader = csv.reader(csvfile)
			# skip header
			next(csvreader)
			for row in csvreader:
				# Sentence_id,Text,Speaker,Speaker_title,Speaker_party,File_id,Length,Line_number,Sentiment,Verdict
				if block_set is not None:
					if row[1] not in block_set:
						if row[-1] != "1":
							train_set.append((row[1], 0))
						else:
							train_set.append((row[1], 1))
							#print (row[1], 1)
							#input("")
		return train_set

class MultiFC_Loader:
	def __init__(self, path_data="MultiFC_data/train.tsv"):
		self.path_data=path_data
	def get_examples(self, block_set = None):
		labels = []
		train_set = []
		with open(self.path_data, 'r') as csvfile:
			csvreader = csv.reader(csvfile, delimiter="\t")
			# skip header
			next(csvreader)
			for row in csvreader:
				# Sentence_id,Text,Speaker,Speaker_title,Speaker_party,File_id,Length,Line_number,Sentiment,Verdict
				if block_set is not None:
					if len(row) != 13:
						continue
					if row[1] not in block_set:
						labels.append(row[2])
						train_set.append((row[1], 1))
						#print (row[1])
						#input("")
						"""
						if row[-1] != "1":
							train_set.append((row[1], 0))
						else:
							train_set.append((row[1], 1))
						"""
		print (Counter(labels))
		return train_set


