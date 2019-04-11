cd OpenNMT-py

#Preprocessing
python preprocess.py -train_src data/src-train.txt -train_tgt data/tgt-train.txt -valid_src data/src-val.txt -valid_tgt data/tgt-val.txt -save_data data/demo

#Training data
python train.py -data data/src-train -save_model test-model


#Generating translations
python translate.py -model demo-model_XYZ.pt -src data/src-test.txt -output pred.txt -replace_unk -verbose

#Evaluating scores
python calculatebleu.py "pred.txt" "tgt-test.txt"


python preprocess.py -train_src data/src-en-afr.txt -train_tgt data/tgt-en-afr.txt -save_data data/prep


python train.py -data data/train_parent -save_model demo-model
