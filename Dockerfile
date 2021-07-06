FROM python:2.7.13
WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y --no-install-recommends \
    python-pip && \
    pip install numpy blossalg
COPY distract-the-trainers.py .
CMD ["distract-the-trainers.py"]
ENTRYPOINT ["python"]
