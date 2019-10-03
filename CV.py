# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:04:05 2019

@Author: Zhi-Jiang Yang, Dong-Sheng Cao
@Institution: CBDD Group, Xiangya School of Pharmaceutical Science, CSU, China
@Homepage: http://www.scbdd.com
@Mail: yzjkid9@gmail.com; oriental-cds@163.com
@Blog: https://blog.moyule.me

♥I love Princess Zelda forever♥
"""

from BuildModel import Model
from GetSHAP import Shap_Value
import pandas as pd
from sklearn.model_selection import train_test_split,KFold
#from load import load


class CV(object):
    """
    """
    def __init__(self, X, label_col, n_splits, model_type='XgbClf', explainer='Tree'):
        self.X = X
#        self.X['ID'] = list(range(len(X)))
        self.y = self.X.pop(label_col)
        self.n_splits = n_splits
        self.model_type = model_type
        self.explainer = explainer
        
    def nFold(self):
        self.out = pd.DataFrame()   
        kf = KFold(n_splits=self.n_splits, shuffle=True)
        for train_index, test_index in kf.split(self.X):
            X_train, X_test = self.X.iloc[train_index,:].copy(), self.X.iloc[test_index,:].copy()
            y_train = self.y[train_index].copy()
            name = X_test.pop('ID')
#            print(name)
            
            X_train.drop('ID',axis=1,inplace=True)
            m = Model(X_train,y_train)            
            
            exec('self.model = m.Build_{}(n_estimators=500,\
                                             learning_rate=0.02,\
                                             subsample=0.8,\
                                             max_depth=6)'.format(self.model_type))
            v = Shap_Value(self.model)
            exec('v.{}_explainer(X_test,X_test.columns)'.format(self.explainer))
            v.shap_values['ID'] = name.values
            self.out = pd.concat([self.out,v.shap_values],ignore_index=True)
        
        
 



# if '__main__'==__name__:
#     from Sampling import Sampling
    
#     df = pd.read_csv(r"01_ampc_final_moe_all.csv")
    
#     cols = ['Label', 'E_place', 'S', 'E_conf', 'E_score1',
#        'E_refine', 'S.1', 'E_conf.1', 'E_score1.1', 'E_refine.1', 'S.2',
#        'E_conf.2', 'E_score1.2', 'E_refine.2', 'S.3', 'E_conf.3', 'E_score1.3',
#        'E_refine.3', 'S.4', 'E_conf.4', 'E_score1.4', 'E_refine.4', 'r152_R',
#        'r289_A', 'r346_A', 'r120_A', 'rW1_O', 'r221_R', 'r349_A', 'r349_I',
#        'r64_A', 'r64_a', 'r152_A', 'r318_a', 'r319_R', 'r120_R', 'r289_R',
#        'r346_D', 'r67_I', 'r317_a', 'r346_R', 'r67_A', 'rW1_R', 'r64_D',
#        'r343_A', 'r343_R', 'r212_a', 'r319_a', 'r318_d', 'r120_D', 'r345_a',
#        'r346_a', 'r318_R', 'r320_a', 'r150_R', 'r152_D', 'r123_R', 'r150_A',
#        'r212_R', 'r289_D', 'r211_R']
    
#     df = df.loc[:,cols]
    
#     data = Sampling(df, label_col='Label', major_label=0, minor_label=1)
#     data = data.UnderSampling()
    
#     cv = CV(data,'Label')
#     cv.nFold()
























           