FROM python:3.8-alpine

# Install required packages
RUN apk add --no-cache git

# Copy the requirements file and install the dependencies
COPY requirements.txt /app/requirements.txt
COPY config.toml /app/config.toml
RUN pip install -r /app/requirements.txt

# Copy the application code
COPY . /app

# Set the working directory
WORKDIR /app

# Set the environment variable for the Github access token
ENV GITHUB_TOKEN=access_token

# Run the command to start the application
CMD ["python", "git_regex_search/git_regex_search.py"]
