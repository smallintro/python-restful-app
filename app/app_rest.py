from fastapi import FastAPI, Query
from logzero import logger as log
from app_service import MobileInfoService
from app_models import MobileInfoRequest, MobileInfoResponse

import uvicorn


app_v1 = FastAPI()

mobile_service = MobileInfoService()


@app_v1.get("/v1/mobilemgr/{mobileid}",)
def get_mobile_info(mobileid: str = "-1"):
    log.info(f"get_mobile_info {mobileid}")
    result = mobile_service.get_mobile_info(mobileid)
    return {"mobile_info": result}


@app_v1.post("/v1/mobilemgr",)
def add_mobile_info(mobile_info: MobileInfoRequest):
    log.info(f"add_mobile_info {mobile_info}")
    result = mobile_service.add_mobile_info(mobile_info)
    return {"mobile_info": result}


@app_v1.put("/v1/mobilemgr/{mobileid}",)
def update_mobile_info(mobileid: str, mobile_info: MobileInfoRequest):
    log.info(f"update_mobile_info {mobile_info}")
    result = mobile_service.update_mobile_info(mobileid, mobile_info)
    return {"mobile_info": result}


@app_v1.delete("/v1/mobilemgr/{mobileid}",)
def del_mobile_info(mobileid: str):
    log.info(f"del_mobile_info {mobileid}")
    result = mobile_service.del_mobile_info(mobileid)
    return {"mobile_info": result}

if __name__ == "__main__":
    uvicorn.run("app_rest:app_v1", host="127.0.0.1", port=5000, log_level="info")