# SERVER

FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apk add --no-cache \
    curl \
    gcc \
    g++ \
    freetype-dev \
    libpng-dev \
    pkgconfig \
    python3-dev \
    jpeg-dev \
    zlib-dev \
    libjpeg \
    ffmpeg

# Set up application environment
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
