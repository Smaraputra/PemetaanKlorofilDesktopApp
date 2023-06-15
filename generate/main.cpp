///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun 17 2015)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "main.h"

///////////////////////////////////////////////////////////////////////////

FrameUtama::FrameUtama( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	this->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_WINDOW ) );
	
	wxBoxSizer* bSizerMain;
	bSizerMain = new wxBoxSizer( wxVERTICAL );
	
	wxBoxSizer* bSizer41;
	bSizer41 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText4 = new wxStaticText( this, wxID_ANY, wxT("Pemetaan Sebaran Klorofil-A di Selat Bali"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE );
	m_staticText4->Wrap( -1 );
	m_staticText4->SetFont( wxFont( 14, 72, 90, 92, false, wxT("Times New Roman") ) );
	
	bSizer41->Add( m_staticText4, 0, wxALL|wxEXPAND, 10 );
	
	
	bSizerMain->Add( bSizer41, 0, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer6;
	bSizer6 = new wxBoxSizer( wxHORIZONTAL );
	
	wxStaticBoxSizer* sbSizer1;
	sbSizer1 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("Input Citra Landsat") ), wxVERTICAL );
	
	wxBoxSizer* bSizer72;
	bSizer72 = new wxBoxSizer( wxHORIZONTAL );
	
	wxBoxSizer* bSizer82;
	bSizer82 = new wxBoxSizer( wxVERTICAL );
	
	citra_b4 = new wxStaticBitmap( sbSizer1->GetStaticBox(), wxID_ANY, wxNullBitmap, wxDefaultPosition, wxSize( 125,125 ), 0 );
	bSizer82->Add( citra_b4, 1, wxALL|wxEXPAND, 5 );
	
	
	bSizer72->Add( bSizer82, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer102;
	bSizer102 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText523 = new wxStaticText( sbSizer1->GetStaticBox(), wxID_ANY, wxT("Citra Band 4"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText523->Wrap( -1 );
	m_staticText523->SetFont( wxFont( 10, 72, 90, 90, false, wxT("Times New Roman") ) );
	
	bSizer102->Add( m_staticText523, 0, wxALL, 5 );
	
	ambil_band4 = new wxFilePickerCtrl( sbSizer1->GetStaticBox(), wxID_ANY, wxEmptyString, wxT("Select a file"), wxT("*tif*"), wxDefaultPosition, wxDefaultSize, wxFLP_DEFAULT_STYLE );
	bSizer102->Add( ambil_band4, 0, wxALL|wxEXPAND, 5 );
	
	
	bSizer72->Add( bSizer102, 1, wxEXPAND, 5 );
	
	
	sbSizer1->Add( bSizer72, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer71;
	bSizer71 = new wxBoxSizer( wxHORIZONTAL );
	
	wxBoxSizer* bSizer81;
	bSizer81 = new wxBoxSizer( wxVERTICAL );
	
	citra_b5 = new wxStaticBitmap( sbSizer1->GetStaticBox(), wxID_ANY, wxNullBitmap, wxDefaultPosition, wxSize( 125,125 ), 0 );
	bSizer81->Add( citra_b5, 1, wxALL|wxEXPAND, 5 );
	
	
	bSizer71->Add( bSizer81, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer101;
	bSizer101 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText522 = new wxStaticText( sbSizer1->GetStaticBox(), wxID_ANY, wxT("Citra Band 5"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText522->Wrap( -1 );
	m_staticText522->SetFont( wxFont( 10, 72, 90, 90, false, wxT("Times New Roman") ) );
	
	bSizer101->Add( m_staticText522, 0, wxALL, 5 );
	
	ambil_band5 = new wxFilePickerCtrl( sbSizer1->GetStaticBox(), wxID_ANY, wxEmptyString, wxT("Select a file"), wxT("*tif*"), wxDefaultPosition, wxDefaultSize, wxFLP_DEFAULT_STYLE );
	bSizer101->Add( ambil_band5, 0, wxALL|wxEXPAND, 5 );
	
	
	bSizer71->Add( bSizer101, 1, wxEXPAND, 5 );
	
	
	sbSizer1->Add( bSizer71, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer7;
	bSizer7 = new wxBoxSizer( wxHORIZONTAL );
	
	wxBoxSizer* bSizer8;
	bSizer8 = new wxBoxSizer( wxVERTICAL );
	
	citra_b6 = new wxStaticBitmap( sbSizer1->GetStaticBox(), wxID_ANY, wxNullBitmap, wxDefaultPosition, wxSize( 125,125 ), 0 );
	bSizer8->Add( citra_b6, 1, wxALL|wxEXPAND, 5 );
	
	
	bSizer7->Add( bSizer8, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer10;
	bSizer10 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText52 = new wxStaticText( sbSizer1->GetStaticBox(), wxID_ANY, wxT("Citra Band 6"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText52->Wrap( -1 );
	m_staticText52->SetFont( wxFont( 10, 72, 90, 90, false, wxT("Times New Roman") ) );
	
	bSizer10->Add( m_staticText52, 0, wxALL|wxEXPAND, 5 );
	
	ambil_band6 = new wxFilePickerCtrl( sbSizer1->GetStaticBox(), wxID_ANY, wxEmptyString, wxT("Select a file"), wxT("*tif*"), wxDefaultPosition, wxDefaultSize, wxFLP_DEFAULT_STYLE );
	bSizer10->Add( ambil_band6, 0, wxALL, 5 );
	
	
	bSizer7->Add( bSizer10, 1, wxEXPAND, 5 );
	
	
	sbSizer1->Add( bSizer7, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer73;
	bSizer73 = new wxBoxSizer( wxHORIZONTAL );
	
	wxBoxSizer* bSizer83;
	bSizer83 = new wxBoxSizer( wxVERTICAL );
	
	citra_bqa = new wxStaticBitmap( sbSizer1->GetStaticBox(), wxID_ANY, wxNullBitmap, wxDefaultPosition, wxSize( 125,125 ), 0 );
	bSizer83->Add( citra_bqa, 1, wxALL|wxEXPAND, 5 );
	
	
	bSizer73->Add( bSizer83, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer103;
	bSizer103 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText521 = new wxStaticText( sbSizer1->GetStaticBox(), wxID_ANY, wxT("Citra Band QA (Opsional)"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText521->Wrap( -1 );
	m_staticText521->SetFont( wxFont( 10, 72, 90, 90, false, wxT("Times New Roman") ) );
	
	bSizer103->Add( m_staticText521, 0, wxALL|wxEXPAND, 5 );
	
	ambil_bandqa = new wxFilePickerCtrl( sbSizer1->GetStaticBox(), wxID_ANY, wxEmptyString, wxT("Select a file"), wxT("*tif*"), wxDefaultPosition, wxDefaultSize, wxFLP_DEFAULT_STYLE );
	bSizer103->Add( ambil_bandqa, 0, wxALL, 5 );
	
	m_staticText17 = new wxStaticText( sbSizer1->GetStaticBox(), wxID_ANY, wxT("*Untuk masking awan"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText17->Wrap( -1 );
	bSizer103->Add( m_staticText17, 0, wxALL, 5 );
	
	
	bSizer73->Add( bSizer103, 1, wxEXPAND, 5 );
	
	
	sbSizer1->Add( bSizer73, 1, wxEXPAND, 5 );
	
	
	bSizer6->Add( sbSizer1, 1, wxALL|wxEXPAND, 5 );
	
	wxBoxSizer* bSizer39;
	bSizer39 = new wxBoxSizer( wxVERTICAL );
	
	wxStaticBoxSizer* sbSizer5;
	sbSizer5 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("Potong Citra") ), wxVERTICAL );
	
	wxBoxSizer* bSizer15;
	bSizer15 = new wxBoxSizer( wxHORIZONTAL );
	
	wxBoxSizer* bSizer16;
	bSizer16 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText11 = new wxStaticText( sbSizer5->GetStaticBox(), wxID_ANY, wxT("Longitude Start"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText11->Wrap( -1 );
	bSizer16->Add( m_staticText11, 0, wxALL, 5 );
	
	
	bSizer15->Add( bSizer16, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer18;
	bSizer18 = new wxBoxSizer( wxVERTICAL );
	
	longitude_start = new wxTextCtrl( sbSizer5->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer18->Add( longitude_start, 0, wxALL|wxEXPAND, 5 );
	
	
	bSizer15->Add( bSizer18, 1, wxEXPAND, 5 );
	
	
	sbSizer5->Add( bSizer15, 0, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer151;
	bSizer151 = new wxBoxSizer( wxHORIZONTAL );
	
	wxBoxSizer* bSizer161;
	bSizer161 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText111 = new wxStaticText( sbSizer5->GetStaticBox(), wxID_ANY, wxT("Longitude End"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText111->Wrap( -1 );
	bSizer161->Add( m_staticText111, 0, wxALL, 5 );
	
	
	bSizer151->Add( bSizer161, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer181;
	bSizer181 = new wxBoxSizer( wxVERTICAL );
	
	longitude_end = new wxTextCtrl( sbSizer5->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer181->Add( longitude_end, 0, wxALL|wxEXPAND, 5 );
	
	
	bSizer151->Add( bSizer181, 1, wxEXPAND, 5 );
	
	
	sbSizer5->Add( bSizer151, 0, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer152;
	bSizer152 = new wxBoxSizer( wxHORIZONTAL );
	
	wxBoxSizer* bSizer162;
	bSizer162 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText112 = new wxStaticText( sbSizer5->GetStaticBox(), wxID_ANY, wxT("Latitude Start"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText112->Wrap( -1 );
	bSizer162->Add( m_staticText112, 0, wxALL, 5 );
	
	
	bSizer152->Add( bSizer162, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer182;
	bSizer182 = new wxBoxSizer( wxVERTICAL );
	
	latitude_start = new wxTextCtrl( sbSizer5->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer182->Add( latitude_start, 0, wxALL|wxEXPAND, 5 );
	
	
	bSizer152->Add( bSizer182, 1, wxEXPAND, 5 );
	
	
	sbSizer5->Add( bSizer152, 0, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer153;
	bSizer153 = new wxBoxSizer( wxHORIZONTAL );
	
	wxBoxSizer* bSizer163;
	bSizer163 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText113 = new wxStaticText( sbSizer5->GetStaticBox(), wxID_ANY, wxT("Latitude End"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText113->Wrap( -1 );
	bSizer163->Add( m_staticText113, 0, wxALL, 5 );
	
	
	bSizer153->Add( bSizer163, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer183;
	bSizer183 = new wxBoxSizer( wxVERTICAL );
	
	latitude_end = new wxTextCtrl( sbSizer5->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer183->Add( latitude_end, 0, wxALL|wxEXPAND, 5 );
	
	
	bSizer153->Add( bSizer183, 1, wxEXPAND, 5 );
	
	
	sbSizer5->Add( bSizer153, 1, wxEXPAND, 5 );
	
	
	bSizer39->Add( sbSizer5, 0, wxEXPAND|wxLEFT|wxRIGHT|wxTOP, 5 );
	
	wxStaticBoxSizer* sbSizer6;
	sbSizer6 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("Variabel") ), wxVERTICAL );
	
	wxBoxSizer* bSizer154;
	bSizer154 = new wxBoxSizer( wxHORIZONTAL );
	
	wxBoxSizer* bSizer164;
	bSizer164 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText114 = new wxStaticText( sbSizer6->GetStaticBox(), wxID_ANY, wxT("Sun Elevation"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText114->Wrap( -1 );
	bSizer164->Add( m_staticText114, 0, wxALL, 5 );
	
	
	bSizer154->Add( bSizer164, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer184;
	bSizer184 = new wxBoxSizer( wxVERTICAL );
	
	sun_elevation = new wxTextCtrl( sbSizer6->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer184->Add( sun_elevation, 0, wxALL|wxEXPAND, 5 );
	
	
	bSizer154->Add( bSizer184, 1, wxEXPAND, 5 );
	
	
	sbSizer6->Add( bSizer154, 0, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer155;
	bSizer155 = new wxBoxSizer( wxHORIZONTAL );
	
	wxBoxSizer* bSizer165;
	bSizer165 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText115 = new wxStaticText( sbSizer6->GetStaticBox(), wxID_ANY, wxT("Reflectance Mult"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText115->Wrap( -1 );
	bSizer165->Add( m_staticText115, 0, wxALL, 5 );
	
	
	bSizer155->Add( bSizer165, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer185;
	bSizer185 = new wxBoxSizer( wxVERTICAL );
	
	reflectance_mult = new wxTextCtrl( sbSizer6->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer185->Add( reflectance_mult, 0, wxALL|wxEXPAND, 5 );
	
	
	bSizer155->Add( bSizer185, 1, wxEXPAND, 5 );
	
	
	sbSizer6->Add( bSizer155, 0, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer156;
	bSizer156 = new wxBoxSizer( wxHORIZONTAL );
	
	wxBoxSizer* bSizer166;
	bSizer166 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText116 = new wxStaticText( sbSizer6->GetStaticBox(), wxID_ANY, wxT("Reflectance Add"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText116->Wrap( -1 );
	bSizer166->Add( m_staticText116, 0, wxALL, 5 );
	
	
	bSizer156->Add( bSizer166, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer186;
	bSizer186 = new wxBoxSizer( wxVERTICAL );
	
	reflectance_add = new wxTextCtrl( sbSizer6->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer186->Add( reflectance_add, 0, wxALL|wxEXPAND, 5 );
	
	
	bSizer156->Add( bSizer186, 1, wxEXPAND, 5 );
	
	
	sbSizer6->Add( bSizer156, 0, wxEXPAND, 5 );
	
	m_staticText13 = new wxStaticText( sbSizer6->GetStaticBox(), wxID_ANY, wxT("SHP Lautan"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText13->Wrap( -1 );
	sbSizer6->Add( m_staticText13, 0, wxALL, 5 );
	
	ambil_shp = new wxFilePickerCtrl( sbSizer6->GetStaticBox(), wxID_ANY, wxEmptyString, wxT("Select a file"), wxT("*shp*"), wxDefaultPosition, wxDefaultSize, wxFLP_DEFAULT_STYLE );
	sbSizer6->Add( ambil_shp, 0, wxALL|wxEXPAND, 5 );
	
	m_staticText131 = new wxStaticText( sbSizer6->GetStaticBox(), wxID_ANY, wxT("Direktori Output"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText131->Wrap( -1 );
	sbSizer6->Add( m_staticText131, 0, wxALL, 5 );
	
	ambil_output = new wxDirPickerCtrl( sbSizer6->GetStaticBox(), wxID_ANY, wxEmptyString, wxT("Select a folder"), wxDefaultPosition, wxDefaultSize, wxDIRP_DEFAULT_STYLE );
	sbSizer6->Add( ambil_output, 0, wxALL|wxEXPAND, 5 );
	
	start = new wxButton( sbSizer6->GetStaticBox(), wxID_ANY, wxT("Mulai Pemetaan"), wxDefaultPosition, wxDefaultSize, 0 );
	sbSizer6->Add( start, 1, wxALL|wxEXPAND, 5 );
	
	reset = new wxButton( sbSizer6->GetStaticBox(), wxID_ANY, wxT("Reset"), wxDefaultPosition, wxDefaultSize, 0 );
	sbSizer6->Add( reset, 0, wxALL|wxEXPAND, 5 );
	
	
	bSizer39->Add( sbSizer6, 1, wxBOTTOM|wxEXPAND|wxLEFT|wxRIGHT|wxTOP, 5 );
	
	
	bSizer6->Add( bSizer39, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer34;
	bSizer34 = new wxBoxSizer( wxVERTICAL );
	
	wxStaticBoxSizer* sbSizer3;
	sbSizer3 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("Hasil Pemetaan") ), wxVERTICAL );
	
	citra_hasil = new wxStaticBitmap( sbSizer3->GetStaticBox(), wxID_ANY, wxNullBitmap, wxDefaultPosition, wxSize( 450,450 ), 0 );
	sbSizer3->Add( citra_hasil, 1, wxALL|wxEXPAND, 5 );
	
	
	bSizer34->Add( sbSizer3, 1, wxALL|wxEXPAND, 5 );
	
	
	bSizer6->Add( bSizer34, 1, wxEXPAND, 5 );
	
	
	bSizerMain->Add( bSizer6, 1, wxEXPAND, 5 );
	
	
	this->SetSizer( bSizerMain );
	this->Layout();
	
	this->Centre( wxBOTH );
	
	// Connect Events
	ambil_band4->Connect( wxEVT_COMMAND_FILEPICKER_CHANGED, wxFileDirPickerEventHandler( FrameUtama::filepick_band4OnFileChanged ), NULL, this );
	ambil_band5->Connect( wxEVT_COMMAND_FILEPICKER_CHANGED, wxFileDirPickerEventHandler( FrameUtama::filepick_band5OnFileChanged ), NULL, this );
	ambil_band6->Connect( wxEVT_COMMAND_FILEPICKER_CHANGED, wxFileDirPickerEventHandler( FrameUtama::filepick_band6OnFileChanged ), NULL, this );
	ambil_bandqa->Connect( wxEVT_COMMAND_FILEPICKER_CHANGED, wxFileDirPickerEventHandler( FrameUtama::ambil_bandqaOnFileChanged ), NULL, this );
	ambil_shp->Connect( wxEVT_COMMAND_FILEPICKER_CHANGED, wxFileDirPickerEventHandler( FrameUtama::ambil_shpOnFileChanged ), NULL, this );
	ambil_output->Connect( wxEVT_COMMAND_DIRPICKER_CHANGED, wxFileDirPickerEventHandler( FrameUtama::dir_outputOnDirChanged ), NULL, this );
	start->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( FrameUtama::startOnButtonClick ), NULL, this );
	reset->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( FrameUtama::resetOnButtonClick ), NULL, this );
}

FrameUtama::~FrameUtama()
{
	// Disconnect Events
	ambil_band4->Disconnect( wxEVT_COMMAND_FILEPICKER_CHANGED, wxFileDirPickerEventHandler( FrameUtama::filepick_band4OnFileChanged ), NULL, this );
	ambil_band5->Disconnect( wxEVT_COMMAND_FILEPICKER_CHANGED, wxFileDirPickerEventHandler( FrameUtama::filepick_band5OnFileChanged ), NULL, this );
	ambil_band6->Disconnect( wxEVT_COMMAND_FILEPICKER_CHANGED, wxFileDirPickerEventHandler( FrameUtama::filepick_band6OnFileChanged ), NULL, this );
	ambil_bandqa->Disconnect( wxEVT_COMMAND_FILEPICKER_CHANGED, wxFileDirPickerEventHandler( FrameUtama::ambil_bandqaOnFileChanged ), NULL, this );
	ambil_shp->Disconnect( wxEVT_COMMAND_FILEPICKER_CHANGED, wxFileDirPickerEventHandler( FrameUtama::ambil_shpOnFileChanged ), NULL, this );
	ambil_output->Disconnect( wxEVT_COMMAND_DIRPICKER_CHANGED, wxFileDirPickerEventHandler( FrameUtama::dir_outputOnDirChanged ), NULL, this );
	start->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( FrameUtama::startOnButtonClick ), NULL, this );
	reset->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( FrameUtama::resetOnButtonClick ), NULL, this );
	
}
