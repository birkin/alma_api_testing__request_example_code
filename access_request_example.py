"""
Request-id example; i.e. for grabbing annex-scan-request specifics

Usage...
- % cd /path/to/request_id_example_code/
- % source ../env_alma_api/bin/activate  # assumes activating env loads environmental-variables
- % python3 ./access_request_example.py
"""

import logging, os, pprint
import requests

## setup ----------------------------------------

API_KEY = os.environ['ALMA_API_TESTING__REQUEST_URL_API_KEY']
ALMA_API_REQUEST_URL_TEMPLATE = os.environ['ALMA_API_TESTING__REQUEST_URL_TEMPLATE']  # like: 'ROOT_URL/v1/users/{PATRON_BARCODE}/requests/{REQUEST_ID}?user_id_type=all_unique&apikey={API_KEY}"
PATRON_BARCODE = os.environ['ALMA_API_TESTING__REQUEST_URL_PATRON_BARCODE']
REQUEST_ID = os.environ['ALMA_API_TESTING__REQUEST_URL_REQUEST_ID']

logging.basicConfig(
    # filename=settings['LOG_PATH'],
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S',
    )
log = logging.getLogger(__name__)
log.debug( '\n\nstarting log\n============' )

## get to work ----------------------------------

request_api_url = ALMA_API_REQUEST_URL_TEMPLATE.replace( '{PATRON_BARCODE}', PATRON_BARCODE ).replace( '{REQUEST_ID}', REQUEST_ID ).replace( '{API_KEY}', API_KEY )
log.debug( f'request_api_url url, ``{request_api_url}``' )

header_data = { 'accept': 'application/json' }  # NB- some errors (like invalid API key) can return xml despite this.

r = requests.get( request_api_url, headers=header_data )
resp_dct = r.json()
log.debug( f'resp_dct, ``{pprint.pformat(resp_dct)}``' )


## yields...

# resp_dct, ``{
#  'author': None,
#  'barcode': '31236098366449',
#  'chapter_or_article_title': 'chapter 2',
#  'comment': None,
#  'description': '1-2 (spring-fall 2007)',
#  'expiry_date': '2021-09-12Z',
#  'full_chapter': 'false',
#  'issue': None,
#  'item_id': '23342844280006966',
#  'material_type': {'desc': 'Issue', 'value': 'ISSUE'},
#  'mms_id': '991031621479706966',
#  'part': None,
#  'partial_digitization': True,
#  'request_date': '2021-09-10Z',
#  'request_id': '(THE-REQUEST-ID)',
#  'request_status': 'HISTORY',
#  'request_sub_type': {'desc': 'Patron digitization request',
#                       'value': 'PHYSICAL_TO_DIGITIZATION'},
#  'request_type': 'DIGITIZATION',
#  'required_pages_range': [{'from_page': '25', 'to_page': '105'}],
#  'target_destination': {'desc': 'Digitization Department For Institution',
#                         'value': 'DIGI_DEPT_INST'},
#  'task_name': 'TransitItem',
#  'title': 'Kadar koli.',
#  'volume': None
# }``


## another example...

# resp_dct, ``{
#  'author': None,
#  'barcode': '31236102808931',
#  'chapter_or_article_author': 'Searle, John',
#  'chapter_or_article_title': 'Minds, brains, and programs',
#  'comment': 'Behavioral and Brain Sciences , Volume 3 , Issue 3 , September '
#             '1980 , pp. 417 - 424 DOI: '
#             'https://doi.org/10.1017/S0140525X00005756',
#  'description': '3 (1980)',
#  'expiry_date': '2021-10-20Z',
#  'full_chapter': 'false',
#  'issue': None,
#  'item_id': '23293943480006966',
#  'material_type': {'desc': 'Issue', 'value': 'ISSUE'},
#  'mms_id': '991007570869706966',
#  'part': None,
#  'partial_digitization': True,
#  'request_date': '2021-12-29Z',
#  'request_id': '(THE-REQUEST-ID)',
#  'request_status': 'HISTORY',
#  'request_sub_type': {'desc': 'Patron digitization request',
#                       'value': 'PHYSICAL_TO_DIGITIZATION'},
#  'request_type': 'DIGITIZATION',
#  'required_pages_range': [{'from_page': '417', 'to_page': '424'}],
#  'target_destination': {'desc': 'Digitization Department For Institution',
#                         'value': 'DIGI_DEPT_INST'},
#  'task_name': 'TransitItem',
#  'title': 'The Behavioral and brain sciences.',
#  'volume': None
# }``

