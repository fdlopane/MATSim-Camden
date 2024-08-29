'''
Creation of MATSim population for the London Borough of Camden

Started coding: August 2024

Author:
Dr Fulvio D. Lopane
The Bartlett Centre for Advanced Spatial Analysis
University College London
'''

import os

import geopandas as gp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pam.activity import Activity, Leg
from pam.core import Household, Person, Population
from pam.plot.stats import plot_activity_times
from pam.read import load_travel_diary
from pam.report.benchmarks import distance_counts, duration_counts
from pam.samplers import facility
from pam.utils import minutes_to_datetime as mtdt
from pam.variables import END_OF_DAY
from pam.write import to_csv, write_matsim, write_od_matrices

# Import geographic data
network_bb_path = os.path.join("data", "network_bounding_box.geojson")
lsoas_path = os.path.join("data", "lsoas")  # lsoas: lower layer super output areas