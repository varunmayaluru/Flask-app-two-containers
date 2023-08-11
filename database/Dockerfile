# Use an official Python runtime as a base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the initialization script into the container at /app
COPY init_db.py /app/

# Run the initialization script when the container launches
CMD ["python", "init_db.py"]
