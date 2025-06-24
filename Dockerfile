FROM apify/actor-python:latest

# Install build essentials and development tools
USER root
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

# Don't switch users - stay as root or let Apify handle it
# USER myuser  <-- Remove this line

# Copy your project files
COPY . ./

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Set the command to run your scraper
CMD python upwork_best_matches_scraper.py
