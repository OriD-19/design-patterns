from abc import ABC, abstractmethod

class Exporter(ABC):

    @abstractmethod
    def export(self):
        pass


class PDFExporter(Exporter):
    def export(self):
        return "PDF"

class HTMLExporter(Exporter):

    def export(self):
        return "HTML"


class JSONExporter(Exporter):

    def export(self):
        return "JSON"

class Report(ABC):

    @abstractmethod
    def generate_report(self) -> str:
        pass

class UserReport(Report):

    def __init__(self, exporter: Exporter):
        self.report_type = "User"
        self.exporter = exporter

    def generate_report(self) -> str:
        return f"Exporting {self.report_type} Report to {self.exporter.export()}..."

class SalesReport(Report):
    def __init__(self, exporter: Exporter):
        self.report_type = "Sales"
        self.exporter = exporter

    def generate_report(self) -> str:
        return f"Exporting {self.report_type} Report to {self.exporter.export()}..."

class InventoryReport(Report):
    def __init__(self, exporter: Exporter):
        self.report_type = "Inventory"
        self.exporter = exporter

    def generate_report(self) -> str:
        return f"Exporting {self.report_type} Report to {self.exporter.export()}..."


pdf = PDFExporter()
html = HTMLExporter()
user_report = UserReport(pdf)
sales_report = SalesReport(pdf)
inventory_report = InventoryReport(html)

print(user_report.generate_report())
print(sales_report.generate_report())
print(inventory_report.generate_report())
