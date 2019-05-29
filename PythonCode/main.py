# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QInputDialog, QLineEdit
    )
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QCoreApplication
import sys
import pandas as pd
import numpy as np
from scipy import stats
import statistics as sts
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Qt5Agg") 
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
import math 

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1239, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.load_data = QtWidgets.QPushButton(self.centralwidget)
        self.load_data.setGeometry(QtCore.QRect(50, 10, 131, 51))
        self.load_data.setObjectName("load_data")
      
        self.load_data.clicked.connect(self.loadData)
        self.univariate_data = QtWidgets.QLabel(self.centralwidget)
        self.univariate_data.setGeometry(QtCore.QRect(70, 70, 121, 31))
        self.univariate_data.setObjectName("univariate_data")
        self.dis_desc = QtWidgets.QPushButton(self.centralwidget)
        self.dis_desc.setGeometry(QtCore.QRect(50, 100, 161, 61))
        self.dis_desc.setObjectName("dis_desc")

        self.dis_desc.clicked.connect(self.click2)
        self.dis_hist = QtWidgets.QPushButton(self.centralwidget)
        self.dis_hist.setGeometry(QtCore.QRect(50, 170, 161, 61))
        self.dis_hist.setObjectName("dis_hist")
        self.dis_hist.clicked.connect(self.hist)
        
        self.fit_hist = QtWidgets.QPushButton(self.centralwidget)
        self.fit_hist.setGeometry(QtCore.QRect(50, 240, 161, 61))
        self.fit_hist.setObjectName("fit_hist")
        self.fit_hist.clicked.connect(self.fitHist)
        
        self.dis_norm = QtWidgets.QPushButton(self.centralwidget)
        self.dis_norm.setGeometry(QtCore.QRect(50, 310, 161, 61))
        self.dis_norm.setObjectName("dis_norm")
        self.dis_norm.clicked.connect(self.disnorm)
        
        self.dis_box = QtWidgets.QPushButton(self.centralwidget)
        self.dis_box.setGeometry(QtCore.QRect(50, 390, 161, 61))
        self.dis_box.setObjectName("dis_box")
        self.dis_box.clicked.connect(self.boxp)
        
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(60, 490, 91, 61))
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(QCoreApplication.instance().quit)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(220, 90, 20, 381))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 90, 20, 381))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(30, 460, 201, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(30, 80, 41, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(190, 80, 41, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.bivariate_data = QtWidgets.QLabel(self.centralwidget)
        self.bivariate_data.setGeometry(QtCore.QRect(270, 70, 121, 31))
        self.bivariate_data.setObjectName("bivariate_data")
        self.t_test = QtWidgets.QPushButton(self.centralwidget)
        self.t_test.setGeometry(QtCore.QRect(250, 100, 161, 51))
        self.t_test.setObjectName("t_test")
        self.t_test.clicked.connect(self.ttest)
        
        self.t_testn = QtWidgets.QPushButton(self.centralwidget)
        self.t_testn.setGeometry(QtCore.QRect(250, 160, 161, 51))
        self.t_testn.setObjectName("t_testn")
        self.t_testn.clicked.connect(self.ttestn)

        self.ANOVA = QtWidgets.QPushButton(self.centralwidget)
        self.ANOVA.setGeometry(QtCore.QRect(250, 240, 161, 51))
        self.ANOVA.setObjectName("ANOVA")
        self.ANOVA.clicked.connect(self.anova)
        self.nANOVA = QtWidgets.QPushButton(self.centralwidget)
        self.nANOVA.setGeometry(QtCore.QRect(250, 300, 161, 51))
        self.nANOVA.setObjectName("nANOVA")
        self.ANOVA.clicked.connect(self.nanova)
        self.PCA = QtWidgets.QPushButton(self.centralwidget)
        self.PCA.setGeometry(QtCore.QRect(250, 380, 161, 51))
        self.PCA.setObjectName("PCA")
        self.PCA.clicked.connect(self.pca2)
        self.PCA3 = QtWidgets.QPushButton(self.centralwidget)
        self.PCA3.setGeometry(QtCore.QRect(250, 440, 161, 51))
        self.PCA3.setObjectName("PCA3")
        
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(250, 80, 21, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(390, 80, 21, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(390, 220, 21, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(250, 220, 21, 16))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.trivariate_data = QtWidgets.QLabel(self.centralwidget)
        self.trivariate_data.setGeometry(QtCore.QRect(270, 210, 121, 31))
        self.trivariate_data.setObjectName("trivariate_data")
        self.mutivariate_data = QtWidgets.QLabel(self.centralwidget)
        self.mutivariate_data.setGeometry(QtCore.QRect(270, 350, 131, 31))
        self.mutivariate_data.setObjectName("mutivariate_data")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(250, 360, 21, 16))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(400, 360, 13, 16))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(404, 87, 16, 121))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(242, 87, 16, 121))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(250, 200, 161, 16))
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setGeometry(QtCore.QRect(403, 227, 16, 121))
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(243, 227, 16, 121))
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setGeometry(QtCore.QRect(250, 340, 161, 16))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setGeometry(QtCore.QRect(406, 367, 16, 121))
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.centralwidget)
        self.line_19.setGeometry(QtCore.QRect(243, 368, 16, 121))
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(self.centralwidget)
        self.line_20.setGeometry(QtCore.QRect(250, 480, 161, 16))
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        
        self.graphicsView = QtWidgets.QLabel(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(440, 50, 421, 451))
        self.graphicsView.setObjectName("graphicsView")
        
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(920, 30, 71, 31))
        self.result.setObjectName("result")
        self.show_res = QtWidgets.QLabel(self.centralwidget)
        self.show_res.setGeometry(QtCore.QRect(920, 60, 251, 441))

        self.show_res.setObjectName("show_res")
        self.load_data.raise_()
        self.dis_desc.raise_()
        self.dis_hist.raise_()
        self.fit_hist.raise_()
        self.dis_norm.raise_()
        self.dis_box.raise_()
        self.exit.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.univariate_data.raise_()
        self.line_5.raise_()
        self.bivariate_data.raise_()
        self.t_test.raise_()
        self.t_testn.raise_()
        self.nANOVA.raise_()
        self.ANOVA.raise_()
        self.PCA.raise_()
        self.PCA3.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.line_8.raise_()
        self.line_9.raise_()
        self.trivariate_data.raise_()
        self.mutivariate_data.raise_()
        self.line_10.raise_()
        self.line_11.raise_()
        self.line_12.raise_()
        self.line_13.raise_()
        self.line_14.raise_()
        self.line_15.raise_()
        self.line_16.raise_()
        self.line_17.raise_()
        self.line_18.raise_()
        self.line_19.raise_()
        self.line_20.raise_()
        self.graphicsView.raise_()
        self.result.raise_()
        self.show_res.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.load_data.setText(_translate("MainWindow", "Load Data"))
        self.univariate_data.setText(_translate("MainWindow", "UNIVARIATE DATA"))
        self.dis_desc.setText(_translate("MainWindow", "Display Descript stat"))
        self.dis_hist.setText(_translate("MainWindow", "Display Histogram"))
        self.fit_hist.setText(_translate("MainWindow", "Fit Histogram"))
        self.dis_norm.setText(_translate("MainWindow", "Display NormPlot"))
        self.dis_box.setText(_translate("MainWindow", "Display Boxplot"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.bivariate_data.setText(_translate("MainWindow", " BIVARIATE DATA"))
        self.t_test.setText(_translate("MainWindow", "Parametric t test"))
        self.t_testn.setText(_translate("MainWindow", "Nonparametric t test"))
        self.nANOVA.setText(_translate("MainWindow", "Nonparametric ANOVA"))
        self.ANOVA.setText(_translate("MainWindow", "ANOVA"))
        self.PCA.setText(_translate("MainWindow", "PCA 2D"))
        self.PCA3.setText(_translate("MainWindow", "PCA 3D"))
        self.trivariate_data.setText(_translate("MainWindow", " TRIVARIATE DATA"))
        self.mutivariate_data.setText(_translate("MainWindow", " MUTIVARIATE DATA"))
        self.result.setText(_translate("MainWindow", "RESULTS"))

    def loadData(self):
        self.fileName, filetype = QFileDialog.getOpenFileName(self,  
                                    "load data",  
                                    "",  
                                    "XLSX Files (*.xlsx)")
        self.data = pd.read_excel(self.fileName,header=None)
        self.dim = len(self.data.columns)
        if self.dim != 2:
            self.data = pd.read_excel(self.fileName,header=0)
            print(self.data)
            print(self.data.columns)
    #choose column and display descriptive data            
    def click2(self):
        self.data
        self.dim
        if self.dim==2:
           text, ok = QInputDialog.getText(self, "Input Dialog", "Choose one column:")
           if ok:
               self.ndata = self.data[int(text)]
#               print(self.ndata)
        elif self.dim == 3:
            text, ok = QInputDialog.getText(self, "Choose one column", "Input index name:")
            if ok:
               self.ndata = self.data[str(text)]
               print(self.ndata)
        else:
            self.ndata = self.data
#            print(type(self.ndata[1]))
        print(self.ndata)
        if self.dim == 2:           
            self.ndata = self.ndata[~np.isnan(self.ndata)]
#        print(self.ndata)
        #mean
        mi = np.mean(self.ndata)       
        ste = np.std(self.ndata)
        med = np.median(self.ndata)
        lowci = mi-1.96*ste
        upci = mi+1.96*ste
        moden = self.ndata.mode().loc[0]
        std = np.std(self.ndata)
        var = np.var(self.ndata)
        kur = stats.skew(self.ndata)
        mini = self.ndata.min()
        maxi = self.ndata.max()
        ran = maxi - mini
        s = self.ndata.sum()
        cou = len(self.ndata)
        print(med,lowci,upci,moden,std,var,kur,mini,maxi,ran,s,cou)
        #show result
        res = 'Mean    '+ str(mi) +'\n\n'+'Standard error   '+str(ste)+'\n\n'+'Median   '+str(med)+'\n\n'+'CI at 95%   '+'('+str(lowci)+'   ,  '+str(upci)+'  )\n\n'+'Mode   '+str(moden)+'\n\n'+'Std   '+str(std)+'\n\n'+'Variance   '+str(var)+'\n\nKurt   '+str(kur)+'\n\n'+'Minimum   '+str(mini)+'\n\nMaximum   '+str(maxi)+'\n\nRange   '+str(ran)+'\n\n'+'Sum   '+str(s)+'\n\nCount  '+str(cou)
        self.show_res.setText(res)    
#plot histgram 
    def hist(self):        
        sns.distplot(self.ndata,bins=100,kde=False,rug=False)
        plt.savefig("his.png", transparent=True)
        plt.clf()
        img1 = QPixmap("his.png")
        img1.scaled(self.graphicsView.size())
        self.graphicsView.setPixmap(img1)
        
#fit histgram 
    def fitHist(self):
        sns.distplot(self.ndata,bins=100,hist=True,rug=False)
        plt.savefig("fithist.png", transparent=True)
        plt.clf()
        img1 = QPixmap("fithist.png")
        img1.scaled(self.graphicsView.size())
        self.graphicsView.setPixmap(img1)

#norm plot
    def disnorm(self):
#        stats.probplot(self.ndata,dist="norm",plot=plt)
        columns = self.ndata.columns.tolist()
        stats.probplot(self.ndata[columns[0]].tolist(),dist="norm",plot=plt)
        plt.savefig("norm.png", transparent=True)
        plt.clf()
        img1 = QPixmap("norm.png")
        img1.scaled(self.graphicsView.size())
        self.graphicsView.setPixmap(img1)

#boxplot    
    def boxp(self):
        self.data.plot(kind = 'box').get_figure()
#        plt.boxplot(self.ndata)
        plt.savefig("boxplot.png", transparent=True)
        plt.clf()
        img1 = QPixmap("boxplot.png")
        img1.scaled(self.graphicsView.size())
        self.graphicsView.setPixmap(img1)

#two sample test 
    def ttest(self):
       print(self.data)
       if self.dim == 2:
           a = self.data[0]
           b = self.data[1]
           a = a[~np.isnan(a)]
           b = b[~np.isnan(b)]
           varA = np.var(a)
           varB = np.var(b)
           if varA == varB:
               t, p = stats.ttest_ind(a,b,equal_var=True)
               print("ttest_ind:            t = %g  p = %g" % (t, p))
               res1 = "Equal variance test:           \n\n t = %g  p = %g " % (t, p)
               self.show_res.setText(res1)
           else:
               t, p = stats.ttest_ind(a,b,equal_var=False)
               print("ttest_ind:            t = %g  p = %g" % (t, p))
               res2 = "Unequal variance test:           \n\n t = %g  p = %g" % (t, p)
               self.show_res.setText(res2)
 
#Nonparametric t test    
    def ttestn(self):
        stats.kruskal(self.ndata)

#ANOVA TEST 
    def anova(self):
        columns = self.data.columns.tolist()               
        ss = columns[0]+' ~ '+columns[1]+ ' + '+columns[2]      
        mod = ols(ss,data=self.data).fit()          
        aov_table = anova_lm(mod)
        res3='ANOVA Table\n\n'+aov_table.to_string()
        self.show_res.setText(res3)

#nonparametric ANOVA test 
    def nanova(self):
        columns = self.data.columns.tolist()
        x = self.data[columns[0]].tolist()
        y = self.data[columns[1]].tolist()
        z = self.data[columns[2]].tolist()
        v=stats.kruskal(x, y, z)
        
        res4 = 'Kruskal-Wallis ANOVA Table\n\n'
        res4+='Chi-sq :'+str(v[0])+'\n'
        res4+='Prob>Chi-sq :'+str(v[1])+'\n'
        self.show_res.setText(res4)
    
        plt.boxplot(self.data)
        plt.savefig("anova.png", transparent=True)
        plt.clf()
        img1 = QPixmap("anova.png")
        img1.scaled(self.graphicsView.size())
        self.graphicsView.setPixmap(img1)

#2D PCA 
    def pca2(self):
        pca = PCA(n_components=2)
        pca.fit(self.data)
        PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,svd_solver='auto', tol=0.0, whiten=False)        
        res5='Explained variance ratio'+pca.explained_variance_ratio_+'\n\n'+'Singular values  '+pca.sigular_values_
        self.show_res.setText(str(res5))
    
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())