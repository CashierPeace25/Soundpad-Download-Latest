class Project:
    def __init__(self, name):
        self.name = name
        self.expenses = []

    def add_expense(self, description, amount):
        self.expenses.append({
            "description": description,
            "amount": amount
        })

    def total_cost(self):
        return sum(item["amount"] for item in self.expenses)


class BudgetManager:
    def __init__(self):
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def print_report(self):
        print("Project Budget Report")
        print("=====================")

        overall_total = 0

        for project in sorted(self.projects, key=lambda p: p.name):
            print(f"\n{project.name}")

            for expense in project.expenses:
                print(
                    f"  {expense['description']} - ${expense['amount']:.2f}"
                )

            total = project.total_cost()
            overall_total += total

            print(f"  Total: ${total:.2f}")

        print("\n=====================")
        print(f"Overall Budget: ${overall_total:.2f}")


def main():
    website = Project("Website")
    website.add_expense("Hosting", 120)
    website.add_expense("Domain", 18)
    website.add_expense("Design", 350)

    mobile = Project("Mobile App")
    mobile.add_expense("Icons", 90)
    mobile.add_expense("Testing", 210)

    manager = BudgetManager()

    manager.add_project(website)
    manager.add_project(mobile)

    manager.print_report()


if __name__ == "__main__":
    main()
