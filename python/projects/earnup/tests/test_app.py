import pytest
from freezegun import freeze_time
from werkzeug.test import Client

SAMPLE_REQUEST_1 = {'loan': {'monthly_payment_amount': 750, 'payment_due_day': 28, 'schedule_type': 'biweekly',
        'debit_start_date'                           : '2021-05-07', 'debit_day_of_week': 'friday'}}

SAMPLE_RESPONSE_1 = [{'today': '2021-05-07', 'amount': 375, 'date': '2021-05-21'},
        {'today': '2021-05-20', 'amount': 375, 'date': '2021-05-21'}, {'today': '2021-05-23', 'amount': 375, 'date': '2021-06-04'},
        {'today': '2021-06-14', 'amount': 375, 'date': '2021-06-18'}]

SAMPLE_RESPONSE_1 = [{'debit': {'amount': 750.0, 'date': '2021-05-21'}}]

SAMPLE_REQUEST_2 = {
        'loan': {'monthly_payment_amount': 990, 'payment_due_day': 1, 'schedule_type': 'biweekly', 'debit_start_date': '2021-05-03',
                'debit_day_of_week'      : 'monday'}}

# SAMPLE_RESPONSE_2 = [
#         {
#                 'today':  '2021-05-02',
#                 'amount': 330,
#                 'date':   '2021-05-03'
#         },
#         {
#                 'today':  '2021-05-12',
#                 'amount': 330,
#                 'date':   '2021-05-17'
#         },
#         {
#                 'today':  '2021-05-23',
#                 'amount': 330,
#                 'date':   '2021-05-31'
#         },
#         {
#                 'today':  '2021-06-05',
#                 'amount': 495,
#                 'date':   '2021-06-14'
#         }
# ]

SAMPLE_RESPONSE_2 = [{'debit': {'amount': 999.0, 'date': '2021-05-17'}}]


@pytest.fixture
def app_client():
    from app import create_app
    app = create_app()
    client = Client(app)
    return client


@pytest.mark.parametrize('expected', SAMPLE_RESPONSE_1)
def test_case_1(app_client, expected):
    request = SAMPLE_REQUEST_1

    with freeze_time(expected['today']):
        response = app_client.post('/get_next_debit', json=request)
        assert response.status_code == 200
        assert response.json['debit']['amount'] == expected['amount']
        assert response.json['debit']['date'] == expected['date']


@pytest.mark.parametrize('expected', SAMPLE_RESPONSE_2)
def test_case_2(app_client, expected):
    request = SAMPLE_REQUEST_2

    with freeze_time(expected['today']):
        response = app_client.post('/get_next_debit', json=request)
        assert response.status_code == 200
        assert response.json['debit']['amount'] == expected['amount']
        assert response.json['debit']['date'] == expected['date']
