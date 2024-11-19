from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class MilesConverter(App):

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self):
        value = float(self.root.ids.miles_input.text)
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment_change(self, change):
        value = float(self.root.ids.miles_input.text) + change
        self.root.ids.miles_input.text = str(value)
        self.handle_calculation()

MilesConverter().run()