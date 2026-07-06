# 1. Use an official Python runtime as the base image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the dependencies file first (for better caching)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code
COPY app.py .
COPY test_app.py .
COPY my-app/* .

# 6. Tell Docker which port this container uses
EXPOSE 5000

# 7. Command to run the app when the container starts
CMD ["python", "app.py"]