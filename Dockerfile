# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt




# Copy the rest of the application code into the container
COPY . .


# Set the environment variable for running the application
ENV PYTHONUNBUFFERED=1

# Expose the port the application will run on
EXPOSE 8000


# Run the command to start the application
# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
