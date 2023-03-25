import os

import pynecone as pc
from pynecone.var import BaseVar


appconfig = {
    'gapi_secrets': 'client_secret_909590922339-6clscftdm8rouesqkrn1e27g199eb5av.apps.googleusercontent.com.json',
    'worksheet': 'Sales_Wise_Report_2105198'
}

for key in appconfig:
    pc.Config.add_field(BaseVar(name=key, type=str), appconfig[key])


config = pc.Config(
    app_name="TicketScanner",
    env=pc.Env.DEV,
    bun_path=os.getcwd() + "/.bun/bin/bun",
)