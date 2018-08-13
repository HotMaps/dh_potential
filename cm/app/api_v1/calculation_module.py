import os
import sys
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.
                                                       abspath(__file__))))
if path not in sys.path:
    sys.path.append(path)
import my_calculation_module_directory.CM.CM_TUW4.run_cm as CM4



from osgeo import gdal

""" Entry point of the calculation module function"""

#TODO: CM provider must "change this code"
#TODO: CM provider must "not change input_raster_selection,output_raster  1 raster input => 1 raster output"
#TODO: CM provider can "add all the parameters he needs to run his CM
#TODO: CM provider can "return as many indicators as he wants"
def calculation(input_raster_selection, factor, output_raster):
    #TODO the folowing code must be changed by the code of the calculation module
    ds = gdal.Open(input_raster_selection)
    ds_band = ds.GetRasterBand(1)

def calculation(input_raster, pix_threshold, DH_threshold, output_raster):
    '''
    inputs:
        hdm in raster format for the selected region
        pix_threshold [GWh/km2]
        DH_threshold [GWh/a]

    Outputs:
        DH_Regions: contains binary values (no units) showing coherent areas

    outRasterPath, outShapefile = CM4.main(heat_density_map, pix_threshold,
                                           DH_threshold, output_dir)
    return {'F13_out_raster_path_0': outRasterPath,
            'F13_out_shapefile_path_0': outShapefile}
    '''
    total_potential = CM4.main(input_raster, pix_threshold, DH_threshold, output_raster)
    return total_potential