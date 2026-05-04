import json

with open('scatter_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Generate JavaScript code
js_code = "const scatterPlanets = " + json.dumps(data, ensure_ascii=False) + ";"

with open('scatter_embedded.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

print(f"Embedded {len(data)} planets into scatter_embedded.js")
print(f"File size: {len(js_code) / 1024:.1f} KB")
