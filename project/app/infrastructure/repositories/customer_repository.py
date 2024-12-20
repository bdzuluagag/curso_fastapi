from domain.models import Customer, CustomerPlan, CustomerPlan, EnumState
from sqlmodel import select, Session

class CustomerRepository:

    def __init__(self, session: Session):
        self.session = session


    def get_customer_by_email_repository(self, email: str) -> Customer:
        return self.session.exec(select(Customer).where(Customer.email == email)).first()
    

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
    

    

    
