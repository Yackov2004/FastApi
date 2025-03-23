from fastapi import APIRouter, Depends
from repository import TaskRepository
from schemas import STaskAdd, STaskId, STask
from typing import Annotated


router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)


@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return STaskId(task_id=task_id)


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
