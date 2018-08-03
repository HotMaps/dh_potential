import os
import sys
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.
                                                       abspath(__file__))))
if path not in sys.path:
    sys.path.append(path)
import dh_potential.CM.CM_TUW4.run_cm as CM4



def calculation(heat_density_map, pix_threshold, DH_threshold, output_dir):
    '''
    inputs:
        hdm in raster format for the selected region
        pix_threshold [GWh/km2]
        DH_threshold [GWh/a]

    Outputs:
        DH_Regions: contains binary values (no units) showing coherent areas
    '''
    output_dir = path + os.dir + 'Outputs'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    '''
    outRasterPath, outShapefile = CM4.main(heat_density_map, pix_threshold,
                                           DH_threshold, output_dir)
    return {'F13_out_raster_path_0': outRasterPath,
            'F13_out_shapefile_path_0': outShapefile}
    '''
    total_potential = CM4.main(heat_density_map, pix_threshold, DH_threshold, output_dir)
    return total_potential