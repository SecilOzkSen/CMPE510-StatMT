import pandas as pd
import numpy as np
from constants import (ENGLISH_CORPUS_PATH,
                       TURKISH_CORPUS_PATH,
                       TRAINING_PERCENTAGE,
                       DEV_PERCENTAGE,
                       EN_TRAINING,
                       EN_DEV,
                       EN_TEST,
                       TR_TRAINING,
                       TR_DEV,
                       TR_TEST)

english_corpus_file = open(ENGLISH_CORPUS_PATH, "r")
turkish_corpus_file = open(TURKISH_CORPUS_PATH, "r")

english_corpus_data = english_corpus_file.read()
turkish_corpus_data = turkish_corpus_file.read()

en_to_list = english_corpus_data.split('\n')
tr_to_list = turkish_corpus_data.split('\n')

data_frame = pd.DataFrame(list(zip(en_to_list, tr_to_list)), columns=['en', 'tr'])

training_size = int(np.floor(len(data_frame)*TRAINING_PERCENTAGE))
dev_size = int(np.floor(len(data_frame)*DEV_PERCENTAGE))

training_data = data_frame.sample(n=training_size, random_state=25)
leftover_data = data_frame.drop(training_data.index)
dev_data = leftover_data.sample(n=dev_size, random_state=25)
test_data = leftover_data.drop(dev_data.index)

en_training = open(EN_TRAINING, "w")
en_dev = open(EN_DEV, "w")
en_test = open(EN_TEST, "w")

tr_training = open(TR_TRAINING, "w")
tr_dev = open(TR_DEV, "w")
tr_test = open(TR_TEST, "w")

lst = training_data['tr'].tolist()
tr_training.write('\n'.join(training_data['tr'].tolist()) + '\n')
en_training.write('\n'.join(training_data['en'].tolist()) + '\n')

tr_dev.write('\n'.join(dev_data['tr'].tolist()) + '\n')
en_dev.write('\n'.join(dev_data['en'].tolist()) + '\n')

tr_test.write('\n'.join(test_data['tr'].tolist()) + '\n')
en_test.write('\n'.join(test_data['en'].tolist()) + '\n')



