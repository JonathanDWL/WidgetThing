from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class GridLayoutExample(GridLayout):
  pass

class BoxLayoutExample(BoxLayout):
  pass

class MainWidget(Widget):
  pass

class WidgetLayoutApp(App):
  pass

class StackLayoutExample(StackLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.orientation = "lr-tb"
    b = Button(text="Touch for good vibes", size_hint=(0.5, 0.5))
    self.add_widget(b)
    c = Button(text="Touch for EVIL vibes.  Absolutely HORRID vibes", size_hint=(0.5, 0.5))
    self.add_widget(c)

class LayoutAssignment(BoxLayout):
  pass

class NumBoard(GridLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.cols = 3
    for i in range(18):
      self.add_widget(Button(text=str(i+1),color=(0.5,1,0.5),background_color=(0,1,0)))


WidgetLayoutApp().run()