import requests as rq
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def api_request(cad_num):
    resp = rq.get(
        url=f'https://rosreestr.ru/fir_lite_rest/api/gkn/fir_lite_object/{cad_num}',
        verify=False,
        headers={'user-agent': 'restclient'}
    )

    if resp.status_code == 200:
        return resp.json()


def get_object_data(cad_num):
    resp = api_request(cad_num)

    if not resp:
        return False

    else:
        object_data = {
            'cad_num': resp.get('objectCn'),
            'obj_type': resp.get('type'),
            'address': resp.get('objectData').get('objectAddress'),
            'update_date': resp.get('objectData').get('actualDate'),
            'created_date': resp.get('objectData').get('dateCreated'),
            'object_desc': resp.get('objectData').get('objectDesc'),
        }

        if resp['type'] == 'parcel':
            parcel_data = {
                'cost': resp.get('objectData').get('parcelData').get('cadCostValue'),
                'utility': resp.get('objectData').get('parcelData').get('utilByDoc'),
            }
            object_data.update(parcel_data)

        elif resp['type'] == 'building':
            building_data = {
                'cost': resp.get('objectData').get('building').get('cadCostValue'),
                'name': resp.get('objectData').get('name'),
            }
            object_data.update(building_data)

        elif resp['type'] == 'flat':
            flat_data = {
                'cost': resp.get('objectData').get('flat').get('cadCostValue'),
                'area': resp.get('objectData').get('flat').get('area'),
            }
            object_data.update(flat_data)

        elif resp['type'] == 'construction':
            construction_data = {
                'cost': resp.get('objectData').get('construction').get('cadCostValue'),
                'name': resp.get('objectData').get('name'),
            }
            object_data.update(construction_data)

        return object_data


def get_cad_data(number):
    try:
        resp = get_object_data(number)
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
