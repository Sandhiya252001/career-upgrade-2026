from fastapi import Header,HTTPException
key="InAC"
def verifyKey(api_key:str=Header(...)):
    if api_key!=key:
        raise HTTPException(status_code=401,detail="Unauthorized")