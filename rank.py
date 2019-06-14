import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

#%matplotlib inline

from urllib.request import urlopen
from bs4 import BeautifulSoup

import ssl

url = "https://www.hubertiming.com/results/2017GPTR10K"
#url = "http://www.google.com"
html = urlopen(url)