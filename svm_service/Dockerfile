FROM python:3.9-slim
WORKDIR /app
COPY . /app/
COPY ./tests /app/tests
RUN pip install --no-cache-dir streamlit librosa numpy joblib
RUN pip install pytest
EXPOSE 5000
CMD ["streamlit", "run", "svm_service.py","--server.port", "5000", "--server.address=0.0.0.0"]