#!/usr/bin/env python3
"""
Convert districts-schools.json to JavaScript object for embedding in HTML
"""

import json

def convert_json_to_js():
    # Read the JSON file
    with open('districts-schools.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Convert to JavaScript object format
    js_content = "const districtsSchools = " + json.dumps(data, indent=4, ensure_ascii=False) + ";"
    
    # Save to JavaScript file
    with open('districts-data.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"✅ Converted JSON to JavaScript")
    print(f"📊 Districts: {len(data)}")
    print(f"📚 Total schools: {sum(len(schools) for schools in data.values())}")
    print(f"📄 Output: districts-data.js")
    
    # Also print the first few lines for verification
    print(f"\n📋 Preview:")
    lines = js_content.split('\n')
    for i, line in enumerate(lines[:10]):
        print(f"  {i+1:2d}| {line}")
    if len(lines) > 10:
        print(f"  ...and {len(lines) - 10} more lines")

if __name__ == "__main__":
    convert_json_to_js()
