import pandas as pd 
import numpy as np

def read_data_for_chars(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    return data

def read_data_for_words(file_path):
    with open(file_path, 'r') as file:
        data = file.read().split()
    return data

class GramsChars:
    def __init__(self, file_path):
        self.data = read_data_for_chars(file_path)
        self.two_grams_set = set()
        self.two_grams_freq = {}

        self.three_grams_set = set()
        self.three_grams_freq = {}

        self.data_strings = read_data_for_words(file_path)
        self.two_grams_words_set = set()
        self.two_grams_words_freq = {}
    
    def get_two_grams_chars(self):
        # print("whole string",self.data)
        for i in range(len(self.data) - 1):
            two_gram = self.data[i:i+2]
            two_gram_str = ''.join(two_gram) 
            self.two_grams_set.add(two_gram_str)

            if two_gram_str in self.two_grams_freq:
                self.two_grams_freq[two_gram_str] += 1
            else:
                self.two_grams_freq[two_gram_str] = 1

        

        return list(self.two_grams_set)

    def get_three_grams_chars(self):
        for i in range(len(self.data) - 2):
            three_gram = self.data[i:i+3]
            # print("three_gram",three_gram)
            three_gram_str = ''.join(three_gram)
            self.three_grams_set.add(three_gram_str)

            if three_gram_str in self.three_grams_freq:
                self.three_grams_freq[three_gram_str] += 1
            else:
                self.three_grams_freq[three_gram_str] = 1

        return list(self.three_grams_set)
    
    def get_tow_grams_words(self):
        # print("stirng array",self.data_strings)
        for i in range(len(self.data_strings) - 1):
            two_gram = self.data_strings[i:i+2]
            two_gram_str = ''.join(two_gram)
            self.two_grams_words_set.add(two_gram_str)

            if two_gram_str in self.two_grams_words_freq:
                self.two_grams_words_freq[two_gram_str] += 1
            else:
                self.two_grams_words_freq[two_gram_str] = 1
        
        return list(self.two_grams_words_set)
    

        

# # path = '/Users/xsyang/Documents/GitHub/miscellaneous/data/D1.txt'
# # chars_instance = GramsChars(path)
# # two_grams = chars_instance.get_two_grams_chars()
# # three_grams = chars_instance.get_three_grams_chars()
# # two_grams_words = chars_instance.get_tow_grams_words()

# # print(len(two_grams))
# # print(len(three_grams))
# # print(len(two_grams_words))

# # print(two_grams_words)

def jacard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union

for i in range(1,5):
    path = (f'/Users/xsyang/Documents/GitHub/miscellaneous/data/D{i}.txt')
    chars_instance = GramsChars(path)
    two_grams_set = chars_instance.get_two_grams_chars()
    three_grams = chars_instance.get_three_grams_chars()
    two_grams_words = chars_instance.get_tow_grams_words()

    print(f"Number of 2-grams chars in D{i}.txt: {len(two_grams_set)}")
    print(f"Number of 3-grams chars in D{i}.txt: {len(three_grams)}")
    print(f"Number of 2-grams words in D{i}.txt: {len(two_grams_words)}")

for i in range(1,5):
    path = (f'/Users/xsyang/Documents/GitHub/miscellaneous/data/D{i}.txt')
    chars_instance = GramsChars(path)
    two_grams = chars_instance.get_two_grams_chars()
    three_grams = chars_instance.get_three_grams_chars()
    two_grams_words = chars_instance.get_tow_grams_words()

    two_grams_set = set(two_grams)
    three_grams_set = set(three_grams)
    two_grams_words_set = set(two_grams_words)

    for j in range(i+1, 5):
        path = (f'/Users/xsyang/Documents/GitHub/miscellaneous/data/D{j}.txt')
        chars_instance = GramsChars(path)
        two_grams = chars_instance.get_two_grams_chars()
        three_grams = chars_instance.get_three_grams_chars()
        two_grams_words = chars_instance.get_tow_grams_words()

        two_grams_set_j = set(two_grams)
        three_grams_set_j = set(three_grams)
        two_grams_words_set_j = set(two_grams_words)

        print(f"Jaccard similarity between D{i}.txt and D{j}.txt for 2-grams chars: {jacard_similarity(two_grams_set, two_grams_set_j):.3f}")
        print(f"Jaccard similarity between D{i}.txt and D{j}.txt for 3-grams chars: {jacard_similarity(three_grams_set, three_grams_set_j):.3f}")
        print(f"Jaccard similarity between D{i}.txt and D{j}.txt for 2-grams words: {jacard_similarity(two_grams_words_set, two_grams_words_set_j):.3f}")




num_hashes_list = [20, 60, 150, 300, 600]


import random as rd
import hashlib


def minhash_signature(n_gram_set, num_hashes, total_size):
    signature = np.full(num_hashes, fill_value=np.inf)
    #random pairs
    m = []
    for _ in range(num_hashes):
        a = rd.randint(1, 1000)
        b = rd.randint(1, 1000)
        m.append((a, b))

    
    for i, (a, b) in enumerate(m):
        min_val = float('inf')
        
        for element in n_gram_set:
            # compute a universal-based index
            salted_element = f"{element}{a}{b}"

            h = int(hashlib.sha1(salted_element.encode('utf8')).hexdigest(), 16) % total_size

            if h < min_val:
                min_val = h
        
        signature[i] = min_val
    
    return signature

t_values = [20, 60, 150, 300, 600]

data1_path = '/Users/xsyang/Documents/GitHub/miscellaneous/data/D1.txt'
data2_path = '/Users/xsyang/Documents/GitHub/miscellaneous/data/D2.txt'

chars_instance1 = GramsChars(data1_path)
three_grams1 = chars_instance1.get_three_grams_chars()

chars_instance2 = GramsChars(data2_path)
three_grams2 = chars_instance2.get_three_grams_chars()

all_ngrams = set(three_grams1).union(set(three_grams2))

# t_values_2 = [60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,]
# t_values_3 = [105,110,115,120,125,130,135,140,145,150,155,160]

for t in t_values:
    sig1 = minhash_signature(three_grams1, t, len(all_ngrams))
    sig2 = minhash_signature(three_grams2, t, len(all_ngrams))
    
    matches = 0
    for x, y in zip(sig1, sig2):
        if x == y:
            matches += 1

    js_apporx = matches / t
    
    print(f"t = {t},  Estimated Jaccard = {js_apporx:.3f}")


for t in range(1060, 1100):
    sig1 = minhash_signature(three_grams1, t, len(all_ngrams))
    sig2 = minhash_signature(three_grams2, t, len(all_ngrams))
    
    matches = 0

    for x, y in zip(sig1, sig2):
        if x == y:
            matches += 1

    js_est = matches / t
    
    print(f"t = {t},  Estimated Jaccard = {js_apporx:.3f}")
