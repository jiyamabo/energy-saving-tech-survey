# apply this coding to variables: "perp5_roof_solar", "increase_ac", "turnoff_ac", "turnoff_water", "stop_laundry", "eff_lightbulb", 
# "eff_ac", "eff_cook", "eff_heat", "eff_cool", "elect_cook1", "cool_load", "elect_cook2", "heat_load", "light", "comp_tv" 
# --------------------------
likert_dict = {
    "Not at all likely": 1, 
    "Slightly likely": 2, 
    "Moderately likely": 3, 
    "Very likely": 4, 
    "Extremely likely": 5
    }

def perp5Scale(rating):
    if rating in likert_dict:
        return likert_dict[rating]
    return rating 