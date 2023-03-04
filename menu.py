import kivy
from subprocess import Popen, PIPE
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window

class VMMenu(GridLayout):

    def __init__(self, **kwargs):
        super(VMMenu, self).__init__(**kwargs)
        self.cols = 1

        # Set the size of the window
        self.size_hint = (None, None)
        self.size = (400, 400)

        # Center the grid in the window
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        # Font Size
        font_size_button = 24

        # Button to create a VM
        self.create_vm_button = Button(
            text='Create a VM',
            font_size=font_size_button
        )
        # On-Click: Create new VM (calls create_vm)
        self.create_vm_button.bind(on_press=self.create_vm)
        self.add_widget(self.create_vm_button)

        # Button to list, start and stop VMs
        self.list_vm_button = Button(
            text='VM List',
            font_size=font_size_button
        )
        self.list_vm_button.bind(on_press=self.list_vm)
        self.add_widget(self.list_vm_button)

        # Button to open GUI to VM
        self.open_vm_button = Button(
            text='Open GUI to VM',
            font_size=font_size_button
        )
        self.open_vm_button.bind(on_press=self.open_vm)
        self.add_widget(self.open_vm_button)

    def create_vm(self, instance):
        # Pop new window by running script
        process = Popen(['python3', 'bin/new_vm.py'], stdout=PIPE, stderr=PIPE)
    
    def list_vm(self, instance):
        print("List VM")

    def open_vm(self, instance):
        print("Open GUI")

class CreateVMWindow(App):

    def build(self):
        Window.title = "Create a VM"
        Window.size = (600, 600)
        # Add your widgets here

class VMMenuApp(App):

    def build(self):
        Window.size = (600, 600)
        return VMMenu()

if __name__ == '__main__':
    VMMenuApp().run()
