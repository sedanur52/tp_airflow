# TP — Job Data + Airflow

## Objectif
l’orchestrer avec Airflow.

## Structure
(… mettre l’arborescence …)

## Variables d’environnement
INPUT_PATH=./data/input.xlsx
OUTPUT_PATH=./output/sales_clean.csv
MIN_AMOUNT=0


## Lancer le job
python -m data_job.main

## Lancer les tests
pytest

## Lancer Airflow
docker-compose up -d
