# apply this coding to variable: perp10_roof_solar
# --------------------------
likert_dict = {
    "Not at all interested": 1,
    "Extremely interested": 2,
    "Very interested": 3,
    "Slightly interested": 4,
    "Moderately interested": 5
    }

def perp105Scale(rating):
    if rating in likert_dict:
        return likert_dict[rating]
    return rating
