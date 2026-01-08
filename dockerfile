# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy all files into container
COPY . /app

# Install dependencies (pytest if tests exist)
RUN pip install --no-cache-dir pytest

# Default command to run your program
CMD ["python", "student.py"]
