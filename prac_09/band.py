class Band:
    """Band class to manage a collection of musicians."""

    def __init__(self, name=""):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"
