#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 19:44:33 2022

@author: oscarohman
"""
#conda yfinance
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date

Aktier=['VOLV-B.ST','SCA-B.ST','ERIC-B.ST','NMAN.ST','FIRE.ST','AFRY.ST','KNOW.ST','FOI-B.ST','KIND-SDB.ST','CHARGE.ST','CIBUS.ST','FSI.TO','HM-B.ST','NXE.TO','NIBE-B.ST','NDA-SE.ST','SDS.ST','ZAP.OL']
Nyckeltal=['trailingPE','priceToSalesTrailing12Months','profitMargins','currentRatio','returnOnEquity','revenuePerShare','currentPrice','marketCap','ebitda','fullTimeEmployees']
Info=pd.DataFrame(columns=[Aktier])
for aktie in Aktier:
    print(aktie)
    Aktie_data= yf.Ticker(aktie)
    Aktie_info=Aktie_data.info
    for ntal in Nyckeltal:
        try:
            Info.loc[ntal,aktie]=Aktie_info[ntal]
        except:
            print(ntal+' was not found for '+aktie)
        
        #%%
        Info.loc['PS',aktie]=Aktie_info['priceToSalesTrailing12Months']
        Info.loc['ProfitMargin',aktie]=Aktie_info['profitMargins']
        Info.loc['CurrentRatio',aktie]=Aktie_info['currentRatio']
        Info.loc['RoE',aktie]=Aktie_info['returnOnEquity']
        Info.loc['RevenuePerShare',aktie]=Aktie_info['revenuePerShare']
        Info.loc['Price',aktie]=Aktie_info['currentPrice']
        Info.loc['MarketCap',aktie]=Aktie_info['marketCap']
        Info.loc['EBITDA',aktie]=Aktie_info['ebitda']
        Info.loc['FulltimeEmployees',aktie]=Aktie_info['fullTimeEmployees']
    
    print(aktie)
#%%
Info=pd.DataFrame(columns=[Aktier])
#%%