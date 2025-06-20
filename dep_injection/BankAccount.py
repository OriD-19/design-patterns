import sys

class Logger:

    def __init__(self, output_stream=sys.stdout):
        self.log_register = []
        self.output_stream = output_stream

    def log(self, content):
        msg = f"[LOG] {content}"
        self.log_register.append(msg)
        print(msg, file=self.output_stream)

    def log_transaction(self, amount):
        self.log(f"Se transfirieron ${amount:.2f}")

class EmailService:
    
    def __init__(self, smtp_conn):
        self.smtp_conn = smtp_conn

    def send_email(self, content):
        print(f"[EMAIL] Enviando email: {content}")

    def send_transaction_confirmed(self, amount):
        self.send_email(f"Se transfirieron ${amount:.2f} a su cuenta")


class CuentaBancaria:

    def __init__(self, logger: Logger, email_service: EmailService):
        self.balance = 0
        self.logger: Logger = logger
        self.email_service: EmailService = email_service

    def transferir(self, amount):
        self.balance += amount
        self.logger.log_transaction(amount)
        self.email_service.send_transaction_confirmed(amount)

logger = Logger()
email = EmailService("SMTP conn")

cuenta = CuentaBancaria(logger, email)

cuenta.transferir(300)
