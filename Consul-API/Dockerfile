FROM python:3.10-slim

RUN useradd -m outbrain
USER outbrain

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV IP_ADDRESS=

WORKDIR /app

#  python dependencies
RUN pip3 install --no-warn-script-location --no-cache-dir flask requests psutil

COPY app .

EXPOSE 5000

# run the Flask application
CMD ["python3", "-m", "flask", "run"]
