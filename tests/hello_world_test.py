from src.hello_world import hello


class TestHelloWorld:
    def test_say_hi(self) -> None:
        assert hello() == "Hello, World!"
