from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

#Define different screens
class StartScreen(Screen):
    pass

class InfoScreen(Screen):
    pass

class FoodListScreen(Screen):
    pass

class WeightingScreen(Screen):
    pass

class MacroTrackerScreen(Screen):
    pass

class FoodSelectionScreen(Screen):
    pass

class PhotoScannerScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

#Designate kv design file
kv = Builder.load_file('design.kv')

class NutritionScanner(App):
    def build(self):
        return kv
    
if __name__ == '__main__':
    ns = NutritionScanner()
    ns.run()