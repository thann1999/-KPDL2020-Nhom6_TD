def count_label():
    f = open('data/topic_detection.txt', "r" ,encoding="utf8") 
    count = {}
    for line in f:
        key = line.split()[0]
        count[key] = count.get(key, 0) + 1
    # for key in count:
    #     print(key, count[key])
    return len(count)


def count_word(count_label):
    total_label = count_label
    f = open('data/topic_detection.txt', "r" ,encoding="utf8")
    vocab = {}
    label_vocab = {}
    for line in f:
        words = line.split()
        # lưu ý từ đầu tiên là nhãn
        label = words[0]
        if label not in label_vocab:
            label_vocab[label] = {}
        for word in words[1:]:
            label_vocab[label][word] = label_vocab[label].get(word, 0) + 1
            if word not in vocab:
                vocab[word] = set()
            vocab[word].add(label)
    count = {}
    for word in vocab:
        if len(vocab[word]) == total_label:
            count[word] = min([label_vocab[x][word] for x in label_vocab])
        
    sorted_count = sorted(count, key=count.get, reverse=True)
    return sorted_count
    # for word in sorted_count[:100]:
    #     print(word, count[word])

def addstopwords(sorted_count):
    stopword = set()
    with open('data/stopwords.txt', 'w', encoding="utf8") as fp:
        for word in sorted_count[:100]:
            stopword.add(word)
            fp.write(word + '\n')

label = count_label()
sorted_count = count_word(label)
# addstopwords(sorted_count)
