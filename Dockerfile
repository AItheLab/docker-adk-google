# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies that might be needed by some Python packages
RUN apt-get update &&     apt-get install -y --no-install-recommends build-essential &&     apt-get clean &&     rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
# We ensure requirements.txt exists, even if empty
RUN if [ ! -f requirements.txt ]; then touch requirements.txt; fi
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir google-adk

# Copy the rest of the application code into the container
COPY ./app /usr/src/app/app

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV NAME World

# Run main.py when the container launches
CMD ["python", "app/main.py"]
