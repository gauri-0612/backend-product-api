from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Connection pool चे parameters
engine = create_engine(
    DATABASE_URL,
    pool_size=20,        # इतक्या connections नेहमी pool मध्ये राहतील
    max_overflow=30,     # pool_size संपल्यास इतक्या extra connections तयार होतील
    pool_pre_ping=True,  # connection वापरण्यापूर्वी ती active आहे का ते check करेल
    pool_recycle=3600,   # 1 तासाने जुन्या connections चा पुनर्वापर करेल (काही databases साठी आवश्यक)
    echo=False
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # हे महत्त्वाचे आहे, connection बंद होते