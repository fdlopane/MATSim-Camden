'''
Creation of MATSim population for the London Borough of Camden

Started coding: August 2024

Author:
Dr Fulvio D. Lopane
The Bartlett Centre for Advanced Spatial Analysis
University College London
'''

import os

import geopandas as gpd
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

from config import *

def run_population_creation(borough='Camden'):
    print('Starting population creation...')
    # Import geographic data

    # Import London LSOAs
    lsoas_london = gpd.read_file(inputs['lsoas_path'])

    # Filter out borough (default = Camden)
    lsoas = lsoas_london.loc[lsoas_london['LA_NAME'] == borough]

    # Iterative Proportional Fitting (IPF)

    # read lsoa data for IPF
    lsoa_data = pd.read_csv(inputs['lsoa-data'])
    lsoa_data.rename(columns={'Codes': 'LSOA_CODE'}, inplace=True)
    lsoa_data.set_index('LSOA_CODE') # remember to change "£" to "GPB" in census table

    # Print fields of lsoa data df:
    for i in lsoa_data.columns:
        print(i)

    # Let's create a seed population which includes every possible combination of attributes:
    dims = {
        'age': ['0-15', '16-29', '30-44', '45-64', '65+'], # Todo: remove 'All Ages', 'working age'


    }


    # USE POPULATION SIM (which uses entropy maximisation) INSTEAD OF PAM+IPF
    # https://activitysim.github.io/populationsim/application_configuration.html
    # https://github.com/ActivitySim/populationsim?tab=readme-ov-file
    # activitysim PTV presentation: https://www.youtube.com/watch?v=kXwwnV7wbMM
    