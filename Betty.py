#Import libraries
from newspaper import Article
import random
import string
# from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import numpy as np
import warnings