from .stockmgr import StockPriceManager

def main():
    stkmgr = StockPriceManager.from_csv('projects/stockpricemanager/sample_stock_prices.csv')
    print(stkmgr.search_by_symbol('AAPL'))
    print(stkmgr.range_search(120, 160))

if __name__ == '__main__':
    main()
