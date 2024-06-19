# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies and clean up to keep the image size small
RUN apt-get update && apt-get install -y \
    tk \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Specify the command to run on container start
CMD ["gunicorn", "-b", "0.0.0.0:8080", "server:app"]
