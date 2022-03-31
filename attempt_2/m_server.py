#SERVER FILE
# ALEXANDER BAEKEY #
# Sat Mar 19 14:37:44 2022 #

#TODO 
# what am I plotting? look at netlogo model
# will look like metric = []

from m_model import *
from m_agent import *
import numpy as np
import matplotlib.pyplot as plt


num_agents = 50 
num_steps  = 200


model = micelle_model(num_agents)
for i in range(num_steps):
    model.step()





