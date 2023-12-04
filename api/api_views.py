from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import config_api
from .schemas import ExpensesSchema
from .models import ExpensesModel

router = APIRouter()


@router.post('/', response_model=ExpensesSchema)
async def create_user(user: ExpensesSchema, session: AsyncSession = Depends(config_api.get_session)):
    valid = ExpensesSchema(**user.dict())
    db_user = ExpensesModel(**valid.dict())
    session.add(db_user)
    await session.commit()
    raise HTTPException(status_code=201, detail='Пользователь создан')

