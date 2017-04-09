# define weather getting function
def weather_get(city_id, apikey):
    import requests, json

    apiaddress = 'http://api.openweathermap.org/data/2.5/'
    
    conditions = { }
    
    for form in ['weather', 'forecast']:
        reqReturn = json.loads(requests.get(apiaddress + form + '?id=' + str(city_id) + '&appid=' + str(apikey)).text)
        
        if form == 'weather':
            if reqReturn['cod'] == 200:
                conditions[form] = str(reqReturn['weather'][0]['id'])
            else:
                conditions[form] = '000'
                
        elif form == 'forecast':
            if reqReturn['cod'] == '200' and reqReturn['cnt'] > 0:
                conditions[form] = [str(row['weather'][0]['id']) for row in reqReturn['list']]
            else:
                conditions[form] = ['000' for i in range(7)]
                
    return(conditions)
