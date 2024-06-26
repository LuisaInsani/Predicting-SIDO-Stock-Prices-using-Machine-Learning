# -*- coding: utf-8 -*-
"""RBL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s4ahBIlEwGoksI4qiypbjIR6UXFDe6LH
"""

# dataset @ https://finance.yahoo.com/quote/SIDO/history/

import pandas as pd
df = pd.read_csv('SIDO.csv')
df = df.set_index('Date')
df

df.describe()

df.info()

# Get the number of rows and columns in the data set
df.shape

import math
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Visualize the closing price history
plt.figure(figsize=(16,8))
plt.title('Close Price History')
plt.plot(df['Close'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price IDR', fontsize=18)
plt.show()

#Visualize the volume of stock being traded history
plt.figure(figsize=(16,8))
plt.title('Sales Volume')
plt.plot(df['Volume'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Sales Volume', fontsize=18)
plt.show()

# Create a new dataframe with only the close columns
data = df.filter(['Close'])
dataset = data.values
training_data_len = math.ceil(len(dataset)*0.8)
training_data_len

#Scale the data
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(dataset)
scaled_data

#Create the training dataset
#Create the scaled training dataset
train_data = scaled_data[0:training_data_len, :]
#Split the data into x-train and y_train dataset
x_train = []
y_train = []

for i in range(10, len(train_data)):
  x_train.append(train_data[i-10:i, 0])
  y_train.append(train_data[i, 0])
  if i<=11:
    print(x_train)
    print(y_train)
    print()

#Convert the x_train and y_train to numpy arrays
x_train, y_train = np.array(x_train), np.array(y_train)

#Reshape the data
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_train.shape

#Build the LSTM Model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape= (x_train.shape[1],1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

#Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

#Train the model
model.fit(x_train, y_train, batch_size=1, epochs=1)

#Create the testing dataset
#Create a new array containing scaled value from index 914 to 1217
test_data = scaled_data[training_data_len - 10: , :]
#Create the data sets x_test and y_test
x_test = []
y_test = dataset[training_data_len:, :]
for i in range(10, len(test_data)):
  x_test.append(test_data[i-10:i, 0])

#Convert the data to numpy array
x_test = np.array(x_test)

#Reshape the data
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

#Get the models predicted price values
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

#Get the Root Mean Squared Error (RMSE)
rmse = np.sqrt(np.mean(predictions - y_test)**2)
rmse

#Plot the data
train = data[:training_data_len]
valid = data[training_data_len:]
valid['Predictions'] = predictions

#Visualize the data
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price IDR', fontsize=18)
plt.plot(train['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
plt.show()

#Show the valid and predicted prices
valid

#Get the quote
SIDO_quote = pd.read_csv('SIDO.csv')

#Create a new dataframe
new_df = SIDO_quote.filter(['Close'])

#Get the last 10 days closing price values and convert the dataframe to an array
last_10_days = new_df[-10:].values

#Scale the data to be values between 0 and 1
last_10_days_scaled = scaler.transform(last_10_days)

#Create an empty list
X_test = []

#append the past 10 days
X_test.append(last_10_days_scaled)

#Convert the x_test dataset to a numpy array
X_test = np.array(X_test)

#Reshape the data
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

#Get the predicted scaled price
pred_price = model.predict(X_test)

#Undo the scaling
pred_price = scaler.inverse_transform(pred_price)
print(pred_price)
