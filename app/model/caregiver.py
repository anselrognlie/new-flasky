from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Caregiver(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    cats: Mapped[List["Cat"]] = relationship(back_populates="caregiver")  # type: ignore

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
        )