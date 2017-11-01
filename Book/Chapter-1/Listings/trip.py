# coding: utf-8

import random
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import statistics
import numpy as np
import scipy
from scipy import stats
import seaborn


data = pd.read_csv('cycle-share-dataset/trip.csv', error_bad_lines=False)
