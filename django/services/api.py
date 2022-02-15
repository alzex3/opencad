import requests as rq
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_request(number):
    object_data = {}
    resp = rq.get(
        url=f'https://rosreestr.ru/fir_lite_rest/api/gkn/fir_lite_object/{number}',
        verify=False,
    ).json()

    obj_type = resp['type']
    if resp['type'] == 'parcel':
        obj_type = 'parcelData'

    object_data[resp['objectCn']] = {
        'cad_num': resp['objectCn'],
        'obj_type': resp['type'],
        'address': resp['objectData']['address']['mergedAddress'],
        'update_date': resp['objectData'][obj_type]['actualDate'],
        'full_address': resp['objectData']['address']['note'],
        'created_date': resp['objectData']['dateCreated'],
        'cost': resp['objectData'][obj_type]['cadCostValue'],
        'object_desc': resp['objectData']['objectDesc'],
        'utility': resp['objectData'][obj_type]['utilByDoc'],
    }

    return object_data


def get_cad_data(number):
    try:
        resp = get_request(number)[number]
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
                'Полный адрес:', resp['full_address']
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
