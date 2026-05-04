import pandas as pd
import json

exoplanets = pd.read_csv('exoplanets.csv')

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

scatter_data = []
for idx, row in exoplanets.iterrows():
    scatter_data.append({
        'name': str(row['pl_name']),
        'radius': round(float(row['pl_rade']), 3),
        'mass': round(float(row['pl_bmasse']), 2),
        'temp': round(float(row['pl_eqt']), 1),
        'year': int(row['disc_year']),
        'method': row['method_simplified'],
        'star': str(row['hostname']),
    })

with open('scatter_data.json', 'w', encoding='utf-8') as f:
    json.dump(scatter_data, f, ensure_ascii=False)

print(f"Generated scatter data for {len(scatter_data)} planets")
