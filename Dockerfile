# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install the missing system dependency for OpenCV/DeepFace
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx && \
    apt-get clean

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Define the command to run your Streamlit application
# This includes the necessary flags for Cloud Run deployment
CMD ["streamlit", "run", "app.py", \
    "--server.port=8080", \
    "--server.address=0.0.0.0", \
    "--server.enableCORS=false", \
    "--server.enableXsrfProtection=false"]