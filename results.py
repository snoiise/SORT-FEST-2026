from pathlib import Path
import csv
import html
from collections import defaultdict
from datetime import datetime


BASE_DIR = Path("algorithms")
BUILD_DIR = BASE_DIR / "benchmark"

RESULTS_FILE = BUILD_DIR / "results.csv"
OUTPUT_FILE = BUILD_DIR / "results.html"


ACCENT = "#e85d04"


def esc(value):
    return html.escape(str(value))


def load_results():
    with RESULTS_FILE.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def format_time(seconds):
    value = float(seconds)

    if value < 0.001:
        return f"{value * 1_000_000:.1f} µs"

    if value < 1:
        return f"{value * 1000:.3f} ms"

    return f"{value:.3f} s"


def generate_html(rows):
    algorithms = defaultdict(list)

    for row in rows:
        algorithms[row["algorithm"]].append(row)

    leaderboard = []

    for algorithm, entries in algorithms.items():
        valid = [
            float(row["time"])
            for row in entries
            if row["result"] == "OK"
        ]

        total = sum(valid) if valid else float("inf")

        leaderboard.append({
            "algorithm": algorithm,
            "author": entries[0]["author"],
            "total": total,
            "entries": entries,
        })

    leaderboard.sort(key=lambda x: x["total"])

    generated = datetime.now().strftime("%d %b %Y")

    leaderboard_rows = []

    for position, item in enumerate(leaderboard, 1):
        total = (
            format_time(item["total"])
            if item["total"] != float("inf")
            else "FAILED"
        )

        leaderboard_rows.append(f"""
        <tr>
            <td class="rank">{position:02}</td>
            <td>
                <a class="algorithm-link" href="#{slug(item["algorithm"])}">
                    {esc(item["algorithm"])}
                </a>
            </td>
            <td class="author">{esc(item["author"])}</td>
            <td class="total">{total}</td>
        </tr>
        """)

    algorithm_sections = []

    for item in leaderboard:
        algorithm = item["algorithm"]
        entries = item["entries"]

        scenarios = []
        for row in entries:
            if row["scenario"] not in scenarios:
                scenarios.append(row["scenario"])

        sizes = []
        for row in entries:
            if row["size"] not in sizes:
                sizes.append(row["size"])

        # Keep the scenario order from the benchmark.
        table_headers = "".join(
            f'<th>{esc(scenario.replace("_", " "))}</th>'
            for scenario in scenarios
        )

        table_rows = []

        for size in sizes:
            cells = []

            for scenario in scenarios:
                matching = next(
                    (
                        row for row in entries
                        if row["size"] == size
                        and row["scenario"] == scenario
                    ),
                    None,
                )

                if matching is None:
                    cells.append("<td>—</td>")
                    continue

                if matching["result"] != "OK":
                    cells.append(
                        f'<td class="failed">{esc(matching["result"])}</td>'
                    )
                else:
                    cells.append(
                        f'<td>{format_time(matching["time"])}</td>'
                    )

            table_rows.append(
                f"""
                <tr>
                    <th class="size">{int(size):,}</th>
                    {"".join(cells)}
                </tr>
                """
            )

        algorithm_sections.append(f"""
        <section class="algorithm" id="{slug(algorithm)}">

            <div class="algorithm-heading">
                <div>
                    <h2>{esc(algorithm)}</h2>
                    <div class="algorithm-author">{esc(item["author"])}</div>
                </div>

                <div class="algorithm-total">
                    <span>TOTAL</span>
                    <strong>{format_time(item["total"])}</strong>
                </div>
            </div>

            <div class="table-wrap">
                <table class="benchmarks">
                    <thead>
                        <tr>
                            <th>SIZE</th>
                            {table_headers}
                        </tr>
                    </thead>
                    <tbody>
                        {"".join(table_rows)}
                    </tbody>
                </table>
            </div>

        </section>
        """)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Sort Fest 2026 — Results</title>

<style>

:root {{
    --bg: #0b0b0b;
    --panel: #101010;
    --line: #292929;
    --line-light: #1d1d1d;
    --text: #eeeeee;
    --muted: #8c8c8c;
    --dim: #5d5d5d;
    --accent: {ACCENT};
}}

* {{
    box-sizing: border-box;
}}

html {{
    scroll-behavior: smooth;
}}

body {{
    margin: 0;
    background: var(--bg);
    color: var(--text);
    font-family:
        "IBM Plex Mono",
        "Cascadia Code",
        "Consolas",
        monospace;
    font-size: 14px;
}}

a {{
    color: inherit;
    text-decoration: none;
}}

.page {{
    width: min(1180px, calc(100% - 40px));
    margin: 0 auto;
}}

header {{
    height: 76px;
    border-bottom: 1px solid var(--line);
    display: flex;
    align-items: center;
    justify-content: space-between;
}}

.logo {{
    font-size: 18px;
    font-weight: 700;
    letter-spacing: -0.5px;
}}

.logo span {{
    color: var(--accent);
}}

.header-right {{
    color: var(--muted);
    font-size: 12px;
}}

main {{
    padding: 58px 0 100px;
}}

.title-row {{
    display: flex;
    justify-content: space-between;
    align-items: end;
    margin-bottom: 25px;
}}

h1 {{
    margin: 0;
    font-size: 32px;
    letter-spacing: -1.5px;
}}

.date {{
    color: var(--muted);
    font-size: 12px;
}}

.leaderboard {{
    border-top: 2px solid var(--text);
    margin-bottom: 90px;
}}

table {{
    border-collapse: collapse;
    width: 100%;
}}

.leaderboard th {{
    text-align: left;
    color: var(--dim);
    font-size: 10px;
    letter-spacing: 1px;
    font-weight: 500;
    padding: 11px 12px;
    border-bottom: 1px solid var(--line);
}}

.leaderboard td {{
    padding: 15px 12px;
    border-bottom: 1px solid var(--line-light);
}}

.leaderboard tr:hover {{
    background: #111;
}}

.rank {{
    width: 60px;
    color: var(--dim);
}}

.algorithm-link {{
    font-weight: 600;
}}

.algorithm-link:hover {{
    color: var(--accent);
}}

.author {{
    color: var(--muted);
}}

.total {{
    text-align: right;
    font-variant-numeric: tabular-nums;
}}

.algorithm {{
    margin-bottom: 76px;
    scroll-margin-top: 30px;
}}

.algorithm-heading {{
    display: flex;
    justify-content: space-between;
    align-items: end;
    border-bottom: 1px solid var(--line);
    padding-bottom: 14px;
    margin-bottom: 18px;
}}

.algorithm-heading h2 {{
    margin: 0;
    font-size: 22px;
    letter-spacing: -0.8px;
}}

.algorithm-author {{
    color: var(--muted);
    font-size: 12px;
    margin-top: 5px;
}}

.algorithm-total {{
    text-align: right;
}}

.algorithm-total span {{
    display: block;
    color: var(--dim);
    font-size: 9px;
    letter-spacing: 1px;
    margin-bottom: 4px;
}}

.algorithm-total strong {{
    font-size: 15px;
    font-weight: 500;
}}

.table-wrap {{
    overflow-x: auto;
}}

.benchmarks {{
    min-width: 720px;
}}

.benchmarks th {{
    color: var(--dim);
    font-size: 10px;
    letter-spacing: 0.7px;
    text-align: right;
    font-weight: 500;
    padding: 9px 12px;
    border-bottom: 1px solid var(--line);
    white-space: nowrap;
}}

.benchmarks th:first-child {{
    text-align: left;
}}

.benchmarks td {{
    text-align: right;
    padding: 11px 12px;
    border-bottom: 1px solid var(--line-light);
    color: #cfcfcf;
    font-variant-numeric: tabular-nums;
    white-space: nowrap;
}}

.benchmarks tr:hover td,
.benchmarks tr:hover th {{
    background: #111;
}}

.size {{
    color: var(--text) !important;
    font-weight: 500 !important;
    font-variant-numeric: tabular-nums;
}}

.failed {{
    color: #d85c5c !important;
}}

footer {{
    border-top: 1px solid var(--line);
    padding: 18px 0 30px;
    display: flex;
    justify-content: space-between;
    color: var(--dim);
    font-size: 10px;
    letter-spacing: 0.4px;
}}

.status {{
    color: var(--accent);
}}

@media (max-width: 700px) {{

    .page {{
        width: min(100% - 24px, 1180px);
    }}

    header {{
        height: 62px;
    }}

    main {{
        padding-top: 38px;
    }}

    .title-row {{
        display: block;
    }}

    .date {{
        margin-top: 8px;
    }}

    h1 {{
        font-size: 26px;
    }}

    .leaderboard th:nth-child(3),
    .leaderboard td:nth-child(3) {{
        display: none;
    }}

    .algorithm-heading {{
        align-items: start;
    }}

    .algorithm-total {{
        padding-top: 3px;
    }}

}}

</style>
</head>

<body>

<div class="page">

<header>
    <div class="logo">SORT<span>FEST</span> 2026</div>
    <div class="header-right">BENCHMARK RESULTS</div>
</header>

<main>

    <div class="title-row">
        <h1>Results</h1>
        <div class="date">{generated}</div>
    </div>

    <div class="leaderboard">

        <table>
            <thead>
                <tr>
                    <th>#</th>
                    <th>ALGORITHM</th>
                    <th>AUTHOR</th>
                    <th style="text-align:right;">TOTAL</th>
                </tr>
            </thead>

            <tbody>
                {"".join(leaderboard_rows)}
            </tbody>
        </table>

    </div>

    {"".join(algorithm_sections)}

</main>

<footer>
    <div>SORT FEST 2026</div>
    <div class="status">SUBMISSIONS OPEN</div>
</footer>

</div>

</body>
</html>
"""


def slug(value):
    result = "".join(
        char.lower() if char.isalnum() else "-"
        for char in value
    )

    while "--" in result:
        result = result.replace("--", "-")

    return result.strip("-")


def main():
    if not RESULTS_FILE.exists():
        print(f"Results file not found: {RESULTS_FILE}")
        return

    rows = load_results()

    if not rows:
        print("Results file is empty.")
        return

    OUTPUT_FILE.write_text(
        generate_html(rows),
        encoding="utf-8",
    )

    print(f"✓ Generated: {OUTPUT_FILE.resolve()}")


if __name__ == "__main__":
    main()