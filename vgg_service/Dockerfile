FROM python:3.10-slim
WORKDIR /app
COPY ./vgg_service/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY ./tests/test_vgg_service.py /app/test_vgg_service.py
COPY ./vgg_service /app/
EXPOSE 5001
CMD ["streamlit", "run", "/app/vgg_service.py", "--server.port=5001", "--server.address=0.0.0.0"]