# CLEF 2018 train set

: <<'END'
python uni_bigram_baseline.py --train_set CLEF_2018
cd clef2019-factchecking-task1/
PYTHONPATH="." python3 scorer/main.py --gold_file_path="data/training/20161019_3pres.tsv,data/training/20160414_9dem.tsv,data/training/20180916_trump_miami.tsv,data/training/20170928_trump_tax.tsv,data/training/20182601_trump_world.tsv,data/training/20160722_trump_acceptance.tsv,data/training/20170228_trump_address.tsv" --pred_file_path="../baseline_predictions/20161019_3pres.tsv,../baseline_predictions/20160414_9dem.tsv,../baseline_predictions/20180916_trump_miami.tsv,../baseline_predictions/20170928_trump_tax.tsv,../baseline_predictions/20182601_trump_world.tsv,../baseline_predictions/20160722_trump_acceptance.tsv,../baseline_predictions/20170228_trump_address.tsv" 
cd ..

# CLEF 2019 train set
python uni_bigram_baseline.py --train_set CLEF_2019
cd clef2019-factchecking-task1/
PYTHONPATH="." python3 scorer/main.py --gold_file_path="data/training/20161019_3pres.tsv,data/training/20160414_9dem.tsv,data/training/20180916_trump_miami.tsv,data/training/20170928_trump_tax.tsv,data/training/20182601_trump_world.tsv,data/training/20160722_trump_acceptance.tsv,data/training/20170228_trump_address.tsv" --pred_file_path="../baseline_predictions/20161019_3pres.tsv,../baseline_predictions/20160414_9dem.tsv,../baseline_predictions/20180916_trump_miami.tsv,../baseline_predictions/20170928_trump_tax.tsv,../baseline_predictions/20182601_trump_world.tsv,../baseline_predictions/20160722_trump_acceptance.tsv,../baseline_predictions/20170228_trump_address.tsv" 
cd ..

# ClaimRank train set
python uni_bigram_baseline.py --train_set ClaimRank
cd clef2019-factchecking-task1/
PYTHONPATH="." python3 scorer/main.py --gold_file_path="data/training/20161019_3pres.tsv,data/training/20160414_9dem.tsv,data/training/20180916_trump_miami.tsv,data/training/20170928_trump_tax.tsv,data/training/20182601_trump_world.tsv,data/training/20160722_trump_acceptance.tsv,data/training/20170228_trump_address.tsv" --pred_file_path="../baseline_predictions/20161019_3pres.tsv,../baseline_predictions/20160414_9dem.tsv,../baseline_predictions/20180916_trump_miami.tsv,../baseline_predictions/20170928_trump_tax.tsv,../baseline_predictions/20182601_trump_world.tsv,../baseline_predictions/20160722_trump_acceptance.tsv,../baseline_predictions/20170228_trump_address.tsv"
cd .. 

# include ClaimRank data
python uni_bigram_baseline.py --train_set CLEF_2019 --include_ClaimRank_data yes
cd clef2019-factchecking-task1/
PYTHONPATH="." python3 scorer/main.py --gold_file_path="data/training/20161019_3pres.tsv,data/training/20160414_9dem.tsv,data/training/20180916_trump_miami.tsv,data/training/20170928_trump_tax.tsv,data/training/20182601_trump_world.tsv,data/training/20160722_trump_acceptance.tsv,data/training/20170228_trump_address.tsv" --pred_file_path="../baseline_predictions/20161019_3pres.tsv,../baseline_predictions/20160414_9dem.tsv,../baseline_predictions/20180916_trump_miami.tsv,../baseline_predictions/20170928_trump_tax.tsv,../baseline_predictions/20182601_trump_world.tsv,../baseline_predictions/20160722_trump_acceptance.tsv,../baseline_predictions/20170228_trump_address.tsv"
cd .. 



# ClaimBuster train set
python uni_bigram_baseline.py --train_set ClaimBuster
cd clef2019-factchecking-task1/
PYTHONPATH="." python3 scorer/main.py --gold_file_path="data/training/20161019_3pres.tsv,data/training/20160414_9dem.tsv,data/training/20180916_trump_miami.tsv,data/training/20170928_trump_tax.tsv,data/training/20182601_trump_world.tsv,data/training/20160722_trump_acceptance.tsv,data/training/20170228_trump_address.tsv" --pred_file_path="../baseline_predictions/20161019_3pres.tsv,../baseline_predictions/20160414_9dem.tsv,../baseline_predictions/20180916_trump_miami.tsv,../baseline_predictions/20170928_trump_tax.tsv,../baseline_predictions/20182601_trump_world.tsv,../baseline_predictions/20160722_trump_acceptance.tsv,../baseline_predictions/20170228_trump_address.tsv"
cd .. 




python uni_bigram_baseline.py --train_set CLEF_2019 --include_ClaimBuster_data yes
cd clef2019-factchecking-task1/
PYTHONPATH="." python3 scorer/main.py --gold_file_path="data/training/20161019_3pres.tsv,data/training/20160414_9dem.tsv,data/training/20180916_trump_miami.tsv,data/training/20170928_trump_tax.tsv,data/training/20182601_trump_world.tsv,data/training/20160722_trump_acceptance.tsv,data/training/20170228_trump_address.tsv" --pred_file_path="../baseline_predictions/20161019_3pres.tsv,../baseline_predictions/20160414_9dem.tsv,../baseline_predictions/20180916_trump_miami.tsv,../baseline_predictions/20170928_trump_tax.tsv,../baseline_predictions/20182601_trump_world.tsv,../baseline_predictions/20160722_trump_acceptance.tsv,../baseline_predictions/20170228_trump_address.tsv" 
cd ..


END

python uni_bigram_baseline.py --train_set CLEF_2019 --include_MultiFC_data yes
cd clef2019-factchecking-task1/
PYTHONPATH="." python3 scorer/main.py --gold_file_path="data/training/20161019_3pres.tsv,data/training/20160414_9dem.tsv,data/training/20180916_trump_miami.tsv,data/training/20170928_trump_tax.tsv,data/training/20182601_trump_world.tsv,data/training/20160722_trump_acceptance.tsv,data/training/20170228_trump_address.tsv" --pred_file_path="../baseline_predictions/20161019_3pres.tsv,../baseline_predictions/20160414_9dem.tsv,../baseline_predictions/20180916_trump_miami.tsv,../baseline_predictions/20170928_trump_tax.tsv,../baseline_predictions/20182601_trump_world.tsv,../baseline_predictions/20160722_trump_acceptance.tsv,../baseline_predictions/20170228_trump_address.tsv" 
