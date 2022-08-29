# apply this coding to variable: buy_electric_vehicle_5pt
# --------------------------
likert_dict = {
    "Not at all likely": 1,
    "Slightly likely": 2,
    "Moderately likely": 3,
    "Very likely": 4,
    "Extremely likely": 5
    }

def electric5Scale(rating):
    if rating in likert_dict:
        return likert_dict[rating]
    return rating