import self
from kivy.uix.floatlayout import FloatLayout

from kivy.app import App

from kivy.uix.label import Label

from kivy.uix.button import Button

from kivy.uix.textinput import TextInput



class Interface(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn=Button(text="hello", size_hint=(0.5,0.1), pos_hint={"center_x":0.5,"center_y":0.5})
        lb1 = Label(text="Amany", size_hint=(0.5, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.4})
        txi1 = TextInput(text="I Love you", size_hint=(0.5, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.3})
        lb2 = Label(text="{for ever}", size_hint=(0.5, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.2})


        self.add_widget(btn)
        self.add_widget(lb1)
        self.add_widget(txi1)
        self.add_widget(lb2)


class ProjectApp(App):
    def build(self):
        return Interface()


ProjectApp().run()



