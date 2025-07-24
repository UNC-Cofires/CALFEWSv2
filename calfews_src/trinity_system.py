import numpy as np
import pandas as pd
import collections as cl
import sys
import calendar
import json
import matplotlib.pyplot as plt
import time
import h5py
from .util import *
from .reservoir_cy import Reservoir
from .delta_cy import Delta
from .canal_cy import Canal
from .district_cy import District
from .private_cy import Private
from .waterbank_cy import Waterbank
from .contract_cy import Contract
from .participant_cy import Participant

  
def initialization_routine(model, initial_condition):
    
  attribute_dict = {}
  attribute_dict['trinity'] = Reservoir(model, 'trinity', 'SHA', model.model_mode, initial_condition)
    
  return attribute_dict

