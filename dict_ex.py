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
        print(d)

dict()
        
    