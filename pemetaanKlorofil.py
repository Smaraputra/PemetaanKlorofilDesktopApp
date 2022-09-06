import os
import math
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly
from PIL import Image
from pyproj import Proj
from wx.core import NO
from pymasker import LandsatMasker
from pymasker import LandsatConfidence
import pathlib

PATH = str(pathlib.Path(__file__).parent.resolve()) + "\\temp"
os.chdir(PATH)

class pemetaanKlorofil:
    TAG = 'pemetaanKlorofil.class'
    _errstr = "Mode is unknown or incompatible with input array shape."
    imagePath4 = ""
    imagePath5 = ""
    imagePath6 = ""
    imagePathQA = ""
    shplautPath = ""
    output = ""
    band4 = None
    band5 = None
    band6 = None
    bandQA = None
    output_cols = 0
    output_rows = 0
    lonStartCrop = 0
    latStartCrop = 0
    lonEndCrop = 0
    latEndCrop = 0
    sun_elev = float
    reflectance_mult = float
    reflectance_add = float

    def __init__(self):
        print("Create Pemetaan Class")

    def reset(self):
        self.band4 = None
        self.band5 = None
        self.band6 = None
        self.bandQA = None
        self.imagePath4 = ""
        self.imagePath5 = ""
        self.imagePath6 = ""
        self.imagePathQA = ""
        self.shplautPath = ""
        self.output = ""
        self.output_cols = 0
        self.output_rows = 0
        self.lonStartCrop = 0
        self.latStartCrop = 0
        self.lonEndCrop = 0
        self.latEndCrop = 0
        self.sun_elev = 0
        self.reflectance_mult = 0
        self.reflectance_add = 0

    def openImage4(self, path):
        print(self.TAG, "File Image Path : ", path)
        openImage = gdal.Open(path, GA_ReadOnly)
        if not openImage:
            print(self.TAG, "Type : Not Image File")
            return False
        else:
            print(self.TAG, "Type : Image File")
            self.imagePath4 = path
            self.band4 = openImage
            return True
    
    def openImage5(self, path):
        print(self.TAG, "File Image Path : ", path)
        openImage = gdal.Open(path, GA_ReadOnly)
        if not openImage:
            print(self.TAG, "Type : Not Image File")
            return False
        else:
            print(self.TAG, "Type : Image File")
            self.imagePath5 = path
            self.band5 = openImage
            return True

    def openImage6(self, path):
        print(self.TAG, "File Image Path : ", path)
        openImage = gdal.Open(path, GA_ReadOnly)
        if not openImage:
            print(self.TAG, "Type : Not Image File")
            return False
        else:
            print(self.TAG, "Type : Image File")
            self.imagePath6 = path
            self.band6 = openImage
            return True
    
    def openImageQA(self, path):
        print(self.TAG, "File Image Path : ", path)
        openImage = gdal.Open(path, GA_ReadOnly)
        if not openImage:
            self.bandQA = None
            self.imagePathQA = ""
            print(self.TAG, "Type : Not Image File")
            return False
        else:
            print(self.TAG, "Type : Image File")
            self.imagePathQA = path
            self.bandQA = openImage
            return True
    
    def openSHP(self, path):
        print(self.TAG, "File SHP Path : ", path)
        openSHP = path
        if not openSHP:
            print(self.TAG, "Type : Not SHP File")
            return False
        else:
            print(self.TAG, "Type : SHP File")
            self.shplautPath = openSHP
            return True

    def SetCropCoordinate(self, lonStart, lonEnd, latStart, latEnd):
        self.lonStartCrop = lonStart
        self.lonEndCrop = lonEnd
        self.latStartCrop = latStart
        self.latEndCrop = latEnd
    
    def SetRefParameter(self, sun, mult, add):
        self.sun_elev = float(sun)
        self.reflectance_mult = float(mult)
        self.reflectance_add = float(add)

    def setDirOutput(self, path):
        self.output = path

    def mulaiPemetaan(self):
        print("--------Memulai Pemetaan Klorofil--------")
        cols = self.band4.RasterXSize
        rows = self.band4.RasterYSize
        bands = self.band4.RasterCount
        print(cols, rows, bands)

        projj = self.band4.GetProjection()
        gt = self.band4.GetGeoTransform()
        print(gt)

        x0 = gt[0]
        y0 = gt[3]
        pwidth = gt[1]
        pheight = gt[5]
        print (x0, y0, pwidth, pheight)

        print("--------Persiapan Cropping--------")
        myProj = Proj(proj='utm', zone=50,  ellps='WGS84', datum='WGS84', units='m')
        lon, lat = myProj(x0, y0, inverse=True)
        x_utm, y_utm = myProj(lon, lat)
        print("lon: ", lon, "\nlat: ", lat)
        print("x_utm", x_utm, "\ny_utm", y_utm)

        x_crop_start, y_crop_start = myProj(self.lonStartCrop, self.latStartCrop)
        x_crop_end, y_crop_end = myProj(self.lonEndCrop, self.latEndCrop)
        print("x_mulai_crop_utm: ", x_crop_start, "\ny_mulai_crop_utm: ", y_crop_start, "\nx_akhir_crop_utm: ",x_crop_end, "\ny_akhir_crop_utm: ", y_crop_end)
        xoff = int((x_crop_start - x0) / pwidth)
        yoff = int((y_crop_start - y0) / pheight)

        print("xoff: ", xoff, "\nyoff: ", yoff)
        output_cols = int((x_crop_end - x_crop_start) / pwidth)
        output_rows = int((y_crop_end - y_crop_start) / pheight)
        print("Output_cols: ", output_cols)
        print("Output_rows: ", output_rows)
        print("Koordinat Valid.")

        print("--------Persiapan Pemetaann--------")

        data_B6_non=(self.band6.GetRasterBand(1).ReadAsArray().astype(np.float64))
        data_B5_non=(self.band5.GetRasterBand(1).ReadAsArray().astype(np.float64))
        data_B4_non=(self.band4.GetRasterBand(1).ReadAsArray().astype(np.float64))

        print((self.sun_elev))
        print((self.reflectance_mult))
        print((self.reflectance_add))

        data_B6 = np.divide(np.add(np.multiply(self.reflectance_mult, data_B6_non), self.reflectance_add), math.sin(math.radians(self.sun_elev)))
        data_B5 = np.divide(np.add(np.multiply(self.reflectance_mult, data_B5_non), self.reflectance_add), math.sin(math.radians(self.sun_elev)))
        data_B4 = np.divide(np.add(np.multiply(self.reflectance_mult, data_B4_non), self.reflectance_add), math.sin(math.radians(self.sun_elev)))

        if(self.bandQA!=None):
            print("Terdapat Band QA.")
            masker = LandsatMasker(self.bandQA.GetRasterBand(1).ReadAsArray(), collection=1)
            conf = LandsatConfidence.high
            mask = masker.get_cloud_mask(conf)
            colsBQ = self.bandQA.RasterXSize
            rowsBQ = self.bandQA.RasterYSize
            projBQ = self.bandQA.GetProjection()
            gtBQ = self.bandQA.GetGeoTransform()

            rasterSet = gdal.GetDriverByName('GTiff').Create('awan.TIF', colsBQ, rowsBQ, 1, gdal.GDT_Float32)
            rasterSet.SetProjection(projBQ)
            rasterSet.SetGeoTransform(gtBQ)
            rasterSet.GetRasterBand(1).WriteArray(mask)
            rasterSet.GetRasterBand(1).SetNoDataValue(-999)
            rasterSet = None

            awan = gdal.Open('awan.TIF', GA_ReadOnly)
            awans = awan.GetRasterBand(1).ReadAsArray().astype(np.float64)
            data_B6[awans == 1] = np.nan
            data_B5[awans == 1] = np.nan
            data_B4[awans == 1] = np.nan

        data_B6[data_B6 < 0] = np.nan
        data_B6[data_B6 > 10000] = np.nan
        data_B5[data_B5 < 0] = np.nan
        data_B5[data_B5 > 10000] = np.nan
        data_B4[data_B4 < 0] = np.nan
        data_B4[data_B4 > 10000] = np.nan
        print("Nilai Reflektan Valid.")

        print("--------Menjalankan Algoritma (Wibowo)--------")
        wibowoAlg = np.multiply(0.2818, np.power(np.divide(np.add(data_B5, data_B6), data_B4), 3.497))
        wibowoAlg[wibowoAlg < 0] = np.nan
        wibowoAlg[wibowoAlg > 10000] = np.nan
        print("Algoritma Sukses.")

        print("--------Menyimpan Hasil Algoritma (Wibowo)--------")
        rasterSet = gdal.GetDriverByName('GTiff').Create('PlotAlgoritmaWibowo.TIF' , cols, rows, 1, gdal.GDT_Float32)
        rasterSet.SetProjection(projj)
        rasterSet.SetGeoTransform(gt)
        rasterSet.GetRasterBand(1).WriteArray(wibowoAlg)
        rasterSet.GetRasterBand(1).SetNoDataValue(-999)
        rasterSet = None
        print("Tersimpan.")

        print("--------Persiapan Cleaning Algoritma (Wibowo)--------")
        wibowoHasil = gdal.Open('PlotAlgoritmaWibowo.TIF')
        gdal.Warp('CitraTanpaPulau.TIF', wibowoHasil, cutlineDSName=self.shplautPath, cropToCutline=False, dstNodata=np.nan)
        wibowoHasilPotong = gdal.Open('CitraTanpaPulau.TIF', GA_ReadOnly)
        hasilAkhir = wibowoHasilPotong.ReadAsArray(xoff, yoff, output_cols, output_rows).astype(np.float64)
        print("Citra Bersih.")

        print("--------Output Akhir--------")
        rasterSet = gdal.GetDriverByName('GTiff').Create(self.output + '\HasilAkhir.TIF', output_cols, output_rows, 1, gdal.GDT_Float32)
        rasterSet.SetProjection(projj)
        rasterSet.SetGeoTransform(gt)
        rasterSet.GetRasterBand(1).WriteArray(hasilAkhir)
        rasterSet.GetRasterBand(1).SetNoDataValue(-999)
        rasterSet = None
        print("Proses Selesai.")

        fig, ax = plt.subplots(1, figsize=(12, 10))
        ax.set_title(
            'Pemetaan Klorofil A di Selat Bali'
        )
        im = plt.imshow(hasilAkhir,cmap = plt.get_cmap('jet'), vmin=0, vmax=2)
        plt.colorbar(im)
        plt.savefig(self.output + '\Plot Klorofil A.png')
        plt.show()
        loadImage = Image.open(self.output + '\Plot Klorofil A.png')
        return loadImage