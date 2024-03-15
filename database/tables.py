from datetime import datetime
from typing import List

from database.database import BASE
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, DateTime, Float


class BirdCommonData(BASE):
    __tablename__ = "bird_common_data"  # noqa 存储鸟类数据共同字段的表名
    unique: Mapped[str] = mapped_column(String(32), primary_key=True)
    species_id: Mapped[int] = mapped_column(
        ForeignKey("bird_species.id"),
        nullable=False,
        comment="鸟类种类id",
    )
    device_name: Mapped[str] = mapped_column(
        String(32), nullable=False, comment="设备号"
    )
    time: Mapped[DateTime] = mapped_column(DateTime, comment="收集时间")
    satellites: Mapped[int] = mapped_column(Integer, comment="卫星维度")
    speed: Mapped[float] = mapped_column(Float, comment="速度")
    altitude: Mapped[float] = mapped_column(Float, comment="高度")
    longitude: Mapped[float] = mapped_column(Float, comment="经度")
    latitude: Mapped[float] = mapped_column(Float, comment="纬度")
    create_time: Mapped[DateTime] = mapped_column(
        DateTime, nullable=False, comment="创建时间", default=datetime.now()
    )
    update_time: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        comment="更新时间",
        default=datetime.now(),
        onupdate=datetime.now(),
    )

    species: Mapped["BirdSpecies"] = relationship(
        "BirdSpecies", back_populates="bird_common_data", foreign_keys=[species_id]
    )


class BirdSpecies(BASE):
    __tablename__ = "bird_species"  # noqa 存储鸟类种类的表名
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(64), nullable=False, unique=True)
    create_time: Mapped[DateTime] = mapped_column(
        DateTime, nullable=False, comment="创建时间", default=datetime.now()
    )
    update_time: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        comment="更新时间",
        default=datetime.now(),
        onupdate=datetime.now(),
    )

    bird_common_data: Mapped[List[BirdCommonData]] = relationship(
        "BirdCommonData",
        back_populates="species",
    )
