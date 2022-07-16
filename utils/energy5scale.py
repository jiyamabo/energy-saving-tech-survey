# apply this coding to variables: "perp_energy", "perp_active", "perp_green1", "perp_green2", "perp_reduce", "elect_consume"
# --------------------------
likert_dict = {
    "Strongly Agree": 5,
    "Agree": 4,
    "Indifferent": 3,
    "Strongly Disagree": 2,
    "Disagree": 1
    }

def energy5scale(rating):
    if rating in likert_dict:
        return likert_dict[rating]
    return rating 