import os, sys
import ROOT as root
import numpy as np
from math import pi


fileLoc="/home/yancy/Code/Git_package/Python_Introduction/examples"
fileName= fileLoc+"/higgs_nnh.root"
print("reading from file",fileName)

file=root.TFile(fileName)
tree=file.Get("datatrain")

#nev = tree.GetEntries()
nev = 2
for iev in range(0,nev):
    tree.GetEntry(iev)
    print ("a new event")
    print ("higgs mc decay",tree.mc_jet_higgs_channel)
    print ("higgs po decay",tree.po_jet_higgs_channel)
    for element  in tree.po_jet_phi:
        print (element)

