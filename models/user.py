from ext.database import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)

    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __init__(self, username):
        self.username = username

    @staticmethod
    def get_by_username(username) -> "User | None":
        return User.query.filter_by(username=username).first()

    def __repr__(self):
        return f"<User {self.username}>"
