FROM python:3.9-slim
WORKDIR /app
COPY svm_service.py /app/
RUN pip install --no-cache-dir streamlit librosa numpy joblib
EXPOSE 5000
CMD ["streamlit", "run", "svm_service.py", "--server.address=0.0.0.0"]