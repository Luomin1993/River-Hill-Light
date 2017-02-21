import pandas as pd
import urllib2 
import requests

def getPreData():
    print "downloading with urllib" 
    E0url = 'http://football-data.co.uk/mmz4281/1617/E0.csv'  
    print "downloading"
    file = urllib2.urlopen(E0url,timeout=3)
    data = file.read()
    df = pd.read_csv(data)
    return df