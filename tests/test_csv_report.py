import pytest

from orderlab.csv_report import revenue_from_csv


def test_csv_revenue(sample_csv):
    assert revenue_from_csv(sample_csv) == 35_000


@pytest.mark.parametrize("content", ["", "price,quantity\n"])
def test_csv_empty(tmp_path, content):
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text(content, encoding="utf-8")

    assert revenue_from_csv(csv_file) == 0


def test_csv_missing(tmp_path):
    with pytest.raises(FileNotFoundError):
        revenue_from_csv(tmp_path / "missing.csv")


def test_csv_invalid_number(tmp_path):
    csv_file = tmp_path / "invalid.csv"
    csv_file.write_text(
        "price,quantity\nwrong,2\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        revenue_from_csv(csv_file)
