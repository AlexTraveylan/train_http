# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire folder to the working directory
COPY . .

# Expose port 5000
EXPOSE 5000

# Set the entry point command
CMD ["flask", "run","--host=0.0.0.0"]
