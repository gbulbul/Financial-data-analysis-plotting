# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 19:47:07 2024

@author: gbulb
"""


import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
class Calculating_1_year_for_selected_stocks:
    
    def function_closing_volatilite(ticker_symbol):
        stock=yf.Ticker(ticker_symbol)
        ten_yrs_closing_price_history = stock.history(period='1y')['Close']
        Log_ret=ten_yrs_closing_price_history/ten_yrs_closing_price_history.shift(1)
        Volatility_5=Log_ret.rolling(5).std()*np.sqrt(5) 
        Volatility_20=Log_ret.rolling(20).std()*np.sqrt(20)
        Volatility_100=Log_ret.rolling(100).std()*np.sqrt(100) 
        print('The closing and volatilite values of' +' '+ticker_symbol.upper() + ' over 1 year')
        return 	ten_yrs_closing_price_history,Volatility_5,Volatility_20,Volatility_100
    
    def plotting(f,Y1,Y2,Y3,i):
        f.add_subplot(1,2,1)
        Y1.plot(style='g--')
        Y2.plot(style='b')
        Y3.plot(style='r--')
        f.suptitle(str(i.upper()) + ' '+ 'Stock')
        plt.legend(['Volatility_5', 'Volatility_20','Volatility_100'], loc='upper left')
        plt.show()
if __name__=="__main__":
   list_tickers=['abbv','aapl','msft','jnj','voo']
   for idx,i in enumerate(list_tickers):
       print(Calculating_1_year_for_selected_stocks.function_closing_volatilite(i)[1])
       print(Calculating_1_year_for_selected_stocks.function_closing_volatilite(i)[2])
       print(Calculating_1_year_for_selected_stocks.function_closing_volatilite(i)[3])
        
       fig_size = (12, 6)
       f= plt.figure(figsize=fig_size)
       Y1 = Calculating_1_year_for_selected_stocks.function_closing_volatilite(i)[1]
       Y2 = Calculating_1_year_for_selected_stocks.function_closing_volatilite(i)[2]
       Y3 = Calculating_1_year_for_selected_stocks.function_closing_volatilite(i)[3]
       Calculating_1_year_for_selected_stocks.plotting(f,Y1,Y2,Y3,i)
                     											