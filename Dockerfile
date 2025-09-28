# STEP 1: Use a stable base image for DeepFace/TensorFlow compatibility
# Python 3.9 is a safer choice for older ML libraries than 3.11.
FROM python:3.9-slim

# STEP 2: Install necessary system dependencies for DeepFace/OpenCV
# libgl1-mesa-glx and related packages fix the persistent 'libGL.so.1' error.
RUN apt-get update && \
    apt-get install -y \
    libgl1-mesa-glx \
    libsm6 \
    libxext6 \
    ffmpeg && \
    apt-get clean

# STEP 3: Set up the application directory
WORKDIR /app

# STEP 4: Copy and install Python dependencies
# This leverages Docker's cache if only code changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# STEP 5: Copy the rest of your application code (including app.py)
COPY . .

# STEP 6: Define the startup command for Streamlit on Cloud Run
# This uses the required port 8080 and disables security checks (CORS/XSRF)
# that interfere with Cloud Run's reverse proxy.
CMD ["streamlit", "run", "app.py", \
    "--server.port=8080", \
    "--server.address=0.0.0.0", \
    "--server.enableCORS=false", \
    "--server.enableXsrfProtection=false"]