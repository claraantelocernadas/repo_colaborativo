#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:32:17 2026

@author: manamoiseeff
"""


























def analizar_habitos (lista):
     resultado = {} 
     
     for actividad in lista:
         if actividad in resultado:
             resultado [actividad]+=1 
         else:
            resultado [actividad] = 1
            
     return resultado 