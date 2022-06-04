from datetime import datetime, timedelta
from jose import jwt


# CONFIG
SECRET_KEY = 'ed70c57d7564e994e7d5f6fd6967cea8b347efbc'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3000

def create_access_token(data:dict):
    data_copy = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    
    data_copy.update({'exp': expire})

    token_jwt = jwt.encode(data_copy, SECRET_KEY, algorithm=ALGORITHM)

    return token_jwt

def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get('id')
    except:
        return False