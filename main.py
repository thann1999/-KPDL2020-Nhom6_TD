from cleandata import * 

# print(text_preprocess("TP HCM phạt người không đeo khẩu trang nơi công cộng. Người dân ở thành phố không đeo khẩu trang nơi công cộng sẽ bị xử phạt mức cao nhất 300.000 đồng, từ ngày 5/8."))
# Loại stopwords
with open('data/topic_detection_prep.txt', 'w', encoding="utf8") as fp:
    for line in open('data/topic_detection.txt', "r", encoding="utf8"):
        line = remove_stopwords(line)
        fp.write(line + '\n')