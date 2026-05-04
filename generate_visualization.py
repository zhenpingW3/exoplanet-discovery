import pandas as pd
import json
from datetime import datetime

# Load data
exoplanets = pd.read_csv('exoplanets.csv')

# Data cleaning and preparation
# ================================

# Simplify discovery methods (group rare ones)
def simplify_method(method):
    if 'Transit' in method:
        return 'Transit'
    elif 'Radial Velocity' in method:
        return 'Radial Velocity'
    elif 'Imaging' in method:
        return 'Imaging'
    else:
        return 'Other'

exoplanets['method_simplified'] = exoplanets['discoverymethod'].apply(simplify_method)

# Categorize planets by type
def categorize_planet(row):
    radius = row['pl_rade']
    mass = row['pl_bmasse']
    temp = row['pl_eqt']

    # Check habitable first
    if 250 <= temp <= 350 and 0.8 <= radius <= 1.5:
        return 'Habitable Earth-like'

    # Hot Jupiter: large radius, very hot (>1000K)
    if radius > 6 and temp > 1000:
        return 'Hot Jupiter'

    # Jupiter-like: large radius
    if radius > 6:
        return 'Jupiter-like'

    # Neptune-like: medium radius
    if 2 <= radius <= 6:
        return 'Neptune-like'

    # Super-Earth: small radius
    return 'Super-Earth'

exoplanets['planet_type'] = exoplanets.apply(categorize_planet, axis=1)

# View 1: Habitability Funnel data
# ================================
total = len(exoplanets)
habitable_zone = len(exoplanets[(exoplanets['pl_eqt'] >= 250) & (exoplanets['pl_eqt'] <= 350)])
earth_sized_habitable = len(exoplanets[
    (exoplanets['pl_eqt'] >= 250) & (exoplanets['pl_eqt'] <= 350) &
    (exoplanets['pl_rade'] >= 0.8) & (exoplanets['pl_rade'] <= 1.5)
])
future_detectable = len(exoplanets[
    (exoplanets['pl_eqt'] >= 250) & (exoplanets['pl_eqt'] <= 350) &
    (exoplanets['pl_rade'] >= 0.8) & (exoplanets['pl_rade'] <= 2.0)
])

funnel_data = {
    'levels': [
        {'label': 'All Exoplanets', 'count': total, 'percent': 100},
        {'label': 'Habitable Zone (250–350K)', 'count': habitable_zone, 'percent': round(habitable_zone/total*100, 1)},
        {'label': 'Earth-sized & Habitable', 'count': earth_sized_habitable, 'percent': round(earth_sized_habitable/total*100, 2)},
        {'label': 'Future Detection Potential', 'count': future_detectable, 'percent': round(future_detectable/total*100, 2)},
    ]
}

# View 2: Discovery Timeline data
# ================================
timeline_data = exoplanets.groupby(['disc_year', 'method_simplified']).size().unstack(fill_value=0).reset_index()
# Convert to cumulative
for col in ['Transit', 'Radial Velocity', 'Imaging', 'Other']:
    if col in timeline_data.columns:
        timeline_data[col] = timeline_data[col].cumsum()

# View 2: Planetary Classification data
# ================================
type_counts = exoplanets['planet_type'].value_counts().to_dict()
type_avg_temp = exoplanets.groupby('planet_type')['pl_eqt'].mean().to_dict()

classification_data = []
for ptype in ['Super-Earth', 'Neptune-like', 'Jupiter-like', 'Hot Jupiter', 'Habitable Earth-like']:
    if ptype in type_counts:
        classification_data.append({
            'type': ptype,
            'count': int(type_counts[ptype]),
            'avg_temp': round(type_avg_temp.get(ptype, 0), 0),
            'percent': round(type_counts[ptype] / total * 100, 1)
        })

# Prepare example planets for each category
examples = {}
for ptype in ['Super-Earth', 'Neptune-like', 'Jupiter-like', 'Hot Jupiter', 'Habitable Earth-like']:
    planets = exoplanets[exoplanets['planet_type'] == ptype]
    if len(planets) > 0:
        sample = planets.nlargest(3, 'pl_rade')[['pl_name', 'pl_rade', 'pl_eqt']].head(2)
        examples[ptype] = [
            {'name': row['pl_name'], 'radius': f"{row['pl_rade']:.1f}", 'temp': f"{row['pl_eqt']:.0f}"}
            for _, row in sample.iterrows()
        ]

# Export data as JSON for HTML
data_json = {
    'funnel': funnel_data,
    'timeline': timeline_data.to_dict('records'),
    'classification': classification_data,
    'examples': examples,
    'total': total,
}

print(json.dumps(data_json, indent=2))
