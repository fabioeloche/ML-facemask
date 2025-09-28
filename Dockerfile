# Use a Python version stable with DeepFace/TensorFlow/Keras
FROM python:3.9-slim

# Set environment variable to prevent installation prompts from hanging the build
ENV DEBIAN_FRONTEND=noninteractive

# Install critical system dependencies (libGL.so.1 fix)
# This includes libgl1-mesa-glx and related multimedia libraries
RUN apt-get update && \
    apt-get install -y \
    libgl1-mesa-glx \
    libsm6 \
    libxext6 \
    ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set up the application directory
WORKDIR /app

# Copy and install Python dependencies
# This leverages Docker's cache if only code changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Define the startup command for Streamlit on Cloud Run
CMD ["streamlit", "run", "app.py", \
    "--server.port=8080", \
    "--server.address=0.0.0.0", \
    "--server.enableCORS=false", \
    "--server.enableXsrfProtection=false"]