#!/usr/bin/env python3
"""
Script to generate districts and schools structure from pubschls.json
Creates a JSON with districts as keys and schools as arrays of values
Filters only Santa Clara County data
"""

import json
from collections import defaultdict

def generate_districts_schools():
    # Read the original JSON file
    try:
        with open('pubschls.json', 'r', encoding='utf-8') as f:
            schools_data = json.load(f)
    except FileNotFoundError:
        print("Error: pubschls.json file not found")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in pubschls.json")
        return
    
    # Dictionary to store districts and their schools
    districts_schools = defaultdict(set)  # Using set to avoid duplicates
    
    # Counter for statistics
    total_records = 0
    santa_clara_records = 0
    
    print("Processing school records...")
    
    # Process each school record
    for record in schools_data:
        total_records += 1
        
        # Filter only Santa Clara County
        if record.get('County') == 'Santa Clara':
            santa_clara_records += 1
            
            district = record.get('District', '').strip()
            school = record.get('School', '').strip()
            
            # Only add if both district and school are valid
            if district and school and school != 'No Data':
                districts_schools[district].add(school)
    
    # Convert sets to sorted lists for better readability
    districts_schools_dict = {}
    for district, schools in districts_schools.items():
        districts_schools_dict[district] = sorted(list(schools))
    
    # Sort districts alphabetically
    sorted_districts = dict(sorted(districts_schools_dict.items()))
    
    # Save to new JSON file
    output_file = 'districts-schools.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(sorted_districts, f, indent=2, ensure_ascii=False)
    
    # Print statistics
    print(f"\n📊 Processing Statistics:")
    print(f"Total records processed: {total_records:,}")
    print(f"Santa Clara County records: {santa_clara_records:,}")
    print(f"Districts found: {len(sorted_districts)}")
    print(f"Total schools: {sum(len(schools) for schools in sorted_districts.values())}")
    
    print(f"\n✅ Successfully generated: {output_file}")
    
    # Print first few districts as preview
    print(f"\n📋 Preview of districts:")
    for i, (district, schools) in enumerate(sorted_districts.items()):
        if i < 5:  # Show first 5 districts
            print(f"  • {district}: {len(schools)} schools")
            if len(schools) <= 3:
                for school in schools:
                    print(f"    - {school}")
            else:
                for school in schools[:3]:
                    print(f"    - {school}")
                print(f"    ... and {len(schools) - 3} more")
        elif i == 5:
            print(f"  ... and {len(sorted_districts) - 5} more districts")
            break
    
    return sorted_districts

if __name__ == "__main__":
    print("🏫 Generating Santa Clara County Districts and Schools")
    print("=" * 50)
    
    result = generate_districts_schools()
    
    if result:
        print(f"\n🎉 Process completed successfully!")
        print(f"The file 'districts-schools.json' is ready to use in your HTML form.")
    else:
        print(f"\n❌ Process failed. Please check the error messages above.")
