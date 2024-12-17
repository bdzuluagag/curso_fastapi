from pydantic import BaseModel

class CustomerModel(BaseModel):
    name: str
    description: str | None
    email: str
    age: int

class Customer(CustomerModel):
    id: int | None = None

class CustomerCreate(CustomerModel):
    pass

class Transaction(BaseModel):
    id: int
    ammount: int
    description: str

class Invoice(BaseModel):
    id: int
    customer: CustomerModel
    transactions: list[Transaction]
    total: int

    @property
    def ammount_total(self):
        return sum(transaction.ammount for transaction in self.transactions)