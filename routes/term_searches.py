'''
This module contains the routes for searching.
'''
from flask import Blueprint
import pickle
import sys 
from utils.CONSTANTS import DATABASE

# -- Setting up the utils path module -- 
sys.path.append('utils')

# -- Importing custom utilities --
from utils.search import generate_search_route
term_searches = Blueprint('term_searches', __name__)

# -- Constants --
DATABASE = pickle.load(open('allDic2', 'rb'))

# -- Generating the routes via function factories:
normal = generate_search_route(DATABASE, 'default')
exact = generate_search_route(DATABASE, 'exact')
alias = generate_search_route(DATABASE, 'alias')
substring = generate_search_route(DATABASE, 'substring')
non_alpha = generate_search_route(DATABASE, 'non-alphanumeric')

# -- Adding the routes --
term_searches.add_url_rule('/normal', endpoint = 'normal', view_func = normal, methods = ['POST'])
term_searches.add_url_rule('/exact', endpoint = 'exact', view_func = exact, methods = ['POST'])
term_searches.add_url_rule('/alias', endpoint = 'alias', view_func = alias, methods = ['POST'])
term_searches.add_url_rule('/substring', endpoint = 'substring', view_func = substring, methods = ['POST'])
term_searches.add_url_rule('/non_alpha', endpoint = 'non_alpha', view_func = non_alpha, methods = ['POST'])