def score_buyer(a):
    score = 0
    if "yes" in a["preapproved"].lower(): score += 3
    if "1" in a["timeframe"] or "month" in a["timeframe"]: score += 3
    if a["budget"]: score += 2
    return score

def score_seller(a):
    score = 0
    if "urgent" in a["reason"].lower(): score += 3
    if "1" in a["timeframe"] or "month" in a["timeframe"]: score += 3
    return score
