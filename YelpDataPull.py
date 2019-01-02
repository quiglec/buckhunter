#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 12:25:22 2018

@author: Conor.Quigley@ibm.com
"""

import sample
MAX_BUSINESS_COUNT = 50
BUSINESS_PATH = '/v3/businesses/' 
API_HOST = 'https://api.yelp.com'
API_KEY = "GGJrd51N8aVpp1SAXl3Un80Za03pNIVdn9AmXALN86MEhQRfkNrUOD3qaQEoCcv0y9U7T8LqX6cBLrsFhN4UPcl4fkIllbVHNrLvi3JLDBPfg8ttzGduvIAmVQEhXHYx"

#Returns list of business dictionaries based on search term, loaction, and desired number of results
def get_businesses(term, location, result_count):
    return sample.query_api(term, location, result_count)

#Returns reviews list from Yelp API
def get_review(business, host, business_path, api_key):
    host_addendum = business_path + business['id'] + '/reviews'
    return sample.request(host, host_addendum, api_key)

#Add Reviews to list of business dictionaries
def append_reviews(businesses):
    for business in businesses:
        business['reviews'] = get_review(business, API_HOST, BUSINESS_PATH, API_KEY)
    return  businesses

def get_businesses_with_reviews(term, location, result_count):
    businesses = get_businesses(term, location, result_count)
    businesses = append_reviews(businesses)
    return businesses

#Input business list to return average business yelp rating
def get_average_rating(businesses):
    total = sum(restaurant['rating'] for restaurant in businesses)
    return float(total)/float(len(businesses))

def output_cuisines(businesses):
    cuisines = []
    for business in businesses:
        for cuisine in business['categories']:
            cuisines.append(cuisine['title'])
    cuisines = set(cuisines)
    cuisines = list(cuisines)
    return cuisines
    

"""
def main():
    entry = 
    sample.main()


if __name__ == '__main__':
    main()
"""


