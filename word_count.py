import re


def w_count(text, word_list=[]):
    words = re.findall(r"[\w']+", text)
    # print(words)
    d = {}
    for x in words:
        if x in words:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
    df = {}
    mx = len(word_list) + 1
    sc = 0
    for x in word_list:
        if x in d:
            sc += d[x] * mx
            df[x] = d[x]
        else:
            df[x] = 0
    df.update({'score': sc})
    return df
