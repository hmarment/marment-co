from marment_co.app import hello


def test_hello():
    assert hello() == 'Hello, Jub!'
