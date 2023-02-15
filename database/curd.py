from fastapi import Request


class Curd:
    _model = None

    def all(self, request: Request, skip: int = 0, limit: int = 100):
        return request.state.db.query(self._model).offset(skip).limit(limit).all()

    def create(self, request: Request, item):
        db_item = self._model(**item.dict())
        db = request.state.db
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def get_user_by_id(self, request: Request, id: int):
        return request.state.db.query(self._model).filter(self._model.id == id).first()
