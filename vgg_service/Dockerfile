FROM python:3.10-slim
WORKDIR /app
COPY ./tests/test_vgg_service.py /app/test_vgg_service.py
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 5001
CMD ["streamlit", "run", "/app/vgg_service.py", "--server.port=5001", "--server.address=0.0.0.0"]