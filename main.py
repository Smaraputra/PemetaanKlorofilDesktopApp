# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
from wx.core import NO
import wx.xrc
import numpy
from PIL import Image
from pemetaanKlorofil import pemetaanKlorofil

###########################################################################
## Class FrameUtama
###########################################################################

class FrameUtama ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PROJECT UAS - 1905551095", pos = wx.DefaultPosition, size = wx.Size( 1200,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizerMain = wx.BoxSizer( wx.VERTICAL )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Pemetaan Sebaran Klorofil-A di Selat Bali", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( 14, 72, 90, 92, False, "Times New Roman" ) )
		
		bSizer41.Add( self.m_staticText4, 0, wx.ALL|wx.EXPAND, 10 )
		
		
		bSizerMain.Add( bSizer41, 0, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Input Citra Landsat" ), wx.VERTICAL )
		
		bSizer72 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer82 = wx.BoxSizer( wx.VERTICAL )
		
		self.citra_b4 = wx.StaticBitmap( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 125,125 ), 0 )
		bSizer82.Add( self.citra_b4, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer72.Add( bSizer82, 1, wx.EXPAND, 5 )
		
		bSizer102 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText523 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Citra Band 4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText523.Wrap( -1 )
		self.m_staticText523.SetFont( wx.Font( 10, 72, 90, 90, False, "Times New Roman" ) )
		
		bSizer102.Add( self.m_staticText523, 0, wx.ALL, 5 )
		
		self.ambil_band4 = wx.FilePickerCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*tif*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer102.Add( self.ambil_band4, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer72.Add( bSizer102, 1, wx.EXPAND, 5 )
		
		
		sbSizer1.Add( bSizer72, 1, wx.EXPAND, 5 )
		
		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer81 = wx.BoxSizer( wx.VERTICAL )
		
		self.citra_b5 = wx.StaticBitmap( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 125,125 ), 0 )
		bSizer81.Add( self.citra_b5, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer71.Add( bSizer81, 1, wx.EXPAND, 5 )
		
		bSizer101 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText522 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Citra Band 5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText522.Wrap( -1 )
		self.m_staticText522.SetFont( wx.Font( 10, 72, 90, 90, False, "Times New Roman" ) )
		
		bSizer101.Add( self.m_staticText522, 0, wx.ALL, 5 )
		
		self.ambil_band5 = wx.FilePickerCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*tif*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer101.Add( self.ambil_band5, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer71.Add( bSizer101, 1, wx.EXPAND, 5 )
		
		
		sbSizer1.Add( bSizer71, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.citra_b6 = wx.StaticBitmap( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 125,125 ), 0 )
		bSizer8.Add( self.citra_b6, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText52 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Citra Band 6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )
		self.m_staticText52.SetFont( wx.Font( 10, 72, 90, 90, False, "Times New Roman" ) )
		
		bSizer10.Add( self.m_staticText52, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.ambil_band6 = wx.FilePickerCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*tif*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer10.Add( self.ambil_band6, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		
		sbSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer73 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer83 = wx.BoxSizer( wx.VERTICAL )
		
		self.citra_bqa = wx.StaticBitmap( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 125,125 ), 0 )
		bSizer83.Add( self.citra_bqa, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer73.Add( bSizer83, 1, wx.EXPAND, 5 )
		
		bSizer103 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText521 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Citra Band QA (Opsional)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText521.Wrap( -1 )
		self.m_staticText521.SetFont( wx.Font( 10, 72, 90, 90, False, "Times New Roman" ) )
		
		bSizer103.Add( self.m_staticText521, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.ambil_bandqa = wx.FilePickerCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*tif*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer103.Add( self.ambil_bandqa, 0, wx.ALL, 5 )
		
		self.m_staticText17 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"*Untuk masking awan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer103.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		
		bSizer73.Add( bSizer103, 1, wx.EXPAND, 5 )
		
		
		sbSizer1.Add( bSizer73, 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( sbSizer1, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Potong Citra" ), wx.VERTICAL )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText11 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Longitude Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer16.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		
		bSizer15.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.longitude_start = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.longitude_start, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer15.Add( bSizer18, 1, wx.EXPAND, 5 )
		
		
		sbSizer5.Add( bSizer15, 0, wx.EXPAND, 5 )
		
		bSizer151 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer161 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText111 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Longitude End", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )
		bSizer161.Add( self.m_staticText111, 0, wx.ALL, 5 )
		
		
		bSizer151.Add( bSizer161, 1, wx.EXPAND, 5 )
		
		bSizer181 = wx.BoxSizer( wx.VERTICAL )
		
		self.longitude_end = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer181.Add( self.longitude_end, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer151.Add( bSizer181, 1, wx.EXPAND, 5 )
		
		
		sbSizer5.Add( bSizer151, 0, wx.EXPAND, 5 )
		
		bSizer152 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer162 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText112 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Latitude Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText112.Wrap( -1 )
		bSizer162.Add( self.m_staticText112, 0, wx.ALL, 5 )
		
		
		bSizer152.Add( bSizer162, 1, wx.EXPAND, 5 )
		
		bSizer182 = wx.BoxSizer( wx.VERTICAL )
		
		self.latitude_start = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer182.Add( self.latitude_start, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer152.Add( bSizer182, 1, wx.EXPAND, 5 )
		
		
		sbSizer5.Add( bSizer152, 0, wx.EXPAND, 5 )
		
		bSizer153 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer163 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText113 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Latitude End", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText113.Wrap( -1 )
		bSizer163.Add( self.m_staticText113, 0, wx.ALL, 5 )
		
		
		bSizer153.Add( bSizer163, 1, wx.EXPAND, 5 )
		
		bSizer183 = wx.BoxSizer( wx.VERTICAL )
		
		self.latitude_end = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer183.Add( self.latitude_end, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer153.Add( bSizer183, 1, wx.EXPAND, 5 )
		
		
		sbSizer5.Add( bSizer153, 1, wx.EXPAND, 5 )
		
		
		bSizer39.Add( sbSizer5, 0, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Variabel" ), wx.VERTICAL )
		
		bSizer154 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer164 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText114 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Sun Elevation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText114.Wrap( -1 )
		bSizer164.Add( self.m_staticText114, 0, wx.ALL, 5 )
		
		
		bSizer154.Add( bSizer164, 1, wx.EXPAND, 5 )
		
		bSizer184 = wx.BoxSizer( wx.VERTICAL )
		
		self.sun_elevation = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer184.Add( self.sun_elevation, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer154.Add( bSizer184, 1, wx.EXPAND, 5 )
		
		
		sbSizer6.Add( bSizer154, 0, wx.EXPAND, 5 )
		
		bSizer155 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer165 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText115 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Reflectance Mult", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText115.Wrap( -1 )
		bSizer165.Add( self.m_staticText115, 0, wx.ALL, 5 )
		
		
		bSizer155.Add( bSizer165, 1, wx.EXPAND, 5 )
		
		bSizer185 = wx.BoxSizer( wx.VERTICAL )
		
		self.reflectance_mult = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer185.Add( self.reflectance_mult, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer155.Add( bSizer185, 1, wx.EXPAND, 5 )
		
		
		sbSizer6.Add( bSizer155, 0, wx.EXPAND, 5 )
		
		bSizer156 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer166 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText116 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Reflectance Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText116.Wrap( -1 )
		bSizer166.Add( self.m_staticText116, 0, wx.ALL, 5 )
		
		
		bSizer156.Add( bSizer166, 1, wx.EXPAND, 5 )
		
		bSizer186 = wx.BoxSizer( wx.VERTICAL )
		
		self.reflectance_add = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer186.Add( self.reflectance_add, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer156.Add( bSizer186, 1, wx.EXPAND, 5 )
		
		
		sbSizer6.Add( bSizer156, 0, wx.EXPAND, 5 )
		
		self.m_staticText13 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"SHP Lautan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		sbSizer6.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.ambil_shp = wx.FilePickerCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*shp*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sbSizer6.Add( self.ambil_shp, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText131 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Direktori Output", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )
		sbSizer6.Add( self.m_staticText131, 0, wx.ALL, 5 )
		
		self.ambil_output = wx.DirPickerCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		sbSizer6.Add( self.ambil_output, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.start = wx.Button( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Mulai Pemetaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer6.Add( self.start, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.reset = wx.Button( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer6.Add( self.reset, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer39.Add( sbSizer6, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
		
		
		bSizer6.Add( bSizer39, 1, wx.EXPAND, 5 )
		
		bSizer34 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Hasil Pemetaan" ), wx.VERTICAL )
		
		self.citra_hasil = wx.StaticBitmap( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 500,500 ), 0 )
		sbSizer3.Add( self.citra_hasil, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer34.Add( sbSizer3, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer6.Add( bSizer34, 1, wx.EXPAND, 5 )
		
		
		bSizerMain.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizerMain )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.ambil_band4.Bind( wx.EVT_FILEPICKER_CHANGED, self.filepick_band4OnFileChanged )
		self.ambil_band5.Bind( wx.EVT_FILEPICKER_CHANGED, self.filepick_band5OnFileChanged )
		self.ambil_band6.Bind( wx.EVT_FILEPICKER_CHANGED, self.filepick_band6OnFileChanged )
		self.ambil_bandqa.Bind( wx.EVT_FILEPICKER_CHANGED, self.ambil_bandqaOnFileChanged )
		self.ambil_shp.Bind( wx.EVT_FILEPICKER_CHANGED, self.ambil_shpOnFileChanged )
		self.ambil_output.Bind( wx.EVT_DIRPICKER_CHANGED, self.dir_outputOnDirChanged )
		self.start.Bind( wx.EVT_BUTTON, self.startOnButtonClick )
		self.reset.Bind( wx.EVT_BUTTON, self.resetOnButtonClick )
	
	def __del__( self ):
		pass
	klorofil = pemetaanKlorofil()

	def resizer(self, width, height, imgs, stats):
		img = numpy.array(imgs)
		if stats:
			rgb = img * 32
			pilImage = Image.fromarray(rgb).convert("RGB")
			image = wx.Image(pilImage.size[0], pilImage.size[1])
			image.SetData(pilImage.tobytes())
		else:
			pilImage = Image.fromarray(img).convert("RGB")
			image = wx.Image(pilImage.size[0], pilImage.size[1])
			image.SetData(pilImage.tobytes())
		H = image.GetHeight()
		W = image.GetWidth()
		if (W > H):
			height = height * H / W
		else:
			width = width * W / H
		image = image.Scale(width, height)
		return image

	def showMessage(self, message):
		dialog = wx.MessageDialog(None, message, "Info", wx.OK | wx.ICON_INFORMATION)
		dialog.ShowModal()

	def showMessageError(self, message):
		dialog = wx.MessageDialog(None, message, "Error", wx.OK | wx.ICON_ERROR)
		dialog.ShowModal()
	
	# Virtual event handlers, overide them in your derived class
	def ambil_bandqaOnFileChanged( self, event ):
		newH = 120
		newW = 120
		path = event.GetPath()
		isImage4 = self.klorofil.openImageQA(path)
		if isImage4:
			loadImage = Image.open(path)
			image = self.resizer(newW, newH, loadImage, True)
			bitmapImage = wx.Bitmap(image)
			self.citra_bqa.SetBitmap(bitmapImage)
		else:
			self.showMessageError("Bukan File yang Valid!")
		event.Skip()
	
	isImage4 = None
	def filepick_band4OnFileChanged( self, event ):
		newH = 120
		newW = 120
		path = event.GetPath()
		self.isImage4 = self.klorofil.openImage4(path)
		if self.isImage4:
			loadImage = Image.open(path)
			image = self.resizer(newW, newH, loadImage, True)
			bitmapImage = wx.Bitmap(image)
			self.citra_b4.SetBitmap(bitmapImage)
		else:
			self.showMessageError("Bukan File yang Valid!")
		event.Skip()
	
	isImage5 = None
	def filepick_band5OnFileChanged( self, event ):
		newH = 120
		newW = 120
		path = event.GetPath()
		self.isImage5 = self.klorofil.openImage5(path)
		if self.isImage5:
			loadImage = Image.open(path)
			image = self.resizer(newW, newH, loadImage, True)
			bitmapImage = wx.Bitmap(image)
			self.citra_b5.SetBitmap(bitmapImage)
		else:
			self.showMessageError("Bukan File yang Valid!")
		event.Skip()
	
	isImage6 = None
	def filepick_band6OnFileChanged( self, event ):
		newH = 120
		newW = 120
		path = event.GetPath()
		self.isImage6 = self.klorofil.openImage6(path)
		if self.isImage6:
			loadImage = Image.open(path)
			image = self.resizer(newW, newH, loadImage, True)
			bitmapImage = wx.Bitmap(image)
			self.citra_b6.SetBitmap(bitmapImage)
		else:
			self.showMessageError("Bukan File yang Valid!")
		event.Skip()
	
	isSHP = None
	def ambil_shpOnFileChanged( self, event ):
		path = event.GetPath()
		self.isSHP = self.klorofil.openSHP(path)
		if not self.isSHP:
			self.showMessageError("Bukan File SHP!")
		else:
			self.isSHP = True
		event.Skip()
	
	isOut = None
	def dir_outputOnDirChanged( self, event ):
		path = event.GetPath()
		self.klorofil.setDirOutput(path)
		self.isOut = True
		event.Skip()
	
	def resetOnButtonClick( self, event ):
		self.ambil_band4.SetPath("")
		self.ambil_band5.SetPath("")
		self.ambil_band6.SetPath("")
		self.ambil_bandqa.SetPath("")
		self.ambil_shp.SetPath("")
		self.ambil_output.SetPath("")

		bmp1 = wx.EmptyBitmapRGBA(500, 500, red=255, green=255, blue=255, alpha=1)
		bmp2 = wx.EmptyBitmapRGBA(120, 120, red=255, green=255, blue=255, alpha=1)
		self.citra_bqa.SetBitmap(bmp2)
		self.citra_b6.SetBitmap(bmp2)
		self.citra_b5.SetBitmap(bmp2)
		self.citra_b4.SetBitmap(bmp2)
		self.citra_hasil.SetBitmap(bmp1)

		self.isImage4 = None
		self.isImage5 = None
		self.isImage6 = None
		self.isSHP = None

		self.longitude_end.Clear()
		self.longitude_start.Clear()
		self.latitude_end.Clear()
		self.latitude_start.Clear()
		self.sun_elevation.Clear()
		self.reflectance_add.Clear()
		self.reflectance_mult.Clear()

		self.klorofil.reset()
		event.Skip()
	
	def startOnButtonClick( self, event ):
		if(self.isOut and self.isSHP and self.isImage6 and self.isImage5 and self.isImage4):
			longstart = self.longitude_start.GetValue()
			longend = self.longitude_end.GetValue()
			latstart = self.latitude_start.GetValue()
			latend = self.latitude_end.GetValue()
			sun_elev = self.sun_elevation.GetValue()
			ref_add = self.reflectance_add.GetValue()
			ref_mult = self.reflectance_mult.GetValue()
			if((longstart is None or longstart=='') or (longend is None or longend=='') or (latstart is None or latstart=='') or (latend is None or latend=='') or (sun_elev is None or sun_elev=='') or (ref_add is None or ref_add=='') or (ref_mult is None or ref_mult=='')):
				self.showMessageError("Parameter Kurang/Salah!")
			else:
				newH = 500
				newW = 500
				self.klorofil.SetCropCoordinate(longstart, longend, latstart, latend)
				self.klorofil.SetRefParameter(sun_elev, ref_mult, ref_add)
				images = self.klorofil.mulaiPemetaan()
				image = self.resizer(newW, newH, images, False)
				bitmapImage = wx.Bitmap(image)
				self.citra_hasil.SetBitmap(bitmapImage)
		else:
			self.showMessageError("Input Belum Lengkap!")
		event.Skip()
	
class MainApp(wx.App) :
   def OnInit(self):
        mainFrame = FrameUtama(None)
        mainFrame.Show(True)
        return True

if __name__ == '__main__':
        app = MainApp()
        app.MainLoop()