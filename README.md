# blog-app-fastapi

# .ENV
    HOST=localhost
    SECRET_KEY =****
    ALGORITHM = HS256
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    TOKEN_URL =/auth/token

### SQLite

    SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

### PostgreSQL

    SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@localhost/<db_name>"

# Auth

docs - [/auth/docs/](/auth/docs)

# Blog

docs - [/blog/docs/](/blog/docs/)
