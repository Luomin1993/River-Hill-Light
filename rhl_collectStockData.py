import tushare as ts

Year = 2016
Season = 4
Date = '2016-12-31'

STOCK = ['600219',        
         '000002',         
         '000623',        
         '000725',        
         '600036',        
         '601166',        
         '600298',        
         '600881',        
         '002582',       
         '600750',        
         '601088',        
         '000338',        
         '000895',        
         '000792']       

class StockData(object):
    """docstring for StockData"""
    histData = 0
    basicData = 0
    def __init__(self, stockID, Year, Season):
        super(StockData, self).__init__()
        self.stockID = stockID
        self.Year = Year
        self.Season = Season

    def collectData(self):
        stockID = self.stockID
        Year = self.Year
        Season = self.Season
        reportData = self.reportData(stockID,Year,Season)
        histData = self.histData(stockID)
        basicData = self.basicData(stockID)
        profitData = self.profitData(stockID,Year,Season)
        operationData = self.operationData(stockID,Year,Season)
        growthData = self.growthData(stockID,Year,Season)
        debtpayingData = self.debtpayingData(stockID,Year,Season)
        cashflowData = self.cashflowData(stockID,Year,Season)
        fundHoldingsData = self.fundHoldingsData(stockID,Year,Season)
        return (reportData,histData,basicData,profitData,operationData,growthData,debtpayingData,cashflowData,fundHoldingsData)

    def reportData(self,stockID,Year,Season):
        df = ts.get_report_data(Year,Season)
        reportData = df[df.code == stockID]
        return reportData    

    def histData(self,stockID):
        df = ts.get_hist_data(stockID)
        return df    

    def basicData(self,stockID):
        df = ts.get_stock_basics()
        basicData = df[df.index == stockID]
        return basicData    

    def profitData(self,stockID,Year,Season):
        df = ts.get_profit_data(Year,Season)
        profitData = df[df.code == stockID]
        return profitData                         

    def operationData(self,stockID,Year,Season):
        df = ts.get_operation_data(Year,Season)
        operationData = df[df.code == stockID]
        return operationData    

    def growthData(self,stockID,Year,Season):
        df = ts.get_growth_data(Year,Season)
        growthData = df[df.code == stockID]
        return growthData    

    def debtpayingData(self,stockID,Year,Season):
        df = ts.get_debtpaying_data(Year,Season)
        debtpayingData = df[df.code == stockID]
        return debtpayingData    

    def cashflowData(self,stockID,Year,Season):
        df = ts.get_cashflow_data(Year,Season)
        cashflowData = df[df.code == stockID]
        return cashflowData     

    def fundHoldingsData(self,stockID,Year,Season):
        df = ts.fund_holdings(Year,Season)
        fundHoldingsData = df[df.code == stockID]
        return fundHoldingsData 

# def exe Data(stockID,Year,Season):
#     df = ts.get_exe_data(Year,Season)
#     exe Data = df[df.code == stockID]
#     return exe Data                    

#################  test   ##########
if __name__ == '__main__':
    stockData = StockData('600606',Year,Season)
    data = stockData.collectData()
    print data

    