# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:35:21 2019

@Author: Zhi-Jiang Yang, Dong-Sheng Cao
@Institution: CBDD Group, Xiangya School of Pharmaceutical Science, CSU, China
@Homepage: http://www.scbdd.com
@Mail: yzjkid9@gmail.com; oriental-cds@163.com
@Blog: https://blog.moyule.me

♥I love Princess Zelda forever♥
"""

__doc__ = """Now only support tree model"""


import shap
import pandas as pd


class Shap_Value(object):
    """
    """
    def __init__(self, model):
        """
        """
        self.model = model
        
    def Tree_explainer(self,data,feature_name):
        explainer = shap.TreeExplainer(self.model)
        shap_values = explainer.shap_values(data)
        y_base = explainer.expected_value       
        shap_values = pd.DataFrame(shap_values)
        shap_values.columns = feature_name
#        shap_values.insert(0,'ID',list(range(len(shap_values))))
        shap_values['Base'] = y_base
        self.shap_values = shap_values
    
    def KernelExplainer(self):
        pass
    
    def DeepExplainer(self):
        pass

    
    