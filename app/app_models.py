from datetime import datetime

from db_connection import Base
from pydantic import BaseModel
from sqlalchemy import Column, Numeric, String, BigInteger, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from typing import List

class MobileInfo(Base):

    __tablename__ = "T_MOBILE_INFO"

    mobile_id = Column(String, primary_key=True)
    mobile_name = Column(String, nullable=False)
    brand_id = Column(Integer,ForeignKey("T_BRAND_INFO.brand_id"))
    storage_size = Column(BigInteger,nullable=False)
    ram_size = Column(Integer,nullable=False)
    added_on = Column(DateTime, nullable=False,default=datetime.now())
    sold_on = Column(DateTime)

    brand = relationship("BrandInfo")

    def __repr__(self):
        return "MobileInfo(%s, %s, %s, %s,%s, %s, %s)" % (
            self.mobile_id,
            self.mobile_name,
            self.brand_id,
            self.added_on,
            self.sold_on,self.storage_size,self.ram_size
        )


class BrandInfo(Base):

    __tablename__ = "T_BRAND_INFO"

    brand_id = Column(Numeric, primary_key=True, nullable=False)
    brand_name = Column(String)

    def __repr__(self):
        return "BrandInfo(%d, %s)" % (self.brand_id, self.brand_name,)



class MobileInfoRequest(BaseModel):
    mobile_name :str
    brand_id :int
    storage_size: int
    ram_size : int


class MobileInfoResponse(BaseModel):
    mobile_id :str
    mobile_name :str
    brand_name :str
    storage_size: int
    ram_size : int
    added_on : datetime
    sold_on : datetime = None


class MobileInfosResponse(BaseModel):
    data = List[MobileInfoResponse]