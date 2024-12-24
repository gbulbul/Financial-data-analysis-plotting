
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 17:02:33 2024

@author: gbulb
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")
class Predicting_closing_price_with_LSTM_model:
    def split_into_train(train_data):
        x_train,y_train = [],[]
        for i in range(60, len(train_data)):
            x_train.append(train_data[i-60:i, 0])
            y_train.append(train_data[i, 0])
            if i<= 61:
                print(x_train)
                print(y_train)
                
        # Convert the x_train and y_train to numpy arrays 
        x_train, y_train = np.array(x_train), np.array(y_train)
        # Reshape the data
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
        return x_train,y_train


    def modeling(model,x_train,y_train):
        
        model.add(LSTM(128, return_sequences=True, input_shape= (x_train.shape[1], 1)))
        model.add(LSTM(64, return_sequences=False))
        model.add(Dense(25))
        model.add(Dense(1))
    
        # Compile the model
        model.compile(optimizer='adam', loss='mean_squared_error')
    
        # Train the model
        model.fit(x_train, y_train, batch_size=1, epochs=1)
        return model

    def testing(training_data_len,scaled_data,dataset):
        test_data = scaled_data[training_data_len - 60: , :]
        # Create the data sets x_test and y_test
        x_test = []
        y_test = dataset[training_data_len:, :]
        for i in range(60, len(test_data)):
            x_test.append(test_data[i-60:i, 0])
            
        # Convert the data to a numpy array
        x_test = np.array(x_test)
        
        # Reshape the data
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1 ))
        return y_test,x_test

    def predicting(x_test):
        predictions1 = model.predict(x_test)
        predictions = scaler.inverse_transform(predictions1)
        return predictions
    def plotting(f,train,valid,title,len_of_data):
        plt.title('Model for' +1*" "+ title)
        plt.xlabel('Date', fontsize=18)
        customized_xticks=[number for number in range(100, len_of_data, 500)]
        plt.xticks(customized_xticks,rotation=45)
        plt.ylabel('Close Price USD ($)', fontsize=18)
        plt.plot(train['Close'])
        plt.plot(valid[['Close', 'Predictions']])
        plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
        plt.show()

# Visualize the data
if __name__=="__main__":
    RMSE=[]
    stocks=['AAPL','MSFT','AMZN','NVDA']
    for idx,i in enumerate(stocks):
        direc='C:/Users/gbulb/Downloads/stock_market_data/nasdaq/csv/' + str(i) +'.csv'
        df = pd.read_csv(direc, index_col=0)
        len_of_data=len(df)
        title=i
        plt.title('Close Price History')
        plt.plot(df['Close'])
        plt.xlabel('Date', fontsize=18)
        customized_xticks= [number for number in range(100, len_of_data, 500)]
        plt.xticks(customized_xticks,rotation=45)
        plt.ylabel('Close Price USD ($)', fontsize=18)
        plt.show()
        #Focusing on sole 'Close' variable
        data = df.filter(['Close'])
        dataset = data.values
        training_data_len = int(np.ceil( len(dataset) * .95 ))
        # Scale the data
    
        scaler = MinMaxScaler(feature_range=(0,1))
        scaled_data = scaler.fit_transform(dataset)
    
        train_data = scaled_data[0:int(training_data_len), :]
        # Split the data into x_train and y_train data sets
        x_train,y_train=Predicting_closing_price_with_LSTM_model.split_into_train(train_data)
        
        # Build the LSTM model
        model = Sequential()
        Predicting_closing_price_with_LSTM_model.modeling(model,x_train,y_train)
        y_test,x_test=Predicting_closing_price_with_LSTM_model.testing(training_data_len,scaled_data,dataset)
        # Get the models predicted price values 
        predictions=Predicting_closing_price_with_LSTM_model.predicting(x_test)
        # Get the root mean squared error (RMSE)
        rmse = np.sqrt(np.mean(((predictions - y_test) ** 2)))
        RMSE.append(rmse)
        print(RMSE)
        # Plot the data
        train = data[:training_data_len]
        valid = data[training_data_len:]
        valid['Predictions'] = predictions
        f=plt.figure(figsize=(26,16))
    
        Predicting_closing_price_with_LSTM_model.plotting(f,train,valid,title,len_of_data)
