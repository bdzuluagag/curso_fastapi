from domain.models import Customer, CustomerPlan, CustomerPlan
from sqlmodel import select
from infrastructure.db import SessionDep

class CustomerRepository:

    def __init__(self, session: SessionDep):
        self.session = session


    def get_customer_by_email_repository(self, email: str) -> Customer:
        statement = select(Customer).where(Customer.email == email)
        result = self.session.exec(statement).first()
        return result
    

    def create_customer_repository(self, customer_data: dict) -> Customer:
        customer = Customer.model_validate(customer_data)
        self.session.add(customer)
        self.session.commit()
        self.session.refresh(customer)
        return customer

    
    def get_customer_repository(self, customer_id: int) -> Customer:
        return self.session.get(Customer, customer_id)
    

    def delete_customer_repository(self, customer: Customer):
        self.session.delete(customer)
        self.session.commit()

    
    def update_customer_repository(self, customer: Customer, customer_data: dict) -> Customer:
        for key, value in customer_data.items():
            setattr(customer, key, value)
        self.session.add(customer)
        self.session.commit()
        self.session.refresh(customer)
        return customer
    

    def get_all_customers_repository(self) -> list[Customer]:
        return self.session.exec(select(Customer)).all()


