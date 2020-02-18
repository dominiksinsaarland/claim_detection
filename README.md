# claim_detection

working repo for claim detection

### installation

* Download and install Anaconda (https://www.anaconda.com/)
* Create a Python Environment and activate it:
```bash 
conda create -n claim_spotting python=3.6
source activate claim_spotting
pip install requirements.txt
```


# download data

```
bash download_data.sh
```

# run baseline
```
python uni_bigram_baseline.py
```

this creates a directory called baseline_predictions where we have predictions for all claims from the CLEF2018 testset


# evaluate baseline

```
cd clef2019-factchecking-task1/
PYTHONPATH="." python3 scorer/main.py --gold_file_path="data/training/20161019_3pres.tsv,data/training/20160414_9dem.tsv,data/training/20180916_trump_miami.tsv,data/training/20170928_trump_tax.tsv,data/training/20182601_trump_world.tsv,data/training/20160722_trump_acceptance.tsv,data/training/20170228_trump_address.tsv" --pred_file_path="../baseline_predictions/20161019_3pres.tsv,../baseline_predictions/20160414_9dem.tsv,../baseline_predictions/20180916_trump_miami.tsv,../baseline_predictions/20170928_trump_tax.tsv,../baseline_predictions/20182601_trump_world.tsv,../baseline_predictions/20160722_trump_acceptance.tsv,../baseline_predictions/20170228_trump_address.tsv" 
```

