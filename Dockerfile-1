# Dockerfile for Flask app
# Use an official Python runtime as a parent image
FROM python:3.6-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Jinja2 version compatible with Flask 1.1.2
RUN pip install Jinja2==2.11.3

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
