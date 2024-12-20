
from sqlmodel import Relationship, Field, SQLModel
from pydantic import BaseModel, EmailStr
from enum import Enum


class EnumState(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class CustomerPlan(SQLModel, table=True):
    id: int = Field(primary_key=True)
    state: EnumState = Field(default=EnumState.ACTIVE)
    customer_id: int = Field(foreign_key="customer.id")
    plan_id: int = Field(foreign_key="plan.id")


class PlanModel(SQLModel):
    name: str = Field(default=None)
    price: int = Field(default=None)
    description: str = Field(default=None)


class Plan(PlanModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customers: list["Customer"] = Relationship(back_populates="plans", link_model=CustomerPlan)


class PlanCreate(PlanModel):
    pass


class CustomerModel(SQLModel):
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    email: EmailStr = Field(default=None, unique=True)
    age: int = Field(default=None)


class Customer(CustomerModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    transactions: list["Transaction"] = Relationship(back_populates="customer")
    plans: list["Plan"] = Relationship(back_populates="customers", link_model=CustomerPlan)


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
    customer: Customer
    transactions: list[Transaction]
    total: int


    @property
    def ammount_total(self):
        return sum(transaction.ammount for transaction in self.transactions)