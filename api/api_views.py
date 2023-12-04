from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import config_api
from .schemas import ExpensesSchema
from .models import ExpensesModel

expense_router = APIRouter()


@expense_router.post('/', response_model=ExpensesSchema)
async def create_expense(expense: ExpensesSchema, session: AsyncSession = Depends(config_api.get_session)):
    valid = ExpensesSchema(**expense.dict())
    db_expense = ExpensesModel(**valid.dict())
    session.add(db_expense)
    await session.commit()
    raise HTTPException(status_code=201, detail='Запись сохранена')

