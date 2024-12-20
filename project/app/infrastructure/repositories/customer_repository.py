from domain.models import Customer, CustomerCreate, CustomerPlan, CustomerUpdate, CustomerPlan, EnumState, Plan
from sqlmodel import select
from infrastructure.db import SessionDep

class CustomerRepository:

    def __init__(self, session: SessionDep):
        self.session = session

    def get_customer_by_email_repository(self, email: str) -> Customer:
        customer = self.session.exec(select(Customer).where(Customer.email == email)).first()
        self.session.add(customer)
        self.session.commit()
        self.session.refresh(customer)
        return customer
    
    def get_customer_repository(self, customer_id: int) -> Customer:
        return self.session.get(Customer, customer_id)
    

    def delete_customer_repository(self, customer: Customer):
        self.session.delete(customer)
        self.session.commit()

    
    def update_customer_repository(self, customer: Customer, customer_data: CustomerUpdate) -> Customer:
        customer.sqlmodel_update(customer_data)
        self.session.add(customer)
        self.session.commit()
        self.session.refresh(customer)
        return customer
    

    def get_all_customers_repository(self) -> list[Customer]:
        return self.session.exec(select(Customer)).all()
        

    def suscribe_to_plan_repository(self, customer_id: int, plan_id: int, state: EnumState) -> CustomerPlan:
        customer_plan = CustomerPlan(customer_id=customer_id, plan_id=plan_id, state=state)
        self.session.add(customer_plan)
        self.session.commit()
        self.session.refresh(customer_plan)
        return customer_plan
    

    

    
