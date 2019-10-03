# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:10:22 2019

@Author: Zhi-Jiang Yang, Dong-Sheng Cao
@Institution: CBDD Group, Xiangya School of Pharmaceutical Science, CSU, China
@Homepage: http://www.scbdd.com
@Mail: yzjkid9@gmail.com; oriental-cds@163.com
@Blog: https://blog.moyule.me

♥I love Princess Zelda forever♥
"""

import pandas as pd


class Sampling(object):
    """
    """
    def __init__(self,data,label_col,major_label,minor_label):
        self.major_data = data[data[label_col]==major_label]
        self.minor_data = data[data[label_col]==minor_label]
                   
    def OverSample(self):
        data = self.minor_data.sample(n=len(self.major_data), replace=True)
        data = pd.concat([data,self.major_data],ignore_index=True)
        return data
        
    def UnderSampling(self):
        data = self.major_data.sample(n=len(self.minor_data), replace=False)
        data = pd.concat([data,self.minor_data],ignore_index=True)
        return data
    