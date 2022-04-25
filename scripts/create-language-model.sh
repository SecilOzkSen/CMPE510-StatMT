#!/usr/bin/env bash
mkdir ../lm
cd ../lm
../kenlm/bin/lmplz -o 3 <../corpus/training/boun_parallel_corpus_train.true.en > \
../language-model/boun_parallel_corpus_train.tr-en.arpa.en