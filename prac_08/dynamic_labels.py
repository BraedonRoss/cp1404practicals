from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App to dynamically create Labels from a list of names."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Jack", "Bradon", "Lindsay"]

    def build(self):
        """Build kivy app that generates Labels from a list of names."""
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)
        return self.root


DynamicLabelsApp().run()
