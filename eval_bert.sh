BERT_BASE_DIR="bert_model/cased_L-12_H-768_A-12"
DATA_DIR="bert_input_files"
OUTPUT_DIR="BERT_CLEF2019_AND_CLAIMBUSTER"
BERT_SCRIPTS="bert"

fns="20161019_3pres.tsv 20160414_9dem.tsv 20180916_trump_miami.tsv 20170928_trump_tax.tsv 20182601_trump_world.tsv 20160722_trump_acceptance.tsv 20170228_trump_address.tsv"
for fn in $fns
do
echo $fn
PYTHONPATH=$BERT_SCRIPTS python $BERT_SCRIPTS"/run_classifier.py" \
  --task_name=CLEF2019 \
  --do_train=false \
  --do_eval=false \
  --do_predict=true \
  --file_to_predict=$fn \
  --file_with_predictions=$fn \
  --data_dir=$DATA_DIR \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
  --max_seq_length=128 \
  --train_batch_size=32 \
  --learning_rate=2e-5 \
  --num_train_epochs=3.0 \
  --do_lower_case=False \
  --output_dir=$OUTPUT_DIR
python postprocess.py $fn $OUTPUT_DIR
done
echo "job finished"
# bsub -n 1 -R "rusage[mem=12800,ngpus_excl_p=1]" bash eval_bert.sh

cd clef2019-factchecking-task1/
PYTHONPATH="." python3 scorer/main.py --gold_file_path="data/training/20161019_3pres.tsv,data/training/20160414_9dem.tsv,data/training/20180916_trump_miami.tsv,data/training/20170928_trump_tax.tsv,data/training/20182601_trump_world.tsv,data/training/20160722_trump_acceptance.tsv,data/training/20170228_trump_address.tsv" --pred_file_path="../BERT_CLEF2019/20161019_3pres.tsv,../BERT_CLEF2019/20160414_9dem.tsv,../BERT_CLEF2019/20180916_trump_miami.tsv,../BERT_CLEF2019/20170928_trump_tax.tsv,../BERT_CLEF2019/20182601_trump_world.tsv,../BERT_CLEF2019/20160722_trump_acceptance.tsv,../BERT_CLEF2019/20170228_trump_address.tsv" 
cd ..





