import pandas as pd
from numpy import *
import numpy as np
from sklearn import preprocessing
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import metrics

from sklearn.model_selection import train_test_split
from sklearn import neighbors

#read the trainig data 
data =pd.read_csv('train_dataset.csv')
array = data.values

#change the string(male, female) values to numerical values(1,0) 
for i in range(len(array)):
	if array[i][0]=="Male":
		array[i][0]=1
	else:
		array[i][0]=0


df=pd.DataFrame(array)

maindf =df[[0,1,2,3,4,5,6]]
mainarray=maindf.values
print (mainarray)


temp=df[7]
train_y =temp.values
# print(train_y)
# print(mainarray)
train_y=temp.values

for i in range(len(train_y)):
	train_y[i] =str(train_y[i])


#load the multinomial Logistic Regression model from sklearn
mul_lr = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg',max_iter =1000)
mul_lr.fit(mainarray, train_y)

#get the test data
testdata =pd.read_csv('test_dataset.csv')
test = testdata.values

#change the string(male, female) values to numerical values(1,0) 

for i in range(len(test)):
	if test[i][0]=="Male":
		test[i][0]=1
	else:
		test[i][0]=0


df1=pd.DataFrame(test)

testdf =df1[[0,1,2,3,4,5,6]]
maintestarray=testdf.values
print(maintestarray)

#predict using test data
y_pred = mul_lr.predict(maintestarray)
for i in range(len(y_pred)) :
	y_pred[i]=str((y_pred[i]))


#function for calling from app.py, takes user input and predicts the personality
def run_personality_prediction(gender, age, openness, neuroticism, conscientiousness, agreeableness, extraversion):
    
	
	if gender=="Male":
			gender=1
	else:
			gender=0

	tdf = []
	tdf.append(list((gender,age,openness,neuroticism,conscientiousness,agreeableness,extraversion)))
	# print(tdf)

	y_pred = mul_lr.predict(tdf)
	for i in range(len(y_pred)) :
		y_pred[i]=str((y_pred[i]))

#return the prediction to app.js 
	return y_pred

