from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def say_hello():
    return {"message": "Hello from /hello endpoint!"} 

@router.get("/user")
def say_hello():
    return {"message": "User Name: John Doe"}

@router.get("/father")
def say_hello():
    return {"message": "User father: John Arthur Doe"}

@router.get("/user/address")
def say_hello():
    return {"message": "User address: Dhaka, Bangladesh"}