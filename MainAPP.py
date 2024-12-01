# LaunchService.py

from kivy.app import App
from GUI.first_UI import HeaderFooterLayout as FirstUI
from ServiceManager import ServiceManager
from GUI import tab1
from GUI.first_UI import HeaderFooterLayout

class PranasApp(App):
    def build(self):
        # Create the Tab1Content UI and ServiceManager
        service_manager = ServiceManager(gui=None)  # Initialize ServiceManager
        layout = HeaderFooterLayout(service_manager)  # Pass ServiceManager to Tab1Content
        
        # Update the ServiceManager with the Tab1Content as the GUI
        service_manager.gui = layout

        return layout

if __name__ == '__main__':
    PranasApp().run()
