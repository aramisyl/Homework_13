class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def change_password(self, new_password):
        print(f"{self.name} is changed password {self.password} to {new_password}")


class AuthService:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def register(self):
        print(f"{self.name} is registered with email {self.email} and password {self.password}")

    def login(self):
        print(f"{self.name} is logged in with email {self.email} and password {self.password}")

    def logout(self):
        print(f"{self.name} is logged out")


class EmailService:
    def __init__(self, name):
        self.name = name

    def send_email(self, subject, message, recipients):
        print(f"{self.name} is sent message {message} with {subject} to {recipients}")


class ReportService:
    def __init__(self, name):
        self.name = name

    def generate_report(self, data):
        print(f"{self.name} is generated report with data {data}")
