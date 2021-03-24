# This file was generated by the "capture_real_responses.py" script.
# On Tue, 23 Mar 2021 22:15:14 +0000.
#
# To update it run:
# python -m tests.providers.capture_real_responses

captured_responses = [
    {
        "request": {
            "full_url": "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente",
            "method": "POST",
            "headers": {},
            "data": bytearray(
                b'<soapenv:Envelope\n            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\n            xmlns:cli="http://cliente.bean.master.sigep.bsb.correios.com.br/"\n        >\n           <soapenv:Header/>\n           <soapenv:Body>\n              <cli:consultaCEP>\n                 <cep>01001-000</cep>\n              </cli:consultaCEP>\n           </soapenv:Body>\n        </soapenv:Envelope>'
            ),
        },
        "response": {
            "type": "success",
            "data": b'<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ns2:consultaCEPResponse xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/"><return><bairro>S\xe9</bairro><cep>01001000</cep><cidade>S\xe3o Paulo</cidade><complemento2>- lado \xedmpar</complemento2><end>Pra\xe7a da S\xe9</end><uf>SP</uf></return></ns2:consultaCEPResponse></soap:Body></soap:Envelope>',
        },
    },
    {
        "request": {
            "full_url": "https://viacep.com.br/ws/01001-000/json/unicode/",
            "method": "GET",
            "headers": {},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{\n  "cep": "01001-000",\n  "logradouro": "Pra\\u00e7a da S\\u00e9",\n  "complemento": "lado \\u00edmpar",\n  "bairro": "S\\u00e9",\n  "localidade": "S\\u00e3o Paulo",\n  "uf": "SP",\n  "ibge": "3550308",\n  "gia": "1004",\n  "ddd": "11",\n  "siafi": "7107"\n}',
        },
    },
    {
        "request": {
            "full_url": "http://cep.republicavirtual.com.br/web_cep.php?cep=01001-000&formato=json",
            "method": "GET",
            "headers": {"Accept": "application/json"},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{"resultado":"1","resultado_txt":"sucesso - cep completo","uf":"SP","cidade":"S\\u00e3o Paulo","bairro":"S\\u00e9","tipo_logradouro":"Pra\\u00e7a","logradouro":"da S\\u00e9"}',
        },
    },
    {
        "request": {
            "full_url": "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente",
            "method": "POST",
            "headers": {},
            "data": bytearray(
                b'<soapenv:Envelope\n            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\n            xmlns:cli="http://cliente.bean.master.sigep.bsb.correios.com.br/"\n        >\n           <soapenv:Header/>\n           <soapenv:Body>\n              <cli:consultaCEP>\n                 <cep>57010-240</cep>\n              </cli:consultaCEP>\n           </soapenv:Body>\n        </soapenv:Envelope>'
            ),
        },
        "response": {
            "type": "success",
            "data": b'<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ns2:consultaCEPResponse xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/"><return><bairro>Prado</bairro><cep>57010240</cep><cidade>Macei\xf3</cidade><complemento2></complemento2><end>Rua Desembargador Inoc\xeancio Lins</end><uf>AL</uf></return></ns2:consultaCEPResponse></soap:Body></soap:Envelope>',
        },
    },
    {
        "request": {
            "full_url": "https://viacep.com.br/ws/57010-240/json/unicode/",
            "method": "GET",
            "headers": {},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{\n  "cep": "57010-240",\n  "logradouro": "Rua Desembargador Inoc\\u00eancio Lins",\n  "complemento": "",\n  "bairro": "Prado",\n  "localidade": "Macei\\u00f3",\n  "uf": "AL",\n  "ibge": "2704302",\n  "gia": "",\n  "ddd": "82",\n  "siafi": "2785"\n}',
        },
    },
    {
        "request": {
            "full_url": "http://cep.republicavirtual.com.br/web_cep.php?cep=57010-240&formato=json",
            "method": "GET",
            "headers": {"Accept": "application/json"},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{"resultado":"1","resultado_txt":"sucesso - cep completo","uf":"AL","cidade":"Macei\\u00f3","bairro":"Prado","tipo_logradouro":"Rua","logradouro":"Desembargador Inoc\\u00eancio Lins"}',
        },
    },
    {
        "request": {
            "full_url": "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente",
            "method": "POST",
            "headers": {},
            "data": bytearray(
                b'<soapenv:Envelope\n            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\n            xmlns:cli="http://cliente.bean.master.sigep.bsb.correios.com.br/"\n        >\n           <soapenv:Header/>\n           <soapenv:Body>\n              <cli:consultaCEP>\n                 <cep>18170-000</cep>\n              </cli:consultaCEP>\n           </soapenv:Body>\n        </soapenv:Envelope>'
            ),
        },
        "response": {
            "type": "success",
            "data": b'<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ns2:consultaCEPResponse xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/"><return><bairro></bairro><cep>18170000</cep><cidade>Piedade</cidade><complemento2></complemento2><end></end><uf>SP</uf></return></ns2:consultaCEPResponse></soap:Body></soap:Envelope>',
        },
    },
    {
        "request": {
            "full_url": "https://viacep.com.br/ws/18170-000/json/unicode/",
            "method": "GET",
            "headers": {},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{\n  "cep": "18170-000",\n  "logradouro": "",\n  "complemento": "",\n  "bairro": "",\n  "localidade": "Piedade",\n  "uf": "SP",\n  "ibge": "3537800",\n  "gia": "5265",\n  "ddd": "15",\n  "siafi": "6857"\n}',
        },
    },
    {
        "request": {
            "full_url": "http://cep.republicavirtual.com.br/web_cep.php?cep=18170-000&formato=json",
            "method": "GET",
            "headers": {"Accept": "application/json"},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{"resultado":"2","resultado_txt":"sucesso - cep \\u00fanico","uf":"SP","cidade":"Piedade","bairro":"","tipo_logradouro":"","logradouro":"","debug":" - encontrado via search_db cep unico - "}',
        },
    },
    {
        "request": {
            "full_url": "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente",
            "method": "POST",
            "headers": {},
            "data": bytearray(
                b'<soapenv:Envelope\n            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\n            xmlns:cli="http://cliente.bean.master.sigep.bsb.correios.com.br/"\n        >\n           <soapenv:Header/>\n           <soapenv:Body>\n              <cli:consultaCEP>\n                 <cep>78175-000</cep>\n              </cli:consultaCEP>\n           </soapenv:Body>\n        </soapenv:Envelope>'
            ),
        },
        "response": {
            "type": "success",
            "data": b'<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ns2:consultaCEPResponse xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/"><return><bairro></bairro><cep>78175000</cep><cidade>Pocon\xe9</cidade><complemento2></complemento2><end></end><uf>MT</uf></return></ns2:consultaCEPResponse></soap:Body></soap:Envelope>',
        },
    },
    {
        "request": {
            "full_url": "https://viacep.com.br/ws/78175-000/json/unicode/",
            "method": "GET",
            "headers": {},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{\n  "cep": "78175-000",\n  "logradouro": "",\n  "complemento": "",\n  "bairro": "",\n  "localidade": "Pocon\\u00e9",\n  "uf": "MT",\n  "ibge": "5106505",\n  "gia": "",\n  "ddd": "65",\n  "siafi": "9129"\n}',
        },
    },
    {
        "request": {
            "full_url": "http://cep.republicavirtual.com.br/web_cep.php?cep=78175-000&formato=json",
            "method": "GET",
            "headers": {"Accept": "application/json"},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{"resultado":"2","resultado_txt":"sucesso - cep \\u00fanico","uf":"MT","cidade":"Pocon\\u00e9","bairro":"","tipo_logradouro":"","logradouro":"","debug":" - encontrado via search_db cep unico - "}',
        },
    },
    {
        "request": {
            "full_url": "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente",
            "method": "POST",
            "headers": {},
            "data": bytearray(
                b'<soapenv:Envelope\n            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\n            xmlns:cli="http://cliente.bean.master.sigep.bsb.correios.com.br/"\n        >\n           <soapenv:Header/>\n           <soapenv:Body>\n              <cli:consultaCEP>\n                 <cep>63200-970</cep>\n              </cli:consultaCEP>\n           </soapenv:Body>\n        </soapenv:Envelope>'
            ),
        },
        "response": {
            "type": "success",
            "data": b'<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ns2:consultaCEPResponse xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/"><return><bairro>Centro</bairro><cep>63200970</cep><cidade>Miss\xe3o Velha</cidade><complemento2></complemento2><end>Rua Jos\xe9 Sobreira da Cruz, 271</end><uf>CE</uf></return></ns2:consultaCEPResponse></soap:Body></soap:Envelope>',
        },
    },
    {
        "request": {
            "full_url": "https://viacep.com.br/ws/63200-970/json/unicode/",
            "method": "GET",
            "headers": {},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{\n  "cep": "63200-970",\n  "logradouro": "Rua Jos\\u00e9 Sobreira da Cruz 271",\n  "complemento": "",\n  "bairro": "Centro",\n  "localidade": "Miss\\u00e3o Velha",\n  "uf": "CE",\n  "ibge": "2308401",\n  "gia": "",\n  "ddd": "88",\n  "siafi": "1469"\n}',
        },
    },
    {
        "request": {
            "full_url": "http://cep.republicavirtual.com.br/web_cep.php?cep=63200-970&formato=json",
            "method": "GET",
            "headers": {"Accept": "application/json"},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{"debug":" - nao encontrado via search_db cep unico - ","resultado":"1","resultado_txt":"sucesso - cep completo","uf":"CE","cidade":"Miss\\u00e3o Velha","bairro":"Centro\\u00a0","tipo_logradouro":"Rua","logradouro":"Jos\\u00e9 Sobreira da Cruz, 271 "}',
        },
    },
    {
        "request": {
            "full_url": "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente",
            "method": "POST",
            "headers": {},
            "data": bytearray(
                b'<soapenv:Envelope\n            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\n            xmlns:cli="http://cliente.bean.master.sigep.bsb.correios.com.br/"\n        >\n           <soapenv:Header/>\n           <soapenv:Body>\n              <cli:consultaCEP>\n                 <cep>69096-970</cep>\n              </cli:consultaCEP>\n           </soapenv:Body>\n        </soapenv:Envelope>'
            ),
        },
        "response": {
            "type": "success",
            "data": b'<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ns2:consultaCEPResponse xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/"><return><bairro>Cidade Nova</bairro><cep>69096970</cep><cidade>Manaus</cidade><complemento2></complemento2><end>Avenida Noel Nutels, 1350</end><uf>AM</uf></return></ns2:consultaCEPResponse></soap:Body></soap:Envelope>',
        },
    },
    {
        "request": {
            "full_url": "https://viacep.com.br/ws/69096-970/json/unicode/",
            "method": "GET",
            "headers": {},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{\n  "cep": "69096-970",\n  "logradouro": "Avenida Noel Nutels 1350",\n  "complemento": "",\n  "bairro": "Cidade Nova",\n  "localidade": "Manaus",\n  "uf": "AM",\n  "ibge": "1302603",\n  "gia": "",\n  "ddd": "92",\n  "siafi": "0255"\n}',
        },
    },
    {
        "request": {
            "full_url": "http://cep.republicavirtual.com.br/web_cep.php?cep=69096-970&formato=json",
            "method": "GET",
            "headers": {"Accept": "application/json"},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{"debug":" - nao encontrado via search_db cep unico - ","resultado":"1","resultado_txt":"sucesso - cep completo","uf":"AM","cidade":"Manaus","bairro":"Cidade Nova\\u00a0","tipo_logradouro":"Avenida","logradouro":"Noel Nutels, 1350 "}',
        },
    },
    {
        "request": {
            "full_url": "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente",
            "method": "POST",
            "headers": {},
            "data": bytearray(
                b'<soapenv:Envelope\n            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\n            xmlns:cli="http://cliente.bean.master.sigep.bsb.correios.com.br/"\n        >\n           <soapenv:Header/>\n           <soapenv:Body>\n              <cli:consultaCEP>\n                 <cep>20010-974</cep>\n              </cli:consultaCEP>\n           </soapenv:Body>\n        </soapenv:Envelope>'
            ),
        },
        "response": {
            "type": "success",
            "data": b'<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ns2:consultaCEPResponse xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/"><return><bairro>Centro</bairro><cep>20010974</cep><cidade>Rio de Janeiro</cidade><complemento2></complemento2><end>Rua Primeiro de Mar\xe7o, 64</end><uf>RJ</uf></return></ns2:consultaCEPResponse></soap:Body></soap:Envelope>',
        },
    },
    {
        "request": {
            "full_url": "https://viacep.com.br/ws/20010-974/json/unicode/",
            "method": "GET",
            "headers": {},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{\n  "cep": "20010-974",\n  "logradouro": "Rua Primeiro de Mar\\u00e7o 64",\n  "complemento": "",\n  "bairro": "Centro",\n  "localidade": "Rio de Janeiro",\n  "uf": "RJ",\n  "ibge": "3304557",\n  "gia": "",\n  "ddd": "21",\n  "siafi": "6001"\n}',
        },
    },
    {
        "request": {
            "full_url": "http://cep.republicavirtual.com.br/web_cep.php?cep=20010-974&formato=json",
            "method": "GET",
            "headers": {"Accept": "application/json"},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{"debug":" - nao encontrado via search_db cep unico - ","resultado":"1","resultado_txt":"sucesso - cep completo","uf":"RJ","cidade":"Rio de Janeiro","bairro":"Centro\\u00a0","tipo_logradouro":"Rua","logradouro":"Primeiro de Mar\\u00e7o, 64 "}',
        },
    },
    {
        "request": {
            "full_url": "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente",
            "method": "POST",
            "headers": {},
            "data": bytearray(
                b'<soapenv:Envelope\n            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\n            xmlns:cli="http://cliente.bean.master.sigep.bsb.correios.com.br/"\n        >\n           <soapenv:Header/>\n           <soapenv:Body>\n              <cli:consultaCEP>\n                 <cep>96010-900</cep>\n              </cli:consultaCEP>\n           </soapenv:Body>\n        </soapenv:Envelope>'
            ),
        },
        "response": {
            "type": "success",
            "data": b'<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ns2:consultaCEPResponse xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/"><return><bairro>Centro</bairro><cep>96010900</cep><cidade>Pelotas</cidade><complemento2></complemento2><end>Rua Tiradentes, 2515</end><uf>RS</uf></return></ns2:consultaCEPResponse></soap:Body></soap:Envelope>',
        },
    },
    {
        "request": {
            "full_url": "https://viacep.com.br/ws/96010-900/json/unicode/",
            "method": "GET",
            "headers": {},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{\n  "cep": "96010-900",\n  "logradouro": "Rua Tiradentes 2515",\n  "complemento": "",\n  "bairro": "Centro",\n  "localidade": "Pelotas",\n  "uf": "RS",\n  "ibge": "4314407",\n  "gia": "",\n  "ddd": "53",\n  "siafi": "8791"\n}',
        },
    },
    {
        "request": {
            "full_url": "http://cep.republicavirtual.com.br/web_cep.php?cep=96010-900&formato=json",
            "method": "GET",
            "headers": {"Accept": "application/json"},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{"debug":" - nao encontrado via search_db cep unico - ","resultado":"1","resultado_txt":"sucesso - cep completo","uf":"RS","cidade":"Pelotas","bairro":"Centro\\u00a0","tipo_logradouro":"Rua","logradouro":"Tiradentes, 2515 "}',
        },
    },
    {
        "request": {
            "full_url": "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente",
            "method": "POST",
            "headers": {},
            "data": bytearray(
                b'<soapenv:Envelope\n            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\n            xmlns:cli="http://cliente.bean.master.sigep.bsb.correios.com.br/"\n        >\n           <soapenv:Header/>\n           <soapenv:Body>\n              <cli:consultaCEP>\n                 <cep>38101-990</cep>\n              </cli:consultaCEP>\n           </soapenv:Body>\n        </soapenv:Envelope>'
            ),
        },
        "response": {
            "type": "success",
            "data": b'<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ns2:consultaCEPResponse xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/"><return><bairro></bairro><cep>38101990</cep><cidade>Baixa (Uberaba)</cidade><complemento2></complemento2><end>Rua Bas\xedlio Eug\xeanio dos Santos</end><uf>MG</uf></return></ns2:consultaCEPResponse></soap:Body></soap:Envelope>',
        },
    },
    {
        "request": {
            "full_url": "https://viacep.com.br/ws/38101-990/json/unicode/",
            "method": "GET",
            "headers": {},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{\n  "cep": "38101-990",\n  "logradouro": "Rua Bas\\u00edlio Eug\\u00eanio dos Santos",\n  "complemento": "",\n  "bairro": "Baixa",\n  "localidade": "Uberaba",\n  "uf": "MG",\n  "ibge": "3170107",\n  "gia": "",\n  "ddd": "34",\n  "siafi": "5401"\n}',
        },
    },
    {
        "request": {
            "full_url": "http://cep.republicavirtual.com.br/web_cep.php?cep=38101-990&formato=json",
            "method": "GET",
            "headers": {"Accept": "application/json"},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{"debug":" - nao encontrado via search_db cep unico - ","resultado":"1","resultado_txt":"sucesso - cep completo","uf":"MG  - Distrito","cidade":"Baixa (Uberaba)","bairro":"\\u00a0","tipo_logradouro":"Rua","logradouro":"Bas\\u00edlio Eug\\u00eanio dos Santos "}',
        },
    },
    {
        "request": {
            "full_url": "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente",
            "method": "POST",
            "headers": {},
            "data": bytearray(
                b'<soapenv:Envelope\n            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\n            xmlns:cli="http://cliente.bean.master.sigep.bsb.correios.com.br/"\n        >\n           <soapenv:Header/>\n           <soapenv:Body>\n              <cli:consultaCEP>\n                 <cep>76840-000</cep>\n              </cli:consultaCEP>\n           </soapenv:Body>\n        </soapenv:Envelope>'
            ),
        },
        "response": {
            "type": "success",
            "data": b'<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ns2:consultaCEPResponse xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/"><return><bairro></bairro><cep>76840000</cep><cidade>Jaci Paran\xe1 (Porto Velho)</cidade><complemento2></complemento2><end></end><uf>RO</uf></return></ns2:consultaCEPResponse></soap:Body></soap:Envelope>',
        },
    },
    {
        "request": {
            "full_url": "https://viacep.com.br/ws/76840-000/json/unicode/",
            "method": "GET",
            "headers": {},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{\n  "cep": "76840-000",\n  "logradouro": "",\n  "complemento": "",\n  "bairro": "Jaci Paran\\u00e1",\n  "localidade": "Porto Velho",\n  "uf": "RO",\n  "ibge": "1100205",\n  "gia": "",\n  "ddd": "69",\n  "siafi": "0003"\n}',
        },
    },
    {
        "request": {
            "full_url": "http://cep.republicavirtual.com.br/web_cep.php?cep=76840-000&formato=json",
            "method": "GET",
            "headers": {"Accept": "application/json"},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{"debug":" - nao encontrado via search_db cep unico - ","resultado":"2","resultado_txt":"sucesso - cep \\u00fanico","uf":"RO  - Distrito","cidade":"Jaci Paran\\u00e1 (Porto Velho)","bairro":"\\u00a0","tipo_logradouro":"","logradouro":""}',
        },
    },
    {
        "request": {
            "full_url": "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente",
            "method": "POST",
            "headers": {},
            "data": bytearray(
                b'<soapenv:Envelope\n            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\n            xmlns:cli="http://cliente.bean.master.sigep.bsb.correios.com.br/"\n        >\n           <soapenv:Header/>\n           <soapenv:Body>\n              <cli:consultaCEP>\n                 <cep>86055-991</cep>\n              </cli:consultaCEP>\n           </soapenv:Body>\n        </soapenv:Envelope>'
            ),
        },
        "response": {
            "type": "success",
            "data": b'<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ns2:consultaCEPResponse xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/"><return><bairro></bairro><cep>86055991</cep><cidade>Londrina</cidade><complemento2></complemento2><end>Rodovia M\xe1bio Gon\xe7alves Palhano, s/n</end><uf>PR</uf></return></ns2:consultaCEPResponse></soap:Body></soap:Envelope>',
        },
    },
    {
        "request": {
            "full_url": "https://viacep.com.br/ws/86055-991/json/unicode/",
            "method": "GET",
            "headers": {},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{\n  "cep": "86055-991",\n  "logradouro": "Rodovia M\\u00e1bio Gon\\u00e7alves Palhano",\n  "complemento": "s/n",\n  "bairro": "",\n  "localidade": "Londrina",\n  "uf": "PR",\n  "ibge": "4113700",\n  "gia": "",\n  "ddd": "43",\n  "siafi": "7667"\n}',
        },
    },
    {
        "request": {
            "full_url": "http://cep.republicavirtual.com.br/web_cep.php?cep=86055-991&formato=json",
            "method": "GET",
            "headers": {"Accept": "application/json"},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{"debug":" - nao encontrado via search_db cep unico - ","resultado":"1","resultado_txt":"sucesso - cep completo","uf":"PR","cidade":"Londrina","bairro":"\\u00a0","tipo_logradouro":"Rodovia","logradouro":"M\\u00e1bio Gon\\u00e7alves Palhano, s\\/n "}',
        },
    },
    {
        "request": {
            "full_url": "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente",
            "method": "POST",
            "headers": {},
            "data": bytearray(
                b'<soapenv:Envelope\n            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\n            xmlns:cli="http://cliente.bean.master.sigep.bsb.correios.com.br/"\n        >\n           <soapenv:Header/>\n           <soapenv:Body>\n              <cli:consultaCEP>\n                 <cep>13917-472</cep>\n              </cli:consultaCEP>\n           </soapenv:Body>\n        </soapenv:Envelope>'
            ),
        },
        "response": {
            "type": "success",
            "data": b'<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ns2:consultaCEPResponse xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/"><return><bairro>Jardim Roseira</bairro><cep>13917472</cep><cidade>Jaguari\xfana</cidade><complemento2>- de 721/722 ao fim</complemento2><end>Rua Amoreira</end><uf>SP</uf></return></ns2:consultaCEPResponse></soap:Body></soap:Envelope>',
        },
    },
    {
        "request": {
            "full_url": "https://viacep.com.br/ws/13917-472/json/unicode/",
            "method": "GET",
            "headers": {},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{\n  "cep": "13917-472",\n  "logradouro": "Rua Amoreira",\n  "complemento": "de 721/722 ao fim",\n  "bairro": "Jardim Roseira",\n  "localidade": "Jaguari\\u00fana",\n  "uf": "SP",\n  "ibge": "3524709",\n  "gia": "3955",\n  "ddd": "19",\n  "siafi": "6595"\n}',
        },
    },
    {
        "request": {
            "full_url": "http://cep.republicavirtual.com.br/web_cep.php?cep=13917-472&formato=json",
            "method": "GET",
            "headers": {"Accept": "application/json"},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{"debug":" - nao encontrado via search_db cep unico - ","resultado":"1","resultado_txt":"sucesso - cep completo","uf":"SP","cidade":"Jaguari\\u00fana","bairro":"Jardim Roseira","tipo_logradouro":"Rua","logradouro":"Amoreira "}',
        },
    },
    {
        "request": {
            "full_url": "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente",
            "method": "POST",
            "headers": {},
            "data": bytearray(
                b'<soapenv:Envelope\n            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\n            xmlns:cli="http://cliente.bean.master.sigep.bsb.correios.com.br/"\n        >\n           <soapenv:Header/>\n           <soapenv:Body>\n              <cli:consultaCEP>\n                 <cep>00000-000</cep>\n              </cli:consultaCEP>\n           </soapenv:Body>\n        </soapenv:Envelope>'
            ),
        },
        "response": {
            "type": "error",
            "status": 500,
            "data": b'<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><soap:Fault><faultcode>soap:Server</faultcode><faultstring>CEP INV\xc1LIDO</faultstring><detail><ns2:SigepClienteException xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/">CEP INV\xc1LIDO</ns2:SigepClienteException></detail></soap:Fault></soap:Body></soap:Envelope>',
        },
    },
    {
        "request": {
            "full_url": "https://viacep.com.br/ws/00000-000/json/unicode/",
            "method": "GET",
            "headers": {},
            "data": None,
        },
        "response": {"type": "success", "data": b'{\n  "erro": true\n}'},
    },
    {
        "request": {
            "full_url": "http://cep.republicavirtual.com.br/web_cep.php?cep=00000-000&formato=json",
            "method": "GET",
            "headers": {"Accept": "application/json"},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{"debug":" - nao encontrado via search_db cep unico - ","resultado":"0","resultado_txt":"sucesso - cep n\\u00e3o encontrado","uf":"","cidade":"","bairro":"","tipo_logradouro":"","logradouro":""}',
        },
    },
    {
        "request": {
            "full_url": "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente",
            "method": "POST",
            "headers": {},
            "data": bytearray(
                b'<soapenv:Envelope\n            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\n            xmlns:cli="http://cliente.bean.master.sigep.bsb.correios.com.br/"\n        >\n           <soapenv:Header/>\n           <soapenv:Body>\n              <cli:consultaCEP>\n                 <cep>11111-111</cep>\n              </cli:consultaCEP>\n           </soapenv:Body>\n        </soapenv:Envelope>'
            ),
        },
        "response": {
            "type": "error",
            "status": 500,
            "data": b'<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><soap:Fault><faultcode>soap:Server</faultcode><faultstring>CEP INV\xc1LIDO</faultstring><detail><ns2:SigepClienteException xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/">CEP INV\xc1LIDO</ns2:SigepClienteException></detail></soap:Fault></soap:Body></soap:Envelope>',
        },
    },
    {
        "request": {
            "full_url": "https://viacep.com.br/ws/11111-111/json/unicode/",
            "method": "GET",
            "headers": {},
            "data": None,
        },
        "response": {"type": "success", "data": b'{\n  "erro": true\n}'},
    },
    {
        "request": {
            "full_url": "http://cep.republicavirtual.com.br/web_cep.php?cep=11111-111&formato=json",
            "method": "GET",
            "headers": {"Accept": "application/json"},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{"debug":" - nao encontrado via search_db cep unico - ","resultado":"0","resultado_txt":"sucesso - cep n\\u00e3o encontrado","uf":"","cidade":"","bairro":"","tipo_logradouro":"","logradouro":""}',
        },
    },
    {
        "request": {
            "full_url": "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente",
            "method": "POST",
            "headers": {},
            "data": bytearray(
                b'<soapenv:Envelope\n            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\n            xmlns:cli="http://cliente.bean.master.sigep.bsb.correios.com.br/"\n        >\n           <soapenv:Header/>\n           <soapenv:Body>\n              <cli:consultaCEP>\n                 <cep>99999-999</cep>\n              </cli:consultaCEP>\n           </soapenv:Body>\n        </soapenv:Envelope>'
            ),
        },
        "response": {
            "type": "error",
            "status": 500,
            "data": b'<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><soap:Fault><faultcode>soap:Server</faultcode><faultstring>CEP INV\xc1LIDO</faultstring><detail><ns2:SigepClienteException xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/">CEP INV\xc1LIDO</ns2:SigepClienteException></detail></soap:Fault></soap:Body></soap:Envelope>',
        },
    },
    {
        "request": {
            "full_url": "https://viacep.com.br/ws/99999-999/json/unicode/",
            "method": "GET",
            "headers": {},
            "data": None,
        },
        "response": {"type": "success", "data": b'{\n  "erro": true\n}'},
    },
    {
        "request": {
            "full_url": "http://cep.republicavirtual.com.br/web_cep.php?cep=99999-999&formato=json",
            "method": "GET",
            "headers": {"Accept": "application/json"},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{"debug":" - nao encontrado via search_db cep unico - ","resultado":"0","resultado_txt":"sucesso - cep n\\u00e3o encontrado","uf":"","cidade":"","bairro":"","tipo_logradouro":"","logradouro":""}',
        },
    },
    {
        "request": {
            "full_url": "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente",
            "method": "POST",
            "headers": {},
            "data": bytearray(
                b'<soapenv:Envelope\n            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\n            xmlns:cli="http://cliente.bean.master.sigep.bsb.correios.com.br/"\n        >\n           <soapenv:Header/>\n           <soapenv:Body>\n              <cli:consultaCEP>\n                 <cep>01111-110</cep>\n              </cli:consultaCEP>\n           </soapenv:Body>\n        </soapenv:Envelope>'
            ),
        },
        "response": {
            "type": "error",
            "status": 500,
            "data": b'<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><soap:Fault><faultcode>soap:Server</faultcode><faultstring>CEP NAO ENCONTRADO</faultstring><detail><ns2:SigepClienteException xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/">CEP NAO ENCONTRADO</ns2:SigepClienteException></detail></soap:Fault></soap:Body></soap:Envelope>',
        },
    },
    {
        "request": {
            "full_url": "https://viacep.com.br/ws/01111-110/json/unicode/",
            "method": "GET",
            "headers": {},
            "data": None,
        },
        "response": {"type": "success", "data": b'{\n  "erro": true\n}'},
    },
    {
        "request": {
            "full_url": "http://cep.republicavirtual.com.br/web_cep.php?cep=01111-110&formato=json",
            "method": "GET",
            "headers": {"Accept": "application/json"},
            "data": None,
        },
        "response": {
            "type": "success",
            "data": b'{"debug":" - nao encontrado via search_db cep unico - ","resultado":"0","resultado_txt":"sucesso - cep n\\u00e3o encontrado","uf":"","cidade":"","bairro":"","tipo_logradouro":"","logradouro":""}',
        },
    },
]

