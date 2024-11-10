import datetime
from operator import attrgetter
from project import Project

FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    """Menu-driven program that allows users to manage projects."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects()
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'l':
            filename = input("Filename to load: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename to save: ")
            save_projects(projects, filename)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_date = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, filter_date)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid option, please choose again.")
        print(MENU)
        choice = input(">>> ").lower()

    save_choice = input("Would you like to save to projects.txt? (y/n): ").lower()
    if save_choice == 'y':
        save_projects(projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename=FILENAME):
    """Load projects from a text file."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()
        for line in file:
            parts = line.strip().split('\t')
            name, start_date, priority, cost_estimate, completion_percentage = parts
            projects.append(Project(name, start_date, int(priority), cost_estimate, int(completion_percentage)))
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def save_projects(projects, filename=FILENAME):
    """Save list to a text file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t${project.cost_estimate:.2f}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Print a neat list of projects sorted by priority."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    complete_projects = [project for project in projects if project.is_complete()]

    incomplete_projects.sort()
    complete_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in complete_projects:
        print(f"  {project}")


def filter_projects_by_date(projects, filter_date):
    """Filter projects after a date."""
    date_obj = datetime.datetime.strptime(filter_date, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.match_start_date(date_obj)]

    print("Filtered projects:")
    for project in sorted(filtered_projects, key=attrgetter('start_date')):
        print(f"  {project}")


def update_project(projects):
    """Update an existing project in a list."""


def add_project(projects):
    """Add a new project to the list."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Completion percentage: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
