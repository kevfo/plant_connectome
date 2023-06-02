import sys
import pickle
sys.path.append('./utils')

DATABASE = pickle.load(open('allDic2', 'rb'))
AUTHORS = pickle.load(open('authors', 'rb'))
TITLES = pickle.load(open('titles', 'rb'))