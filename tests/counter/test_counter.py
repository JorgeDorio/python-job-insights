from src.counter import count_ocurrences


def test_counter():
    count = count_ocurrences("src/jobs.csv", "New York")
    assert count == 597 != 596
