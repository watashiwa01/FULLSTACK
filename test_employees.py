from app import app

with app.test_client() as client:
    resp = client.get('/employees')
    html = resp.get_data(as_text=True)
    print('STATUS:', resp.status_code)
    print('CONTAINS_TABLE:', '<table' in html)
    print('\nSNIPPET:\n', html.split('\n')[:20])