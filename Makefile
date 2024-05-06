run:
	opentelemetry-instrument --service_name fastapi.hexagonal python3 main.py

run_collector:
	opentelemetry-instrument --service_name fastapi.hexagonal --logs_exporter otlp python3 main.py

debug:
	opentelemetry-instrument --traces_exporter console --metrics_exporter none python3 main.py