# main.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.graphics import Line, Color

from tab1 import Tab1Content
from tab2 import Tab2Content
from tab3 import Tab3Content

class HeaderFooterLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Create and add the header
        header = self.create_header()
        self.add_widget(header)

        # Create and add the body with tabs and the reset button
        body = self.create_body()
        self.add_widget(body)

        # Create and add the footer
        footer = self.create_footer()
        self.add_widget(footer)

    def create_header(self):
        """Create the header layout with an image and text."""
        header = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), padding=10)

        with header.canvas.after:
            Color(1, 0, 0, 1)  # Red color
            self.header_line = Line(points=[0, 0, header.width, 0], width=2)

        header.bind(size=self.update_header_line, pos=self.update_header_line)

        header.add_widget(Image(source='Images/icon.ico', size_hint=(0.1, 1)))

        header.add_widget(Label(
            text='Personal Respiratory Analyzing System',
            font_size=48, bold=True, halign='left', color=(0, 1, 0, 1)
        ))

        return header

    def create_body(self):
        """Create the body layout with a reset button and tabs."""
        body = BoxLayout(orientation='horizontal', size_hint=(1, 0.8), padding=10, spacing=10)

        # Create the left column with the reset button and tabs
        left_column = BoxLayout(orientation='vertical', size_hint_x=0.6)

        # Add the reset button at the top of the left column
        reset_button = Button(
            text='Reset Tabs', 
            size_hint=(1, 0.1), 
            background_color=(1, 0, 0, 1)  # Red color
        )
        reset_button.bind(on_press=self.reset_tabs)

        # Add the reset button to the left column
        left_column.add_widget(reset_button)

        # Add the TabbedPanel below the reset button
        self.tab_panel = self.create_tabs()
        left_column.add_widget(self.tab_panel)

        # Create the right column content
        right_column = BoxLayout(orientation='vertical', size_hint_x=0.4)
        right_column.add_widget(Label(text='Right Column Content', font_size=24))

        # Add the left and right columns to the body
        body.add_widget(left_column)

        with body.canvas.after:
            Color(1, 1, 1, 1)  # White color
            self.separator_line = Line(width=2)

        body.add_widget(right_column)

        body.bind(size=self.update_body_separator, pos=self.update_body_separator)

        return body

    def create_tabs(self):
        """Create a TabbedPanel with three tabs."""
        tab_panel = TabbedPanel(do_default_tab=False)  # Disable default tab

        # Create Tab 1
        self.tab1 = TabbedPanelItem(text='Tab 1')
        self.tab1.content = Tab1Content()
        tab_panel.add_widget(self.tab1)

        # Create Tab 2
        self.tab2 = TabbedPanelItem(text='Tab 2')
        self.tab2.content = Tab2Content()
        tab_panel.add_widget(self.tab2)

        # Create Tab 3
        self.tab3 = TabbedPanelItem(text='Tab 3')
        self.tab3.content = Tab3Content()
        tab_panel.add_widget(self.tab3)

        return tab_panel

    def reset_tabs(self, instance):
        """Reset the content of all tabs to their initial state."""
        # Reset the content of each tab
        self.tab1.content = Tab1Content()
        self.tab2.content = Tab2Content()
        self.tab3.content = Tab3Content()

    def create_footer(self):
        """Create the footer layout with images and text."""
        footer = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), padding=10)

        with footer.canvas.before:
            Color(1, 0, 0, 1)  # Red color
            self.footer_line = Line(points=[0, footer.height, footer.width, footer.height], width=2)

        footer.bind(size=self.update_footer_line, pos=self.update_footer_line)

        footer.add_widget(Image(source='Images/ugalogo.png', size_hint=(0.1, 1)))

        footer.add_widget(Label(
            text='Developed at Design Informatics and Computational Engineering Lab,\n'
                 'University of Georgia, Athens, GA, USA',
            font_size=18, halign='center'
        ))

        footer.add_widget(Image(source='Images/dicelogo.jpg', size_hint=(0.1, 1)))

        return footer

    def update_header_line(self, instance, value):
        """Update the header line dynamically."""
        self.header_line.points = [instance.x, instance.y, instance.right, instance.y]

    def update_footer_line(self, instance, value):
        """Update the footer line dynamically."""
        self.footer_line.points = [instance.x, instance.top, instance.right, instance.top]

    def update_body_separator(self, instance, value):
        """Update the separator line dynamically between columns."""
        separator_x = instance.width * 0.6  # 60% of the body's width
        self.separator_line.points = [separator_x, instance.y, separator_x, instance.top]

class PranasApp(App):
    def build(self):
        return HeaderFooterLayout()

if __name__ == '__main__':
    PranasApp().run()
