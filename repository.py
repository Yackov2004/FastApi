from database import new_session, TaskOrm, select
from schemas import STaskAdd, STask
import logging

logging.basicConfig(level=logging.INFO)


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        try:
            async with new_session() as session:
                task_dict = data.model_dump()
                task = TaskOrm(**task_dict)
                session.add(task)
                await session.flush()
                await session.commit()
                return task.id
        except Exception as e:
            logging.error(f"Error adding task: {e}")
            raise

    @classmethod
    async def find_all(cls) -> list[STask]:
        try:
            async with new_session() as session:
                query = select(TaskOrm)
                result = await session.execute(query)
                task_models = result.scalars().all()
                task_schemas = [STask.from_orm(task_model)
                                for task_model in task_models]
                return task_schemas
        except Exception as e:
            logging.error(f"Error retrieving tasks: {e}")
            raise
