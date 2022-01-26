run:
	uvicorn api:app --host 0.0.0.0 --port 8000
install:
	pip install -r requirements.txt