from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, DateTime
from datetime import datetime

import config_api


class CategoryModel(config_api.Base):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    category_name: Mapped[str] = mapped_column(unique=True)
    expenses: Mapped[list['ExpensesModel']] = relationship(back_populates='category.id')


class ExpensesModel(config_api.Base):
    __tablename__ = 'expenses'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    category: Mapped[int] = mapped_column(ForeignKey('category.id'))
    summa: Mapped[int]
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    comment: Mapped[str] = mapped_column(String(250))
    category_id: Mapped[CategoryModel] = relationship(back_populates='expenses')
