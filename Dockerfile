FROM apify/actor-python:latest

COPY . ./

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "upwork_best_matches_scraper.py"]
