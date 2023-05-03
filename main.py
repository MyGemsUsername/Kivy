from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.vertex_instructions import Rectangle

import dataTerm1
import dataTerm2
import dataTerm3

# -----------------------------------------BORDER----------------------------------------- #




class TermsWidget(BoxLayout):
    pass
class MainWindow(Screen):
    pass
class Term1Window(Screen):
    pass
class Term2Window(Screen):
    pass
class Term3Window(Screen):
    pass
class WindowManager(ScreenManager):
    pass
class mymain(App):
    pass

# Term 1 Windows
class T1W1Window(Screen):
    topicY9=dataTerm1.Y9T1topic1
    topicY8=dataTerm1.Y8T1topic1
    topicY7=dataTerm1.Y7T1topic1
    topicY6=dataTerm1.Y6T1topic1
    hostY9=dataTerm1.Y9T1host1
    hostY8=dataTerm1.Y9T1host1
    hostY7=dataTerm1.Y9T1host1
    hostY6=dataTerm1.Y9T1host1
    presenterY9=dataTerm1.Y9T1presenter1
    presenterY8=dataTerm1.Y9T1presenter1
    presenterY7=dataTerm1.Y9T1presenter1
    presenterY6=dataTerm1.Y9T1presenter1
class T1W2Window(Screen):
    topicY9=dataTerm1.Y9T1topic2
    topicY8=dataTerm1.Y8T1topic2
    topicY7=dataTerm1.Y7T1topic2
    topicY6=dataTerm1.Y6T1topic2
    hostY9=dataTerm1.Y9T1host2
    hostY8=dataTerm1.Y9T1host2
    hostY7=dataTerm1.Y9T1host2
    hostY6=dataTerm1.Y9T1host2
    presenterY9=dataTerm1.Y9T1presenter2
    presenterY8=dataTerm1.Y9T1presenter2
    presenterY7=dataTerm1.Y9T1presenter2
    presenterY6=dataTerm1.Y9T1presenter2
class T1W3Window(Screen):
    topicY9=dataTerm1.Y9T1topic3
    topicY8=dataTerm1.Y8T1topic3
    topicY7=dataTerm1.Y7T1topic3
    topicY6=dataTerm1.Y6T1topic3
    hostY9=dataTerm1.Y9T1host3
    hostY8=dataTerm1.Y9T1host3
    hostY7=dataTerm1.Y9T1host3
    hostY6=dataTerm1.Y9T1host3
    presenterY9=dataTerm1.Y9T1presenter3
    presenterY8=dataTerm1.Y9T1presenter3
    presenterY7=dataTerm1.Y9T1presenter3
    presenterY6=dataTerm1.Y9T1presenter3
class T1W4Window(Screen):
    topicY9=dataTerm1.Y9T1topic4
    topicY8=dataTerm1.Y8T1topic4
    topicY7=dataTerm1.Y7T1topic4
    topicY6=dataTerm1.Y6T1topic4
    hostY9=dataTerm1.Y9T1host4
    hostY8=dataTerm1.Y9T1host4
    hostY7=dataTerm1.Y9T1host4
    hostY6=dataTerm1.Y9T1host4
    presenterY9=dataTerm1.Y9T1presenter4
    presenterY8=dataTerm1.Y9T1presenter4
    presenterY7=dataTerm1.Y9T1presenter4
    presenterY6=dataTerm1.Y9T1presenter4
class T1W5Window(Screen):
    topicY9=dataTerm1.Y9T1topic5
    topicY8=dataTerm1.Y8T1topic5
    topicY7=dataTerm1.Y7T1topic5
    topicY6=dataTerm1.Y6T1topic5
    hostY9=dataTerm1.Y9T1host5
    hostY8=dataTerm1.Y9T1host5
    hostY7=dataTerm1.Y9T1host5
    hostY6=dataTerm1.Y9T1host5
    presenterY9=dataTerm1.Y9T1presenter5
    presenterY8=dataTerm1.Y9T1presenter5
    presenterY7=dataTerm1.Y9T1presenter5
    presenterY6=dataTerm1.Y9T1presenter5
class T1W6Window(Screen):
    topicY9=dataTerm1.Y9T1topic6
    topicY8=dataTerm1.Y8T1topic6
    topicY7=dataTerm1.Y7T1topic6
    topicY6=dataTerm1.Y6T1topic6
    hostY9=dataTerm1.Y9T1host6
    hostY8=dataTerm1.Y9T1host6
    hostY7=dataTerm1.Y9T1host6
    hostY6=dataTerm1.Y9T1host6
    presenterY9=dataTerm1.Y9T1presenter6
    presenterY8=dataTerm1.Y9T1presenter6
    presenterY7=dataTerm1.Y9T1presenter6
    presenterY6=dataTerm1.Y9T1presenter6
class T1W7Window(Screen):
    topicY9=dataTerm1.Y9T1topic7
    topicY8=dataTerm1.Y8T1topic7
    topicY7=dataTerm1.Y7T1topic7
    topicY6=dataTerm1.Y6T1topic7
    hostY9=dataTerm1.Y9T1host7
    hostY8=dataTerm1.Y9T1host7
    hostY7=dataTerm1.Y9T1host7
    hostY6=dataTerm1.Y9T1host7
    presenterY9=dataTerm1.Y9T1presenter7
    presenterY8=dataTerm1.Y9T1presenter7
    presenterY7=dataTerm1.Y9T1presenter7
    presenterY6=dataTerm1.Y9T1presenter7
class T1W8Window(Screen):
    topicY9=dataTerm1.Y9T1topic8
    topicY8=dataTerm1.Y8T1topic8
    topicY7=dataTerm1.Y7T1topic8
    topicY6=dataTerm1.Y6T1topic8
    hostY9=dataTerm1.Y9T1host8
    hostY8=dataTerm1.Y9T1host8
    hostY7=dataTerm1.Y9T1host8
    hostY6=dataTerm1.Y9T1host8
    presenterY9=dataTerm1.Y9T1presenter8
    presenterY8=dataTerm1.Y9T1presenter8
    presenterY7=dataTerm1.Y9T1presenter8
    presenterY6=dataTerm1.Y9T1presenter8
class T1W9Window(Screen):
    topicY9=dataTerm1.Y9T1topic9
    topicY8=dataTerm1.Y8T1topic9
    topicY7=dataTerm1.Y7T1topic9
    topicY6=dataTerm1.Y6T1topic9
    hostY9=dataTerm1.Y9T1host9
    hostY8=dataTerm1.Y9T1host9
    hostY7=dataTerm1.Y9T1host9
    hostY6=dataTerm1.Y9T1host9
    presenterY9=dataTerm1.Y9T1presenter9
    presenterY8=dataTerm1.Y9T1presenter9
    presenterY7=dataTerm1.Y9T1presenter9
    presenterY6=dataTerm1.Y9T1presenter9
class T1W10Window(Screen):
    topicY9=dataTerm1.Y9T1topic10
    topicY8=dataTerm1.Y8T1topic10
    topicY7=dataTerm1.Y7T1topic10
    topicY6=dataTerm1.Y6T1topic10
    hostY9=dataTerm1.Y9T1host10
    hostY8=dataTerm1.Y9T1host10
    hostY7=dataTerm1.Y9T1host10
    hostY6=dataTerm1.Y9T1host10
    presenterY9=dataTerm1.Y9T1presenter10
    presenterY8=dataTerm1.Y9T1presenter10
    presenterY7=dataTerm1.Y9T1presenter10
    presenterY6=dataTerm1.Y9T1presenter10
class T1W11Window(Screen):
    topicY9=dataTerm1.Y9T1topic11
    topicY8=dataTerm1.Y8T1topic11
    topicY7=dataTerm1.Y7T1topic11
    topicY6=dataTerm1.Y6T1topic11
    hostY9=dataTerm1.Y9T1host11
    hostY8=dataTerm1.Y9T1host11
    hostY7=dataTerm1.Y9T1host11
    hostY6=dataTerm1.Y9T1host11
    presenterY9=dataTerm1.Y9T1presenter11
    presenterY8=dataTerm1.Y9T1presenter11
    presenterY7=dataTerm1.Y9T1presenter11
    presenterY6=dataTerm1.Y9T1presenter11
class T1W12Window(Screen):
    topicY9=dataTerm1.Y9T1topic12
    topicY8=dataTerm1.Y8T1topic12
    topicY7=dataTerm1.Y7T1topic12
    topicY6=dataTerm1.Y6T1topic12
    hostY9=dataTerm1.Y9T1host12
    hostY8=dataTerm1.Y9T1host12
    hostY7=dataTerm1.Y9T1host12
    hostY6=dataTerm1.Y9T1host12
    presenterY9=dataTerm1.Y9T1presenter12
    presenterY8=dataTerm1.Y9T1presenter12
    presenterY7=dataTerm1.Y9T1presenter12
    presenterY6=dataTerm1.Y9T1presenter12
class T1W13Window(Screen):
    topicY9=dataTerm1.Y9T1topic13
    topicY8=dataTerm1.Y8T1topic13
    topicY7=dataTerm1.Y7T1topic13
    topicY6=dataTerm1.Y6T1topic13
    hostY9=dataTerm1.Y9T1host13
    hostY8=dataTerm1.Y9T1host13
    hostY7=dataTerm1.Y9T1host13
    hostY6=dataTerm1.Y9T1host13
    presenterY9=dataTerm1.Y9T1presenter13
    presenterY8=dataTerm1.Y9T1presenter13
    presenterY7=dataTerm1.Y9T1presenter13
    presenterY6=dataTerm1.Y9T1presenter13
class T1W14Window(Screen):
    topicY9=dataTerm1.Y9T1topic14
    topicY8=dataTerm1.Y8T1topic14
    topicY7=dataTerm1.Y7T1topic14
    topicY6=dataTerm1.Y6T1topic14
    hostY9=dataTerm1.Y9T1host14
    hostY8=dataTerm1.Y9T1host14
    hostY7=dataTerm1.Y9T1host14
    hostY6=dataTerm1.Y9T1host14
    presenterY9=dataTerm1.Y9T1presenter14
    presenterY8=dataTerm1.Y9T1presenter14
    presenterY7=dataTerm1.Y9T1presenter14
    presenterY6=dataTerm1.Y9T1presenter14

# Term 2 Windows
class T2W1Window(Screen):
    topicY9=dataTerm2.Y9T2topic1
    topicY8=dataTerm2.Y8T2topic1
    topicY7=dataTerm2.Y7T2topic1
    topicY6=dataTerm2.Y6T2topic1
    hostY9=dataTerm2.Y9T2host1
    hostY8=dataTerm2.Y9T2host1
    hostY7=dataTerm2.Y9T2host1
    hostY6=dataTerm2.Y9T2host1
    presenterY9=dataTerm2.Y9T2presenter1
    presenterY8=dataTerm2.Y9T2presenter1
    presenterY7=dataTerm2.Y9T2presenter1
    presenterY6=dataTerm2.Y9T2presenter1
class T2W2Window(Screen):
    topicY9=dataTerm2.Y9T2topic2
    topicY8=dataTerm2.Y8T2topic2
    topicY7=dataTerm2.Y7T2topic2
    topicY6=dataTerm2.Y6T2topic2
    hostY9=dataTerm2.Y9T2host2
    hostY8=dataTerm2.Y9T2host2
    hostY7=dataTerm2.Y9T2host2
    hostY6=dataTerm2.Y9T2host2
    presenterY9=dataTerm2.Y9T2presenter2
    presenterY8=dataTerm2.Y9T2presenter2
    presenterY7=dataTerm2.Y9T2presenter2
    presenterY6=dataTerm2.Y9T2presenter2
class T2W3Window(Screen):
    topicY9=dataTerm2.Y9T2topic3
    topicY8=dataTerm2.Y8T2topic3
    topicY7=dataTerm2.Y7T2topic3
    topicY6=dataTerm2.Y6T2topic3
    hostY9=dataTerm2.Y9T2host3
    hostY8=dataTerm2.Y9T2host3
    hostY7=dataTerm2.Y9T2host3
    hostY6=dataTerm2.Y9T2host3
    presenterY9=dataTerm2.Y9T2presenter3
    presenterY8=dataTerm2.Y9T2presenter3
    presenterY7=dataTerm2.Y9T2presenter3
    presenterY6=dataTerm2.Y9T2presenter3
class T2W4Window(Screen):   
    topicY9=dataTerm2.Y9T2topic4
    topicY8=dataTerm2.Y8T2topic4
    topicY7=dataTerm2.Y7T2topic4
    topicY6=dataTerm2.Y6T2topic4
    hostY9=dataTerm2.Y9T2host4
    hostY8=dataTerm2.Y9T2host4
    hostY7=dataTerm2.Y9T2host4
    hostY6=dataTerm2.Y9T2host4
    presenterY9=dataTerm2.Y9T2presenter4
    presenterY8=dataTerm2.Y9T2presenter4
    presenterY7=dataTerm2.Y9T2presenter4
    presenterY6=dataTerm2.Y9T2presenter4
class T2W5Window(Screen):
    topicY9=dataTerm2.Y9T2topic5
    topicY8=dataTerm2.Y8T2topic5
    topicY7=dataTerm2.Y7T2topic5
    topicY6=dataTerm2.Y6T2topic5
    hostY9=dataTerm2.Y9T2host5
    hostY8=dataTerm2.Y9T2host5
    hostY7=dataTerm2.Y9T2host5
    hostY6=dataTerm2.Y9T2host5
    presenterY9=dataTerm2.Y9T2presenter5
    presenterY8=dataTerm2.Y9T2presenter5
    presenterY7=dataTerm2.Y9T2presenter5
    presenterY6=dataTerm2.Y9T2presenter5
class T2W6Window(Screen):
    topicY9=dataTerm2.Y9T2topic6
    topicY8=dataTerm2.Y8T2topic6
    topicY7=dataTerm2.Y7T2topic6
    topicY6=dataTerm2.Y6T2topic6
    hostY9=dataTerm2.Y9T2host6
    hostY8=dataTerm2.Y9T2host6
    hostY7=dataTerm2.Y9T2host6
    hostY6=dataTerm2.Y9T2host6
    presenterY9=dataTerm2.Y9T2presenter6
    presenterY8=dataTerm2.Y9T2presenter6
    presenterY7=dataTerm2.Y9T2presenter6
    presenterY6=dataTerm2.Y9T2presenter6
class T2W7Window(Screen):
    topicY9=dataTerm2.Y9T2topic7
    topicY8=dataTerm2.Y8T2topic7
    topicY7=dataTerm2.Y7T2topic7
    topicY6=dataTerm2.Y6T2topic7
    hostY9=dataTerm2.Y9T2host7
    hostY8=dataTerm2.Y9T2host7
    hostY7=dataTerm2.Y9T2host7
    hostY6=dataTerm2.Y9T2host7
    presenterY9=dataTerm2.Y9T2presenter7
    presenterY8=dataTerm2.Y9T2presenter7
    presenterY7=dataTerm2.Y9T2presenter7
    presenterY6=dataTerm2.Y9T2presenter7
class T2W8Window(Screen):
    topicY9=dataTerm2.Y9T2topic8
    topicY8=dataTerm2.Y8T2topic8
    topicY7=dataTerm2.Y7T2topic8
    topicY6=dataTerm2.Y6T2topic8
    hostY9=dataTerm2.Y9T2host8
    hostY8=dataTerm2.Y9T2host8
    hostY7=dataTerm2.Y9T2host8
    hostY6=dataTerm2.Y9T2host8
    presenterY9=dataTerm2.Y9T2presenter8
    presenterY8=dataTerm2.Y9T2presenter8
    presenterY7=dataTerm2.Y9T2presenter8
    presenterY6=dataTerm2.Y9T2presenter8
class T2W9Window(Screen):
    topicY9=dataTerm2.Y9T2topic9
    topicY8=dataTerm2.Y8T2topic9
    topicY7=dataTerm2.Y7T2topic9
    topicY6=dataTerm2.Y6T2topic9
    hostY9=dataTerm2.Y9T2host9
    hostY8=dataTerm2.Y9T2host9
    hostY7=dataTerm2.Y9T2host9
    hostY6=dataTerm2.Y9T2host9
    presenterY9=dataTerm2.Y9T2presenter9
    presenterY8=dataTerm2.Y9T2presenter9
    presenterY7=dataTerm2.Y9T2presenter9
    presenterY6=dataTerm2.Y9T2presenter9
class T2W10Window(Screen):
    topicY9=dataTerm2.Y9T2topic10
    topicY8=dataTerm2.Y8T2topic10
    topicY7=dataTerm2.Y7T2topic10
    topicY6=dataTerm2.Y6T2topic10
    hostY9=dataTerm2.Y9T2host10
    hostY8=dataTerm2.Y9T2host10
    hostY7=dataTerm2.Y9T2host10
    hostY6=dataTerm2.Y9T2host10
    presenterY9=dataTerm2.Y9T2presenter10
    presenterY8=dataTerm2.Y9T2presenter10
    presenterY7=dataTerm2.Y9T2presenter10
    presenterY6=dataTerm2.Y9T2presenter10
class T2W11Window(Screen):
    topicY9=dataTerm2.Y9T2topic11
    topicY8=dataTerm2.Y8T2topic11
    topicY7=dataTerm2.Y7T2topic11
    topicY6=dataTerm2.Y6T2topic11
    hostY9=dataTerm2.Y9T2host11
    hostY8=dataTerm2.Y9T2host11
    hostY7=dataTerm2.Y9T2host11
    hostY6=dataTerm2.Y9T2host11
    presenterY9=dataTerm2.Y9T2presenter11
    presenterY8=dataTerm2.Y9T2presenter11
    presenterY7=dataTerm2.Y9T2presenter11
    presenterY6=dataTerm2.Y9T2presenter11
class T2W12Window(Screen):
    topicY9=dataTerm2.Y9T2topic12
    topicY8=dataTerm2.Y8T2topic12
    topicY7=dataTerm2.Y7T2topic12
    topicY6=dataTerm2.Y6T2topic12
    hostY9=dataTerm2.Y9T2host12
    hostY8=dataTerm2.Y9T2host12
    hostY7=dataTerm2.Y9T2host12
    hostY6=dataTerm2.Y9T2host12
    presenterY9=dataTerm2.Y9T2presenter12
    presenterY8=dataTerm2.Y9T2presenter12
    presenterY7=dataTerm2.Y9T2presenter12
    presenterY6=dataTerm2.Y9T2presenter12
# Term 3 Windows
class T3W1Window(Screen):
    topicY9=dataTerm3.Y9T3topic1
    topicY8=dataTerm3.Y8T3topic1
    topicY7=dataTerm3.Y7T3topic1
    topicY6=dataTerm3.Y6T3topic1
    hostY9=dataTerm3.Y9T3host1
    hostY8=dataTerm3.Y9T3host1
    hostY7=dataTerm3.Y9T3host1
    hostY6=dataTerm3.Y9T3host1
    presenterY9=dataTerm3.Y9T3presenter1
    presenterY8=dataTerm3.Y9T3presenter1
    presenterY7=dataTerm3.Y9T3presenter1
    presenterY6=dataTerm3.Y9T3presenter1
class T3W2Window(Screen):
    topicY9=dataTerm3.Y9T3topic2
    topicY8=dataTerm3.Y8T3topic2
    topicY7=dataTerm3.Y7T3topic2
    topicY6=dataTerm3.Y6T3topic2
    hostY9=dataTerm3.Y9T3host2
    hostY8=dataTerm3.Y9T3host2
    hostY7=dataTerm3.Y9T3host2
    hostY6=dataTerm3.Y9T3host2
    presenterY9=dataTerm3.Y9T3presenter2
    presenterY8=dataTerm3.Y9T3presenter2
    presenterY7=dataTerm3.Y9T3presenter2
    presenterY6=dataTerm3.Y9T3presenter2
class T3W3Window(Screen):
    topicY9=dataTerm3.Y9T3topic3
    topicY8=dataTerm3.Y8T3topic3
    topicY7=dataTerm3.Y7T3topic3
    topicY6=dataTerm3.Y6T3topic3
    hostY9=dataTerm3.Y9T3host3
    hostY8=dataTerm3.Y9T3host3
    hostY7=dataTerm3.Y9T3host3
    hostY6=dataTerm3.Y9T3host3
    presenterY9=dataTerm3.Y9T3presenter3
    presenterY8=dataTerm3.Y9T3presenter3
    presenterY7=dataTerm3.Y9T3presenter3
    presenterY6=dataTerm3.Y9T3presenter3
class T3W4Window(Screen):
    topicY9=dataTerm3.Y9T3topic4
    topicY8=dataTerm3.Y8T3topic4
    topicY7=dataTerm3.Y7T3topic4
    topicY6=dataTerm3.Y6T3topic4
    hostY9=dataTerm3.Y9T3host4
    hostY8=dataTerm3.Y9T3host4
    hostY7=dataTerm3.Y9T3host4
    hostY6=dataTerm3.Y9T3host4
    presenterY9=dataTerm3.Y9T3presenter4
    presenterY8=dataTerm3.Y9T3presenter4
    presenterY7=dataTerm3.Y9T3presenter4
    presenterY6=dataTerm3.Y9T3presenter4
class T3W5Window(Screen):
    topicY9=dataTerm3.Y9T3topic5
    topicY8=dataTerm3.Y8T3topic5
    topicY7=dataTerm3.Y7T3topic5
    topicY6=dataTerm3.Y6T3topic5
    hostY9=dataTerm3.Y9T3host5
    hostY8=dataTerm3.Y9T3host5
    hostY7=dataTerm3.Y9T3host5
    hostY6=dataTerm3.Y9T3host5
    presenterY9=dataTerm3.Y9T3presenter5
    presenterY8=dataTerm3.Y9T3presenter5
    presenterY7=dataTerm3.Y9T3presenter5
    presenterY6=dataTerm3.Y9T3presenter5
class T3W6Window(Screen):
    topicY9=dataTerm3.Y9T3topic6
    topicY8=dataTerm3.Y8T3topic6
    topicY7=dataTerm3.Y7T3topic6
    topicY6=dataTerm3.Y6T3topic6
    hostY9=dataTerm3.Y9T3host6
    hostY8=dataTerm3.Y9T3host6
    hostY7=dataTerm3.Y9T3host6
    hostY6=dataTerm3.Y9T3host6
    presenterY9=dataTerm3.Y9T3presenter6
    presenterY8=dataTerm3.Y9T3presenter6
    presenterY7=dataTerm3.Y9T3presenter6
    presenterY6=dataTerm3.Y9T3presenter6
class T3W7Window(Screen):
    topicY9=dataTerm3.Y9T3topic7
    topicY8=dataTerm3.Y8T3topic7
    topicY7=dataTerm3.Y7T3topic7
    topicY6=dataTerm3.Y6T3topic7
    hostY9=dataTerm3.Y9T3host7
    hostY8=dataTerm3.Y9T3host7
    hostY7=dataTerm3.Y9T3host7
    hostY6=dataTerm3.Y9T3host7
    presenterY9=dataTerm3.Y9T3presenter7
    presenterY8=dataTerm3.Y9T3presenter7
    presenterY7=dataTerm3.Y9T3presenter7
    presenterY6=dataTerm3.Y9T3presenter7
class T3W8Window(Screen):
    topicY9=dataTerm3.Y9T3topic8
    topicY8=dataTerm3.Y8T3topic8
    topicY7=dataTerm3.Y7T3topic8
    topicY6=dataTerm3.Y6T3topic8
    hostY9=dataTerm3.Y9T3host8
    hostY8=dataTerm3.Y9T3host8
    hostY7=dataTerm3.Y9T3host8
    hostY6=dataTerm3.Y9T3host8
    presenterY9=dataTerm3.Y9T3presenter8
    presenterY8=dataTerm3.Y9T3presenter8
    presenterY7=dataTerm3.Y9T3presenter8
    presenterY6=dataTerm3.Y9T3presenter8
class T3W9Window(Screen):
    topicY9=dataTerm3.Y9T3topic9
    topicY8=dataTerm3.Y8T3topic9
    topicY7=dataTerm3.Y7T3topic9
    topicY6=dataTerm3.Y6T3topic9
    hostY9=dataTerm3.Y9T3host9
    hostY8=dataTerm3.Y9T3host9
    hostY7=dataTerm3.Y9T3host9
    hostY6=dataTerm3.Y9T3host9
    presenterY9=dataTerm3.Y9T3presenter9
    presenterY8=dataTerm3.Y9T3presenter9
    presenterY7=dataTerm3.Y9T3presenter9
    presenterY6=dataTerm3.Y9T3presenter9
class T3W10Window(Screen):
    topicY9=dataTerm3.Y9T3topic10
    topicY8=dataTerm3.Y8T3topic10
    topicY7=dataTerm3.Y7T3topic10
    topicY6=dataTerm3.Y6T3topic10
    hostY9=dataTerm3.Y9T3host10
    hostY8=dataTerm3.Y9T3host10
    hostY7=dataTerm3.Y9T3host10
    hostY6=dataTerm3.Y9T3host10
    presenterY9=dataTerm3.Y9T3presenter10
    presenterY8=dataTerm3.Y9T3presenter10
    presenterY7=dataTerm3.Y9T3presenter10
    presenterY6=dataTerm3.Y9T3presenter10
class T3W11Window(Screen):
    topicY9=dataTerm3.Y9T3topic11
    topicY8=dataTerm3.Y8T3topic11
    topicY7=dataTerm3.Y7T3topic11
    topicY6=dataTerm3.Y6T3topic11
    hostY9=dataTerm3.Y9T3host11
    hostY8=dataTerm3.Y9T3host11
    hostY7=dataTerm3.Y9T3host11
    hostY6=dataTerm3.Y9T3host11
    presenterY9=dataTerm3.Y9T3presenter11
    presenterY8=dataTerm3.Y9T3presenter11
    presenterY7=dataTerm3.Y9T3presenter11
    presenterY6=dataTerm3.Y9T3presenter11
class T3W12Window(Screen):
    topicY9=dataTerm3.Y9T3topic12
    topicY8=dataTerm3.Y8T3topic12
    topicY7=dataTerm3.Y7T3topic12
    topicY6=dataTerm3.Y6T3topic12
    hostY9=dataTerm3.Y9T3host12
    hostY8=dataTerm3.Y9T3host12
    hostY7=dataTerm3.Y9T3host12
    hostY6=dataTerm3.Y9T3host12
    presenterY9=dataTerm3.Y9T3presenter12
    presenterY8=dataTerm3.Y9T3presenter12
    presenterY7=dataTerm3.Y9T3presenter12
    presenterY6=dataTerm3.Y9T3presenter12




kv = Builder.load_file("mymain.kv")


class MyMainApp(App):
    def build(self):
        return kv
if __name__ == "__main__":
    MyMainApp().run()


