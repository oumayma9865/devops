FROM python:3.9-slim
WORKDIR /app
COPY . /app/
COPY ./tests/test_svm_service.py /app/test_svm_service.py
RUN pip install -r /app/requirements.txt

EXPOSE 5000
CMD ["streamlit", "run", "/app/svm_service.py","--server.port", "5000", "--server.address=0.0.0.0"]