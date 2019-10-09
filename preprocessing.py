#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:14:32 2019

@author: ian
"""

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

k = "JKN-KIS menanggung perawatan penyakit Orang Dengan Gangguan Jiwa, agar tidak tercipta Joker lainnya :)"
print('kalimat asli')
print(k)
print()
"""
    Tahapan Preprocessing
    Case Folding
    Filtering
    Stemming -> dapat refrensi opsional karena menambah kinerja server
    Tokenize
    Stopword Removal
    
    Caterin Stenize SR
"""


case_folding = k.lower()
print("Case Folding : ")
print(case_folding)
print()
fil = case_folding.translate(str.maketrans("","",string.punctuation))
print("Filtering")
print(fil)
print()
print('Stemming')
factory = StemmerFactory()
stemmer = factory.create_stemmer()
stemm = stemmer.stem(fil)
print(stemm)
print()
tokens = word_tokenize(stemm)
print("Tokenize")
print(tokens)

stopword = set(stopwords.words('indonesian'))

removed = []
for t in tokens:
    if t not in stopword:
        removed.append(t)
print()
print('stopwords removal')
print(removed)

