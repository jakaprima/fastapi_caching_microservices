# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy everything
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for FastAPI
EXPOSE 8000

# Command to run FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
