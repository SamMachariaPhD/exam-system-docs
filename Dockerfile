# Use the official Python 3.8 image as a base
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project folder into the container
COPY . /app

# Install system-level dependencies (if any)
# For example, you can install system packages here

# Install Python dependencies using pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install any additional system-level dependencies or software as needed

# Expose any necessary ports (if your application needs them)
# EXPOSE 8080

# Define the command to run your application
CMD ["python", "main.py"]
