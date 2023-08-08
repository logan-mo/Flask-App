from fastapi import FastAPI, status, HTTPException
from sqlalchemy import create_engine, insert, MetaData, Table, text




app = FastAPI()

db_path = 'notifications.db'
table_name = "data"

# define meta information
engine = create_engine('sqlite+pysqlite:///' + db_path)

@app.get("/notify")
async def notify(incoming_number: str, outgoing_number: str):
    print("Incoming number: ", incoming_number)
    print("Outgoing number: ", outgoing_number)

    with engine.connect() as conn:
        conn.execute(text(f"INSERT INTO {table_name} (incoming_number, outgoing_number) VALUES ('{incoming_number}', '{outgoing_number}')"))
        conn.commit()

    return {"status_code": status.HTTP_200_OK, "message": "Notification sent successfully"}