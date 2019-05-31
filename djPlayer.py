import kivy

kivy.require('1.0.7')
from kivy.uix.button import Label,Button
from kivy.uix.video import Video
from kivy.app import App
from kivy.uix.filechooser import FileChooser
from kivy.uix.boxlayout import BoxLayout


class Pan(BoxLayout):
    nb=0
    def __init__(self):
        super(Pan, self).__init__()
        self.filech=FileChooser()
        self.orientation='vertical'
        self.size_hint=(1,1)
        self.btn1=Button(text='ouvrir')
        self.aff=Label(text="Nombre de click ".format(Pan.nb))
        def hello(v):
            Pan.nb+=1
            self.aff.text="Nombre de click {}".format(Pan.nb)
            print("ca marche")
        self.btn1.bind(on_press=hello)
        self.add_widget(self.aff)
        self.add_widget(self.btn1)
        print('je suis la')


class Mon(App):
    def build(self):

        p=Pan()
        #p.Pan()
        #p.orientation='vertical'
        self.title="djPlayer"
        p.add_widget(Label(text='prenom'))
        p.add_widget(Label(text='nom'))
        return p


Mon().run()