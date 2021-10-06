from passlib.context import CryptContext

pws_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    @staticmethod
    def bcrypt(password: str):
        return pws_cxt.hash(password)

    @staticmethod
    def verify(plain_password: str, hashed_password: str):
        return pws_cxt.verify(plain_password, hashed_password)
