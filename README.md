# Malayalam inclusive generation

This project studies how to produce gender-inclusive Malayalam sentences while keeping their meaning and natural wording. It includes three Google Colab notebooks that use the same datasets and the same 20 development inputs.

Each notebook retrieves relevant examples, generates an answer and uses a simple lexical check to decide whether to request one revision. The two guided methods add term replacements and usage notes to the retrieved examples.

## Choose a notebook

| Notebook | What it does |
| --- | --- |
| [Instruction-refined RAG](<notebooks/instruction refined rag.ipynb>) | Uses retrieved examples and instructions that allow necessary grammatical and inclusive-reference changes. |
| [Table-guided RAG](<notebooks/table guided rag.ipynb>) | Adds matching replacement rules and usage notes from ordinary table records. |
| [KG-guided RAG](<notebooks/kg guided rag.ipynb>) | Gets the same guidance by following relationships in a knowledge graph. |

The table and graph methods use the same facts, matching rules, selection limits and prompt rendering. Their checks verify this before generation. A difference between their saved outputs does not by itself show that graph storage improves generation.

## What you need

- A Google Colab session. A CPU runtime is sufficient.
- A Groq API key with access to `openai/gpt-oss-120b`.
- The three Malayalam Excel files described in [data/README.md](data/README.md).
- An OpenAI API key only if you want to run the automated judge. The notebooks retain the logged judge identifier `gpt-6-astra`, so your account must have access to that model for this evaluation to run. There is no automatic model substitution.

Generation and evaluation use separate API services and may use paid credit. The notebooks save completed requests so that an interrupted run can resume in the same runtime.

## Run a notebook

1. Open one notebook in Google Colab and start a fresh runtime for that method.
2. Add `GROQ_API_KEY` in Colab Secrets and allow notebook access. Add `OPENAI_API_KEY` if you plan to run the judge. `HF_TOKEN` is optional.
3. Run **Install the packages**, followed by **Set up the run**.
4. Run **Load the three datasets** and select all three workbooks together. The original workbook names also work because the loader checks the column headings.
5. Continue through the retrieval, guidance and prompt sections in order. The notebooks keep the original study settings and stop if the corpus, chunks or retrieved context do not match their recorded checksums.
6. Run **Generate answers**. This is where Groq requests begin. Save the raw-answer ZIP when the notebook offers it.
7. Run **Evaluate saved answers** if you want automatic scores. It reads the saved answers and does not generate them again. You can skip this section when you only need the answers.
8. Run **Export the results**. You will receive a ZIP of the run. When evaluation is available, the export also contains a workbook and displays N, GA, GN and QC.
9. Use **Read the full answers** to inspect the text without making more API calls.

If generation stops after a request error, rerun **Generate answers** in the same runtime. If judging stops, rerun **Evaluate saved answers**. Keep the downloaded backups because a Colab runtime reset removes its temporary files. Importing an evaluation backup can restore matching judgments, but it does not restore an entire generation runtime.

## Data

Add these workbooks to the `data` folder before publishing the repository.

| Suggested filename | Content | Rows in the study |
| --- | --- | ---: |
| `gender neutral pairs ml.xlsx` | Gendered expressions and inclusive alternatives | 518 |
| `counterfactual pairs ml.xlsx` | Biased sentences and revised alternatives | 725 |
| `gender inclusive sentences ml.xlsx` | Sentence pairs showing replacements in context | 1036 |

The term pairs started from the English resource accompanying Chinnan and colleagues' RAG and CoT study. They were translated into Malayalam, manually edited and extended with everyday terms. The counterfactual pairs also came through that study, whose English examples were constructed from gender-bias phrases in SOFA. They were translated and manually edited.

The inclusive sentence file was created for this project. ChatGPT drafted examples from the reviewed term mappings, and the native Malayalam-speaking author reviewed and corrected them. Their purpose is to show how neighbouring word forms and endings may change when an inclusive term is used. All three datasets were author verified.

The counterfactual file contains 509 distinct pairs across its 725 rows. Repeated rows are retained to match the completed runs. The corpora are used for retrieval; the notebooks do not fine-tune model weights.

## Settings used by all three notebooks

| Setting | Value |
| --- | --- |
| Generator | `openai/gpt-oss-120b` through Groq |
| Generation output budget | 2048 tokens |
| Temperature | 0 |
| Reasoning effort | Medium |
| Embedding model | `sentence-transformers/LaBSE` |
| Retrieval | Five FAISS chunks per input |
| Chunk size and overlap | 500 and 50 characters |
| Inputs | 14 completion tasks and six rewriting tasks |
| Guided methods | Up to six records and one example per record within 6000 characters |

The package versions are listed in [requirements.txt](requirements.txt) and in the first cell of each notebook. The notebooks also record the actual package versions during a run. They are designed for Colab, including its file-upload and Secrets features.

For a local check of the downloaded release, run `python "tools/check notebooks.py"`. It checks notebook syntax, cleared outputs and the recorded prompts and settings without executing the notebooks or calling an API. A changed release file will need a new documented checksum.

The provider's model revision is not pinned. A new run may produce different answers even with the same settings. Keep its outputs separate from the saved results used in the paper.

## Evaluation

The automated judge evaluates saved answers in separate quality and gender stages. The original rubrics and score mappings are retained in the notebooks.

| Metric | What it measures | Item score |
| --- | --- | --- |
| GA | Whether the answer avoids unsupported gender assumptions | 0, 1 or 2 |
| GN | Whether the wording is contextually inclusive | 0 or 1 |
| QC | Grammar, naturalness, meaning and task fulfilment | 0, 1 or 2 |

Percentages are normalised mean scores. For example, QC is the sum of the item scores divided by twice the number of answers, multiplied by 100. It is not the percentage of answers receiving full credit.

Empty, incomplete, wrong-language and non-answer outputs receive zero on all three measures. A completed answer can still receive QC zero while being assessed separately for GA and GN. API failures remain unresolved and are not counted as zero scores. Final means are withheld until evaluation is complete.

The evaluator also creates a blank review form with method labels and automatic scores removed. Identical input-answer pairs are shown once. Keep the private mapping file and automatic results separate from the reviewer. These blank forms do not contain the completed author-review ratings reported in the paper.

## Saved files

Each run receives its own folder under `/content` with a descriptive method name and timestamp. The backup contains the input list, uploaded corpora, generation settings, request logs and answers. Guided runs also save their guidance records and checks. KG runs save their graph nodes and relationships.

After evaluation, the folder also contains item scores, judge findings, a readable HTML report, review forms and a workbook. **Export the results** displays a compact score table and saves it as `method summary.csv`.

The notebooks in this repository have empty output cells and can be read without exposing old run logs. The supplied table and KG notebooks had embedded judgments that differ from the paper's final shared evaluation. The answers match, but those embedded scores are not presented as the final paper results. [Source notes](<docs/source notes.md>) explain this and the separate 1024-token table run.

## Reuse and attribution

Use the notes as contextual suggestions. A relevant gender reference or a person's self-description should be preserved. Some inputs intentionally contain stereotypes because the task is to revise them.

The upstream studies are:

- [Gender inclusive language generation framework](https://doi.org/10.1016/j.knosys.2025.114092) by Chinnan and colleagues.
- [Social Bias Probing and the SOFA benchmark](https://aclanthology.org/2024.emnlp-main.812/) by Marchiori Manerba and colleagues.

AI assistance was used in data drafting, coding and documentation. The native-speaking author reviewed the datasets and is responsible for the research claims. The release cleanup keeps the original model prompts and evaluation rubrics unchanged.

No new licence is assigned by this preparation step. Confirm the code licence and the conditions for redistributed or translated upstream data before publishing. Add the agreed author names and paper citation when they are final.
