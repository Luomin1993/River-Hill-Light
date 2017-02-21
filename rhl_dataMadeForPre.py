import numpy as np
from rhl_keyIndexData import *

STOCK = ['600219','000002','000623','000725','600036','601166','600298', '600881', '002582','600750', '601088', '000338', '000895', '000792']
#DATE = [['2015-01-04','2015-01-05','2015-01-06'],['2016-12-29','2016-12-30','2016-12-31'],['2017-01-04','2017-01-05','2017-01-06'],['2017-01-05','2017-01-06','2017-01-07']]
DATE = [['2015-01-05','2015-01-06'],['2016-12-29','2016-12-30'],['2017-01-05','2017-01-06'],['2017-01-09','2017-01-10']]

knownData = []
preData = []

for stockID in STOCK:
	keyindexdata = KeyIndexData(stockID)
	for date in DATE: 
	    knownData.append(keyindexdata.knownData(date[0]))
	    preData.append(keyindexdata.predictData(date[1]))

np.save('Data/Kno1517',np.array(knownData))
np.save('Data/Pre1517',np.array(preData))	    