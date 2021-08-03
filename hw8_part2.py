"""
Author: Christina Elmore
RIN: 661542904
Section #: 2
Assignment: HW 8 Part 2
Purpose: Given a business name, find all reviwes of all business locations
"""
import json
import textwrap

if __name__ == '__main__':
    bus_name = raw_input('Enter a business name => ')
    print bus_name
    
    #matches business names with ids
    g = open('businesses.json')
    id_name = []
    for line in g:
        business = json.loads(line) 
        id_name.append([business['name'], business['business_id']])
       
    #pulls out ids for wanted business
    bus_ids = [] 
    i = 0
    while i < len(id_name):
        if id_name[i][0] == bus_name:
            bus_ids.append(id_name[i][1])
        i += 1
    
    #gets reviews for ids from wanted business
    f = open('reviews.json')
    review_list = []
    for line in f:
        review = json.loads(line)
        i = 0
        while i < len(bus_ids):
            if review['business_id'] == bus_ids[i]:
                review_list.append(review['text'])
            i += 1
    
    #prints reviews
    if len(bus_ids) < 1:
        print "This business is not found"
        
    elif len(review_list) < 1:
        print "No reviews for this business are found"
        
    else:
        i = 0
        while i < len(review_list):
            review_pars = review_list[i].split('\n')
            print 'Review %d:' %(i+1)
            for par in review_pars:
                paragraph = textwrap.wrap(par)
                if paragraph == []:
                    print
                for line in paragraph:
                    print '    %s' %line

            print
        
            i += 1