# api/Dockerfile
FROM python:3.11-slim

WORKDIR /apicode

# 1) Install system packages needed to build cryptography, mysql-connector, etc.
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential \
      libssl-dev \
      libffi-dev \
      default-libmysqlclient-dev \
      pkg-config \
 && rm -rf /var/lib/apt/lists/*

# 2) Copy and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 3) Copy your API source in
COPY . .

# 4) Expose port & default command
EXPOSE 4000
CMD ["python", "backend_app.py"]
