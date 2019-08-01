import os
import time
import sys
import numpy as np
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.
                                                       abspath(__file__))))
if path not in sys.path:
    sys.path.append(path)
from CM.CM_TUW4.polygonize import polygonize
from CM.CM_TUW0.rem_mk_dir import rm_mk_dir, rm_file
import CM.CM_TUW4.district_heating_potential as DHP
import CM.CM_TUW19.run_cm as CM19


def main(heat_density_map, pix_threshold, DH_threshold, output_raster1,
         output_raster2, output_shp1, output_shp2, in_orig=None,
         only_return_areas=False):
    # The CM can be run for the following ranges of pixel and Dh thresholds:
    if pix_threshold < 1:
        raise ValueError("Pixel threshold cannot be smaller than 1 GWh/km2!")
    if DH_threshold < 1:
        raise ValueError("DH threshold cannot be smaller than 1 GWh/year!")
    # DH_Regions: boolean array showing DH regions
    DH_Regions, geo_transform, total_heat_demand = DHP.DHReg(heat_density_map,
                                                             pix_threshold,
                                                             DH_threshold,
                                                             in_orig)
    if only_return_areas:
        geo_transform = None
        return DH_Regions
    DHPot, labels = DHP.DHPotential(DH_Regions, heat_density_map)
    total_potential = np.around(np.sum(DHPot),2)
    total_heat_demand = np.around(total_heat_demand, 2)
    if total_potential == 0:
        dh_area_flag = False
    else:
        dh_area_flag = True
    graphics  = [
            {
                    "type": "bar",
                    "xLabel": "DH Area Label",
                    "yLabel": "Potential (GWh/year)",
                    "data": {
                            "labels": [str(x) for x in range(1, 1+len(DHPot))],
                            "datasets": [{
                                    "label": "Potential in coherent areas",
                                    "backgroundColor": ["#3e95cd"]*len(DHPot),
                                    "data": list(np.around(DHPot,2))
                                    }]
                    }
                },{
                    "type": "bar",
                    "xLabel": "",
                    "yLabel": "Demand / Potential (GWh/year)",
                    "data": {
                            "labels": ["Annual heat demand", "DH potential"],
                            "datasets": [{
                                    "label": "Heat Demand Vs. DH Potential (GWh/year)",
                                    "backgroundColor": ["#fe7c60", "#3e95cd"],
                                    "data": [total_heat_demand, total_potential]
                                    }]
                    }
                }]
    symbol_vals_str = []
    if dh_area_flag:
        CM19.main(output_raster1, geo_transform, 'int8', DH_Regions)
        CM19.main(output_raster2, geo_transform, 'int32', labels)
        symbol_vals_str = polygonize(output_raster1, output_raster2,
                                     output_shp1, output_shp2, DHPot)
        rm_file(output_raster2, output_raster2[:-4] + '.tfw')

    return total_potential, total_heat_demand, graphics, symbol_vals_str
