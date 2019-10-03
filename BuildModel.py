# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:08:56 2019

@Author: Zhi-Jiang Yang, Dong-Sheng Cao
@Institution: CBDD Group, Xiangya School of Pharmaceutical Science, CSU, China
@Homepage: http://www.scbdd.com
@Mail: yzjkid9@gmail.com; oriental-cds@163.com
@Blog: https://blog.moyule.me

♥I love Princess Zelda forever♥
"""


class Model(object):
    """
    """
    def __init__(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
        
    def Build_RfClf(self,n_estimators=500,n_jobs=-1):
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier(n_estimators=n_estimators,
                                       n_jobs=n_jobs)
        
        model.fit(self.X_train, self._train)
        return model
    
    def Build_RfReg(self,n_estimators=500,n_jos=-1):
        from sklearn.ensemble import RandomForestRegressor
        model = RandomForestRegressor(n_estimators=n_estimators,
                                      n_jobs=n_jos)
        
        model.fit(self.X_train, self.y_train)
        return model
    
    def Build_XgbClf(self, n_estimators=500, learning_rate=0.02, subsample=0.8, max_depth=6):
        from xgboost import XGBClassifier
        model = XGBClassifier(n_estimators=n_estimators,
                              learning_rate=learning_rate,
                              subsample=subsample,
                              max_depth=max_depth)
        model.fit(self.X_train, self.y_train)
        return model
    
    
#if '__main__'==__name__:
#    import pandas as pd
#    import numpy as np
#    
#    data = pd.read_csv(r"01_ampc_final_moe_all.csv")
#    pos_data = data[data.Label==1]
#    neg_data = data[data.Label==0]
#    n_pos = len(pos_data)
#    X = neg_data.sample(n=n_pos).copy()
#    X = pd.concat([pos_data,X],ignore_index=True)
#    y = X.pop('Label')
#    X = X.loc[:,'E_place':]
#    model = Model(X,y)
#    model = model.Build_XgbClf()
#    
#    
#    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    