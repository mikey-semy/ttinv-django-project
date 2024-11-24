# Use a variable for the Python version
ARG PYTHON_VERSION=3.12.1

# Use a variable for the Alpine Linux version
ARG ALPINE_VERSION=3.19

# Use the latest Python and Alpine Linux versions by default
FROM python:${PYTHON_VERSION}-alpine${ALPINE_VERSION}

WORKDIR /usr/src/ttinv

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update the package index and install dependencies
RUN apk update \
    && apk add --no-cache postgresql-client build-base postgresql-dev libpq-dev

# Install pip and requirements
RUN apk add --no-cache python3-pip \
    && pip3 install --upgrade pip \
    && pip3 install -r requirements.txt

# Copy files and directories, set ownership and permissions
COPY . /usr/src/ttinv
COPY entrypoint.sh /usr/src/ttinv/entrypoint.sh
RUN mkdir -p /usr/src/ttinv/static \
    && mkdir -p /usr/src/ttinv/media \
    && chown -R 1000:1000 /usr/src/ttinv/media \
    && chmod +x /usr/src/ttinv/entrypoint.sh

# Expose the port
EXPOSE 8000

# Create a new user and switch to it
RUN adduser --disabled-password ttinv \
    && usermod -u 1000 ttinv \
    && groupmod -g 1000 ttinv \
    && chown -R ttinv:ttinv /usr/src/ttinv

USER ttinv

# Set the entrypoint
ENTRYPOINT ["sh", "/usr/src/ttinv/entrypoint.sh"]