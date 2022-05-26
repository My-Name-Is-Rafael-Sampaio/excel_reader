import pandas as pd
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"
client = Client(account_sid, auth_token)
months = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]


for month in months:
    salesTable = pd.read_excel(f"./src/archive/{month}.xlsx")

    if (salesTable["Vendas"] > 55000).any():
        seller = salesTable.loc[salesTable["Vendas"] > 55000, "Vendedor"].values[0]
        sales = salesTable.loc[salesTable["Vendas"] > 55000, "Vendas"].values[0]
        queryResult = f"No mês de {month} a meta de vendas foi batida. Vencedor: {seller}, vendeu: R${sales}"
        message = client.messages.create(
            to="+15558675309", 
            from_="+15017250604",
            body=queryResult
        )
        print(message.sid)