"""Smoke test so CI has something to run until real tests land."""

import pytest


def test_packages_import():
    import common
    import ingest
    import ml
    import serving

    assert all([common, ingest, ml, serving])


@pytest.mark.spark
def test_spark_session_starts():
    pyspark = pytest.importorskip("pyspark")
    spark = pyspark.sql.SparkSession.builder.master("local[1]").appName("ci").getOrCreate()
    try:
        assert spark.range(3).count() == 3
    finally:
        spark.stop()
