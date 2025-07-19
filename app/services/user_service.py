from app.models.user import User


class UserService:
    """
    Service class to handle operations related to users.
    """

    def __init__(self, db) -> None:
        self.db = db

    def get_all_users(self, params: dict = {}) -> list[User]:
        """
        Retrieve a list of users based on filter parameters.

        Args:
            params (dict): A dictionary containing filter parameters such as 'name' and 'email'.

        Returns:
            list[User]: A list of users matching the filter criteria.
        """
        result = self.db.query(User)
        if params.get("name"):
            result = result.filter(User.name.ilike(f"%{params.get('name')}%"))
        if params.get("email"):
            result = result.filter(User.email.ilike(f"%{params.get('email')}%"))
        if params.get("is_active"):
            result = result.filter_by(is_active=params.get("is_active"))
        return result.all()

    def get_user(self, id_user: int) -> User:
        """
        Retrieve a single user by its ID.

        Args:
            id_user (int): The ID of the user to retrieve.

        Returns:
            User: The user object if found, otherwise None.
        """
        result = self.db.query(User).filter_by(id=id_user).first()
        return result

    def create_user(self, user: User) -> User:
        """
        Create a new user in the database.

        Args:
            user (User): The user data to be created.

        Returns:
            User: The newly created user object.
        """
        new_user = User(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def update_user(self, id_user: int, data: User) -> User:
        """
        Update an existing user in the database.

        Args:
            id_user (int): The ID of the user to update.
            data (User): The updated user data.

        Returns:
            User: The updated user object if found, otherwise None.
        """
        _user = self.db.query(User).filter(User.id == id_user).first()
        if _user:
            for key, value in data.dict().items():
                setattr(_user, key, value)
            self.db.commit()
            self.db.refresh(_user)
        return _user

    def delete_user(self, id_user: int) -> bool:
        """
        Delete a user from the database.

        Args:
            id_user (int): The ID of the user to delete.

        Returns:
            bool: True if the user was deleted, otherwise False.
        """
        _user = self.db.query(User).filter(User.id == id_user).first()
        if _user:
            self.db.delete(_user)
            self.db.commit()
            return True
        return False

    def activate_user(self, id_user: int, status: bool) -> User:
        """
        Activate a user by its ID.

        Args:
            id_user (int): The ID of the user to activate.
            status (bool): The ID of the user to activate.

        Returns:
            User: The activated user object if found, otherwise None.
        """
        _user = self.db.query(User).filter(User.id == id_user).first()
        if _user:
            _user.is_active = status
            self.db.commit()
            self.db.refresh(_user)
        return _user
