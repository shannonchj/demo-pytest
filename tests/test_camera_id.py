import pytest
from fastapi.testclient import TestClient

from app.main import app, EVENTS
from tests.test_events import make_event

client = TestClient(app)


@pytest.mark.parametrize("camera_id, expected", [
    ("cam2", 201),      # 正常
    ("s2cam1", 201),    # 二館的攝影機
    ("", 422),          # 空的
    ("   ", 422),       # 只有空格
    ("cam 2", 422),     # 中間有空格
])
def test_camera_id(camera_id, expected):
    EVENTS.clear()
    r = client.post("/events", json=make_event(camera_id=camera_id))
    assert r.status_code == expected