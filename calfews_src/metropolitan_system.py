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


def initialization_routine(model, initial_condition, scenario = 'baseline'):

  attribute_dict = {}
  attribute_dict['anaheim'] = District(model, 'anaheim', 'BDM', scenario)
  attribute_dict['beverlyhills'] = District(model, 'beverlyhills', 'BDM', scenario)
  attribute_dict['burbank'] = District(model, 'burbank', 'BDM', scenario)
  attribute_dict['compton'] = District(model, 'compton', 'BDM', scenario)
  attribute_dict['fullerton'] = District(model, 'fullerton', 'BDM', scenario)
  attribute_dict['glendale'] = District(model, 'glendale', 'BDM', scenario)
  attribute_dict['longbeach'] = District(model, 'longbeach', 'BDM', scenario)
  attribute_dict['losangeles'] = District(model, 'losangeles', 'BDM', scenario)
  attribute_dict['pasadena'] = District(model, 'pasadena', 'BDM', scenario)
  attribute_dict['sanfernando'] = District(model, 'sanfernando', 'BDM', scenario)
  attribute_dict['sanmarino'] = District(model, 'sanmarino', 'BDM', scenario)
  attribute_dict['santaana'] = District(model, 'santaana', 'BDM', scenario)
  attribute_dict['santamonica'] = District(model, 'santamonica', 'BDM', scenario)
  attribute_dict['torrance'] = District(model, 'torrance', 'BDM', scenario)
  attribute_dict['calleguas'] = District(model, 'calleguas', 'BDM', scenario)
  attribute_dict['centralbasin'] = District(model, 'centralbasin', 'BLR', scenario)
  attribute_dict['eastern'] = District(model, 'eastern', 'BVA', scenario)
  attribute_dict['foothill'] = District(model, 'foothill', 'CWO', scenario)
  attribute_dict['inlandempire'] = District(model, 'inlandempire', 'HML', scenario)
  attribute_dict['lasvirgenes'] = District(model, 'lasvirgenes', 'HML', scenario)
  attribute_dict['orangecounty'] = District(model, 'orangecounty', 'HML', scenario)
  attribute_dict['sandiegocounty'] = District(model, 'sandiegocounty', 'HML', scenario)
  attribute_dict['threevalleys'] = District(model, 'threevalleys', 'HML', scenario)
  attribute_dict['westbasin'] = District(model, 'westbasin', 'HML', scenario)
  attribute_dict['riversidecounty'] = District(model, 'riversidecounty', 'HML', scenario)
  attribute_dict['uppersangabriel'] = District(model, 'uppersangabriel', 'HML', scenario)

  return attribute_dict

