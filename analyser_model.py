# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:46:25 2019

@author: K P
"""

    
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import roc_auc_score

def senti_analyser():
    df = pd.read_csv("Amazon_Unlocked_mobile.csv")
#print(df.head())
#df.info()
#print(df['Rating'])

    df.dropna(inplace = True)
    df[df['Rating'] != 3]
    df['values'] = np.where(df['Rating']> 3,1,0)
#df.head(10)



    X_train, X_test, y_train, y_test = train_test_split(df['Reviews'], df['values'], random_state = 0)

#print('X_train first entry: \n\n', X_train[0])
#print('\n\nX_train shape: ', X_train.shape)



    vect = CountVectorizer().fit(X_train)
    X_train_vectorised = vect.transform(X_train)


    model = LogisticRegression(solver='saga')
    model.fit(X_train_vectorised, y_train)

#from sklearn.metrics import roc_auc_score

#predictions = model.predict(vect.transform(X_test))

#print('AUC: ', roc_auc_score(y_test, predictions))



    vect = TfidfVectorizer(min_df = 5, ngram_range = (1,2)).fit(X_train)
    len(vect.get_feature_names())

    X_train_vectorised = vect.transform(X_train)

    model = LogisticRegression(solver='saga')
    model.fit(X_train_vectorised, y_train)

    #predictions = model.predict(vect.transform(X_test))
    #print('AUC: ', roc_auc_score(y_test, predictions))
    return model,vect

#mo , ve = anamo.senti_analyser()
#print(mo.predict(ve.transform(['The candy is not good, I would never buy them again','The candy is not bad, I will buy them again'])))
