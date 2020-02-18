import csv
import os

class CLEF_Loader:
	def __init__(self, path_data="clef2019-factchecking-task1/data/training"):
		self.dev_fns = ["20161019_3pres.tsv", "20160414_9dem.tsv", "20180916_trump_miami.tsv", "20170928_trump_tax.tsv", "20182601_trump_world.tsv", "20160722_trump_acceptance.tsv", "20170228_trump_address.tsv"]
		self.path_data = path_data

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

	def get_examples(self):
		train_set = []
		for filename in os.listdir(self.path_data):
			with open(os.path.join(self.path_data, filename)) as infile:
				for i, line in enumerate(infile):
					if i == 0:
						# skip header
						continue 
					line = line.strip().split("\t")
					# format is: ID      Speaker ALL     CT      ABC     CNN     WP      NPR     PF      TG      NYT     FC      Text
					train_set.append((line[-1], int(line[2])))
		return train_set


class ClaimBuster_Loader:
	def __init__(self, path_data="claim_buster_data/crowdsourced.csv"):
		self.path_data=path_data

	def get_examples(self):
		train_set = []
		with open(self.path_data, 'r') as csvfile:
			csvreader = csv.reader(csvfile)
			# skip header
			next(csvreader)
			for row in csvreader:
				# Sentence_id,Text,Speaker,Speaker_title,Speaker_party,File_id,Length,Line_number,Sentiment,Verdict
				if row[-1] != "1":
					train_set.append((row[1], 0))
				else:
					train_set.append((row[1], 1))
		return train_set

