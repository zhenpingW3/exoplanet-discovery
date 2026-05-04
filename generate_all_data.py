import pandas as pd
import json

# Load data
exoplanets = pd.read_csv('exoplanets.csv')

# Simplify discovery methods
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

# Categorize planets
def categorize_planet(row):
    radius = row['pl_rade']
    temp = row['pl_eqt']

    if 250 <= temp <= 350 and 0.8 <= radius <= 1.5:
        return 'Habitable Earth-like'
    if radius > 6 and temp > 1000:
        return 'Hot Jupiter'
    if radius > 6:
        return 'Jupiter-like'
    if 2 <= radius <= 6:
        return 'Neptune-like'
    return 'Super-Earth'

exoplanets['planet_type'] = exoplanets.apply(categorize_planet, axis=1)

# Prepare detailed planet data for scatterplot
planets_data = []
for _, row in exoplanets.iterrows():
    planets_data.append({
        'name': row['pl_name'],
        'star': row['hostname'],
        'radius': float(row['pl_rade']),
        'mass': float(row['pl_bmasse']),
        'temp': float(row['pl_eqt']),
        'year': int(row['disc_year']),
        'method': row['method_simplified'],
        'type': row['planet_type'],
    })

# Prepare aggregated data
total = len(exoplanets)
habitable_zone = len(exoplanets[(exoplanets['pl_eqt'] >= 250) & (exoplanets['pl_eqt'] <= 350)])
earth_sized_habitable = len(exoplanets[
    (exoplanets['pl_eqt'] >= 250) & (exoplanets['pl_eqt'] <= 350) &
    (exoplanets['pl_rade'] >= 0.8) & (exoplanets['pl_rade'] <= 1.5)
])

funnel_data = {
    'levels': [
        {'label': 'All Exoplanets', 'count': total, 'percent': 100},
        {'label': 'Habitable Zone (250–350K)', 'count': habitable_zone, 'percent': round(habitable_zone/total*100, 1)},
        {'label': 'Earth-sized & Habitable', 'count': earth_sized_habitable, 'percent': round(earth_sized_habitable/total*100, 2)},
    ]
}

# Timeline
timeline_data = exoplanets.groupby(['disc_year', 'method_simplified']).size().unstack(fill_value=0).reset_index()
for col in ['Transit', 'Radial Velocity', 'Imaging', 'Other']:
    if col in timeline_data.columns:
        timeline_data[col] = timeline_data[col].cumsum()

# Classification
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

# Examples
examples = {}
for ptype in ['Super-Earth', 'Neptune-like', 'Jupiter-like', 'Hot Jupiter', 'Habitable Earth-like']:
    planets = exoplanets[exoplanets['planet_type'] == ptype]
    if len(planets) > 0:
        sample = planets.nlargest(3, 'pl_rade')[['pl_name', 'pl_rade', 'pl_eqt']].head(2)
        examples[ptype] = [
            {'name': row['pl_name'], 'radius': f"{row['pl_rade']:.1f}", 'temp': f"{row['pl_eqt']:.0f}"}
            for _, row in sample.iterrows()
        ]

data_json = {
    'funnel': funnel_data,
    'timeline': timeline_data.to_dict('records'),
    'classification': classification_data,
    'examples': examples,
    'total': total,
    'planets': planets_data,  # All planets for scatterplot
}

# Output as Python dict that can be embedded
print('const vizData = ' + json.dumps(data_json, ensure_ascii=False) + ';')
