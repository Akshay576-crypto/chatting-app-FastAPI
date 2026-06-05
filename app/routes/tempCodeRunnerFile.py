
@router.get("/current_user")
async def current_user( authorization: str = Header(None)):

    return {"Token_user":authorization}