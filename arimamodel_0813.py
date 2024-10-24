# -*- coding: utf-8 -*-
"""ArimaModel_0813.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bIqM9RVXVHUb4SJEAEzq2Cd6qpNS4p91

### ARMA Models
"""

# Import modules
import pandas as pd
import matplotlib.pyplot as plt

# Load in the time series
candy = pd.read_csv('candy_production.csv',
            index_col='date',
            parse_dates=True)

# Plot and show the time series on axis ax1
fig, ax1 = plt.subplots()
candy.plot(ax=ax1)
plt.show()

# Split the data into a train and test set
candy_train=candy.loc[:'2006']
candy_test=candy.loc['2007':]

# Create an axis
fig,ax = plt.subplots()

# Plot the train and test sets on the axis ax
candy_train.plot(ax=ax)
candy_test.plot(ax=ax)
plt.show()

# Import augmented dicky-fuller test function
from statsmodels.tsa.stattools import adfuller

# Run test
result = adfuller(earthquake['earthquakes_per_year'])

# Print test statistic
print(result[0])

# Print p-value
print(result[1])

# Print critical values
print(result[4])

# Run the ADF test on the time series
result = adfuller(city['city_population'])

# Plot the time series
fig, ax = plt.subplots()
city.plot(ax=ax)
plt.show()

# Print the test statistic and the p-value
print('ADF Statistic:', result[0])
print('p-value:', result[1])

# Calculate the first difference and drop the nans
amazon_diff = amazon.diff()
amazon_diff = amazon_diff.dropna()

# Run test and print
result_diff = adfuller(amazon_diff['close'])
print(result_diff)

# Calculate the first difference and drop the nans
amazon_diff = amazon.diff()
amazon_diff = amazon_diff.dropna()

# Run test and print
result_diff = adfuller(amazon_diff['close'])
print(result_diff)

# Calculate log-return and drop nans
amazon_log = np.log(amazon/amazon.shift(1))
amazon_log = amazon_log.dropna()

# Run test and print
result_log = adfuller(amazon_log['close'])
print(result_log)

# Import data generation function and set random seed
from statsmodels.tsa.arima_process import arma_generate_sample
np.random.seed(1)

# Set coefficients
ar_coefs = [1]
ma_coefs = [1, -0.7]

# Generate data
y = arma_generate_sample(ar_coefs, ma_coefs, nsample=100, scale=0.5)

plt.plot(y)
plt.ylabel(r'$y_t$')
plt.xlabel(r'$t$')
plt.show()

# Import the ARIMA model
from statsmodels.tsa.arima.model import ARIMA

# Instantiate the model
model = ARIMA(y, order=(1,0,1))

# Fit the model
results = model.fit()

"""### Fitting the Future"""

# Instantiate the model
model = ARIMA(sample["timeseries_1"], order=(2,0,0))

# Fit the model
results = model.fit()

# Print summary
print(results.summary())

# Instantiate the model
model = ARIMA(sample["timeseries_2"], order=(0,0,3))

# Fit the model
results = model.fit()

# Print summary
print(results.summary())

# Instantiate the model 2
model = ARIMA(earthquake, order = (3,0,1))

# Fit the model
results = model.fit()

# Print model fit summary
print(results.summary())

# Instantiate the model
model = ARIMA(hospital["wait_times_hrs"], order = (2,0,1), exog = hospital["nurse_count"])

# Fit the model
results = model.fit()

# Print model fit summary
print(results.summary())

results
# Generate predictions
one_step_forecast = results.get_prediction(start=-30)

# Extract prediction mean
mean_forecast = one_step_forecast.predicted_mean

# Get confidence intervals of  predictions
confidence_intervals = one_step_forecast.conf_int()

# Select lower and upper confidence limits
lower_limits = confidence_intervals.loc[:,'lower close']
upper_limits = confidence_intervals.loc[:,'upper close']

# Print best estimate  predictions
print(mean_forecast)


# plot the amazon data
plt.plot(amazon.index, amazon, label='observed')

# plot your mean predictions
plt.plot(mean_forecast.index, mean_forecast, color='r', label='forecast')

# shade the area between your confidence limits
plt.fill_between(lower_limits.index, lower_limits,
		 upper_limits, color='pink')

# set labels, legends and show plot
plt.xlabel('Date')
plt.ylabel('Amazon Stock Price - Close USD')
plt.legend()
plt.show()

# Generate predictions
dynamic_forecast = results.get_prediction(start=-30, dynamic=True)

# Extract prediction mean
mean_forecast = dynamic_forecast.predicted_mean

# Get confidence intervals of predictions
confidence_intervals = dynamic_forecast.conf_int()

# Select lower and upper confidence limits
lower_limits = confidence_intervals.loc[:,'lower close']
upper_limits = confidence_intervals.loc[:,'upper close']

# Print best estimate predictions
print(mean_forecast)

# plot the amazon data
plt.plot(amazon.index, amazon, label='observed')

# plot your mean forecast
plt.plot(mean_forecast.index, mean_forecast, color='r', label='forecast')

# shade the area between your confidence limits
plt.fill_between(lower_limits.index, lower_limits,
         upper_limits, color='pink')

# set labels, legends and show plot
plt.xlabel('Date')
plt.ylabel('Amazon Stock Price - Close USD')
plt.legend()
plt.show()

# Take the first difference of the data
amazon_diff = amazon.diff().dropna()

# Create ARMA(2,2) model
arma = ARIMA(amazon_diff, order = (2,0,2))

# Fit model
arma_results = arma.fit()

# Print fit summary
print(arma_results.summary())

# Make arma forecast of next 10 differences
arma_diff_forecast = arma_results.get_forecast(steps=10).predicted_mean

# Integrate the difference forecast
from numpy import cumsum
arma_int_forecast = cumsum(arma_diff_forecast)

# Make absolute value forecast
arma_value_forecast = arma_int_forecast + amazon.iloc[-1,0]

# Print forecast
print(arma_value_forecast)

# Create ARIMA(2,1,2) model
arima = ARIMA(amazon, order = (2,1,2))

# Fit ARIMA model
arima_results = arima.fit()

# Make ARIMA forecast of next 10 values
arima_value_forecast = arima_results.get_forecast(steps=10).predicted_mean

# Print forecast
print(arima_value_forecast)

"""### The Best of the Best Models"""

# Import
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Create figure
fig, (ax1, ax2) = plt.subplots(2,1, figsize=(12,8))

# Plot the ACF of df
plot_acf(df, lags=10, zero=False, ax=ax1)

# Plot the PACF of df
plot_pacf(df, lags=10, zero=False, ax=ax2)

plt.show()

# Create figure
fig, (ax1, ax2) = plt.subplots(2,1, figsize=(12,8))

# Plot ACF and PACF
plot_acf(earthquake, lags=15, zero=False, ax=ax1)
plot_pacf(earthquake, lags=15, zero=False, ax=ax2)

# Show plot
plt.show()

# Create figure
fig, (ax1, ax2) = plt.subplots(2,1, figsize=(12,8))

# Plot ACF and PACF
plot_acf(earthquake, lags=10, zero=False, ax=ax1)
plot_pacf(earthquake, lags=10, zero=False, ax=ax2)

# Show plot
plt.show()

# Instantiate model
model = ARIMA(earthquake, order =(1,0,0))

# Train model
results = model.fit()

# Create empty list to store search results
order_aic_bic=[]

# Loop over p values from 0-2
for p in range(3):
  # Loop over q values from 0-2
    for q in range(3):
      	# create and fit ARMA(p,q) model
        model = ARIMA(df, order=(p,0,q))
        results = model.fit()

        # Append order and results tuple
        order_aic_bic.append((p,q,results.aic, results.bic))

print(order_aic_bic)

# Construct DataFrame from order_aic_bic
order_df = pd.DataFrame(order_aic_bic,
                        columns=['p','q','AIC','BIC'])

# Print order_df in order of increasing AIC
print(order_df.sort_values('AIC'))

# Print order_df in order of increasing BIC
print(order_df.sort_values('BIC'))

# Loop over p values from 0-2
for p in range(3):
    # Loop over q values from 0-2
    for q in range(3):

        try:
            # create and fit ARMA(p,q) model
            model = ARIMA(earthquake, order=(p,0,q))
            results = model.fit()

            # Print order and results
            print(p, q, results.aic, results.bic)

        except:
            print(p, q, None, None)

# Fit model
model = ARIMA(earthquake, order=(1,0,1))
results = model.fit()

# Calculate the mean absolute error from residuals
mae = np.mean(np.abs(results.resid))

# Print mean absolute error
print(mae)

# Make plot of time series for comparison
earthquake.plot()
plt.show()

# Create and fit model
model1 = ARIMA(df, order=(3,0,1))
results1 = model1.fit()

# Print summary
print(results1.summary())

# Create and fit model
model2 = ARIMA(df, order=(2,0,0))
results2 = model2.fit()

# Print summary
print(results2.summary())

# Create and fit model
model = ARIMA(df, order=(1,1,1))
results=model.fit()

# Create the 4 diagostics plots
results.plot_diagnostics()
plt.show()

# Plot time series
savings.plot()
plt.show()

# Run Dicky-Fuller test
result = adfuller(savings['savings'])

# Print test statistic
print(result[0])

# Print p-value
print(result[1])

# Create figure
fig, (ax1, ax2) = plt.subplots(2,1, figsize=(12,8))

# Plot the ACF of savings on ax1
plot_acf(savings, lags=10, zero=False, ax=ax1)

# Plot the PACF of savings on ax2
plot_pacf(savings, lags=10, zero=False, ax=ax2)

plt.show()

# Loop over p values from 0-3
for p in range(4):

  # Loop over q values from 0-3
    for q in range(4):
      try:
        # Create and fit ARMA(p,q) model
        model = ARIMA(savings, order=(p,0,q))
        results = model.fit()

        # Print p, q, AIC, BIC
        print(p, q, results.aic, results.bic)

      except:
        print(p, q, None, None)

# Create and fit model
model = ARIMA(savings, order=(1,0,2))
results = model.fit()

# Create the 4 diagostics plots
results.plot_diagnostics()
plt.show()

# Print summary
print(results.summary())

"""### Seasonal ARIMA Models"""

# Import seasonal decompose
from statsmodels.tsa.seasonal import seasonal_decompose

# Perform additive decomposition
decomp = seasonal_decompose(milk_production['pounds_per_cow'], period=12)

# Plot decomposition
decomp.plot()
plt.show()

# Create figure and subplot
fig, ax1 = plt.subplots()

# Plot the ACF on ax1
plot_acf(water['water_consumers'], lags=25, zero=False,  ax=ax1)

# Show figure
plt.show()

# Import the SARIMAX class
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Import the SARIMAX class
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Create a SARIMAX model
model = SARIMAX(df1, order=(1,0,0), seasonal_order=(1,1,0,7))

# Fit the model
results = model.fit()

# Print the results summary
print(results.summary())

# Import the SARIMAX class
from statsmodels.tsa.statespace.sarimax import SARIMAX
# Create a SARIMAX model
model = SARIMAX(df2, order=(2,1,1), seasonal_order=(1,0,0,4))

# Fit the model
results = model.fit()

# Print the results summary
print(results.summary())

# Import the SARIMAX class
from statsmodels.tsa.statespace.sarimax import SARIMAX
# Create a SARIMAX model
model = SARIMAX(df3, order=(1,1,0), seasonal_order=(0,1,1,12))

# Fit the model
results = model.fit()

# Print the results summary
print(results.summary())

# Take the first and seasonal differences and drop NaNs
aus_employment_diff = aus_employment.diff().diff(12).dropna()

# Create the figure
fig, (ax1, ax2) = plt.subplots(2,1,figsize=(8,6))

# Plot the ACF on ax1
plot_acf(aus_employment_diff, lags=11, zero = False, ax=ax1)

# Plot the PACF on ax2
plot_pacf(aus_employment_diff, lags=11, zero = False, ax=ax2)

plt.show()

# Make list of lags
lags = [12, 24, 36, 48, 60]

# Create the figure
fig, (ax1, ax2) = plt.subplots(2,1,figsize=(8,6))

# Plot the ACF on ax1
plot_acf(aus_employment_diff, lags = lags, zero=False, ax=ax1)

# Plot the PACF on ax2
plot_pacf(aus_employment_diff, lags = lags, zero=False, ax=ax2)

plt.show()

# Create ARIMA mean forecast
arima_pred = arima_results.get_forecast(steps=25)
arima_mean = arima_pred.predicted_mean

# Create SARIMA mean forecast
sarima_pred = sarima_results.get_forecast(steps=25)
sarima_mean = sarima_pred.predicted_mean

# Plot mean ARIMA and SARIMA predictions and observed
plt.plot(dates, sarima_mean, label='SARIMA')
plt.plot(dates, arima_mean, label='ARIMA')
plt.plot(wisconsin_test, label='observed')
plt.legend()
plt.show()

import pmdarima as pm


# Create auto_arima model
model1 = pm.auto_arima(df1,
                      seasonal=True, m=7,
                      d=0, D=1,
                 	  max_p=2, max_q=2,
                      trace=True,
                      error_action='ignore',
                      suppress_warnings=True)

# Print model summary
print(model1.summary())

# Create model for SARIMAX(p,1,q)(P,1,Q)7
model3 = pm.auto_arima(df3,
                      seasonal=True, m=7,
                      d=1, D=1,
                      start_p=1, start_q=1,
                      max_p=1, max_q=1,
                      max_P=1, max_Q=1,
                      trace=True,
                      error_action='ignore',
                      suppress_warnings=True)

# Print model summary
print(model3.summary())

# Import joblib
import joblib

# Set model name
filename = 'candy_model.pkl'

# Pickle it
joblib.dump(model, filename)

# Import
import joblib

# Set model name
filename = "candy_model.pkl"

# Load the model back in
loaded_model = joblib.load(filename)

# Update the model
loaded_model.update(df_new)

print(df_new)

# Import model class
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Create model object
model = SARIMAX(co2,
                order=(1, 1, 1),
                seasonal_order=(0, 1, 1, 12),
)
# Fit model
results = model.fit()

# Plot common diagnostics
results.plot_diagnostics()
plt.show()

# Create forecast object
forecast_object = results.get_forecast(steps=136)

# Extract prediction mean
mean = forecast_object.predicted_mean

# Extract the confidence intervals
conf_int = forecast_object.conf_int()

# Extract the forecast dates
dates = mean.index

plt.figure()

# Plot past CO2 levels
plt.plot(co2.index, co2, label='past')

# Plot the prediction means as line
plt.plot(dates, mean, label='predicted')

# Shade between the confidence intervals
plt.fill_between(dates, conf_int.iloc[:,0], conf_int.iloc[:,1], alpha=0.2)

# Plot legend and show figure
plt.legend()
plt.show()

# Print last predicted mean
print(mean.iloc[-1])

# Print last confidence interval
print(conf_int.iloc[-1])

"""### 따릉이 데이터"""

import warnings

# 경고를 한 번만 표시
warnings.filterwarnings('ignore')

# Import modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_process import arma_generate_sample
from statsmodels.tsa.arima.model import ARIMA

# Font
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

import matplotlib.pyplot as plt
plt.rc('font', family='NanumGothicCoding')
plt.rcParams['axes.unicode_minus'] =False

# 런타임 재시작

# Load in the time series data
bike_train = pd.read_csv('bike_train.csv', index_col='대여일시', parse_dates=True, encoding='utf-8')
bike_test = pd.read_csv('bike_test.csv', index_col='대여일시', parse_dates=True, encoding='cp949')

bike_train = bike_train.dropna()

# '대여건수' 열의 공백이나 특수 문자를 제거 (필요 시)
bike_train['대여건수'] = bike_train['대여건수'].str.replace('[^\d.]', '', regex=True)

# '대여건수' 열을 수치형으로 변환
bike_train['대여건수'] = pd.to_numeric(bike_train['대여건수'], errors='coerce')

bike_train

# '대여건수' 열의 공백이나 특수 문자를 제거 (필요 시)
bike_test['대여건수'] = bike_test['대여건수'].str.replace('[^\d.]', '', regex=True)

bike_test['대여건수'] = pd.to_numeric(bike_test['대여건수'], errors='coerce')

bike_test

# Plot and show the train and test time series
fig, ax1 = plt.subplots()
bike_train.plot(ax=ax1, label='Train Set')
bike_test.plot(ax=ax1, label='Test Set')
plt.legend()
plt.show()

"""- ADF Statstic : 값이 충분히 작을수록 시계열 데이터가 정상성을 가지며, 단위근이 없다는 가설 지지"""

# Run the augmented Dickey-Fuller test on the train data
result_train = adfuller(bike_train['대여건수'])  # 'target_column_name'를 실제 열 이름으로 대체

# Print test statistic, p-value, and critical values
print('Train Set ADF Statistic:', result_train[0])
print('Train Set p-value:', result_train[1])
print('Critical Values:', result_train[4])

# Run the augmented Dickey-Fuller test on the test data
result_test = adfuller(bike_test['대여건수'])  # 'target_column_name'를 실제 열 이름으로 대체

# Print test statistic, p-value, and critical values
print('Test Set ADF Statistic:', result_test[0])
print('Test Set p-value:', result_test[1])
print('Critical Values:', result_test[4])

# Calculate the first difference and drop the NaNs for the train set
bike_train_diff = bike_train.diff().dropna()

# Run test and print for differenced train data
result_diff_train = adfuller(bike_train_diff['대여건수'])  # 'target_column_name'를 실제 열 이름으로 대체
print('Differenced Train Set ADF Statistic:', result_diff_train[0])
print('Differenced Train Set p-value:', result_diff_train[1])

# 차분을 했을 때, 드디어 정상성 가진다는 것 확인 가능

# Calculate the first difference and drop the NaNs for the test set
bike_test_diff = bike_test.diff().dropna()

# Run test and print for differenced test data
result_diff_test = adfuller(bike_test_diff['대여건수'])  # 'target_column_name'를 실제 열 이름으로 대체
print('Differenced Test Set ADF Statistic:', result_diff_test[0])
print('Differenced Test Set p-value:', result_diff_test[1])

# Calculate log-return and drop NaNs for the train set
bike_train_log = np.log(bike_train / bike_train.shift(1)).dropna()

# Run test and print for log-returned train data
result_log_train = adfuller(bike_train_log['대여건수'])  # 'target_column_name'를 실제 열 이름으로 대체
print('Log-Returned Train Set ADF Statistic:', result_log_train[0])
print('Log-Returned Train Set p-value:', result_log_train[1])

# 로그변환도 가능

"""######"""

# Instantiate the ARIMA model using '대여건수' as the target variable
# order = (p, d, q)
model = ARIMA(bike_train['대여건수'], order=(2,0,1))  # ARIMA 모델의 파라미터 (2,0,1)

# Fit the model
results = model.fit()

# Print model fit summary
print(results.summary())

# Generate predictions for the model
one_step_forecast = results.get_prediction(start=-30)

# Extract prediction mean
mean_forecast = one_step_forecast.predicted_mean

# Get confidence intervals of predictions
confidence_intervals = one_step_forecast.conf_int()

# Select lower and upper confidence limits
lower_limits = confidence_intervals.loc[:,'lower 대여건수']
upper_limits = confidence_intervals.loc[:,'upper 대여건수']

# Print best estimate predictions
print(mean_forecast)

# Plot the observed '대여건수' data and forecasts
plt.plot(bike_train.index, bike_train['대여건수'], label='Observed')

# Plot your mean predictions
plt.plot(mean_forecast.index, mean_forecast, color='r', label='Forecast')

# Shade the area between your confidence limits
plt.fill_between(lower_limits.index, lower_limits, upper_limits, color='pink')

# Set labels, legends, and show plot
plt.xlabel('Date')
plt.ylabel('대여건수')
plt.legend()
plt.show()

# 예측 부분 데이터만 선택
bike_train_end = bike_train.iloc[-30:]
mean_forecast_end = mean_forecast.iloc[-30:]
lower_limits_end = lower_limits.iloc[-30:]
upper_limits_end = upper_limits.iloc[-30:]

# Plot the observed '대여건수' data and forecasts for 2023 and later
plt.plot(bike_train_end.index, bike_train_end['대여건수'], label='Observed')

# Plot your mean predictions
plt.plot(mean_forecast_end.index, mean_forecast_end, color='r', label='Forecast')

# Shade the area between your confidence limits
plt.fill_between(lower_limits_end.index, lower_limits_end, upper_limits_end, color='pink')

# Set labels, legends, and show plot
plt.xlabel('Date')
plt.ylabel('대여건수')
plt.legend()
plt.show()

"""- One-step-ahead Predictions
  - 실제 관측된 데이터를 사용하여 다음 시점의 값 예측
  - 단기 예측에 사용
  - 매 시점에서 모델이 매번 새롭게 관측된 데이터를 이용해 예측을 갱신하기 때문에 오류가 누적되지 않음
"""

# Generate dynamic predictions
dynamic_forecast = results.get_prediction(start=-30, dynamic=True)

# Extract prediction mean
mean_forecast = dynamic_forecast.predicted_mean

# Get confidence intervals of predictions
confidence_intervals = dynamic_forecast.conf_int()

# Select lower and upper confidence limits
lower_limits = confidence_intervals.loc[:,'lower 대여건수']
upper_limits = confidence_intervals.loc[:,'upper 대여건수']

# Print best estimate predictions
print(mean_forecast)

# Plot the observed '대여건수' data and dynamic forecasts
plt.plot(bike_train.index, bike_train['대여건수'], label='Observed')

# Plot your mean forecast
plt.plot(mean_forecast.index, mean_forecast, color='r', label='Dynamic Forecast')

# Shade the area between your confidence limits
plt.fill_between(lower_limits.index, lower_limits, upper_limits, color='pink')

# Set labels, legends, and show plot
plt.xlabel('Date')
plt.ylabel('대여건수')
plt.legend()
plt.show()

# 예측 부분 데이터만 선택
bike_train_end = bike_train.iloc[-30:]
mean_forecast_end = mean_forecast.iloc[-30:]
lower_limits_end = lower_limits.iloc[-30:]
upper_limits_end = upper_limits.iloc[-30:]

# Plot the observed '대여건수' data and forecasts
plt.plot(bike_train_end.index, bike_train_end['대여건수'], label='Observed')

# Plot your mean predictions
plt.plot(mean_forecast_end.index, mean_forecast_end, color='r', label='Forecast')

# Shade the area between your confidence limits
plt.fill_between(lower_limits_end.index, lower_limits_end, upper_limits_end, color='pink')

# Set labels, legends, and show plot
plt.xlabel('Date')
plt.ylabel('대여건수')
plt.legend()
plt.show()

"""- Dynamic Predictions
  - 초기 몇 시점에서만 실제 데이터를 사용하고, 그 후에는 이전 시점의 예측 값들을 사용하여 다음 시점의 값 예측
  - 장기 예측
  - 오류가 누적될 가능성, 점차 확대될 수..ㅋㅋㅋ
"""

# 차분으로 Fit
# Take the first difference of the data
bike_train_diff = bike_train['대여건수'].diff().dropna()

# Create ARMA(2,2) model with the differenced data
arma_model = ARIMA(bike_train_diff, order=(2,0,2))

# Fit model
arma_results = arma_model.fit()

# Print fit summary
print(arma_results.summary())

# Make ARMA forecast of next 10 differences
arma_diff_forecast = arma_results.get_forecast(steps=10).predicted_mean

# Integrate the difference forecast
arma_int_forecast = arma_diff_forecast.cumsum()

# Make absolute value forecast
arma_value_forecast = arma_int_forecast + bike_train['대여건수'].iloc[-1]

# Print forecast
print(arma_value_forecast)

# Create ARIMA(2,1,2) model using original '대여건수' data
arima_model = ARIMA(bike_train['대여건수'], order=(2,1,2))

# Fit ARIMA model
arima_results = arima_model.fit()

# Make ARIMA forecast of next 10 values
arima_value_forecast = arima_results.get_forecast(steps=10).predicted_mean

# Print forecast
print(arima_value_forecast)

"""######"""

# Import necessary functions for ACF and PACF plots
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Create figure for ACF and PACF of '대여건수'
fig, (ax1, ax2) = plt.subplots(2,1, figsize=(12,8))

# Plot the ACF of '대여건수'
plot_acf(bike_train['대여건수'], lags=10, zero=False, ax=ax1)

# Plot the PACF of '대여건수'
plot_pacf(bike_train['대여건수'], lags=10, zero=False, ax=ax2)

plt.show()

# AR(1) 모델로 보임

"""- AIC(Akaike Information Criterion)
- BIC(Bayesian Information Crieterion)
"""

# Loop over p and q values to find the best ARIMA model based on AIC and BIC
order_aic_bic = []

for p in range(3):
    for q in range(3):
        try:
            # Create and fit ARIMA model
            model = ARIMA(bike_train['대여건수'], order=(p,0,q))
            results = model.fit()

            # Append order and results to the list
            order_aic_bic.append((p, q, results.aic, results.bic))
        except:
            order_aic_bic.append((p, q, None, None))

# Construct DataFrame from order_aic_bic
order_df = pd.DataFrame(order_aic_bic, columns=['p', 'q', 'AIC', 'BIC'])

# Print order_df sorted by AIC
print(order_df.sort_values('AIC'))

# Print order_df sorted by BIC
print(order_df.sort_values('BIC'))

# Fit the best model found (e.g., ARIMA(1,0,2))
model = ARIMA(bike_train['대여건수'], order=(1,0,2))
results = model.fit()

# Calculate and print the mean absolute error from residuals
mae = np.mean(np.abs(results.resid))
print("Mean Absolute Error:", mae)

# Plot the observed '대여건수' data
bike_train['대여건수'].plot()
plt.show()

# MAE 매우 이상..

# Create and fit another ARIMA model 두번째로 좋은
model1 = ARIMA(bike_train['대여건수'], order=(2,0,2))
results1 = model1.fit()
print(results1.summary())

# Create and fit another ARIMA model 세번째로 좋은
model2 = ARIMA(bike_train['대여건수'], order=(2,0,0))
results2 = model2.fit()
print(results2.summary())

# Create and fit ARIMA model with differencing (order=(1,0,2))
model = ARIMA(bike_train['대여건수'], order=(1,0,2))
results = model.fit()

# Create the diagnostics plots
results.plot_diagnostics()
plt.show()

"""######"""

!pip install pmdarima

from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.statespace.sarimax import SARIMAX
import pmdarima as pm

# 1. Perform seasonal decomposition
decomp = seasonal_decompose(bike_train['대여건수'], period=12)
decomp.plot()
plt.show()

# 2. Plot the ACF of '대여건수'
fig, ax1 = plt.subplots()
plot_acf(bike_train['대여건수'], lags=25, zero=False, ax=ax1)
plt.show()

# Create a SARIMAX model

# order(p, d, q)
# seasonal_order(P, D, Q, s)
model = SARIMAX(bike_train['대여건수'], order=(1,0,0), seasonal_order=(1,1,0,7))
results = model.fit()
print(results.summary())

# Create another SARIMAX model with different parameters
model2 = SARIMAX(bike_train['대여건수'], order=(2,1,1), seasonal_order=(1,0,0,4))
results2 = model2.fit()
print(results2.summary())

## 이게 AIC, BIC 가장 낮아서 성능 좋음

# Create another SARIMAX model with different parameters
model3 = SARIMAX(bike_train['대여건수'], order=(1,1,0), seasonal_order=(0,1,1,12))
results3 = model3.fit()
print(results3.summary())

# Take first and seasonal differences
# 1차 차분 -> 계절 차분 진행 (지난 번 준희꺼 참고, 연도별 루프)
bike_diff = bike_train['대여건수'].diff().diff(12).dropna()

# Plot ACF and PACF of differenced data
fig, (ax1, ax2) = plt.subplots(2,1,figsize=(8,6))
plot_acf(bike_diff, lags=11, zero=False, ax=ax1)
plot_pacf(bike_diff, lags=11, zero=False, ax=ax2)
plt.show()

# Compare ARIMA and SARIMA forecasts (assuming arima_results and sarima_results are from previous models)
# Generate forecasts
arima_pred = results.get_forecast(steps=25)
arima_mean = arima_pred.predicted_mean
sarima_pred = results3.get_forecast(steps=25)
sarima_mean = sarima_pred.predicted_mean

# Plot forecasts
plt.plot(bike_train.index[-25:], sarima_mean, label='SARIMA')
plt.plot(bike_train.index[-25:], arima_mean, label='ARIMA')
plt.plot(bike_train['대여건수'].iloc[-25:], label='Observed')
plt.legend()
plt.show()

# 1년을 비교하는 건데, 계절성을 제거해버리니 당연히 밋밋

# Create an auto_arima model
auto_model = pm.auto_arima(bike_train['대여건수'], seasonal=True, m=7, d=0, D=1, max_p=2, max_q=2, trace=True, error_action='ignore', suppress_warnings=True)
print(auto_model.summary())

# (1,1,1) 최적

model = SARIMAX(bike_train['대여건수'], order=(1, 1, 1), seasonal_order=(0, 1, 1, 12))
results = model.fit()
results.plot_diagnostics()
plt.show()

# Create forecast
forecast_object = results.get_forecast(steps=180)

mean = forecast_object.predicted_mean
conf_int = forecast_object.conf_int()

# Plot forecast
plt.figure()
plt.plot(bike_train.index, bike_train['대여건수'], label='Past')
plt.plot(mean.index, mean, label='Forecast')
plt.fill_between(mean.index, conf_int.iloc[:,0], conf_int.iloc[:,1], alpha=0.2)
plt.legend()
plt.show()

## 뭐임.?

# Print last predicted mean and confidence interval
print(mean.iloc[-1])
print(conf_int.iloc[-1])

