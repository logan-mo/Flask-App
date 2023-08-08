from fastapi import FastAPI, status
import pandas as pd

app = FastAPI()
number_mapping = pd.read_csv("number_mapping.csv")
lead_tracking = pd.read_csv("client_lead_tracking.csv")

@app.get("/notify")
async def notify(caller_number: int, routing_number: int):

    # Mark entry
    client_id = number_mapping.loc[number_mapping['user_number'] == caller_number, 'client_id'].iloc[0]
    lead_tracking.loc[len(lead_tracking.index)] = [client_id, caller_number]

    client_number = number_mapping.loc[number_mapping['routing_number'] == routing_number, 'client_number'].iloc[0]

    return {"status_code": status.HTTP_200_OK, "message": "Notification sent successfully", "client_number": int(client_number)}