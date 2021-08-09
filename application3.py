import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.graphics import *
Window.clearcolor=(0.5,0.6,0.1,1)



    with self.canvas:
        Color(1,1,1)
        Rectangle(pos(10,10),size=(500,500))

class KvApp(App):
    def build(self):
        return


if __name__ == "__main__":
    KvApp().run()