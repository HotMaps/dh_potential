import os
import time
import sys
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.
                                                       abspath(__file__))))
if path not in sys.path:
    sys.path.append(path)
from CM.CM_TUW4.polygonize import polygonize
from CM.CM_TUW0.rem_mk_dir import rm_mk_dir
import CM.CM_TUW4.district_heating_potential as DHP
import CM.CM_TUW19.run_cm as CM19


verbose = False

def main(heat_density_map, pix_threshold, DH_threshold, output_dir,
         in_orig=None, only_return_areas=False):
    # DH_Regions: boolean array showing DH regions
    DH_Regions, geo_transform = DHP.DHReg(heat_density_map, pix_threshold,
                                          DH_threshold, in_orig)
    
    if only_return_areas:
        geo_transform = None
        return DH_Regions
    outRasterPath1 = output_dir + os.sep + 'F13_' + 'Pot_areas.tif'
    outRasterPath2 = output_dir + os.sep + 'F13_' + 'labels.tif'
    outShapefilePath = output_dir + os.sep + 'F13_' + 'Pot_AT_TH30.shp'
    DHPot, labels = DHP.DHPotential(DH_Regions, heat_density_map)
    """potential of each coherent area in GWh is assigned to its pixels"""
    CM19.main(outRasterPath1, geo_transform, 'int16', DH_Regions)
    
    if verbose:
        CM19.main(outRasterPath2, geo_transform, 'int32', labels)
        polygonize(outRasterPath1, outRasterPath2, outShapefilePath, DHPot)
        return outRasterPath1, outShapefilePath
    else:
        import numpy as np
        return np.sum(DHPot)
    
    

if __name__ == "__main__":
    start = time.time()
    data_warehouse = path + os.sep + 'AD/data_warehouse'
    heat_density_map = data_warehouse + os.sep + 'heat_tot_curr_density_AT.tif'
    output_dir = path + os.sep + 'Outputs'
    outRasterPath = output_dir + os.sep + 'F13_' + 'Pot_AT_TH30.tif'
    rm_mk_dir(output_dir)
    # pix_threshold [GWh/km2]
    pix_threshold = 10
    # DH_threshold [GWh/a]
    DH_threshold = 30
    main(heat_density_map, pix_threshold, DH_threshold, output_dir)
    elapsed = time.time() - start
    print("%0.3f seconds" % elapsed)
