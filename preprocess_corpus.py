from constants import (RAW_CORPUS_PATH,
                       ENGLISH_CORPUS_PATH,
                       TURKISH_CORPUS_PATH)

english_corpus_file = open(ENGLISH_CORPUS_PATH, "w")
turkish_corpus_file = open(TURKISH_CORPUS_PATH, "w")
raw_corpus_file = open(RAW_CORPUS_PATH, 'r')

it_file = iter(raw_corpus_file)
for line in it_file:
    line = line.strip('\n')
    if not line:
        continue
    line = next(it_file) # Turkish
    turkish_corpus_file.write(line)
    line = next(it_file) # English
    english_corpus_file.write(line)






