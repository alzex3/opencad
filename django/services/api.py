import requests as rq
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_request(number):
    object_data = {}
    resp = rq.get(
        url=f'https://rosreestr.ru/fir_lite_rest/api/gkn/fir_lite_object/{number}',
        verify=False,
        headers={'user-agent': 'restclient'}
    ).json()

    obj_type = resp['type']
    if resp['type'] == 'parcel':
        obj_type = 'parcelData'

    object_data = {
        'cad_num': resp['objectCn'],
        'obj_type': resp['type'],
        'address': resp['objectData']['objectAddress'],
        'update_date': resp['objectData']['actualDate'],
        'created_date': resp['objectData']['dateCreated'],
        'cost': resp['objectData'][obj_type]['cadCostValue'],
        'object_desc': resp['objectData']['objectDesc'],
        # 'utility': resp['objectData'][obj_type].get('utilByDoc'),
    }

    return object_data


def get_cad_data(number):
    try:
        resp = get_request(number)
        answer = [
            (
                'Кадастровый номер:', resp['cad_num']
            ),
            (
                'Тип:', resp['obj_type']
            ),
            (
                'Адрес:', resp['address']
            ),
            (
                'Стоимость:', resp['cost']
            ),
            (
                'Описание:', resp['utility']
            ),
            (
                'Разрешённое использование:', resp['object_desc']
            )
        ]
        return answer

    except KeyError:
        return False
