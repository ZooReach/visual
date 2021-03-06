import json
from app.helper.constants import api
from app.helper.rest_client import get

def main():
    category_stats = get_result()
    json_val ={"data":category_stats}
    return json.dumps(json_val)


def get_result():
    url = api['datastore_search_sql']
    query = 'SELECT COUNT(_id), category_level1 FROM "609b1130-2169-471b-978c-a0b6e344795d" GROUP BY category_level1'
    query_param = {"sql": query}
    response = get(url=url, queryparams=query_param)
    ckan_species_list_response = response['result']['records']
    return ckan_species_list_response