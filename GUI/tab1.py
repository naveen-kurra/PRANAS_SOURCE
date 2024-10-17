# tab1.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox

class Tab1Content(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 10

        # Create input box for "Enter Bacteria Name"
        self.add_widget(self.create_labeled_input('Enter Bacteria Name:', 'Enter bacteria name'))

        # Create input box for "Trial Number"
        self.add_widget(self.create_labeled_input('Trial Number:', 'Enter trial number'))

        # Create the Analysis Type label and radio buttons
        self.add_widget(Label(text='Analysis Type:', size_hint=(1, 0.1), font_size=18))

        # Create a horizontal layout for the radio buttons
        radio_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))

        self.option1 = CheckBox(group='radio', size_hint=(None, 1), width=50)
        self.option2 = CheckBox(group='radio', size_hint=(None, 1), width=50)
        self.option3 = CheckBox(group='radio', size_hint=(None, 1), width=50)

        # Add radio buttons with their labels
        radio_layout.add_widget(Label(text='Option 1'))
        radio_layout.add_widget(self.option1)
        radio_layout.add_widget(Label(text='Option 2'))
        radio_layout.add_widget(self.option2)
        radio_layout.add_widget(Label(text='Option 3'))
        radio_layout.add_widget(self.option3)

        # Add the radio layout to the main layout
        self.add_widget(radio_layout)

        # Create the control buttons: Start, Pause, Stop
        button_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2), spacing=10)

        start_button = Button(
            text='START',
            font_size=25,
            size_hint_y=0.5,
            color=(0, 0, 0, 1),  # Black text color
            background_color=(0, 1, 0, 1),  # Green background color
            background_normal=""  # Remove default background image
        )

        pause_button = Button(
            text='PAUSE',
            font_size=25,
            size_hint_y=0.5,
            color=(0, 0, 0, 1),  # Black text color
            background_color=(1, 0.65, 0, 1),  # Orange background color
            background_normal=""  # Remove default background image
        )

        stop_button = Button(
            text='STOP',
            font_size=25,
            size_hint_y=0.5,
            color=(0, 0, 0, 1),  # Black text color
            background_color=(1, 0, 0, 1),  # Red background color
            background_normal=""  # Remove default background image
        )

        # Bind the Start button to the start function
        start_button.bind(on_press=self.start_action)

        # Add buttons to the layout
        button_layout.add_widget(start_button)
        button_layout.add_widget(pause_button)
        button_layout.add_widget(stop_button)

        # Add the button layout to the main layout
        self.add_widget(button_layout)

    def create_labeled_input(self, label_text, hint_text):
        """Create a horizontal layout with a label and input box."""
        layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), spacing=10)
        label = Label(text=label_text, size_hint=(0.3, 1))
        text_input = TextInput(hint_text=hint_text, size_hint=(0.7, 1))
        setattr(self, f'{label_text.lower().replace(" ", "_").replace(":", "")}_input', text_input)  # Store input reference
        layout.add_widget(label)
        layout.add_widget(text_input)
        return layout

    def start_action(self, instance):
        """Print the entered details to the console when Start is clicked."""
        bacteria_name = self.enter_bacteria_name_input.text
        trial_number = self.trial_number_input.text

        # Determine which radio button is selected
        if self.option1.active:
            radio_value = 'Option 1'
        elif self.option2.active:
            radio_value = 'Option 2'
        elif self.option3.active:
            radio_value = 'Option 3'
        else:
            radio_value = 'No option selected'

        # Print the results to the console
        print(f'Bacteria Name: {bacteria_name}')
        print(f'Trial Number: {trial_number}')
        print(f'Selected Analysis Type: {radio_value}')
