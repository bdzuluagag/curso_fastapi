from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship


class CustomerModel(SQLModel):
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    email: str = Field(default=None)
    age: int = Field(default=None)


class Customer(CustomerModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    transactions: list["Transaction"] = Relationship(back_populates="customer")


class CustomerCreate(CustomerModel):
    pass


class CustomerUpdate(CustomerModel):
    pass


class TransactionModel(SQLModel):
    ammount: int
    description: str


class Transaction(TransactionModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key=("customer.id"))
    customer: Customer = Relationship(back_populates="transactions")


class TransactionCreate(TransactionModel):
    customer_id: int = Field(foreign_key=("customer.id"))


class Invoice(BaseModel):
    id: int
    customer: CustomerModel
    transactions: list[Transaction]
    total: int


    @property
    def ammount_total(self):
        return sum(transaction.ammount for transaction in self.transactions)