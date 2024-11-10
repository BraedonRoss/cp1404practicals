import datetime

class Project:
    """Add Project class instance"""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize Project class instance"""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = float(cost_estimate.strip('$'))
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """String representation of Project class instance"""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Less than operator for sorting projects"""
        return self.priority < other.priority

    def is_complete(self):
        """Determine if project is complete"""
        return self.completion_percentage == 100

    def update(self, percentage=None, priority=None):
        """Update percentage and priority of project"""
        if percentage is not None:
            self.completion_percentage = percentage
        if priority is not None:
            self.priority = priority

    def match_start_date(self, filter_date):
        """Determine if project start date matches filter date"""
        return self.start_date > filter_date