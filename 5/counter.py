from collections import Counter
breakfast = ['spam','spamr','eggs','spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)


# 降順
breakfast_counter.most_common()
# 個数
breakfast_counter.most_common(1)