# Use a lightweight Python base image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=app.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=5000

# Create a working directory
WORKDIR /app

# Copy only requirements first to cache dependencies
COPY requirements.txt /app/

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y build-essential \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the rest of the application
COPY . /app

# Expose the port Flask will run on
EXPOSE 5000

# Use a non-root user for security
RUN useradd -m flaskuser
USER flaskuser

# Default command to run the Flask app
CMD ["flask", "run"]
