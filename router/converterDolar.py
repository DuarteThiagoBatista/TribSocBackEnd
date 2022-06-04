import requests

def converterDolarToReal(dolar):
    moeda= requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    cotacao_dolar=round(float(moeda.json()["USDBRL"]["ask"]),2)
    real=cotacao_dolar*dolar
    moeda= requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    cotacao_dolar=round(float(moeda.json()["USDBRL"]["ask"]),2)
    converter=cotacao_dolar*dolar
    valor_IRRF,irrf=calculo_irrf(converter)
    valor_IRRF=round(valor_IRRF,2)
    return {'valor_inserido':dolar,"dolar":cotacao_dolar,
    "convertido":"%.2f" % converter,"DescontoIRRF":valor_IRRF,
    "salario_liquido":"%.2f" %(converter-valor_IRRF),"IRRF":irrf}
    

def calculo_irrf(real):
    if real<= 1903.98:
        return 0,0
    elif real<=2826.65:
        return (real*7.5)/100,7.5
    elif real<=3751.05:
        return (real*15)/100,15
    elif real<=4664.68:
        return (real*22.5)/100,22.5
    else:
        return(real*27.5)/100,27.5
