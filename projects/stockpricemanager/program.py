from .stockmgr import StockPriceManager

def main():
    stkmgr = StockPriceManager()
    stkmgr.stocks_from_csv('projects/stockpricemanager/synthetic_stock_data.csv')
    print(stkmgr.search_by_symbol('AAPL'))
    for stock in stkmgr.find_top_k(5):
        print(stock)
    print(stkmgr.range_search(72,73))

if __name__ == '__main__':
    main()
