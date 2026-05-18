from fastapi import Header,HTTPException
API_KEY="secret"
def verify_key(key:str=Header(None)):
    if key!=API_KEY:
        raise HTTPException(status_code=401,data="Unauthorized access key")