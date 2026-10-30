# Source files and release changes

## Selected notebooks

| Uploaded file | Release filename | Generation budget |
| --- | --- | ---: |
| `e11-Revised instructions` | `instruction refined rag.ipynb` | 2048 |
| `table guidance ncreaed token budget` | `table guided rag.ipynb` | 2048 |
| `graph guidance` | `kg guided rag.ipynb` | 2048 |

The additional upload `table guidancetled0.ipynb` uses 1024 tokens in both its settings and its saved request log. It is a different run. Thirteen of its 20 input-answer pairs match the table method's answers in the current paper evidence. All 20 pairs from the selected 2048-token table notebook match. The 1024-token notebook is therefore not used for the main release copy.

## Embedded scores and the paper

All 60 input-answer pairs in the three selected notebooks match the saved answer pairs used for the paper. Their embedded automatic results are not all the same as the paper's final shared-evaluation results.

| Method | Embedded GA | Embedded GN | Embedded QC | Final paper GA | Final paper GN | Final paper QC |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Instruction-refined RAG | 90 | 90 | 55 | 90 | 90 | 55 |
| Table-guided RAG | 90 | 90 | 62.5 | 90 | 90 | 57.5 |
| KG-guided RAG | 90 | 90 | 60 | 90 | 90 | 52.5 |

These are automatic scores, not the separate blinded author-review scores. The comparison was checked against the paper's existing `automatic_item scores.json` records. The code cleanup did not rerun a judge or change those records. Matching answers do not imply matching judgments across different evaluation sessions. The differing embedded values have not been substituted for the paper's final values.

The release notebooks have their output cells cleared. They create new run folders and new results when executed. They are not substitutes for the frozen answer and judgment exports supporting the paper. Preserve those exports separately when releasing the full research resource.

## What changed

- Gave the notebooks descriptive filenames and titles.
- Added plain-language instructions before each code section.
- Simplified comments, status messages and several variable names used for reference checks.
- Used descriptive run-folder names and suggested shorter dataset filenames.
- Removed the duplicate input-and-retrieval-check cell from the table notebook.
- Added the same workbook and ZIP export step to every notebook.
- Allowed generation without an OpenAI key. The judge still requires one when making new requests.
- Made the full-answer display work for both raw generation and scored records.
- Removed a redundant backup cell that referred to an undefined summary variable.
- Cleared saved outputs, execution counts and Colab-specific execution metadata.
- Replaced outdated cell-number instructions with section names.
- Updated code-source checksums and recorded the original uploaded file hashes.

The model prompts, 20 test inputs, generation settings, scoring rubrics, score mappings and guidance text remain unchanged. Data and retrieval checks remain active. The scorer stays in one code cell because it records and fingerprints its own source.

Historical identifiers such as `E11`, `E12` and `E13` remain in item IDs and some provenance fields to keep saved records traceable. They are not the public method names or the current paper's experiment numbering. The readable sections use the method names throughout.

The language guidance was checked for equivalent table and graph records. This does not establish a separate causal advantage for the graph representation.

See [source manifest.json](<source manifest.json>) for the exact source-file and release-file hashes. The cleanup was checked offline. No generation or judging API calls were made during preparation.

## Filenames with spaces

The release files, suggested dataset names, run folders and result exports use spaces instead of underscores. Documentation links and quoted commands follow the new names. The saved-answer loader accepts both naming styles, so existing backups can still be imported. Python identifiers, API key names, JSON fields, study identifiers and the recorded upstream filename keep their original spelling. The model inputs, generation settings and scoring rules are unchanged.
