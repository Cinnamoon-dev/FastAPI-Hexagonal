#!/usr/bin/env bash

opentelemetry-instrument --traces_exporter console --metrics_exporter none python3 main.py