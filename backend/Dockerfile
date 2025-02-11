# Use official Python image
FROM python:3.11

# Set working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Expose the Flask port
EXPOSE 5000

# Set the entry point to run Gunicorn
CMD ["gunicorn", "-c", "gunicorn_config.py", "run:app"]
