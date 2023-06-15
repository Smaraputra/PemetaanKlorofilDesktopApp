///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun 17 2015)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __MAIN_H__
#define __MAIN_H__

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/sizer.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/statbmp.h>
#include <wx/filepicker.h>
#include <wx/statbox.h>
#include <wx/textctrl.h>
#include <wx/button.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class FrameUtama
///////////////////////////////////////////////////////////////////////////////
class FrameUtama : public wxFrame 
{
	private:
	
	protected:
		wxStaticText* m_staticText4;
		wxStaticBitmap* citra_b4;
		wxStaticText* m_staticText523;
		wxFilePickerCtrl* ambil_band4;
		wxStaticBitmap* citra_b5;
		wxStaticText* m_staticText522;
		wxFilePickerCtrl* ambil_band5;
		wxStaticBitmap* citra_b6;
		wxStaticText* m_staticText52;
		wxFilePickerCtrl* ambil_band6;
		wxStaticBitmap* citra_bqa;
		wxStaticText* m_staticText521;
		wxFilePickerCtrl* ambil_bandqa;
		wxStaticText* m_staticText17;
		wxStaticText* m_staticText11;
		wxTextCtrl* longitude_start;
		wxStaticText* m_staticText111;
		wxTextCtrl* longitude_end;
		wxStaticText* m_staticText112;
		wxTextCtrl* latitude_start;
		wxStaticText* m_staticText113;
		wxTextCtrl* latitude_end;
		wxStaticText* m_staticText114;
		wxTextCtrl* sun_elevation;
		wxStaticText* m_staticText115;
		wxTextCtrl* reflectance_mult;
		wxStaticText* m_staticText116;
		wxTextCtrl* reflectance_add;
		wxStaticText* m_staticText13;
		wxFilePickerCtrl* ambil_shp;
		wxStaticText* m_staticText131;
		wxDirPickerCtrl* ambil_output;
		wxButton* start;
		wxButton* reset;
		wxStaticBitmap* citra_hasil;
		
		// Virtual event handlers, overide them in your derived class
		virtual void filepick_band4OnFileChanged( wxFileDirPickerEvent& event ) { event.Skip(); }
		virtual void filepick_band5OnFileChanged( wxFileDirPickerEvent& event ) { event.Skip(); }
		virtual void filepick_band6OnFileChanged( wxFileDirPickerEvent& event ) { event.Skip(); }
		virtual void ambil_bandqaOnFileChanged( wxFileDirPickerEvent& event ) { event.Skip(); }
		virtual void ambil_shpOnFileChanged( wxFileDirPickerEvent& event ) { event.Skip(); }
		virtual void dir_outputOnDirChanged( wxFileDirPickerEvent& event ) { event.Skip(); }
		virtual void startOnButtonClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void resetOnButtonClick( wxCommandEvent& event ) { event.Skip(); }
		
	
	public:
		
		FrameUtama( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("PROJECT UAS - 1905551095"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 1200,720 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		
		~FrameUtama();
	
};

#endif //__MAIN_H__
