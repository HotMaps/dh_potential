import os
import sys
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.
                                                       abspath(__file__))))
from ..helper import generate_output_file_tif
from ..helper import generate_output_file_shp
from ..helper import create_zip_shapefiles
""" Entry point of the calculation module function"""
if path not in sys.path:
    sys.path.append(path)
import my_calculation_module_directory.CM.CM_TUW4.run_cm as CM4



def calculation(output_directory, inputs_raster_selection, inputs_parameter_selection):

    """ def calculation()"""
    '''
    inputs:
        hdm in raster format for the selected region
        pix_threshold [GWh/km2]
        DH_threshold [GWh/a]

    Outputs:
        DH_Regions: contains binary values (no units) showing coherent areas
    '''
    print ('*******************************CALCULATION*******************************************')
    print ('input_raster_selectio_xxxxn', inputs_raster_selection)
    input_raster_selection =  inputs_raster_selection["heat_tot_curr_density_tif"]

    pix_threshold = int(inputs_parameter_selection["pix_threshold"])
    DH_threshold = int(inputs_parameter_selection["DH_threshold"])

    output_raster1 = generate_output_file_tif(output_directory)
    output_raster2 = generate_output_file_tif(output_directory)
    output_shp1 = generate_output_file_shp(output_directory)
    output_shp2 = generate_output_file_shp(output_directory)



    total_potential, graphics = CM4.main(input_raster_selection, pix_threshold,
                                         DH_threshold, output_raster1,
                                         output_raster2, output_shp1,
                                         output_shp2)

    #need to zip the directory for a shapefile
    print ('wiill zip', output_shp2)

    output_shp2 = create_zip_shapefiles(output_directory, output_shp2)


    print ('shape_file', output_shp2)
    result = dict()
    result['name'] = 'CM District Heating Potential'
    result["raster_layers"]=[{"name": "district heating coherent areas","path": output_raster1, "type": "custome", "legend": [[1, 46, 154, 88]]}]
    result["vector_layers"]=[{"name": "shapefile of coherent areas with their potential","path": output_shp2}]
    result['indicator'] = [{"unit": "GWh", "name": "Total district heating potential in GWh in the region","value": total_potential},
                           {"unit": "GWh", "name": "test","value": total_potential}]
    result['graphics'] = graphics
    return result