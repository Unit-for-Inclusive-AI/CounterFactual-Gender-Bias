# Add the three Malayalam datasets here

The code package does not include the workbooks yet. Add the three reviewed files to this folder. Renaming the files is optional because the notebooks identify each dataset by its column headings.

| Suggested filename | Original filename | Source column | Target column |
| --- | --- | --- | --- |
| `gender neutral pairs ml.xlsx` | `Gender-Neutral Pairs Malayalam.xlsx` | `Original Terms (Malayalam)` | `Corrected Translation(Inclusive Terms)` |
| `counterfactual pairs ml.xlsx` | `Counterfactual Sentence Pairs Malayalam.xlsx` | `Biased Sentence(Malayalam)` | `Counterfactual Sentence(Malayalam)` |
| `gender inclusive sentences ml.xlsx` | `Gender-Inclusive Sentence Pairs Malayalam.xlsx` | `non-inclusive (Malayalam)` | `inclusive (Malayalam)` |

The notebook reads the first worksheet. Keep the column names and row order. Spaces around column headings are removed when loading the files. Missing pairs are dropped, and unchanged term mappings are filtered as in the study. The original workbooks are also saved in each run for reference.

The notebooks check the processed data against the recorded study corpus. A spelling correction, a reordered row or deduplication can change the retrieval setup and trigger this check. Record such a change as a new dataset version instead of silently changing the reproduction files.

The expected row counts in the original files are 518 term pairs, 725 counterfactual rows and 1036 inclusive sentence pairs. The counterfactual file has 509 distinct pairs and retains its repeated rows.

All three resources were reviewed by the author, who is a native Malayalam speaker. The inclusive sentence file was drafted with ChatGPT and manually corrected to illustrate changes to neighbouring words around a replacement. The other two resources were translated and edited from the material described in the main README.

Record each dataset's source and release licence alongside the files when you publish them.
