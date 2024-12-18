from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class CustomerModel(SQLModel):
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    email: str = Field(default=None)
    age: int = Field(default=None)

class Customer(CustomerModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

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