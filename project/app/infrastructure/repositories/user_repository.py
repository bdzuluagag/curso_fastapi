from domain.models import User
from sqlmodel import Session, select

class UserRepository:

    def __init__(self, session: Session):
        self.session = session

    
    def create_user_repository(self, user_data: dict) -> User:
        user = User.model_validate(user_data)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    

    def get_user_repository(self, user_id: int) -> User:
        return self.session.get(User, user_id)
    

    def delete_user_repository(self, user: User):
        self.session.delete(user)
        self.session.commit()


    def update_user_repository(self, user: User, user_data: dict) -> User:
        for key, value in user_data.items():
            setattr(user, key, value)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    

    def get_all_users_repository(self) -> list[User]:
        return self.session.exec(select(User)).all()

    def get_user_by_email(self, email: str) -> User:
        statement = select(User).where(User.email == email)
        print("bieeeeeeeeeeeeeeeeeeeeeeeeen")
        result = self.session.exec(statement).first()
        print("bieeeeeeeeeeeeeeeeeeeeeeeeen")
        return result