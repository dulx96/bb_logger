import os
import sys
import pytest
import time
# Make test able to find batch module
src_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(src_path)

# monkey patch session


@pytest.fixture(scope="session")
def monkeysession(request):
    from _pytest.monkeypatch import MonkeyPatch
    mpatch = MonkeyPatch()
    yield mpatch
    # mpatch.undo()


@pytest.fixture(scope='session', autouse=True)
def change_time_sleep(monkeysession):
    def mock_sleep(*args):
        pass
    monkeysession.setattr(time, 'sleep', mock_sleep)


@pytest.fixture(scope='session', autouse=True)
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'


# * mock env
os.environ['ENV'] = 'dev'
os.environ['ACCOUNT'] = 'dummy'
os.environ['PASSWORD'] = 'dummy'
