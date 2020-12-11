from cleandata import *
with open('data/topic_detection_test_prep.txt', 'w', encoding="utf8") as fp:
    for line in open('data/topic_detection_test.txt', 'r', encoding="utf8"):
        line = text_preprocess(line)
        line = remove_stopwords(line)
        fp.write(line + '\n')