# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 23:56:57 2019

@Author: Zhi-Jiang Yang, Dong-Sheng Cao
@Institution: CBDD Group, Xiangya School of Pharmaceutical Science, CSU, China
@Homepage: http://www.scbdd.com
@Mail: yzjkid9@gmail.com; oriental-cds@163.com
@Blog: https://blog.moyule.me

♥I love Princess Zelda forever♥
"""

from CV import CV
from Sampling import Sampling
import pandas as pd

class Loop(object):
    """
    """
    def __init__(self,data,label_col,loop,n_splits,sample_mode,major_label,minor_label):
        self.loop = loop
        self.data = data
        self.data['ID'] = list(range(len(data)))#ID may be same
        self.label_col = label_col
        self.sample_mode = sample_mode
        self.major_label = major_label
        self.minor_label = minor_label
        self.n_splits = n_splits
        
    def getdata(self):       
        data = Sampling(self.data, self.label_col, self.major_label, self.minor_label)
        if self.sample_mode == 'Undersampling':
            return data.UnderSampling()
        elif self.sample_mode == 'Oversampling':
            return data.OverSample()
        else:
            return self.data
        
    def Loop(self):
        out = pd.DataFrame()
        for t in range(self.loop):
            data = self.getdata()
            cv = CV(data,self.label_col,self.n_splits)
            cv.nFold()
            out = pd.concat([out,cv.out],ignore_index=True)
            out = out.groupby('ID').apply(lambda x: x.mean())
        return out
            
            
# if '__main__'==__name__:
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
#     l = Loop(df,'Label',loop=5,sample_mode='Undersampling',
#              n_splits=5,
#              major_label=0,
#              minor_label=1)
#     out = l.Loop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    