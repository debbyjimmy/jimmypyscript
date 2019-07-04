import arcpy
import pythonaddins
import os
import sys

class ButtonClass1(object):
    """Implementation for CadasPyT_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        for row in arcpy.SearchCursor("sde.SDE.Index_grid"):
            print row.Tile_ID
        new= int (row.Tile_ID)
        nem= str(new)
        print nem
        file1 = open("Y:\CadasPyT\config2.txt","r")
        #file1 = open("Y:\CadasPyT\config2.txt","r")
        #file1 = open("config2.txt","r")
        rasterPath =file1.read()+ nem +'.ecw'
        print rasterPath
        #rasterPath ="C:/Users/jabah\Desktop/AJE/CadasPyT/Images/Satellite.jpg"
        rasterLayerName = 'demoimage'

        md = arcpy.mapping.MapDocument("CURRENT")
        df = arcpy.mapping.ListDataFrames(md)[0]
        result = arcpy.MakeRasterLayer_management(rasterPath, rasterLayerName)
        layer = result.getOutput(0)
        arcpy.mapping.AddLayer(df, layer, 'AUTO_ARRANGE')
        #md.save()
        arcpy.RefreshActiveView()
