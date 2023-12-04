from pydantic import BaseModel, Field


class ExpensesSchema(BaseModel):
    category: int
    summa: int
    comment: str = Field(min_length=5, max_length=250)
