# apply this coding to variable: gender
# --------------------------
likert_dict = {
    "Male": 0,
    "Female": 1,
    "Prefer not to say": 2
    }

def genderscale(rating):
    if rating in likert_dict:
        return likert_dict[rating]
    return rating
