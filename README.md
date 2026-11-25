# batatastream

Big Data course project (UPB), team **batata**. A Spark pipeline that ingests public
jailbreak and prompt-injection datasets, cleans and deduplicates them, classifies
adversarial prompts with MLlib, finds emerging attack patterns, and serves results
through a streaming path and a dashboard.

## Team
| Role | Person | Folder |
|---|---|---|
| A. Data engineering (ingest, schema, Kafka, dedup, docker-compose) | mo (@m00ddy) | `ingest/` |
| B. ML and analytics | @Ali-1a | `ml/` |
| C. Serving, dashboard, scalability experiment | @OmarMahmoud1024 | `serving/` |

## Repository layout
```
common/    shared schema, config, utils (changes need agreement from all three of us)
ingest/    download, load, normalize, dedup (MinHash LSH), Kafka producers
ml/        features, MLlib models, clustering, evaluation
serving/   streaming consumer, storage, Streamlit/Grafana dashboard, scalability runs
scripts/   dataset download scripts (datasets are never committed)
report/    PDF report sources and individual essays
docs/      workflow and design notes
```

## Datasets
Downloaded by scripts, never committed:
JBB-Behaviors, WildJailbreak, In-the-Wild Jailbreak Prompts,
jayavibhav/prompt-injection-safety, Qualifire benchmark.

```bash
python scripts/download_datasets.py   # TODO (A)
```

## Quick start
Needs Python 3.11, Java 17 (Spark 3.5 does not start on newer Java), and Docker Desktop.
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
cp .env.example .env
pytest
docker compose up -d                  # TODO (A): Kafka, Postgres, Spark
```

## Pipeline stages
1. Schema and ingestion
2. Cleaning and deduplication (MinHash LSH)
3. Feature extraction
4. MLlib classification
5. Clustering and emerging patterns
6. Streaming (Kafka to Spark Structured Streaming)
7. Dashboard
8. Scalability experiment

## Contributing
Read [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/workflow.md](docs/workflow.md).
If you use an AI coding assistant, it must follow [AGENTS.md](AGENTS.md). New teammates: paste
[docs/onboarding-prompt.md](docs/onboarding-prompt.md) into your Claude to get set up.
