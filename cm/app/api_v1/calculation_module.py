import os
import sys
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.
                                                       abspath(__file__))))
from ..helper import generate_output_file_tif
from ..helper import generate_output_file_shp
""" Entry point of the calculation module function"""
if path not in sys.path:
    sys.path.append(path)
import my_calculation_module_directory.CM.CM_TUW4.run_cm as CM4



def calculation(output_directory,inputs_raster_selection, pix_threshold, DH_threshold):

    """ def calculation()"""
    '''
    inputs:
        hdm in raster format for the selected region
        pix_threshold [GWh/km2]
        DH_threshold [GWh/a]

    Outputs:
        DH_Regions: contains binary values (no units) showing coherent areas
    '''
    output_raster1 = generate_output_file_tif(output_directory)
    output_raster2 = generate_output_file_tif(output_directory)
    output_shp1 = generate_output_file_shp(output_directory)
    output_shp2 = generate_output_file_shp(output_directory)

    input_raster_selection =  inputs_raster_selection["heat_tot_curr_density"]
    total_potential, graphics = CM4.main(input_raster_selection, pix_threshold,
                                         DH_threshold, output_raster1,
                                         output_raster2, output_shp1,
                                         output_shp2)
    result = dict()
    result['name'] = 'CM District Heating Potential'
    result["raster_layers"]=[{"name": "district heating coherent areas","path": output_raster1}]
    result["vector_layers"]=[{"name": "shapefile of coherent areas with their potential","path": output_shp2}]
    result['indicator'] = [{"unit": "GWh", "name": "Total district heating potential in GWh in the region","value": total_potential},
                           {"unit": "GWh", "name": "test","value": total_potential}]
    result['graphics'] = graphics
    return result