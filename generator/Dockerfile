# generator.Dockerfile
FROM python:3.9
WORKDIR /usr/app
ADD ./requirements.txt ./
RUN pip install -r requirements.txt
ADD ./ ./
RUN export PYTHONPATH=$PYTHONPATH;.
CMD ["python", "app.py"]