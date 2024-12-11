FROM python:3.9-slim
WORKDIR /app
COPY ./tests/test_svm_service.py /app/test_svm_service.py
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 5000
CMD ["streamlit", "run", "/app/svm_service.py","--server.port", "5000", "--server.address=0.0.0.0"]