import models
import configs
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine(configs.DB_URL, echo=True)
    models.Base.metadata.create_all(engine)
