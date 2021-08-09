import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.inside =GridLayout()
        self.inside.cols =2

        self.cols=1
        self.inside.add_widget(Label(text="First Name: "))
        self.name= TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lname = TextInput(multiline=False)
        self.inside.add_widget(self.lname)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit")
        self.submit.bind(on_press =self.pressed)
        self.add_widget(self.submit)
    def pressed(self,instance):
        name=self.name.text
        last=self.lname.text
        email=self.email.text

        print("Name: ",name,"Last: ",last,"email: ",email)
        self.name.text=""
        self.lname.text=''
        self.email.text=""



class MyApp(App):
    def build(self):
        return MyGrid()

if __name__=="__main__":
    MyApp().run()