FROM python:3.10-slim
WORKDIR /app
COPY . /app/
COPY ./tests/test_vgg_service.py /app/test_vgg_service.py

RUN pip install -r /app/requirements.txt

EXPOSE 5001
CMD ["streamlit", "run", "/app/vgg_service.py", "--server.port=5001", "--server.address=0.0.0.0"]