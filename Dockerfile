# Use an official lightweight Python image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy app files into container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Flask's default port
EXPOSE 5000

# Default command to run the app
CMD ["python", "app.py"]
