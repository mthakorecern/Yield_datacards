import sys, os
import ROOT
import numpy as np


histo_2016 = []
histo_2017 = []
histo_2018 = []
histo_2026_Phase1 = []
histo_2026_Phase2 = []

arr_2016 = []
arr_2017 = []
arr_2018 = []
arr_2026_Phase1 = []
arr_2026_Phase2 = []

yieldfile = open("yields.txt", 'w') 

f = ROOT.TFile.Open('fileCombine2016H_merged.root')
keys = [f.Get(k.GetName()) for k in f.GetListOfKeys()]

for n in keys:
    if "SignalRegion" in n.GetName():
        if "_nom" in n.GetName():
           integral = n.Integral()
           sampleName = n.GetName().split("___")[1].split("_nom")[0]
           histo_2016.append("%s"%sampleName)
           arr_2016.append("%.1f"%integral)
           yieldfile.write("%s:%.1f\n"%(sampleName, integral));
           
 
yieldfile.write("\n\n")


f = ROOT.TFile.Open('fileCombine2017H_merged.root')
keys = [f.Get(k.GetName()) for k in f.GetListOfKeys()]

for n in keys:
    if "SignalRegion" in n.GetName():
        if "_nom" in n.GetName():
           integral = n.Integral()
           sampleName = n.GetName().split("___")[1].split("_nom")[0]
           histo_2017.append("%s"%sampleName)
           arr_2017.append("%.1f"%integral)
           yieldfile.write("%s:%.1f\n"%(sampleName, integral));

yieldfile.write("\n\n")

f = ROOT.TFile.Open('fileCombine2018H_merged.root')
keys = [f.Get(k.GetName()) for k in f.GetListOfKeys()]

for n in keys:
    if "SignalRegion" in n.GetName():
        if "_nom" in n.GetName():
           integral = n.Integral()
           sampleName = n.GetName().split("___")[1].split("_nom")[0]
           histo_2018.append("%s"%sampleName)
           arr_2018.append("%.1f"%integral)
           yieldfile.write("%s:%.1f\n"%(sampleName, integral));

yieldfile.write("\n\n")
           
f = ROOT.TFile.Open('fileCombine2026H_100_Phase1.root')
keys = [f.Get(k.GetName()) for k in f.GetListOfKeys()]

for n in keys:
    if "SignalRegion" in n.GetName():
        if "_nom" in n.GetName():
           integral = n.Integral()
           sampleName = n.GetName().split("___")[1].split("_nom")[0]
           histo_2026_Phase1.append("%s"%sampleName)
           arr_2026_Phase1.append("%.1f"%integral)
           yieldfile.write("%s:%.1f\n"%(sampleName, integral));


histo_2026_Phase1.append('SignalRegionPhase1_VV:')
arr_2026_Phase1.append('0')
yieldfile.write('SignalRegionPhase1_VV:0')

yieldfile.write("\n\n")

f = ROOT.TFile.Open('fileCombine2026H_100_Phase2.root')
keys = [f.Get(k.GetName()) for k in f.GetListOfKeys()]

for n in keys:
    if "SignalRegion" in n.GetName():
        if "_nom" in n.GetName():
           integral = n.Integral()
           sampleName = n.GetName().split("___")[1].split("_nom")[0]
           histo_2026_Phase2.append("%s"%sampleName)
           arr_2026_Phase2.append("%.1f"%integral)
           yieldfile.write("%s:%.1f\n"%(sampleName, integral));


histo_2026_Phase2.append('SignalRegionPhase2_VV:')
arr_2026_Phase2.append('0')
yieldfile.write('SignalRegionPhase2_VV:0')
yieldfile.write("\n\n")

yieldfile.close() 


print(histo_2016)
print(type(histo_2016))
arr_2016 = np.array(arr_2016)
arr_2016 = arr_2016.astype(np.float)
print("2016:",arr_2016)
print(type(arr_2016))
print("\n")


print(histo_2017)
print(type(histo_2017))
arr_2017 = np.array(arr_2017)
arr_2017 = arr_2017.astype(np.float)
print("2017:",arr_2017)
print(type(arr_2017))
print("\n")

print(histo_2018)
print(type(histo_2018))
arr_2018 = np.array(arr_2018)
arr_2018 = arr_2018.astype(np.float)
print("2012:",arr_2018)
print(type(arr_2018))
print("\n")

print(histo_2026_Phase1)
print(type(histo_2026_Phase1))
arr_2026_Phase1 = np.array(arr_2026_Phase1)
arr_2026_Phase1 = arr_2026_Phase1.astype(np.float)
print("Phase1:",arr_2026_Phase1)
print(type(arr_2026_Phase1))
print("\n")

print(histo_2026_Phase2)
print(type(histo_2026_Phase2))
arr_2026_Phase2 = np.array(arr_2026_Phase2)
arr_2026_Phase2 = arr_2026_Phase2.astype(np.float)
print("Phase2:",arr_2026_Phase2)
print(type(arr_2026_Phase2))
print("\n")

arr_m = arr_2016 + arr_2017 + arr_2018
print("Sum of 2016+2017+2018:",arr_m)

arr_ratio_Phase1 = np.divide(arr_2026_Phase1, arr_m)
print("Phase1 ratios:",arr_ratio_Phase1)

arr_ratio_Phase2 = np.divide(arr_2026_Phase2, arr_m)
print("Phase2 ratios:",arr_ratio_Phase2)

