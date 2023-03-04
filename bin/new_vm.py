import kivy
import os

from kivy.uix.filechooser import FileChooser
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.popup import Popup
from kivy.core.window import Window

class NewVMWindow(Popup):

    def __init__(self):
        default_text_size = 24
        super(NewVMWindow, self).__init__()
        self.title = "Create a new VM"
        self.size_hint = (None, None)
        self.size = (600, 1200)
        self.text_size = 24

        layout = GridLayout(cols=2, spacing=10, padding=10)

        # Name input
        layout.add_widget(Label(text="Name:", font_size=default_text_size))
        self.name_input = TextInput(multiline=False)
        layout.add_widget(self.name_input)

        # Memory slider
        memory_layout = GridLayout(cols=2)
        memory_layout.add_widget(Label(text="Memory (GB):", font_size=default_text_size))
        self.memory_slider = Slider(min=1, max=8, value=2, step=1)
        memory_layout.add_widget(self.memory_slider)
        self.memory_label = Label(text=str(self.memory_slider.value), font_size=default_text_size)

        self.memory_slider.bind(value=self.update_memory_label)

        layout.add_widget(memory_layout)
        layout.add_widget(self.memory_label)

        # HDD size input
        layout.add_widget(Label(text="HDD (GB):", font_size=default_text_size))
        self.hdd_input = TextInput(multiline=False)
        layout.add_widget(self.hdd_input)

        # ISO file picker
        layout.add_widget(Label(text="ISO Path:", font_size=default_text_size))
        self.iso_input = TextInput(multiline=False)
        layout.add_widget(self.iso_input)


        # CPU count input
        layout.add_widget(Label(text="CPUs:", font_size=default_text_size))
        self.cpu_input = TextInput(multiline=False)
        layout.add_widget(self.cpu_input)

        # IP address input
        layout.add_widget(Label(text="IP Address:", font_size=default_text_size))
        self.ip_input = TextInput(multiline=False)
        layout.add_widget(self.ip_input)

        # Subnet input
        layout.add_widget(Label(text="Subnet:", font_size=default_text_size))
        self.subnet_input = TextInput(multiline=False)
        layout.add_widget(self.subnet_input)

        # Gateway input
        layout.add_widget(Label(text="Gateway:", font_size=default_text_size))
        self.gateway_input = TextInput(multiline=False)
        layout.add_widget(self.gateway_input)

        # DNS input
        layout.add_widget(Label(text="DNS:", font_size=default_text_size))
        self.dns_input = TextInput(multiline=False, text="1.1.1.1,1.0.0.1")
        layout.add_widget(self.dns_input)

        # Button to create VM
        create_button = Button(text="Create VM", font_size=default_text_size)
        create_button.bind(on_press=self.create_vm)
        layout.add_widget(create_button)

        self.add_widget(layout)

    # Triggers when memory slider is changed
    def update_memory_label(self, instance, value):
        self.memory_label.text = str(value)

    def create_vm(self, instance):
        # Get input values
        name = self.name_input.text
        memory = int(self.memory_slider.value)
        hdd = int(self.hdd_input.text)
        iso = self.iso_input.text
        cpus = int(self.cpu_input.text)
        ip = self.ip_input.text
        subnet = self.subnet_input.text
        gateway = self.gateway_input.text
        dns = self.dns_input.text

        # Print input values (for testing)
        print("Name:", name)
        print("Memory (GB):", memory)
        print("HDD (GB):", hdd)
        print("ISO file:", iso)
        print("CPUs:", cpus)
        print("IP Address:", ip)
        print("Subnet:", subnet)
        print("Gateway:", gateway)
        print("DNS:", dns)

class NewVMApp(App):

    def build(self):
        Window.size = (600, 1200)
        new_vm_window = NewVMWindow()
        return new_vm_window

if __name__ == '__main__':
    NewVMApp().run()
