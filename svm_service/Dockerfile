FROM python:3.9-slim
WORKDIR /app
COPY svm.py /app/
EXPOSE 5000
CMD ["streamlit", "run", "svm_service.py", "--server.address=0.0.0.0"]