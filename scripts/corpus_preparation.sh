#!/usr/bin/env bash

../mosesdecoder/scripts/tokenizer/tokenizer.perl -l en < ../corpus/training/boun_parallel_corpus_train.en   \
    > ../corpus/training/boun_parallel_corpus_train.tok.en
../mosesdecoder/scripts/tokenizer/tokenizer.perl -l en < ../corpus/training/boun_parallel_corpus_train.tr    \
    > ../corpus/training/boun_parallel_corpus_train.tok.tr

../mosesdecoder/scripts/recaser/train-truecaser.perl --model ../corpus/training/truecase-model.en --corpus     \
     ../corpus/training/boun_parallel_corpus_train.tok.en
../mosesdecoder/scripts/recaser/train-truecaser.perl --model ../corpus/training/truecase-model.fr --corpus     \
     ../corpus/training/boun_parallel_corpus_train.tok.tr

../mosesdecoder/scripts/recaser/truecase.perl --model ../corpus/training/truecase-model.en        \
   < ../corpus/training/boun_parallel_corpus_train.tok.en > ../corpus/training/boun_parallel_corpus_train.true.en
../mosesdecoder/scripts/recaser/truecase.perl --model ../corpus/training/truecase-model.tr        \
   < ../corpus/training/boun_parallel_corpus_train.tok.tr > ../corpus/training/boun_parallel_corpus_train.true.tr

../mosesdecoder/scripts/training/clean-corpus-n.perl ../corpus/training/boun_parallel_corpus_train.true tr en \
    ./corpus/training/boun_parallel_corpus_train.tr-en.clean 1 80