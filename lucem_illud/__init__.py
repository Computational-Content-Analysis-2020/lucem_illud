import os
#For Windows
if os.name == 'nt':
    os.environ['JAVAHOME'] =  "C:/Program Files/Java/jdk1.8.0_161/bin/java.exe"

import nltk

#setting the path for nltk
try:
    #adding path for both local and server, only one of these will actually be used at a time
    nltk.data.path.append('/project2/macs60000/shared_data/nltk')
    nltk.data.path.append('../data')
    #Check that everything is in place
    nltk.corpus.gutenberg.fileids()
except LookupError:
    print("You have to download all the nltk documents")
    print("Downloading to ../data this should only take a couple minutes")
    nltk.download('all', download_dir = '../data')
    nltk.data.path.append('../data')

#gensim uses a couple of deprecated features
#we can't do anything about them so lets ignore them
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)


from .data_dirs  import *
from .downloaders import *
from .loaders import *
from .visualizers import *
from .proccessing import *
from .cartoons import *
from .metrics import *
from .bayesian import *

from .info_extract import *


import requests
import re
import pkg_resources

_setupURL = 'https://raw.githubusercontent.com/Computational-Content-Analysis-2018/lucem_illud/master/setup.py'

def _checkCurrentVersion():
    r = requests.get(_setupURL, timeout=0.5)
    serverVersion = re.search(r'versionString = \'(.+)\'', r.text).group(1)
    localVersion = pkg_resources.get_distribution('lucem_illud').version
    if serverVersion != serverVersion:
        print('lucem_illud is out of date, please update')
        print('pip install -U git+git://github.com/Computational-Content-Analysis-2018/lucem_illud.git')

try:
    checkCurrentVersion()
except:
    pass
