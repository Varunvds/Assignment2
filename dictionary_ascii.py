# -*- coding: utf-8 -*-
"""dictionary_ascii.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AstrhdCyJfW8r1ypkAQCM3K-s1yYu03B
"""

#Python program to print dictionary of alphabet in lower case as key and their ascii as value

alpha_dict = dict()
for i in range(97,123):
    alpha_dict[str(i)] = chr(i)
print(alpha_dict)

