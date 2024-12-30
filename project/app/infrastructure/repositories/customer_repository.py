from domain.models import Customer, CustomerPlan, CustomerPlan
from sqlmodel import select, Session

class CustomerRepository:

    def __init__(self, session: Session):
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
        

    def suscribe_to_plan_repository(self, customer_id: int, plan_id: int) -> CustomerPlan:
        customer_plan = CustomerPlan(customer_id=customer_id, plan_id=plan_id, state="active")
        self.session.add(customer_plan)
        self.session.commit()
        self.session.refresh(customer_plan)
        return customer_plan
    

    def unsuscribe_to_plan_repository(self, customer_id: int, plan_id: int) -> CustomerPlan:
        customer_plan = self.session.exec(select(CustomerPlan).where(CustomerPlan.customer_id == customer_id, CustomerPlan.plan_id == plan_id)).first()
        if customer_plan:
            customer_plan.state = "inactive"
            self.session.add(customer_plan)
            self.session.commit()
            self.session.refresh(customer_plan)
        return customer_plan

    def is_already_subscribed(self, customer_id: int, plan_id: int) -> bool:
        customer_plan = self.session.exec(select(CustomerPlan).where(CustomerPlan.customer_id == customer_id, CustomerPlan.plan_id == plan_id, CustomerPlan.state == "active")).first()
        print(customer_plan)
        if customer_plan:
            return True
        return False


