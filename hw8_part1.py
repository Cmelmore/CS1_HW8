"""
Author: Christina Elmore
RIN: 661542904
Section #: 2
Assignment: HW 8 Part 1
Purpose: Determine which categories co-occur with the given category more than the given number of times.
"""

import json

if __name__ == '__main__':
    selected_cat = raw_input('Enter a category ==> ')
    print selected_cat
    cutoff = int(raw_input('Cutoff for displaying categories => '))
    print cutoff
    
    #create count of categories that co-occur with selected category
    cat_count = {}
    f = open('businesses.json')
    for line in f:
        business = json.loads(line)
        if selected_cat in business['categories']:
            for category in business['categories']:
                if category not in cat_count:
                    cat_count[category] = 1
                else:
                    cat_count[category] += 1
    sorted_cat_count = sorted(cat_count.keys())
    
    #seporates categories with counts above the cutoff
    met_cutoff = []
    for category in sorted_cat_count:
        if cat_count[category] >= cutoff:
            met_cutoff.append([category, cat_count[category]])
    
    #prints appropriate responses
    if len(cat_count) < 1: 
        print "Searched category is not found"
    elif len(met_cutoff) < 1:
        print "Categories co-occurring with %s:" %selected_cat
        print "None above the cutoff"
    else: 
        print "Categories co-occurring with %s:" %selected_cat
        for cat in met_cutoff:
            if cat[0] == selected_cat:
                continue
            print '%30s: %d' %(cat[0], cat[1])