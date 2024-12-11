FROM python:3.9-slim
WORKDIR /app
COPY ./svm_service/requirements.txt /app/requirements.txt
COPY ./tests/test_svm_service.py /app/test_svm_service.py
RUN pip install -r /app/requirements.txt
COPY ./svm_service /app/
EXPOSE 5000
CMD ["streamlit", "run", "/app/svm_service.py","--server.port", "5000", "--server.address=0.0.0.0"]