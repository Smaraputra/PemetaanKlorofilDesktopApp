<?php

/*
* PHP code generated with wxFormBuilder (version Jun 17 2015)
* http://www.wxformbuilder.org/
*
* PLEASE DO "NOT" EDIT THIS FILE!
*/

/*
 * Class FrameUtama
 */

class FrameUtama extends wxFrame {
	
	function __construct( $parent=null ){
		parent::__construct ( $parent, wxID_ANY, "PROJECT UAS - 1905551095", wxDefaultPosition, new wxSize( 1200,720 ), wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		
		$this->SetSizeHints( wxDefaultSize, wxDefaultSize );
		$this->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_WINDOW ) );
		
		$bSizerMain = new wxBoxSizer( wxVERTICAL );
		
		$bSizer41 = new wxBoxSizer( wxVERTICAL );
		
		$this->m_staticText4 = new wxStaticText( $this, wxID_ANY, "Pemetaan Sebaran Klorofil-A di Selat Bali", wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE );
		$this->m_staticText4->Wrap( -1 );
		$this->m_staticText4->SetFont( new wxFont( 14, 72, 90, 92, false, "Times New Roman" ) );
		
		$bSizer41->Add( $this->m_staticText4, 0, wxALL|wxEXPAND, 10 );
		
		
		$bSizerMain->Add( $bSizer41, 0, wxEXPAND, 5 );
		
		$bSizer6 = new wxBoxSizer( wxHORIZONTAL );
		
		$sbSizer1 = new wxStaticBoxSizer( new wxStaticBox( $this, wxID_ANY, "Input Citra Landsat" ), wxVERTICAL );
		
		$bSizer72 = new wxBoxSizer( wxHORIZONTAL );
		
		$bSizer82 = new wxBoxSizer( wxVERTICAL );
		
		$this->citra_b4 = new wxStaticBitmap( $sbSizer1->GetStaticBox(), wxID_ANY, wxNullBitmap, wxDefaultPosition, new wxSize( 125,125 ), 0 );
		$bSizer82->Add( $this->citra_b4, 1, wxALL|wxEXPAND, 5 );
		
		
		$bSizer72->Add( $bSizer82, 1, wxEXPAND, 5 );
		
		$bSizer102 = new wxBoxSizer( wxVERTICAL );
		
		$this->m_staticText523 = new wxStaticText( $sbSizer1->GetStaticBox(), wxID_ANY, "Citra Band 4", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_staticText523->Wrap( -1 );
		$this->m_staticText523->SetFont( new wxFont( 10, 72, 90, 90, false, "Times New Roman" ) );
		
		$bSizer102->Add( $this->m_staticText523, 0, wxALL, 5 );
		
		$this->ambil_band4 = new wxFilePickerCtrl( $sbSizer1->GetStaticBox(), wxID_ANY, wxEmptyString, "Select a file", "*tif*", wxDefaultPosition, wxDefaultSize, wxFLP_DEFAULT_STYLE );
		$bSizer102->Add( $this->ambil_band4, 0, wxALL|wxEXPAND, 5 );
		
		
		$bSizer72->Add( $bSizer102, 1, wxEXPAND, 5 );
		
		
		$sbSizer1->Add( $bSizer72, 1, wxEXPAND, 5 );
		
		$bSizer71 = new wxBoxSizer( wxHORIZONTAL );
		
		$bSizer81 = new wxBoxSizer( wxVERTICAL );
		
		$this->citra_b5 = new wxStaticBitmap( $sbSizer1->GetStaticBox(), wxID_ANY, wxNullBitmap, wxDefaultPosition, new wxSize( 125,125 ), 0 );
		$bSizer81->Add( $this->citra_b5, 1, wxALL|wxEXPAND, 5 );
		
		
		$bSizer71->Add( $bSizer81, 1, wxEXPAND, 5 );
		
		$bSizer101 = new wxBoxSizer( wxVERTICAL );
		
		$this->m_staticText522 = new wxStaticText( $sbSizer1->GetStaticBox(), wxID_ANY, "Citra Band 5", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_staticText522->Wrap( -1 );
		$this->m_staticText522->SetFont( new wxFont( 10, 72, 90, 90, false, "Times New Roman" ) );
		
		$bSizer101->Add( $this->m_staticText522, 0, wxALL, 5 );
		
		$this->ambil_band5 = new wxFilePickerCtrl( $sbSizer1->GetStaticBox(), wxID_ANY, wxEmptyString, "Select a file", "*tif*", wxDefaultPosition, wxDefaultSize, wxFLP_DEFAULT_STYLE );
		$bSizer101->Add( $this->ambil_band5, 0, wxALL|wxEXPAND, 5 );
		
		
		$bSizer71->Add( $bSizer101, 1, wxEXPAND, 5 );
		
		
		$sbSizer1->Add( $bSizer71, 1, wxEXPAND, 5 );
		
		$bSizer7 = new wxBoxSizer( wxHORIZONTAL );
		
		$bSizer8 = new wxBoxSizer( wxVERTICAL );
		
		$this->citra_b6 = new wxStaticBitmap( $sbSizer1->GetStaticBox(), wxID_ANY, wxNullBitmap, wxDefaultPosition, new wxSize( 125,125 ), 0 );
		$bSizer8->Add( $this->citra_b6, 1, wxALL|wxEXPAND, 5 );
		
		
		$bSizer7->Add( $bSizer8, 1, wxEXPAND, 5 );
		
		$bSizer10 = new wxBoxSizer( wxVERTICAL );
		
		$this->m_staticText52 = new wxStaticText( $sbSizer1->GetStaticBox(), wxID_ANY, "Citra Band 6", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_staticText52->Wrap( -1 );
		$this->m_staticText52->SetFont( new wxFont( 10, 72, 90, 90, false, "Times New Roman" ) );
		
		$bSizer10->Add( $this->m_staticText52, 0, wxALL|wxEXPAND, 5 );
		
		$this->ambil_band6 = new wxFilePickerCtrl( $sbSizer1->GetStaticBox(), wxID_ANY, wxEmptyString, "Select a file", "*tif*", wxDefaultPosition, wxDefaultSize, wxFLP_DEFAULT_STYLE );
		$bSizer10->Add( $this->ambil_band6, 0, wxALL, 5 );
		
		
		$bSizer7->Add( $bSizer10, 1, wxEXPAND, 5 );
		
		
		$sbSizer1->Add( $bSizer7, 1, wxEXPAND, 5 );
		
		$bSizer73 = new wxBoxSizer( wxHORIZONTAL );
		
		$bSizer83 = new wxBoxSizer( wxVERTICAL );
		
		$this->citra_bqa = new wxStaticBitmap( $sbSizer1->GetStaticBox(), wxID_ANY, wxNullBitmap, wxDefaultPosition, new wxSize( 125,125 ), 0 );
		$bSizer83->Add( $this->citra_bqa, 1, wxALL|wxEXPAND, 5 );
		
		
		$bSizer73->Add( $bSizer83, 1, wxEXPAND, 5 );
		
		$bSizer103 = new wxBoxSizer( wxVERTICAL );
		
		$this->m_staticText521 = new wxStaticText( $sbSizer1->GetStaticBox(), wxID_ANY, "Citra Band QA (Opsional)", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_staticText521->Wrap( -1 );
		$this->m_staticText521->SetFont( new wxFont( 10, 72, 90, 90, false, "Times New Roman" ) );
		
		$bSizer103->Add( $this->m_staticText521, 0, wxALL|wxEXPAND, 5 );
		
		$this->ambil_bandqa = new wxFilePickerCtrl( $sbSizer1->GetStaticBox(), wxID_ANY, wxEmptyString, "Select a file", "*tif*", wxDefaultPosition, wxDefaultSize, wxFLP_DEFAULT_STYLE );
		$bSizer103->Add( $this->ambil_bandqa, 0, wxALL, 5 );
		
		$this->m_staticText17 = new wxStaticText( $sbSizer1->GetStaticBox(), wxID_ANY, "*Untuk masking awan", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_staticText17->Wrap( -1 );
		$bSizer103->Add( $this->m_staticText17, 0, wxALL, 5 );
		
		
		$bSizer73->Add( $bSizer103, 1, wxEXPAND, 5 );
		
		
		$sbSizer1->Add( $bSizer73, 1, wxEXPAND, 5 );
		
		
		$bSizer6->Add( $sbSizer1, 1, wxALL|wxEXPAND, 5 );
		
		$bSizer39 = new wxBoxSizer( wxVERTICAL );
		
		$sbSizer5 = new wxStaticBoxSizer( new wxStaticBox( $this, wxID_ANY, "Potong Citra" ), wxVERTICAL );
		
		$bSizer15 = new wxBoxSizer( wxHORIZONTAL );
		
		$bSizer16 = new wxBoxSizer( wxVERTICAL );
		
		$this->m_staticText11 = new wxStaticText( $sbSizer5->GetStaticBox(), wxID_ANY, "Longitude Start", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_staticText11->Wrap( -1 );
		$bSizer16->Add( $this->m_staticText11, 0, wxALL, 5 );
		
		
		$bSizer15->Add( $bSizer16, 1, wxEXPAND, 5 );
		
		$bSizer18 = new wxBoxSizer( wxVERTICAL );
		
		$this->longitude_start = new wxTextCtrl( $sbSizer5->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
		$bSizer18->Add( $this->longitude_start, 0, wxALL|wxEXPAND, 5 );
		
		
		$bSizer15->Add( $bSizer18, 1, wxEXPAND, 5 );
		
		
		$sbSizer5->Add( $bSizer15, 0, wxEXPAND, 5 );
		
		$bSizer151 = new wxBoxSizer( wxHORIZONTAL );
		
		$bSizer161 = new wxBoxSizer( wxVERTICAL );
		
		$this->m_staticText111 = new wxStaticText( $sbSizer5->GetStaticBox(), wxID_ANY, "Longitude End", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_staticText111->Wrap( -1 );
		$bSizer161->Add( $this->m_staticText111, 0, wxALL, 5 );
		
		
		$bSizer151->Add( $bSizer161, 1, wxEXPAND, 5 );
		
		$bSizer181 = new wxBoxSizer( wxVERTICAL );
		
		$this->longitude_end = new wxTextCtrl( $sbSizer5->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
		$bSizer181->Add( $this->longitude_end, 0, wxALL|wxEXPAND, 5 );
		
		
		$bSizer151->Add( $bSizer181, 1, wxEXPAND, 5 );
		
		
		$sbSizer5->Add( $bSizer151, 0, wxEXPAND, 5 );
		
		$bSizer152 = new wxBoxSizer( wxHORIZONTAL );
		
		$bSizer162 = new wxBoxSizer( wxVERTICAL );
		
		$this->m_staticText112 = new wxStaticText( $sbSizer5->GetStaticBox(), wxID_ANY, "Latitude Start", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_staticText112->Wrap( -1 );
		$bSizer162->Add( $this->m_staticText112, 0, wxALL, 5 );
		
		
		$bSizer152->Add( $bSizer162, 1, wxEXPAND, 5 );
		
		$bSizer182 = new wxBoxSizer( wxVERTICAL );
		
		$this->latitude_start = new wxTextCtrl( $sbSizer5->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
		$bSizer182->Add( $this->latitude_start, 0, wxALL|wxEXPAND, 5 );
		
		
		$bSizer152->Add( $bSizer182, 1, wxEXPAND, 5 );
		
		
		$sbSizer5->Add( $bSizer152, 0, wxEXPAND, 5 );
		
		$bSizer153 = new wxBoxSizer( wxHORIZONTAL );
		
		$bSizer163 = new wxBoxSizer( wxVERTICAL );
		
		$this->m_staticText113 = new wxStaticText( $sbSizer5->GetStaticBox(), wxID_ANY, "Latitude End", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_staticText113->Wrap( -1 );
		$bSizer163->Add( $this->m_staticText113, 0, wxALL, 5 );
		
		
		$bSizer153->Add( $bSizer163, 1, wxEXPAND, 5 );
		
		$bSizer183 = new wxBoxSizer( wxVERTICAL );
		
		$this->latitude_end = new wxTextCtrl( $sbSizer5->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
		$bSizer183->Add( $this->latitude_end, 0, wxALL|wxEXPAND, 5 );
		
		
		$bSizer153->Add( $bSizer183, 1, wxEXPAND, 5 );
		
		
		$sbSizer5->Add( $bSizer153, 1, wxEXPAND, 5 );
		
		
		$bSizer39->Add( $sbSizer5, 0, wxEXPAND|wxLEFT|wxRIGHT|wxTOP, 5 );
		
		$sbSizer6 = new wxStaticBoxSizer( new wxStaticBox( $this, wxID_ANY, "Variabel" ), wxVERTICAL );
		
		$bSizer154 = new wxBoxSizer( wxHORIZONTAL );
		
		$bSizer164 = new wxBoxSizer( wxVERTICAL );
		
		$this->m_staticText114 = new wxStaticText( $sbSizer6->GetStaticBox(), wxID_ANY, "Sun Elevation", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_staticText114->Wrap( -1 );
		$bSizer164->Add( $this->m_staticText114, 0, wxALL, 5 );
		
		
		$bSizer154->Add( $bSizer164, 1, wxEXPAND, 5 );
		
		$bSizer184 = new wxBoxSizer( wxVERTICAL );
		
		$this->sun_elevation = new wxTextCtrl( $sbSizer6->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
		$bSizer184->Add( $this->sun_elevation, 0, wxALL|wxEXPAND, 5 );
		
		
		$bSizer154->Add( $bSizer184, 1, wxEXPAND, 5 );
		
		
		$sbSizer6->Add( $bSizer154, 0, wxEXPAND, 5 );
		
		$bSizer155 = new wxBoxSizer( wxHORIZONTAL );
		
		$bSizer165 = new wxBoxSizer( wxVERTICAL );
		
		$this->m_staticText115 = new wxStaticText( $sbSizer6->GetStaticBox(), wxID_ANY, "Reflectance Mult", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_staticText115->Wrap( -1 );
		$bSizer165->Add( $this->m_staticText115, 0, wxALL, 5 );
		
		
		$bSizer155->Add( $bSizer165, 1, wxEXPAND, 5 );
		
		$bSizer185 = new wxBoxSizer( wxVERTICAL );
		
		$this->reflectance_mult = new wxTextCtrl( $sbSizer6->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
		$bSizer185->Add( $this->reflectance_mult, 0, wxALL|wxEXPAND, 5 );
		
		
		$bSizer155->Add( $bSizer185, 1, wxEXPAND, 5 );
		
		
		$sbSizer6->Add( $bSizer155, 0, wxEXPAND, 5 );
		
		$bSizer156 = new wxBoxSizer( wxHORIZONTAL );
		
		$bSizer166 = new wxBoxSizer( wxVERTICAL );
		
		$this->m_staticText116 = new wxStaticText( $sbSizer6->GetStaticBox(), wxID_ANY, "Reflectance Add", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_staticText116->Wrap( -1 );
		$bSizer166->Add( $this->m_staticText116, 0, wxALL, 5 );
		
		
		$bSizer156->Add( $bSizer166, 1, wxEXPAND, 5 );
		
		$bSizer186 = new wxBoxSizer( wxVERTICAL );
		
		$this->reflectance_add = new wxTextCtrl( $sbSizer6->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
		$bSizer186->Add( $this->reflectance_add, 0, wxALL|wxEXPAND, 5 );
		
		
		$bSizer156->Add( $bSizer186, 1, wxEXPAND, 5 );
		
		
		$sbSizer6->Add( $bSizer156, 0, wxEXPAND, 5 );
		
		$this->m_staticText13 = new wxStaticText( $sbSizer6->GetStaticBox(), wxID_ANY, "SHP Lautan", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_staticText13->Wrap( -1 );
		$sbSizer6->Add( $this->m_staticText13, 0, wxALL, 5 );
		
		$this->ambil_shp = new wxFilePickerCtrl( $sbSizer6->GetStaticBox(), wxID_ANY, wxEmptyString, "Select a file", "*shp*", wxDefaultPosition, wxDefaultSize, wxFLP_DEFAULT_STYLE );
		$sbSizer6->Add( $this->ambil_shp, 0, wxALL|wxEXPAND, 5 );
		
		$this->m_staticText131 = new wxStaticText( $sbSizer6->GetStaticBox(), wxID_ANY, "Direktori Output", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_staticText131->Wrap( -1 );
		$sbSizer6->Add( $this->m_staticText131, 0, wxALL, 5 );
		
		$this->ambil_output = new wxDirPickerCtrl( $sbSizer6->GetStaticBox(), wxID_ANY, wxEmptyString, "Select a folder", wxDefaultPosition, wxDefaultSize, wxDIRP_DEFAULT_STYLE );
		$sbSizer6->Add( $this->ambil_output, 0, wxALL|wxEXPAND, 5 );
		
		$this->start = new wxButton( $sbSizer6->GetStaticBox(), wxID_ANY, "Mulai Pemetaan", wxDefaultPosition, wxDefaultSize, 0 );
		$sbSizer6->Add( $this->start, 1, wxALL|wxEXPAND, 5 );
		
		$this->reset = new wxButton( $sbSizer6->GetStaticBox(), wxID_ANY, "Reset", wxDefaultPosition, wxDefaultSize, 0 );
		$sbSizer6->Add( $this->reset, 0, wxALL|wxEXPAND, 5 );
		
		
		$bSizer39->Add( $sbSizer6, 1, wxBOTTOM|wxEXPAND|wxLEFT|wxRIGHT|wxTOP, 5 );
		
		
		$bSizer6->Add( $bSizer39, 1, wxEXPAND, 5 );
		
		$bSizer34 = new wxBoxSizer( wxVERTICAL );
		
		$sbSizer3 = new wxStaticBoxSizer( new wxStaticBox( $this, wxID_ANY, "Hasil Pemetaan" ), wxVERTICAL );
		
		$this->citra_hasil = new wxStaticBitmap( $sbSizer3->GetStaticBox(), wxID_ANY, wxNullBitmap, wxDefaultPosition, new wxSize( 450,450 ), 0 );
		$sbSizer3->Add( $this->citra_hasil, 1, wxALL|wxEXPAND, 5 );
		
		
		$bSizer34->Add( $sbSizer3, 1, wxALL|wxEXPAND, 5 );
		
		
		$bSizer6->Add( $bSizer34, 1, wxEXPAND, 5 );
		
		
		$bSizerMain->Add( $bSizer6, 1, wxEXPAND, 5 );
		
		
		$this->SetSizer( $bSizerMain );
		$this->Layout();
		
		$this->Centre( wxBOTH );
		
		// Connect Events
		$this->ambil_band4->Connect( wxEVT_COMMAND_FILEPICKER_CHANGED, array($this, "filepick_band4OnFileChanged") );
		$this->ambil_band5->Connect( wxEVT_COMMAND_FILEPICKER_CHANGED, array($this, "filepick_band5OnFileChanged") );
		$this->ambil_band6->Connect( wxEVT_COMMAND_FILEPICKER_CHANGED, array($this, "filepick_band6OnFileChanged") );
		$this->ambil_bandqa->Connect( wxEVT_COMMAND_FILEPICKER_CHANGED, array($this, "ambil_bandqaOnFileChanged") );
		$this->ambil_shp->Connect( wxEVT_COMMAND_FILEPICKER_CHANGED, array($this, "ambil_shpOnFileChanged") );
		$this->ambil_output->Connect( wxEVT_COMMAND_DIRPICKER_CHANGED, array($this, "dir_outputOnDirChanged") );
		$this->start->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "startOnButtonClick") );
		$this->reset->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "resetOnButtonClick") );
	}
	
	
	function __destruct( ){
	}
	
	
	// Virtual event handlers, overide them in your derived class
	function filepick_band4OnFileChanged( $event ){
		$event->Skip();
	}
	
	function filepick_band5OnFileChanged( $event ){
		$event->Skip();
	}
	
	function filepick_band6OnFileChanged( $event ){
		$event->Skip();
	}
	
	function ambil_bandqaOnFileChanged( $event ){
		$event->Skip();
	}
	
	function ambil_shpOnFileChanged( $event ){
		$event->Skip();
	}
	
	function dir_outputOnDirChanged( $event ){
		$event->Skip();
	}
	
	function startOnButtonClick( $event ){
		$event->Skip();
	}
	
	function resetOnButtonClick( $event ){
		$event->Skip();
	}
	
}

?>
