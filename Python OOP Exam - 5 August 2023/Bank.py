from abc import ABC, abstractmethod
from typing import List


class BaseLoan(ABC):
    @abstractmethod
    def __init__(self, interest_rate: float, amount: float):
        self.interest_rate = interest_rate
        self.amount = amount

    @abstractmethod
    def increase_interest_rate(self):
        pass


class StudentLoan(BaseLoan):
    INTEREST_RATE = 1.5
    AMOUNT = 2000.0

    def __init__(self):
        super().__init__(interest_rate=StudentLoan.INTEREST_RATE, amount=StudentLoan.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.2


class MortgageLoan(BaseLoan):
    INTEREST_RATE = 3.5
    AMOUNT = 50000.0

    def __init__(self):
        super().__init__(interest_rate=MortgageLoan.INTEREST_RATE, amount=MortgageLoan.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.5


class BaseClient(ABC):
    @abstractmethod
    def __init__(self, name: str, client_id: str, income: float, interest: float):
        self.name = name
        self.client_id = client_id
        self.income = income
        self.interest = interest
        self.loans: List[BaseLoan] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Client name cannot be empty!")
        self.__name = value

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        if len(value) != 10:
            raise ValueError("Client ID should be 10 symbols long!")
        self.__client_id = value

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, value):
        if value <= 0.0:
            raise ValueError("Income must be greater than zero!")
        self.__income = value

    @abstractmethod
    def increase_clients_interest(self):
        pass


class Student(BaseClient):
    INTEREST = 2.0

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, Student.INTEREST)

    def increase_clients_interest(self):
        self.interest += 1.0


class Adult(BaseClient):
    INTEREST = 4.0

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, Adult.INTEREST)

    def increase_clients_interest(self):
        self.interest += 2.0


class BankApp:
    VALID_LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENT_TYPES = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.clients: List[BaseClient] = []
        self.loans: List[BaseLoan] = []

    def get_client(self, client_id: str):
        for client in self.clients:
            if client.client_id == client_id:
                return client

    def get_loan(self, loan_type: str):
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                return loan

    def add_loan(self, loan_type: str):
        if loan_type not in BankApp.VALID_LOAN_TYPES:
            raise Exception("Invalid loan type")
        loan = self.VALID_LOAN_TYPES[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in BankApp.VALID_CLIENT_TYPES:
            raise Exception("Invalid client type")
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."
        new_client = self.VALID_CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self.get_client(client_id)
        loan = self.get_loan(loan_type)
        if loan_type == "StudentLoan" and client.__class__.__name__ != "Student":
            raise Exception("Inappropriate loan type!")
        elif loan_type == "MortgageLoan" and client.__class__.__name__ != "Adult":
            raise Exception("Inappropriate loan type!")
        client.loans.append(loan)
        self.loans.remove(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client.client_id}."

    def remove_client(self, client_id: str):
        client = self.get_client(client_id)
        if not client:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client.client_id}."

    def increase_loan_interest(self, loan_type: str):
        loans = [l for l in self.loans if l.__class__.__name__ == loan_type]
        for loan in loans:
            loan.increase_interest_rate()
        return f"Successfully changed {len(loans)} loans."

    def increase_clients_interest(self, min_rate: float):
        clients = [c for c in self.clients if c.interest < min_rate]
        for client in clients:
            client.increase_clients_interest()
        return f"Number of clients affected: {len(clients)}."

    def get_statistics(self):
        active_clients = len(self.clients)
        total_income = sum([c.income for c in self.clients])

        # Calculate statistics for granted loans
        granted_loans_count = 0
        granted_loans_sum = 0.0
        for client in self.clients:
            for loan in client.loans:
                granted_loans_count += 1
                granted_loans_sum += loan.amount

        # Calculate statistics for available loans
        available_loans_count = len(self.loans)
        available_loans_sum = sum([l.amount for l in self.loans])

        # Calculate average client interest rate
        avg_client_interest_rate = sum([c.interest for c in self.clients]) / active_clients if active_clients else 0

        # Return the formatted string
        return f"Active Clients: {active_clients}\n" \
               f"Total Income: {total_income:.2f}\n" \
               f"Granted Loans: {granted_loans_count}, Total Sum: {granted_loans_sum:.2f}\n" \
               f"Available Loans: {available_loans_count}, Total Sum: {available_loans_sum:.2f}\n" \
               f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"


bank = BankApp(3)

print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))


print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))

print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))

print(bank.remove_client('1234567999'))

print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))

print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))

print(bank.get_statistics())
