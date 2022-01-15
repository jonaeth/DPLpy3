#!/bin/bash

# bash ./generate_data_soft.sh gene 5 3 0 1-3 0

source ~/.bashrc

data_type=gene
source=pubmed_parsed # data source
length=5
length_train=3
input_split=0 # cross validation

#if [ ! -f data/${source}/${data_type}_${input_split}/${4}/soft_featureset_${5}/train_${length_train}.pkl ] || [ ! -f data/${source}/${data_type}_${input_split}/${4}/soft_featureset_${5}/test_${length}.pkl ] || [ ! -f data/${source}/${data_type}_${input_split}/${4}/soft_featureset_${5}/validation_${length}.pkl ]; then 
python generate_dataset.py \
        --input_clinlical_matching data/pubmed_parsed/pubmed_parsed_splits_dict_0.pkl \
        --ouput_train data/pubmed_parsed/gene_0_new/0/soft_featureset_${5}/train_3.pkl \
        --ouput_test data/pubmed_parsed/gene_0_new/0/soft_featureset_${5}/test_5pkl \
        --ouput_val data/pubmed_parsed/gene_0_new/0/soft_featureset_${5}/validation_5.pkl \
        --entity_type gene \
        --min_length 5 \
        --html_file data/pubmed_parsed/gene_0_new/0/soft_featureset_${5}/sample_3.html \
        --min_length_train 3 \
        --cv 0 \
        --hard_em 0 \
        --factor_set ${5}
#fi
