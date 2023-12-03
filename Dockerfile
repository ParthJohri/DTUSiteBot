# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Download and install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor --output /usr/share/keyrings/google-archive-keyring.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/google-archive-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -y google-chrome-stable && rm -rf /var/lib/apt/lists/*

# Install ChromeDriver
ARG CHROMEDRIVER_VERSION
RUN wget -q -O chromedriver.zip https://chromedriver.storage.googleapis.com/119.0.6045.105/chromedriver_linux64.zip \
    && unzip -o chromedriver.zip -d /tmp \
    && mv /tmp/chromedriver /usr/local/bin/ \
    && rm chromedriver.zip



# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run main_script.py when the container launches
CMD ["python", "main.py"]
