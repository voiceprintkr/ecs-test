import os

import uvicorn
from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse

app = FastAPI()


@app.get("/", response_class=ORJSONResponse)
async def main() -> ORJSONResponse:
    _hostname: str = os.uname().nodename
    _version: str = "v1.0.0"

    _body: dict = {
        "Hostname": _hostname,
        "Version": _version,
    }

    return ORJSONResponse(
        content=jsonable_encoder(obj=_body),
        status_code=status.HTTP_200_OK,
    )


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=80,
        access_log=True,
    )
