import main

# resid["perp5_roof_solar"].value_counts()

# inspect the coding structure of all likert-type variables
# for i in resid[["perp5_roof_solar", "perp10_roof_solar", "buy_electric_vehicle", "perp_energy", "perp_active", "perp_green1", "perp_green2", "perp_reduce", "elect_consume", "increase_ac", "turnoff_ac", "turnoff_water", "stop_laundry", "eff_lightbulb", "eff_ac", "eff_cook", "eff_heat", "eff_cool", "elect_cook1", "cool_load", "elect_cook2", "heat_load", "light", "comp_tv"]]:
#     print("-" * 20 + i + "-" * 20) 
#     print(resid[i].value_counts(sort=False, dropna=False))


#  cross-check: # recode likert scales
# resid[["perp5_roof_solar", "increase_ac", "turnoff_ac", "turnoff_water", "stop_laundry", "eff_lightbulb", "eff_ac", "eff_cook", "eff_heat", "eff_cool", "elect_cook1", "cool_load", "elect_cook2", "heat_load", "light", "comp_tv"]].head(9)

#  cross-check
# resid["buy_electric_vehicle"].head(9)

#  cross-check
# resid[["perp_energy", "perp_active", "perp_green1", "perp_green2", "perp_reduce", "elect_consume"]].head(9)


# if __name__ == "__main__":
#     pass