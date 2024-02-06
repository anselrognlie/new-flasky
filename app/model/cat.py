from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db

class Cat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    caregiver_id: Mapped[int] = mapped_column(ForeignKey("caregiver.id"), nullable=True)
    caregiver: Mapped["Caregiver"] = relationship(back_populates="cats")  # type: ignore

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            caregiver=self.caregiver.name if self.caregiver else None
        )