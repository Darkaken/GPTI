FROM python:3.10-slim-bullseye

#Install necessary dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y gcc
RUN pipenv lock

# Establish working directory
WORKDIR /usr/src/backend

# Copy Pipfile and Pipfile.lock to image
COPY Pipfile Pipfile.lock ./

# Install packages
RUN pipenv install --dev --system --deploy

# Copy application files to image
COPY . /usr/src/backend/

# Expose port
EXPOSE 8000

# Run script every time the container starts
# ENTRYPOINT ["python", "-m", "pipenv", "run"]

# Run this command when no command is specified
CMD ["uvicorn", "main:app", "--reload", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]