import os               
import csv             
import json
import requests  
import numpy as np         
import pandas  as pd 


def dict():
    d = {}
    with open('states.json','r') as us_states:
        d = json.load(us_states)
    #print(d['states'])
    with open('states_tx.json', 'w') as out_states:
        #print(d.get('states'))
        json.dump(d,out_states, indent=4)
    state_abbr = {}
    for i in d['states']:
        #print(f"State: {i['abbreviation']} {i['area_codes']}")
        state_area = i['name'].join(i['area_codes'])
    
    with open('area_st.json' , 'w') as st_cd:
        for i in d['states']:
            print(i['name'] + str(i['area_codes']))
            #son.dump(i['name'].join(['area_codes']), st_cd, indent=4)
            print('\n')
            
        
        
            

dict()
        
    