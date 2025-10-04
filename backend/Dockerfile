FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create templates directory and move HTML files
RUN mkdir -p templates static/css static/js
RUN cp *.html templates/
RUN cp styles.css static/css/
RUN cp *.js static/js/ 2>/dev/null || true

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
