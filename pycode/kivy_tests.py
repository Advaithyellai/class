from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        
        self.cols = 1

        self.top_grid = GridLayout()
        self.top_grid.cols = 2
        
        self.top_grid.add_widget(Label(text = "Name: ", font_size = 32))
        
        self.name = TextInput(multiline = False, font_size = 32)
        self.top_grid.add_widget(self.name)
        
        self.top_grid.add_widget(Label(text = "Age: ", font_size = 32))
        
        self.age = TextInput(multiline = False, font_size = 32)
        self.top_grid.add_widget(self.age)
        
        self.top_grid.add_widget(Label(text = "Favourite Colour: ", font_size = 32))
        
        self.colour = TextInput(multiline = False, font_size = 32)
        self.top_grid.add_widget(self.colour)

        self.add_widget(self.top_grid)

        self.submit = Button(text = "SUBMIT!!!", font_size = 32, size_hint_y = None, height = 175)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    
    def press(self, instance):
        self.add_widget(Label(text = f"Hello {self.name.text},\nYou are {self.age.text} years old.\nYour favourite colour is {self.colour.text}!", font_size = 32))

class MyApp(App):
    def build(self):
        return MyGridLayout()

MyApp().run()