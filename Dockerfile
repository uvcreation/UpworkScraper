FROM apify/actor-python:latest

# Install build essentials and development tools
USER root
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

# Switch back to the default user
USER myuser

# Copy your project files
COPY . ./

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Set the command to run your scraper
CMD python upwork_best_matches_scraper.py
