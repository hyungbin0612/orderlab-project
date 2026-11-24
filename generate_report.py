from pathlib import Path

from orderlab.csv_report import revenue_from_csv


def main() -> None:
    root = Path(__file__).resolve().parent
    revenue = revenue_from_csv(root / "data" / "sample_orders.csv")
    site = root / "site"
    site.mkdir(exist_ok=True)

    (site / "index.html").write_text(
        f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>OrderLab Report</title>
</head>
<body>
  <h1>OrderLab Report</h1>
  <p>Revenue: {revenue:,} KRW</p>
</body>
</html>
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
