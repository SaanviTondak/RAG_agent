"""Write dev_answers.json (the submission file) from one run of the final system on the dev questions.

  python -m eval.export_dev_answers --run <run_id> [--run-index 0]

Answers are copied exactly as the system produced them (the text the API returns). Fails if any dev question
is missing, so the file is never partly filled.
"""

import argparse
import json

from eval.run_eval import RESULTS_DIR, ROOT, read_jsonl


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", required=True)
    ap.add_argument("--run-index", type=int, default=0, help="which repeat of the run to export")
    ap.add_argument("--out", default=str(ROOT / "dev_answers.json"))
    a = ap.parse_args()

    template = json.loads((ROOT / "questions/dev_answers_example.json").read_text())
    answers = {x["id"]: x["result"]["answer"] for x in read_jsonl(RESULTS_DIR / a.run / "answers.jsonl")
               if x["run"] == a.run_index}
    missing = [i for i in template if i not in answers]
    if missing:
        raise SystemExit(f"{a.run} run {a.run_index} has no answer for: {', '.join(missing)}")
    with open(a.out, "w") as f:
        json.dump({i: answers[i] for i in template}, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Wrote {len(template)} answers from {a.run} (run {a.run_index}) to {a.out}")


if __name__ == "__main__":
    main()
