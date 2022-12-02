# 실행 시 파일 이름: main.py

import time
from fastapi import FastAPI, Request
import jwt

app = FastAPI()  # 프레임워크는 재생 버튼으로 실행하는 것이 아님

@app.get("/jwt")  # jwt 주소로 요청 / @app.get("/") 일 경우 바로 됨
async def get_jwt():
    temp = {
        "id": "아이디",
        "exp": time.time() + 30  # 30초 뒤 만료
    }
    
    return jwt.encode(temp, "비밀소금", algorithm="HS256")  # jwt.encode: jwt를 만든다는 뜻 / 시크릿키 = 솔트 = 소금


@app.get("/")
async def root(request: Request):
    if (request.headers.get("Authorization") == None):
        return "토큰 없음"
    
    token = request.headers.get("Authorization").replace("Bearer ", "")
    
    print(token)
    
    try:
        decoded = jwt.decode(token, "비밀소금", algorithms=["HS256"])  # -s 대괄호 필요 / 리스트
    except Exception as e:
        print(e)
        return "문제있음"
    
    return decoded

    