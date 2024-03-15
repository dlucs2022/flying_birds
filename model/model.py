from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict, field_serializer


class BirdCommonDataBase(BaseModel):
    unique: str = Field(..., max_length=32, title="唯一标识")
    species_id: int = Field(..., title="鸟类种类id")
    device_name: Optional[str] = Field(None, title="设备号")
    time: Optional[datetime] = Field(None, title="收集时间")
    satellites: Optional[int] = Field(None, title="卫星维度")
    speed: Optional[float] = Field(None, title="速度")
    altitude: Optional[float] = Field(None, title="高度")
    longitude: Optional[float] = Field(None, title="经度")
    latitude: Optional[float] = Field(None, title="纬度")
    create_time: Optional[datetime] = Field(None, title="创建时间")
    update_time: Optional[datetime] = Field(None, title="更新时间")

    model_config = ConfigDict(from_attributes=True)

    @field_serializer("time", "create_time", "update_time")
    def serialize_time(self, v: datetime) -> str:
        return v.strftime("%Y-%m-%d %H:%M:%S") if v else None


class BirdCommonData(BirdCommonDataBase):
    species: Optional["SpeciesBase"] = Field({}, title="鸟类种类信息")


class SpeciesBase(BaseModel):
    id: int = Field(..., title="鸟类种类id")
    name: str = Field(..., max_length=64, title="鸟类名称")
    create_time: Optional[datetime] = Field(None, title="创建时间")
    update_time: Optional[datetime] = Field(None, title="更新时间")

    model_config = ConfigDict(from_attributes=True)

    @field_serializer("create_time", "update_time")
    def serialize_time(self, v: datetime) -> str:
        return v.strftime("%Y-%m-%d %H:%M:%S") if v else None


class Species(SpeciesBase):
    bird_common_data: Optional[List[BirdCommonData]] = Field([], title="数据")
