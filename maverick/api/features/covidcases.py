import requests
import pandas as pd

class covidcasesfun:
    def cases(state,district):
        url='https://api.covid19india.org/state_district_wise.json'
        res=requests.get(url)

        response= str(pd.DataFrame(pd.read_json(res.text)[state]).iloc[0,0][district])
        res={'msg':response,'data':NULL}
        return res
