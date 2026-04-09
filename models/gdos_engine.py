# GDOS Core Engine

def gdos_score(data_integrity, context_awareness, risk_projection, ethical_weight, noise):
    """
    Calculate GDOS decision score
    """
    if noise == 0:
        return 0
    return (data_integrity * context_awareness * risk_projection * ethical_weight) / noise


def calculate_country_index(country_data):
    """
    Calculate average GDOS index for a country
    """
    scores = []
    
    for c in country_data:
        score = gdos_score(
            c['DI'],
            c['CA'],
            c['RP'],
            c['EW'],
            c['N']
        )
        scores.append(score)
    
    return sum(scores) / len(scores)


# Example test run
if __name__ == "__main__":
    india_data = [
        {'DI': 0.8, 'CA': 0.7, 'RP': 0.75, 'EW': 0.6, 'N': 0.2}
    ]
    
    print("India GDOS Index:", calculate_country_index(india_data))
