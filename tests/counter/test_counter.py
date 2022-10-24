from src.counter import count_ocurrences


def test_counter() -> None:
    path: str = "src/jobs.csv"
    assert count_ocurrences(path, "New York") == 597, "Should be 597"
    assert count_ocurrences(path, "job") == 3454, "Should be 3454"
