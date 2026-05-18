from fastapi import Header,HTTPException
auth_key="AccInf"
def Auth(key:str=Header(None)):
    if key!=auth_key:
        raise HTTPException(status_code=401,data="Unauthorized")