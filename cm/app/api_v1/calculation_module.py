import os
import sys
path = os.path.dirname(os.path.abspath(__file__))
from ..helper import generate_output_file_tif
from ..helper import generate_output_file_shp
from ..helper import create_zip_shapefiles
from ..constant import CM_NAME
from ..exceptions import ValidationError
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
    input_raster_selection =  inputs_raster_selection["heat"]


    pix_threshold = float(inputs_parameter_selection["pix_threshold"])
    DH_threshold = float(inputs_parameter_selection["DH_threshold"])



    output_raster1 = generate_output_file_tif(output_directory)
    output_raster2 = generate_output_file_tif(output_directory)
    output_shp1 = generate_output_file_shp(output_directory)
    output_shp2 = generate_output_file_shp(output_directory)


    total_potential, total_heat_demand, \
    graphics, symbol_vals_str = CM4.main(input_raster_selection, pix_threshold,
                                         DH_threshold, output_raster1,
                                         output_raster2, output_shp1,
                                         output_shp2)

    result = dict()
    result['name'] = CM_NAME
    result['indicator'] = [{"unit": "GWh", "name": "Total heat demand in GWh within the selected zone","value": total_heat_demand},
                          {"unit": "GWh", "name": "Total district heating potential in GWh within the selected zone","value": total_potential},
                          {"unit": "%", "name": "Potential share of district heating from total demand in selected zone","value": 100*round(total_potential/total_heat_demand, 4)}
                           ]
    # if graphics is not None:
    if total_potential > 0:
        output_shp2 = create_zip_shapefiles(output_directory, output_shp2)
        step = float(symbol_vals_str[4]) - float(symbol_vals_str[3])
        result["raster_layers"]=[{"name": "District heating areas - raster","path": output_raster1, "type": "custom",
                          "symbology": [{"red":254,"green":237,"blue":222,"opacity":0.5,"value":symbol_vals_str[0],"label":symbol_vals_str[0] + " GWh"},
                                    {"red":253,"green":208,"blue":162,"opacity":0.5,"value":symbol_vals_str[1],"label":symbol_vals_str[1] + " GWh"},
                                    {"red":253,"green":174,"blue":107,"opacity":0.5,"value":symbol_vals_str[2],"label":symbol_vals_str[2] + " GWh"},
                                    {"red":253,"green":141,"blue": 60,"opacity":0.5,"value":symbol_vals_str[3],"label":symbol_vals_str[3] + " GWh"},
                                    {"red":230,"green": 85,"blue": 13,"opacity":0.5,"value":symbol_vals_str[4],"label":symbol_vals_str[4] + " GWh"},
                                    {"red":166,"green": 54,"blue":  3,"opacity":0.5,"value":str(float(symbol_vals_str[4]) + step),"label":">" +symbol_vals_str[4] + " GWh"}]
                                    },
                          {"name": "Heat density map in potential DH areas - raster","path": output_raster2, "type": "heat"
                                    }
                                    ]
        result["vector_layers"]=[{"name": "District heating areas and their potentials - shapefile","path": output_shp2, "type": "custom",
                                  "symbology": [{"red":254,"green":237,"blue":222,"opacity":0.5,"value":symbol_vals_str[0],"label":symbol_vals_str[0] + " GWh"},
                                                {"red":253,"green":208,"blue":162,"opacity":0.5,"value":symbol_vals_str[1],"label":symbol_vals_str[1] + " GWh"},
                                                {"red":253,"green":174,"blue":107,"opacity":0.5,"value":symbol_vals_str[2],"label":symbol_vals_str[2] + " GWh"},
                                                {"red":253,"green":141,"blue": 60,"opacity":0.5,"value":symbol_vals_str[3],"label":symbol_vals_str[3] + " GWh"},
                                                {"red":230,"green": 85,"blue": 13,"opacity":0.5,"value":symbol_vals_str[4],"label":symbol_vals_str[4] + " GWh"},
                                                {"red":166,"green": 54,"blue":  3,"opacity":0.5,"value":str(float(symbol_vals_str[4]) + step),"label":">" +symbol_vals_str[4] + " GWh"}]
                                  }]
    result['graphics'] = graphics
    return result