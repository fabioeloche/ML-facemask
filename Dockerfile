# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies for OpenCV and DeepFace
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libgcc-s1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set environment variables for Cloud Run
ENV PORT=8080
ENV QT_QPA_PLATFORM=offscreen
ENV QT_ASSISTANT_IGNORE_VERSIONS=1

# Expose the port
EXPOSE 8080

# Command to run Streamlit application
CMD streamlit run app.py --server.port $PORT --server.address 0.0.0.0 --server.enableCORS false --server.enableXsrfProtection false