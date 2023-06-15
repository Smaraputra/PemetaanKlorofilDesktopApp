----------------------------------------------------------------------------
-- Lua code generated with wxFormBuilder (version Jun 17 2015)
-- http://www.wxformbuilder.org/
----------------------------------------------------------------------------

-- Load the wxLua module, does nothing if running from wxLua, wxLuaFreeze, or wxLuaEdit
package.cpath = package.cpath..";./?.dll;./?.so;../lib/?.so;../lib/vc_dll/?.dll;../lib/bcc_dll/?.dll;../lib/mingw_dll/?.dll;"
require("wx")

UI = {}


-- create FrameUtama
UI.FrameUtama = wx.wxFrame (wx.NULL, wx.wxID_ANY, "PROJECT UAS - 1905551095", wx.wxDefaultPosition, wx.wxSize( 1200,720 ), wx.wxDEFAULT_FRAME_STYLE+wx.wxTAB_TRAVERSAL )
	UI.FrameUtama:SetSizeHints( wx.wxDefaultSize, wx.wxDefaultSize )
	UI.FrameUtama :SetBackgroundColour( wx.wxSystemSettings.GetColour( wx.wxSYS_COLOUR_WINDOW ) )
	
	UI.bSizerMain = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.bSizer41 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.m_staticText4 = wx.wxStaticText( UI.FrameUtama, wx.wxID_ANY, "Pemetaan Sebaran Klorofil-A di Selat Bali", wx.wxDefaultPosition, wx.wxDefaultSize, wx.wxALIGN_CENTRE )
	UI.m_staticText4:Wrap( -1 )
	UI.m_staticText4:SetFont( wx.wxFont( 14, 72, 90, 92, False, "Times New Roman" ) )
	
	UI.bSizer41:Add( UI.m_staticText4, 0, wx.wxALL + wx.wxEXPAND, 10 )
	
	
	UI.bSizerMain:Add( UI.bSizer41, 0, wx.wxEXPAND, 5 )
	
	UI.bSizer6 = wx.wxBoxSizer( wx.wxHORIZONTAL )
	
	UI.sbSizer1 = wx.wxStaticBoxSizer( wx.wxStaticBox( UI.FrameUtama, wx.wxID_ANY, "Input Citra Landsat" ), wx.wxVERTICAL )
	
	UI.bSizer72 = wx.wxBoxSizer( wx.wxHORIZONTAL )
	
	UI.bSizer82 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.citra_b4 = wx.wxStaticBitmap( UI.sbSizer1:GetStaticBox(), wx.wxID_ANY, wx.wxNullBitmap, wx.wxDefaultPosition, wx.wxSize( 125,125 ), 0 )
	UI.bSizer82:Add( UI.citra_b4, 1, wx.wxALL + wx.wxEXPAND, 5 )
	
	
	UI.bSizer72:Add( UI.bSizer82, 1, wx.wxEXPAND, 5 )
	
	UI.bSizer102 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.m_staticText523 = wx.wxStaticText( UI.sbSizer1:GetStaticBox(), wx.wxID_ANY, "Citra Band 4", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_staticText523:Wrap( -1 )
	UI.m_staticText523:SetFont( wx.wxFont( 10, 72, 90, 90, False, "Times New Roman" ) )
	
	UI.bSizer102:Add( UI.m_staticText523, 0, wx.wxALL, 5 )
	
	UI.ambil_band4 = wx.wxFilePickerCtrl( UI.sbSizer1:GetStaticBox(), wx.wxID_ANY, "", "Select a file", "*tif*", wx.wxDefaultPosition, wx.wxDefaultSize, wx.wxFLP_DEFAULT_STYLE )
	UI.bSizer102:Add( UI.ambil_band4, 0, wx.wxALL + wx.wxEXPAND, 5 )
	
	
	UI.bSizer72:Add( UI.bSizer102, 1, wx.wxEXPAND, 5 )
	
	
	UI.sbSizer1:Add( UI.bSizer72, 1, wx.wxEXPAND, 5 )
	
	UI.bSizer71 = wx.wxBoxSizer( wx.wxHORIZONTAL )
	
	UI.bSizer81 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.citra_b5 = wx.wxStaticBitmap( UI.sbSizer1:GetStaticBox(), wx.wxID_ANY, wx.wxNullBitmap, wx.wxDefaultPosition, wx.wxSize( 125,125 ), 0 )
	UI.bSizer81:Add( UI.citra_b5, 1, wx.wxALL + wx.wxEXPAND, 5 )
	
	
	UI.bSizer71:Add( UI.bSizer81, 1, wx.wxEXPAND, 5 )
	
	UI.bSizer101 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.m_staticText522 = wx.wxStaticText( UI.sbSizer1:GetStaticBox(), wx.wxID_ANY, "Citra Band 5", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_staticText522:Wrap( -1 )
	UI.m_staticText522:SetFont( wx.wxFont( 10, 72, 90, 90, False, "Times New Roman" ) )
	
	UI.bSizer101:Add( UI.m_staticText522, 0, wx.wxALL, 5 )
	
	UI.ambil_band5 = wx.wxFilePickerCtrl( UI.sbSizer1:GetStaticBox(), wx.wxID_ANY, "", "Select a file", "*tif*", wx.wxDefaultPosition, wx.wxDefaultSize, wx.wxFLP_DEFAULT_STYLE )
	UI.bSizer101:Add( UI.ambil_band5, 0, wx.wxALL + wx.wxEXPAND, 5 )
	
	
	UI.bSizer71:Add( UI.bSizer101, 1, wx.wxEXPAND, 5 )
	
	
	UI.sbSizer1:Add( UI.bSizer71, 1, wx.wxEXPAND, 5 )
	
	UI.bSizer7 = wx.wxBoxSizer( wx.wxHORIZONTAL )
	
	UI.bSizer8 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.citra_b6 = wx.wxStaticBitmap( UI.sbSizer1:GetStaticBox(), wx.wxID_ANY, wx.wxNullBitmap, wx.wxDefaultPosition, wx.wxSize( 125,125 ), 0 )
	UI.bSizer8:Add( UI.citra_b6, 1, wx.wxALL + wx.wxEXPAND, 5 )
	
	
	UI.bSizer7:Add( UI.bSizer8, 1, wx.wxEXPAND, 5 )
	
	UI.bSizer10 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.m_staticText52 = wx.wxStaticText( UI.sbSizer1:GetStaticBox(), wx.wxID_ANY, "Citra Band 6", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_staticText52:Wrap( -1 )
	UI.m_staticText52:SetFont( wx.wxFont( 10, 72, 90, 90, False, "Times New Roman" ) )
	
	UI.bSizer10:Add( UI.m_staticText52, 0, wx.wxALL + wx.wxEXPAND, 5 )
	
	UI.ambil_band6 = wx.wxFilePickerCtrl( UI.sbSizer1:GetStaticBox(), wx.wxID_ANY, "", "Select a file", "*tif*", wx.wxDefaultPosition, wx.wxDefaultSize, wx.wxFLP_DEFAULT_STYLE )
	UI.bSizer10:Add( UI.ambil_band6, 0, wx.wxALL, 5 )
	
	
	UI.bSizer7:Add( UI.bSizer10, 1, wx.wxEXPAND, 5 )
	
	
	UI.sbSizer1:Add( UI.bSizer7, 1, wx.wxEXPAND, 5 )
	
	UI.bSizer73 = wx.wxBoxSizer( wx.wxHORIZONTAL )
	
	UI.bSizer83 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.citra_bqa = wx.wxStaticBitmap( UI.sbSizer1:GetStaticBox(), wx.wxID_ANY, wx.wxNullBitmap, wx.wxDefaultPosition, wx.wxSize( 125,125 ), 0 )
	UI.bSizer83:Add( UI.citra_bqa, 1, wx.wxALL + wx.wxEXPAND, 5 )
	
	
	UI.bSizer73:Add( UI.bSizer83, 1, wx.wxEXPAND, 5 )
	
	UI.bSizer103 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.m_staticText521 = wx.wxStaticText( UI.sbSizer1:GetStaticBox(), wx.wxID_ANY, "Citra Band QA (Opsional)", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_staticText521:Wrap( -1 )
	UI.m_staticText521:SetFont( wx.wxFont( 10, 72, 90, 90, False, "Times New Roman" ) )
	
	UI.bSizer103:Add( UI.m_staticText521, 0, wx.wxALL + wx.wxEXPAND, 5 )
	
	UI.ambil_bandqa = wx.wxFilePickerCtrl( UI.sbSizer1:GetStaticBox(), wx.wxID_ANY, "", "Select a file", "*tif*", wx.wxDefaultPosition, wx.wxDefaultSize, wx.wxFLP_DEFAULT_STYLE )
	UI.bSizer103:Add( UI.ambil_bandqa, 0, wx.wxALL, 5 )
	
	UI.m_staticText17 = wx.wxStaticText( UI.sbSizer1:GetStaticBox(), wx.wxID_ANY, "*Untuk masking awan", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_staticText17:Wrap( -1 )
	UI.bSizer103:Add( UI.m_staticText17, 0, wx.wxALL, 5 )
	
	
	UI.bSizer73:Add( UI.bSizer103, 1, wx.wxEXPAND, 5 )
	
	
	UI.sbSizer1:Add( UI.bSizer73, 1, wx.wxEXPAND, 5 )
	
	
	UI.bSizer6:Add( UI.sbSizer1, 1, wx.wxALL + wx.wxEXPAND, 5 )
	
	UI.bSizer39 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.sbSizer5 = wx.wxStaticBoxSizer( wx.wxStaticBox( UI.FrameUtama, wx.wxID_ANY, "Potong Citra" ), wx.wxVERTICAL )
	
	UI.bSizer15 = wx.wxBoxSizer( wx.wxHORIZONTAL )
	
	UI.bSizer16 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.m_staticText11 = wx.wxStaticText( UI.sbSizer5:GetStaticBox(), wx.wxID_ANY, "Longitude Start", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_staticText11:Wrap( -1 )
	UI.bSizer16:Add( UI.m_staticText11, 0, wx.wxALL, 5 )
	
	
	UI.bSizer15:Add( UI.bSizer16, 1, wx.wxEXPAND, 5 )
	
	UI.bSizer18 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.longitude_start = wx.wxTextCtrl( UI.sbSizer5:GetStaticBox(), wx.wxID_ANY, "", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.bSizer18:Add( UI.longitude_start, 0, wx.wxALL + wx.wxEXPAND, 5 )
	
	
	UI.bSizer15:Add( UI.bSizer18, 1, wx.wxEXPAND, 5 )
	
	
	UI.sbSizer5:Add( UI.bSizer15, 0, wx.wxEXPAND, 5 )
	
	UI.bSizer151 = wx.wxBoxSizer( wx.wxHORIZONTAL )
	
	UI.bSizer161 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.m_staticText111 = wx.wxStaticText( UI.sbSizer5:GetStaticBox(), wx.wxID_ANY, "Longitude End", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_staticText111:Wrap( -1 )
	UI.bSizer161:Add( UI.m_staticText111, 0, wx.wxALL, 5 )
	
	
	UI.bSizer151:Add( UI.bSizer161, 1, wx.wxEXPAND, 5 )
	
	UI.bSizer181 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.longitude_end = wx.wxTextCtrl( UI.sbSizer5:GetStaticBox(), wx.wxID_ANY, "", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.bSizer181:Add( UI.longitude_end, 0, wx.wxALL + wx.wxEXPAND, 5 )
	
	
	UI.bSizer151:Add( UI.bSizer181, 1, wx.wxEXPAND, 5 )
	
	
	UI.sbSizer5:Add( UI.bSizer151, 0, wx.wxEXPAND, 5 )
	
	UI.bSizer152 = wx.wxBoxSizer( wx.wxHORIZONTAL )
	
	UI.bSizer162 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.m_staticText112 = wx.wxStaticText( UI.sbSizer5:GetStaticBox(), wx.wxID_ANY, "Latitude Start", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_staticText112:Wrap( -1 )
	UI.bSizer162:Add( UI.m_staticText112, 0, wx.wxALL, 5 )
	
	
	UI.bSizer152:Add( UI.bSizer162, 1, wx.wxEXPAND, 5 )
	
	UI.bSizer182 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.latitude_start = wx.wxTextCtrl( UI.sbSizer5:GetStaticBox(), wx.wxID_ANY, "", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.bSizer182:Add( UI.latitude_start, 0, wx.wxALL + wx.wxEXPAND, 5 )
	
	
	UI.bSizer152:Add( UI.bSizer182, 1, wx.wxEXPAND, 5 )
	
	
	UI.sbSizer5:Add( UI.bSizer152, 0, wx.wxEXPAND, 5 )
	
	UI.bSizer153 = wx.wxBoxSizer( wx.wxHORIZONTAL )
	
	UI.bSizer163 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.m_staticText113 = wx.wxStaticText( UI.sbSizer5:GetStaticBox(), wx.wxID_ANY, "Latitude End", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_staticText113:Wrap( -1 )
	UI.bSizer163:Add( UI.m_staticText113, 0, wx.wxALL, 5 )
	
	
	UI.bSizer153:Add( UI.bSizer163, 1, wx.wxEXPAND, 5 )
	
	UI.bSizer183 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.latitude_end = wx.wxTextCtrl( UI.sbSizer5:GetStaticBox(), wx.wxID_ANY, "", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.bSizer183:Add( UI.latitude_end, 0, wx.wxALL + wx.wxEXPAND, 5 )
	
	
	UI.bSizer153:Add( UI.bSizer183, 1, wx.wxEXPAND, 5 )
	
	
	UI.sbSizer5:Add( UI.bSizer153, 1, wx.wxEXPAND, 5 )
	
	
	UI.bSizer39:Add( UI.sbSizer5, 0, wx.wxEXPAND + wx.wxLEFT + wx.wxRIGHT + wx.wxTOP, 5 )
	
	UI.sbSizer6 = wx.wxStaticBoxSizer( wx.wxStaticBox( UI.FrameUtama, wx.wxID_ANY, "Variabel" ), wx.wxVERTICAL )
	
	UI.bSizer154 = wx.wxBoxSizer( wx.wxHORIZONTAL )
	
	UI.bSizer164 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.m_staticText114 = wx.wxStaticText( UI.sbSizer6:GetStaticBox(), wx.wxID_ANY, "Sun Elevation", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_staticText114:Wrap( -1 )
	UI.bSizer164:Add( UI.m_staticText114, 0, wx.wxALL, 5 )
	
	
	UI.bSizer154:Add( UI.bSizer164, 1, wx.wxEXPAND, 5 )
	
	UI.bSizer184 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.sun_elevation = wx.wxTextCtrl( UI.sbSizer6:GetStaticBox(), wx.wxID_ANY, "", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.bSizer184:Add( UI.sun_elevation, 0, wx.wxALL + wx.wxEXPAND, 5 )
	
	
	UI.bSizer154:Add( UI.bSizer184, 1, wx.wxEXPAND, 5 )
	
	
	UI.sbSizer6:Add( UI.bSizer154, 0, wx.wxEXPAND, 5 )
	
	UI.bSizer155 = wx.wxBoxSizer( wx.wxHORIZONTAL )
	
	UI.bSizer165 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.m_staticText115 = wx.wxStaticText( UI.sbSizer6:GetStaticBox(), wx.wxID_ANY, "Reflectance Mult", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_staticText115:Wrap( -1 )
	UI.bSizer165:Add( UI.m_staticText115, 0, wx.wxALL, 5 )
	
	
	UI.bSizer155:Add( UI.bSizer165, 1, wx.wxEXPAND, 5 )
	
	UI.bSizer185 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.reflectance_mult = wx.wxTextCtrl( UI.sbSizer6:GetStaticBox(), wx.wxID_ANY, "", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.bSizer185:Add( UI.reflectance_mult, 0, wx.wxALL + wx.wxEXPAND, 5 )
	
	
	UI.bSizer155:Add( UI.bSizer185, 1, wx.wxEXPAND, 5 )
	
	
	UI.sbSizer6:Add( UI.bSizer155, 0, wx.wxEXPAND, 5 )
	
	UI.bSizer156 = wx.wxBoxSizer( wx.wxHORIZONTAL )
	
	UI.bSizer166 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.m_staticText116 = wx.wxStaticText( UI.sbSizer6:GetStaticBox(), wx.wxID_ANY, "Reflectance Add", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_staticText116:Wrap( -1 )
	UI.bSizer166:Add( UI.m_staticText116, 0, wx.wxALL, 5 )
	
	
	UI.bSizer156:Add( UI.bSizer166, 1, wx.wxEXPAND, 5 )
	
	UI.bSizer186 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.reflectance_add = wx.wxTextCtrl( UI.sbSizer6:GetStaticBox(), wx.wxID_ANY, "", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.bSizer186:Add( UI.reflectance_add, 0, wx.wxALL + wx.wxEXPAND, 5 )
	
	
	UI.bSizer156:Add( UI.bSizer186, 1, wx.wxEXPAND, 5 )
	
	
	UI.sbSizer6:Add( UI.bSizer156, 0, wx.wxEXPAND, 5 )
	
	UI.m_staticText13 = wx.wxStaticText( UI.sbSizer6:GetStaticBox(), wx.wxID_ANY, "SHP Lautan", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_staticText13:Wrap( -1 )
	UI.sbSizer6:Add( UI.m_staticText13, 0, wx.wxALL, 5 )
	
	UI.ambil_shp = wx.wxFilePickerCtrl( UI.sbSizer6:GetStaticBox(), wx.wxID_ANY, "", "Select a file", "*shp*", wx.wxDefaultPosition, wx.wxDefaultSize, wx.wxFLP_DEFAULT_STYLE )
	UI.sbSizer6:Add( UI.ambil_shp, 0, wx.wxALL + wx.wxEXPAND, 5 )
	
	UI.m_staticText131 = wx.wxStaticText( UI.sbSizer6:GetStaticBox(), wx.wxID_ANY, "Direktori Output", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_staticText131:Wrap( -1 )
	UI.sbSizer6:Add( UI.m_staticText131, 0, wx.wxALL, 5 )
	
	UI.ambil_output = wx.wxDirPickerCtrl( UI.sbSizer6:GetStaticBox(), wx.wxID_ANY, "", "Select a folder", wx.wxDefaultPosition, wx.wxDefaultSize, wx.wxDIRP_DEFAULT_STYLE )
	UI.sbSizer6:Add( UI.ambil_output, 0, wx.wxALL + wx.wxEXPAND, 5 )
	
	UI.start = wx.wxButton( UI.sbSizer6:GetStaticBox(), wx.wxID_ANY, "Mulai Pemetaan", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.sbSizer6:Add( UI.start, 1, wx.wxALL + wx.wxEXPAND, 5 )
	
	UI.reset = wx.wxButton( UI.sbSizer6:GetStaticBox(), wx.wxID_ANY, "Reset", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.sbSizer6:Add( UI.reset, 0, wx.wxALL + wx.wxEXPAND, 5 )
	
	
	UI.bSizer39:Add( UI.sbSizer6, 1, wx.wxBOTTOM + wx.wxEXPAND + wx.wxLEFT + wx.wxRIGHT + wx.wxTOP, 5 )
	
	
	UI.bSizer6:Add( UI.bSizer39, 1, wx.wxEXPAND, 5 )
	
	UI.bSizer34 = wx.wxBoxSizer( wx.wxVERTICAL )
	
	UI.sbSizer3 = wx.wxStaticBoxSizer( wx.wxStaticBox( UI.FrameUtama, wx.wxID_ANY, "Hasil Pemetaan" ), wx.wxVERTICAL )
	
	UI.citra_hasil = wx.wxStaticBitmap( UI.sbSizer3:GetStaticBox(), wx.wxID_ANY, wx.wxNullBitmap, wx.wxDefaultPosition, wx.wxSize( 450,450 ), 0 )
	UI.sbSizer3:Add( UI.citra_hasil, 1, wx.wxALL + wx.wxEXPAND, 5 )
	
	
	UI.bSizer34:Add( UI.sbSizer3, 1, wx.wxALL + wx.wxEXPAND, 5 )
	
	
	UI.bSizer6:Add( UI.bSizer34, 1, wx.wxEXPAND, 5 )
	
	
	UI.bSizerMain:Add( UI.bSizer6, 1, wx.wxEXPAND, 5 )
	
	
	UI.FrameUtama:SetSizer( UI.bSizerMain )
	UI.FrameUtama:Layout()
	
	UI.FrameUtama:Centre( wx.wxBOTH )
	
	-- Connect Events
	
	UI.ambil_band4:Connect( wx.wxEVT_COMMAND_FILEPICKER_CHANGED, function(event)
	--implements filepick_band4OnFileChanged
	
	event:Skip()
	end )
	
	UI.ambil_band5:Connect( wx.wxEVT_COMMAND_FILEPICKER_CHANGED, function(event)
	--implements filepick_band5OnFileChanged
	
	event:Skip()
	end )
	
	UI.ambil_band6:Connect( wx.wxEVT_COMMAND_FILEPICKER_CHANGED, function(event)
	--implements filepick_band6OnFileChanged
	
	event:Skip()
	end )
	
	UI.ambil_bandqa:Connect( wx.wxEVT_COMMAND_FILEPICKER_CHANGED, function(event)
	--implements ambil_bandqaOnFileChanged
	
	event:Skip()
	end )
	
	UI.ambil_shp:Connect( wx.wxEVT_COMMAND_FILEPICKER_CHANGED, function(event)
	--implements ambil_shpOnFileChanged
	
	event:Skip()
	end )
	
	UI.ambil_output:Connect( wx.wxEVT_COMMAND_DIRPICKER_CHANGED, function(event)
	--implements dir_outputOnDirChanged
	
	event:Skip()
	end )
	
	UI.start:Connect( wx.wxEVT_COMMAND_BUTTON_CLICKED, function(event)
	--implements startOnButtonClick
	
	event:Skip()
	end )
	
	UI.reset:Connect( wx.wxEVT_COMMAND_BUTTON_CLICKED, function(event)
	--implements resetOnButtonClick
	
	event:Skip()
	end )
	


--wx.wxGetApp():MainLoop()
