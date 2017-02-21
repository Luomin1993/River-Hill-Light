
import tushare as ts

class KeyIndexData(object):
	"""docstring for KeyIndexData"""
	def __init__(self, stockID):
		super(KeyIndexData, self).__init__()
		self.stockID = stockID

	def knownData(self,knownDate):
		
		cybIN = float(ts.get_hist_data('cyb',start=knownDate,end=knownDate).high)
		df = ts.get_hist_data(self.stockID,start=knownDate,end=knownDate)
		highPrice = float(df.high)
		priceChange = float(df.p_change)
		ma5Price = float(df.ma5)
		ma10Price = float(df.ma10)
		ma20Price = float(df.ma20)
		return [shIN,szIN,hs300IN,sz50IN,zxbIN,cybIN,highPrice,priceChange,ma5Price,ma10Price,ma20Price]

	def predictData(self,predictDate):
	    df = ts.get_hist_data(self.stockID,start=predictDate,end=predictDate)
	    highPrice = float(df.high)
	    return highPrice
