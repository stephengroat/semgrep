from pathlib import Path
from subprocess import CalledProcessError

import pytest


def idfn(options):
    return "-and-".join(flag.strip("-") for flag in options if flag.startswith("--"))


@pytest.mark.parametrize(
    "options",
    [
        ["--exclude", "excluded.*"],
        ["--include", "included.*"],
        ["--exclude-dir", "excluded"],
        ["--include-dir", "included"],
        ["--include-dir", "included", "--exclude", "excluded.*"],
        ["--exclude-dir", "excluded", "--include", "included.*"],
        ["--exclude", "excluded.*", "--exclude", "included.*"],
        ["--exclude-dir", "excluded", "--exclude-dir", "excluded"],
        ["--include", "excluded.*", "--include", "included.*"],
        ["--include-dir", "excluded", "--include-dir", "excluded"],
    ],
    ids=idfn,
)
def test_exclude_include(run_semgrep, snapshot, options):
    snapshot.assert_match(
        run_semgrep("rules/eqeq.yaml", options=options, target_name="exclude_include",),
        "results.json",
    )