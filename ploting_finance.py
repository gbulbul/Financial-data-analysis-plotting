# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 16:48:37 2024

@author: gbulb
"""

import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
class Calculating_10_years_for_selected_stocks:
    
    def function_closing_volatilite(ticker_symbol):
        stock=yf.Ticker(ticker_symbol)
        ten_yrs_closing_price_history = stock.history(period='10y')['Close']
        Log_ret=ten_yrs_closing_price_history/ten_yrs_closing_price_history.shift(1)
        Volatility=Log_ret.rolling(252).std()*np.sqrt(252)
        print('The closing and volatilite values of' +' '+ticker_symbol.upper() + ' over 10 years')
        return 	ten_yrs_closing_price_history,Volatility
    
    def plotting(f,Y1,Y2,i):
        f.add_subplot(1,2,1)
        Y1.plot(style='k')
        plt.title("Closing")
            
        f.add_subplot(1, 2, 2)
        Y2.plot(style='b')
        plt.title("Volatilite")
        f.suptitle(str(i.upper()) + ' '+ 'Stock')
        plt.show()
if __name__=="__main__":
   list_tickers=['abbv','aapl','msft','jnj','voo']
   for idx,i in enumerate(list_tickers):
       print(Calculating_10_years_for_selected_stocks.function_closing_volatilite(i)[0])
       print(Calculating_10_years_for_selected_stocks.function_closing_volatilite(i)[1])
        
       fig_size = (12, 6)
       f = plt.figure(figsize=fig_size)
        
       Y1 = Calculating_10_years_for_selected_stocks.function_closing_volatilite(i)[0]
       Y2 = Calculating_10_years_for_selected_stocks.function_closing_volatilite(i)[1]
       Calculating_10_years_for_selected_stocks.plotting(f,Y1,Y2,i)
                     											