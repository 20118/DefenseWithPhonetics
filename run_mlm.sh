python3 run_mlm.py \
    --model_name_or_path bert-base-uncased \
    --train_file path to train data \
    --validation_file path to dev data \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --line_by_line True \
    --do_train \
    --do_eval \
    --output_dir tmp/test-mlm
