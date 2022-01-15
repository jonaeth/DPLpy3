#!/bin/bash

data_type=gene # gene mention, also can choose disease, drug etc
source=pubmed_parsed # pubmed dataset
length=5  # length heuristic for validation
length_train=3 # length heuristic for train

#for i in {0..0}; do
#for j in {0..0}; do
#mkdir data/${source}/${data_type}_${i}/${j}/hard
#bash ./generate_data.sh ${data_type} ${length} ${length_train} ${j} ${i} 
#done         
#done

# all soft em with full feature set
for i in {0..0}; do
for j in {0..0}; do
for k in {1..3}; do # k=1,2,3 represent different supervision level
mkdir data/${source}/${data_type}_${i}_new/${j}/soft_featureset_${k}
bash ./generate_data_soft.sh ${data_type} ${length} ${length_train} ${j} ${k} ${i}
done
done
done