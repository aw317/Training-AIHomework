import json
from multiprocessing import Process

import pytest

from ping.app import create_ping_app
from receiver.app import create_receiver_app


@pytest.fixture
def receiver_client():
    test_port = 8000
    app = create_receiver_app()
    app_process = Process(target=app.run, kwargs={"host": "0.0.0.0", "port": test_port, "debug": False})
    app_process.start()
    yield app_process
    app_process.terminate()
    app_process.join()


@pytest.fixture
def ping_client():
    app = create_ping_app()
    with app.test_client() as client:
        yield client


def test_ping_endpoint(receiver_client, ping_client):
    resp = ping_client.post('/api/v1/ping', json=dict(
        url='http://localhost:8000/api/v1/info'
    ))
    assert json.loads(resp.data.decode('utf-8')) == {"Receiver": "Cisco is the best!"}
    assert resp.status_code == 200
