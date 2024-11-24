from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class MilesConverter(App):
    """App to convert miles to kilometers."""

    def build(self):
        """Build the Kivy app interface."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self):
        """Calculate kilometers from miles and update the output label."""
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment_change(self, change):
        """Increment or decrement the miles value and recalculate."""
        value = self.get_validated_miles() + change
        self.root.ids.miles_input.text = str(value)
        self.handle_calculation()

    def get_validated_miles(self):
        """Validate the miles input and return it as a float, or 0 if invalid."""
        try:
            value = float(self.root.ids.miles_input.text)
            return value
        except ValueError:
            return 0

MilesConverter().run()
