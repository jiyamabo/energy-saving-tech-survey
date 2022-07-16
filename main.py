# install conda && setup a venv for this project
# if conda is already installed, run" conda activate <venv> 
# conda activate conda-lab1

from cProfile import label
import numpy as np
import pandas as pd
import utils 

from scipy.stats import sem
from scipy.cluster import hierarchy
from scipy.spatial import distance

from sklearn import preprocessing
# from sklearn import AgglomerativeClustering
import sklearn.metrics as sm

from matplotlib import pyplot as plt

pd.set_option("display.max_rows", 100)
pd.set_option("display.max_columns", None)
plt.style.use("seaborn-white")

# objectives
# to create user personas (cluster analysis) based on technology of use 
# cluster survey respondents as follows: austere resource poor, normal, overuse/resource rich users
# selected variables for cluster analysis: demographic (), 

# ----------------------------------------------------------------------------------
# data preprocessing
# import codebook
codebook = pd.read_csv("data/codebook.csv") 

# data import && cleaning

col_names = pd.read_excel("data/Residential Consumer Survey Response (copy).xlsx",
                                    sheet_name="codebook", usecols="C")
col_names = col_names["new_var"].tolist()

resid = pd.read_excel("data/Residential Consumer Survey Response (copy).xlsx", 
                                    sheet_name="Responses", names=col_names)

# note that likert scales is inconsistent
# plus we want numeric values of likert scales
resid.columns
resid.info()
resid.head(5)
resid.tail(5)
resid.dtypes
resid.shape

# ----------------------------------------------------------------------------------
# drop variables with < 10% data
# drop NAs: if we drop NAs, n=165; 39% of df
# resid = resid.dropna()
resid = resid.drop(["months_use_airheater", "own_roof_solar", "charge_electric_vehicle", "electric_vehicle"], axis="columns")
resid.shape

# also, dataset contains a row where id=208 is deceased. delete row where respondent was deceased,  id=208
resid = resid[resid["age"].notna()]
resid.iloc[206:209, 2] # inspect data

# ----------------------------------------------------------------------------------
# recode likert scales using perp5Scale function
resid[["perp5_roof_solar", "increase_ac", "turnoff_ac", "turnoff_water", "stop_laundry", "eff_lightbulb", "eff_ac", "eff_cook", "eff_heat", "eff_cool", "elect_cook1", "cool_load", "elect_cook2", "heat_load", "light", "comp_tv"]] = resid[["perp5_roof_solar", "increase_ac", "turnoff_ac", "turnoff_water", "stop_laundry", "eff_lightbulb", "eff_ac", "eff_cook", "eff_heat", "eff_cool", "elect_cook1", "cool_load", "elect_cook2", "heat_load", "light", "comp_tv"]].applymap(utils.perp5Scale)

# recode likert scales using electric5Scale function
resid["buy_electric_vehicle"] = resid["buy_electric_vehicle"].map(utils.electric5Scale)

# recode likert scales using energy5scale function
resid[["perp_energy", "perp_active", "perp_green1", "perp_green2", "perp_reduce", "elect_consume"]] = resid[["perp_energy", "perp_active", "perp_green1", "perp_green2", "perp_reduce", "elect_consume"]].applymap(utils.energy5scale)

# recode likert scales using perp105Scale function
resid["perp10_roof_solar"] = resid["perp10_roof_solar"].map(utils.perp105Scale)

# recode gender var
resid["gender"] = resid["gender"].map(utils.genderscale)

# ----------------------------------------------------------------------------------
# check data type per var: 
var_select = ["ac_num", "ac_type", "age", "heaters_owned", "coolers_owned", "adult_num", "child_num", "temp_set_summer", "temp_set_winter", "ac_control", "house_type", "buy_electric_vehicle", "employ_num", "employ_status", "gender", "geyser_heater", "start_use_airheater", "ac_control", "perp10_roof_solar", "perp5_roof_solar", "roof_solar", "solar_heater", "washing_machine", "dryer", "increase_ac", "turnoff_ac", "turnoff_water", "stop_laundry", "eff_ac", "perp_active"]

resid[var_select].info()
resid[var_select].dtypes

# subset of categorical vars for cross-tabulation
crosstab_vars = ["ac_num", "ac_type", "heaters_owned", "coolers_owned", "adult_num", "child_num", "temp_set_summer", "temp_set_winter", "ac_control", "house_type", "employ_num", "employ_status", "gender", "geyser_heater", "start_use_airheater", "ac_control", "roof_solar", "solar_heater", "washing_machine", "dryer"]

for i in crosstab_vars:
    print("-" * 20 + i + "-" * 20)
    resid[i].value_counts(dropna = False, sort=True, ascending=False)

# ----------------------------------------------------------------------------------
# plotting
# note that all likert features are on 5pt likert scales
# likert_features = ["buy_electric_vehicle", "comp_tv", "cool_load", "eff_ac", "eff_cook", "eff_cool", "eff_heat", "eff_lightbulb", "elect_consume", "elect_cook1", "elect_cook2", "heat_load", "increase_ac", "light", "perp_active", "perp_energy", "perp_green1", "perp_green2", "perp_reduce", "perp10_roof_solar", "perp5_roof_solar", "stop_laundry", "turnoff_ac", "turnoff_water"]

likert_features = ["eff_lightbulb", "elect_consume", "eff_ac", "perp_active", "perp_energy", "perp_green1", "perp_reduce", "perp_green2", "stop_laundry", "comp_tv", "cool_load", "eff_cook", "eff_cool", "eff_heat", "elect_cook1", "elect_cook2", "heat_load", "increase_ac", "light", "turnoff_ac", "turnoff_water", "buy_electric_vehicle", "perp10_roof_solar", "perp5_roof_solar"]

# resid[likert_features].info()

resid[likert_features].plot(kind = "box")
plt.xticks(rotation = 45)
plt.yticks(np.arange(1, 6, 1)) 
plt.title("Distribution of Likert-scale measures", fontsize=16)
plt.tight_layout()
# plt.show()
plt.savefig("plots/likert_boxplots", dpi = 300)

# ----------------------------------------------------------------------------------
# pivot table for vars of interest
resid.pivot_table(values= ["eff_lightbulb", "elect_consume", "eff_ac", "perp_active", "perp_energy", "perp_green1", "perp_reduce", "perp_green2", "stop_laundry", "comp_tv", "cool_load", "eff_cook", "eff_cool", "eff_heat", "elect_cook1", "elect_cook2", "heat_load", "increase_ac", "light", "turnoff_ac", "turnoff_water", "buy_electric_vehicle", "perp10_roof_solar", "perp5_roof_solar"], index="geyser_on", aggfunc= [np.mean, sem])

# ----------------------------------------------------------------------------------
# preprocessing data for clustering; note that in addition to likert vars, we're including age, gender in clustering
# scale data

# selecting vars
resid_subset = resid[["gender", "eff_lightbulb", "elect_consume", "eff_ac", "perp_active", "perp_energy", "perp_green1", "perp_reduce", "perp_green2", "stop_laundry", "comp_tv", "cool_load", "eff_cook", "eff_cool", "eff_heat", "elect_cook1", "elect_cook2", "heat_load", "increase_ac", "light", "turnoff_ac", "turnoff_water", "buy_electric_vehicle", "perp10_roof_solar", "perp5_roof_solar"]]

# first check for NAs
resid_subset.loc[:, resid_subset.isnull().any()].columns

# fill NAs with mean of vector[i]
resid_subset.fillna(resid_subset.mean(), inplace=True)
resid_subset.head()

# scaling selected variables
resid_subset_scaled = pd.DataFrame(preprocessing.scale(resid_subset), columns=resid_subset.columns)

# ----------------------------------------------------------------------------------
# hierarchical clustering
linkages = hierarchy.linkage(resid_subset_scaled, method="ward")
hierarchy.dendrogram(linkages, leaf_rotation=45, color_threshold=25)

plt.title("Truncated Hierarchical Clustering Dendogram")
plt.xlabel("Cluster Size")
plt.ylabel("Distance")
plt.axhline(y = 25)
plt.show()

# cophenetic correlation coefficient (CPCC)
# 0.4770361482010881
hierarchy.cophenet(linkages, distance.pdist(resid_subset_scaled))[0]

# labels
labels = hierarchy.fcluster(linkages, t=4, criterion="maxclust")
list(zip(*np.unique(labels, return_counts=True)))

# def cluster_plot(x, y, labls):
#     for i in np.unique(labls):
#         idx = labls == i
#         plt.scatter(x[idx], y[idx], labls = i)
#     plt.legend()
#     plt.xlabel(x)
#     plt.ylabel(y)

# cluster_plot(resid_subset_scaled.gender, resid_subset_scaled.eff_lightbulb, labels)
# # plt.show()






# ----------------------------------------------------------------------------------
# test
