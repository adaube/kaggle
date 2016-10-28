import pandas as pd
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
matplotlib.style.use('ggplot')

pd.options.display.max_columns = 100
pd.options.display.max_rows = 100

data = pd.read_csv('/data/train.csv')
