# Use Python 3.8 Alpine as the base image
FROM python:3.8-alpine

# Define the working directory inside the container
ENV APP_DIR /app
RUN mkdir -p $APP_DIR
WORKDIR $APP_DIR

# Install required system dependencies (Removed MongoDB)
RUN apk add --no-cache \
    gcc \
    musl-dev \
    python3-dev \
    libjpeg-turbo-dev \
    zlib-dev \
    freetype-dev \
    rabbitmq-server

# Copy the application files
COPY . $APP_DIR

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Set the correct working directory for the API
WORKDIR $APP_DIR/API

# Expose the API port
EXPOSE 8094

# Start the API
CMD ["python3", "api.py"]

