run:
	opentelemetry-instrument --service_name fastapi.hexagonal python3 main.py

run_collector:
	opentelemetry-instrument --service_name fastapi.hexagonal --logs_exporter otlp python3 main.py

collector:
	docker run -p 4317:4317 -p 4318:4318 --rm -v $(pwd)/collector-config.yaml:/etc/otelcol/config.yaml otel/opentelemetry-collector

debug:
	opentelemetry-instrument --traces_exporter console --metrics_exporter none python3 main.py