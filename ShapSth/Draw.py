# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:37:08 2019

@Author: Zhi-Jiang Yang, Dong-Sheng Cao
@Institution: CBDD Group, Xiangya School of Pharmaceutical Science, CSU, China
@Homepage: http://www.scbdd.com
@Mail: yzjkid9@gmail.com; oriental-cds@163.com
@Blog: https://blog.moyule.me

♥I love Princess Zelda forever♥
"""

import matplotlib.pyplot as plt
import pandas as pd
from load import load
from itertools import cycle

class Draw(object):
    """
    """
    def __init__(self,data,read_file,mode):
        if mode == 'Compute':
            self.data = pd.DataFrame(data)
        else:
            self.data = load(data)
        data = self.data.iloc[:,:-2]
        data = data.applymap(lambda x: abs(x))
        shap_mean = data.apply(lambda x: x.mean())
        self.shap_mean = shap_mean.sort_values(ascending=True)
        ori = load(read_file)
        self.ori = ori.reindex(self.data.ID.values)
        
    def hist(self,savedir):
        f,ax = plt.subplots(figsize=(5*0.618,5)) 
        for x,shap in zip(range(len(self.shap_mean)), self.shap_mean.values):
            ax.barh(x,shap,color='#1E88E5') 
            ax.tick_params(direction='in', which='both', labelsize=5, length=2)
            ax.set_yticks(range(len(self.shap_mean)))
            ax.set_yticklabels(self.shap_mean.keys(),fontdict={'size':3})
            ax.set_ylim([-0.5,len(self.shap_mean)-0.5])
            ax.spines['bottom'].set_linewidth(0.5)
            ax.spines['left'].set_linewidth(0.5)
            ax.spines['right'].set_linewidth(0.5)
            ax.spines['top'].set_linewidth(0.5)
            ax.set_xlabel('mean(|SHAP value|)\n(average impact on model output magnitude)',fontdict={'size':7})
        
        if savedir:
            plt.savefig(savedir,bbox_inches = 'tight')
        else:
            pass
        plt.show()
        
    def violin(self,top,savedir):
        shap_mean = self.shap_mean.sort_values(ascending=False)
        shap_mean = shap_mean.iloc[:top]
        data = self.data.T.reindex(shap_mean.keys()).T
    
        f,ax = plt.subplots()
        colors = cycle(['#3be0d9','#3dbb2f','#2b49ac','#2dc481','#6283f1','#898846','#da7985','#c61920','#f2c44a','#1d2ea8',
        '#aa1948','#00afd8','#f58233','#7ab800','#eeaf00','#f7347a','#ffd8ef','#a97afb','#32f3c9','#db0545'])
        violin_parts = ax.violinplot([data[col] for col in data.columns])
        for partname in ('cbars','cmins','cmaxes'):
            vp = violin_parts[partname]
            vp.set_edgecolor('black')
            vp.set_linewidth(0.5)
    
        for vp,color in zip(violin_parts['bodies'],colors):
            vp.set_facecolor(color)
            vp.set_edgecolor(color)
            vp.set_alpha(0.8)
    
        ax.set_xlim([0.5,top+0.5])
        ax.hlines(0,0.5,top+0.5,lw=0.5)
        ax.set_xticks(range(1,top+1))
        ax.set_xticklabels(data.columns,rotation=90,fontdict={'size':7})
        ax.spines['bottom'].set_linewidth(1.2)
        ax.spines['left'].set_linewidth(1.2)
        ax.spines['right'].set_linewidth(1.2)
        ax.spines['top'].set_linewidth(1.2)
        ax.tick_params(direction='in', which='both')
        if savedir:           
            plt.savefig(savedir,bbox_inches = 'tight')
        else:
            pass
        plt.show()
        
    def scatter(self,feature,savedir):
        f,ax = plt.subplots()
        font_kws = {'size':8}
        ax.scatter(self.ori[feature], self.data[feature],s=5,color='#1E88E5',alpha=0.8)
        ax.spines['right'].set_linewidth(1.2)
        ax.spines['top'].set_linewidth(1.2)
        ax.spines['bottom'].set_linewidth(1.2)
        ax.spines['left'].set_linewidth(1.2)
        ax.hlines(0,self.ori[feature].min()-0.1,self.ori[feature].max()+0.1,lw=0.8)
        ax.set_xlim(self.ori[feature].min()-0.1,self.ori[feature].max()+0.1)
        ax.set_xlabel(feature, fontdict=font_kws)
        ax.tick_params(direction='in', which='both',labelsize=5)
        ax.set_ylabel('SHAP Value', fontdict=font_kws,labelpad=0.5)
        if savedir:
            plt.savefig(savedir,bbox_inches = 'tight')
        else:
            pass
        plt.show()




# if '__main__'==__name__:
#     val = Draw(r"parp.csv",
#                r"08_parp1_final_moe_docking_all_renumber.csv",
#                'read')
    
    