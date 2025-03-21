#fixtures
#functions used for setup and tear down methods
#help manage test dependency
#scope can be defined
import pytest


@pytest.fixture
def sample_data():
    print("\n Setup: Creating test data")
    data = {"name": "Alice", "age": 30}
    yield data
    print("Tear down: cleaning up test data")


#fixture passed as argument - dependency injection
#executes first fixture and then below function
def test_example(sample_data):
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30
    print("Test Executed successfully")

#yield will transfer code control until tear down
#after yield everything is teardown
