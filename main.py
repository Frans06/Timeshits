import requests
import json

if __name__ == '__main__':
    '''
    name: Nombre completo
    status7: Proyecto{5:"Otro(especificar)"}
    numbers: Horas Invertidas en la Semana
    date2: Fecha Fin
    date: Fecha inicio
    '''
    json={"answers":{
            "name":"Pepito",
            "status7":"5","text99":"Proyecto",
            "numbers":"45",
            "date2":"2018-12-27",
            "date":"2018-12-24"}}
    headers={
        'Content-Type': "application/json",
        'cache-control': "no-cache"
        }
    r = requests.post('https://forms.monday.com/forms/a48d63c0764f740996ff1b90e496b53a/submit_form', json=json, headers=headers)
    print('Response:')
    print(r.status_code)
    print('Done')
