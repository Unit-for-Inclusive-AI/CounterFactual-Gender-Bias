#!/usr/bin/env python3
"""Check the prepared notebooks without running them or calling an API."""
from pathlib import Path
import ast
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


def checksum(data):
    return hashlib.sha256(data).hexdigest()


def check_notebook(record):
    path = ROOT / record["notebook"]
    assert checksum(path.read_bytes()) == record["release_sha256"], f"File changed: {path.name}"
    notebook = json.loads(path.read_text(encoding="utf-8"))
    assert notebook["nbformat"] == 4
    values = {}
    for index, cell in enumerate(notebook["cells"]):
        if cell["cell_type"] != "code":
            continue
        assert cell["execution_count"] is None and not cell["outputs"]
        source = "".join(cell["source"])
        if source.lstrip().startswith("%pip "):
            continue
        tree = ast.parse(source, filename=f"{path.name} cell {index + 1}")
        compile(tree, str(path), "exec")
        for node in tree.body:
            if not isinstance(node, ast.Assign):
                continue
            for target in node.targets:
                if isinstance(target, ast.Name):
                    try:
                        values[target.id] = ast.literal_eval(node.value)
                    except (ValueError, TypeError):
                        pass
    for name, expected in record["protected_value_sha256"].items():
        encoded = json.dumps(values[name], ensure_ascii=False, sort_keys=True).encode("utf-8")
        assert checksum(encoded) == expected, f"Study setting changed: {path.name} / {name}"
    assert values["GENERATION_KWARGS"]["max_tokens"] == 2048
    assert len(values["test_prompts"]) == 20
    print(f"OK  {path.name}")
    return values


def main():
    records = json.loads((ROOT / "docs/source manifest.json").read_text())
    values = [check_notebook(record) for record in records]
    for key in ("test_prompts", "FIRST_PASS_TEMPLATE", "COT_TEMPLATE",
                "GENDER_RUBRIC", "QUALITY_RUBRIC", "SCORING_POLICY"):
        assert all(value[key] == values[0][key] for value in values), key
    print("All three notebooks have matching study inputs, prompts and scoring rules.")
    print("No notebook cells, package installers or model requests were executed.")


if __name__ == "__main__":
    main()
