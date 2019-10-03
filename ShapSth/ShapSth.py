# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:57:07 2019

@Author: Zhi-Jiang Yang, Dong-Sheng Cao
@Institution: CBDD Group, Xiangya School of Pharmaceutical Science, CSU, China
@Homepage: http://www.scbdd.com
@Mail: yzjkid9@gmail.com; oriental-cds@163.com
@Blog: https://blog.moyule.me

♥I love Princess Zelda forever♥
"""

import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
from load import load
from tkinter import ttk
from Loop import Loop


def warning():
    messagebox.showerror(title='Error!', message="You should choose a Folder!!!")

  
def choose_loadfile():
    loadfile = askopenfilename(filetypes=(("Excel file", "*.xlsx*;*.xls*"), ("csv file", "*.csv*"), ("Text file", "*.txt*")))
    if loadfile:
        var_read.set(loadfile)
        lb.delete(0,tk.END)
#        lb_id.delete(0,tk.END)
        lb_label.delete(0,tk.END)
        lb_feature.delete(0,tk.END)
        cols = list(load(loadfile).columns)      
        var_scores.set(cols)  
  
def lbtolabel():
    indexes = lb.curselection()[::-1]
    for idx in indexes: 
        lb_label.insert(0,lb.get(idx))
        lb.delete(idx)

def lbtofeature():
    indexes = lb.curselection()[::-1]
    for idx in indexes:
        lb_feature.insert(0,lb.get(idx))
        lb.delete(idx)

def labeltolb():
    indexs = lb_label.curselection()[::-1]
    for idx in indexs: 
        lb.insert(0,lb_label.get(idx))
        lb_label.delete(idx)

def featuretolb():
    indexs = lb_feature.curselection()[::-1]
    for idx in indexs: 
        lb.insert(0,lb_feature.get(idx))
        lb_feature.delete(idx)




def MajorMinor(x):
    flag = cmb.get()
    tk.Label(root,text='Majority',bg='#fae8eb',font=('Arial', 10)).place(x=430, y=220
                 )
    tk.Label(root,text='Minority',bg='#fae8eb',font=('Arial', 10)).place(x=430, y=250
             )
    if flag != 'None':
        major = tk.Entry(width=6,textvariable=var_major)
        major.place(x=500,y=220)   
        minor = tk.Entry(width=6,textvariable=var_minor)
        minor.place(x=500,y=250)
    else:
        major = tk.Entry(state=tk.DISABLED,width=6)
        major.place(x=500,y=220)   
        minor = tk.Entry(state=tk.DISABLED,width=6)
        minor.place(x=500,y=250)
        
        
def SHAPit():
    if var_read.get():
        df = load(var_read.get())
        label = list(lb_label.get(0,tk.END))
        feature = list(lb_feature.get(0,tk.END))
        feature.extend(label)
        data = df.loc[:,feature].copy()
        data[label[0]] = data[label[0]].map(lambda x: str(x))
        l = Loop(data,label[0],
                 loop=var_loop.get(),
                 n_splits=var_splits.get(),
                 sample_mode=cmb.get(),
                 major_label=var_major.get(),
                 minor_label=var_minor.get()
                 )
        out = l.Loop()
        var_data.set(out.to_dict())
        if not messagebox.askyesno('Finished!','Would you want to save the result?'):
                savefile = asksaveasfilename(filetypes=(("Excel file", "*.xlsx*;*.xls*"), ("csv file", "*.csv*"), ("Text file", "*.txt*")))
                out.to_csv(savefile,index=False)
        else:
            pass
        
    else:
        pass


def draw_hist():
    pass




if '__main__' == __name__:
    root = tk.Tk()
    root.geometry('600x370+500+200')
    root.resizable(0,0)  
    bbg = tk.Label(root,bg='#fae8eb',width=500,height=300)
    bbg.pack()
    root.title("Explain your model under shaply")
    
    btn1 = tk.Button(root, text='Select data file',font=('Arial', 10),command=choose_loadfile,width=15,height=1,bg='#d6c4dd').place(x=35,y=20)
    var_read = tk.StringVar()
    lr = tk.Label(root, textvariable=var_read, bg='#eaf6e8', fg='#494546', font=('Arial', 10),width=45,height=1).place(x=175,y=23
                  )
    
    btn3 = tk.Button(root, text='SHAP!',font=('Arial', 10),command=SHAPit,width=15,height=1,bg='#cd1041')
    btn3.place(x=430, y=95)
    
    var_data = tk.StringVar()
    var_ori = tk.StringVar()
    var_scores = tk.StringVar()
    var_loop = tk.IntVar(value=100)
    var_splits = tk.IntVar(value=5)
    var_int = tk.IntVar() 
    var_major = tk.StringVar()
    var_minor = tk.StringVar()
    
    lb = tk.Listbox(root,selectmode='extended',listvariable=var_scores)
    lb.place(x=35,y=60,relwidth=0.3,relheight=0.8)
    scrollbar = tk.Scrollbar(lb,command=lb.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lb.config(yscrollcommand=scrollbar.set)
    
    tk.Label(root,text='Label',bg='#fae8eb').place(x=35*9, y=65)
    lb_label = tk.Listbox(root,selectmode='extended')
    lb_label.place(x=35*8, y=85, relwidth=0.2, relheight=0.1)
    scrollbar = tk.Scrollbar(lb_label,command=lb_label.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lb_label.config(yscrollcommand=scrollbar.set)
    
    tk.Label(root,text='Feature',bg='#fae8eb').place(x=35*9, y=135)
    lb_feature = tk.Listbox(root,selectmode='extended')
    lb_feature.place(x=35*8, y=155, relwidth=0.2, relheight=0.50)
    scrollbar = tk.Scrollbar(lb_feature,command=lb_feature.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lb_feature.config(yscrollcommand=scrollbar.set)
    
    theButton = tk.Button(root, text="→", command=lbtolabel, bg='#cd1041', height=1)
    theButton.place(x=30*8,y=70+5)
    theButton = tk.Button(root, text="←", command=labeltolb, bg='#cd1041', height=1)
    theButton.place(x=30*8,y=110+5)
    
    theButton = tk.Button(root, text="→", command=lbtofeature, bg='#cd1041', height=1)
    theButton.place(x=30*8,y=198+5)
    theButton = tk.Button(root, text="←", command=featuretolb, bg='#cd1041', height=1)
    theButton.place(x=30*8,y=238+5)       
    
    tk.Label(root,text='Loop times',bg='#fae8eb',font=('Arial', 10)).place(x=430, y=130)
    e1 = tk.Entry(root, show=None, font=('Arial', 10), textvariable=var_loop,width=6)
    e1.place(x=500, y=130)

    tk.Label(root,text='n_splits',bg='#fae8eb',font=('Arial', 10)).place(x=430, y=160)
    e2 = tk.Entry(root, show=None, font=('Arial', 10), textvariable=var_splits,width=6)
    e2.place(x=500, y=160)
    
    tk.Label(root,text='sample',bg='#fae8eb',font=('Arial', 10)).place(x=430, y=190)
    cmb = ttk.Combobox(root,width=10)
    cmb.bind("<<ComboboxSelected>>",MajorMinor)
    cmb.place(x=500,y=190)
    cmb['value'] = (None, 'Undersampling', 'Oversampling')
    cmb.current(0)      
    
    root.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    