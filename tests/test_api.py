from idiet.tracking.wsgi import create_app
import pytest
import webtest


@pytest.fixture
def test_app():
    app = webtest.TestApp(create_app())
    return app


class TestApi(object):

    def test_healthcheck(self, test_app):
        resp = test_app.get("/api/hc")

        assert resp.status_int == 200
