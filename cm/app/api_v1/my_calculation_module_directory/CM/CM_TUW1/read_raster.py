from osgeo import gdal


def raster_array(raster, dType=float, return_gt=None):
    ds = gdal.Open(raster)
    geo_transform = ds.GetGeoTransform()
    band1 = ds.GetRasterBand(1)
    arr = band1.ReadAsArray().astype(dType)
    ds = None
    if return_gt:
        return arr, geo_transform
    else:
        return arr

