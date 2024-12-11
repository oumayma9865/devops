FROM python:3.10-slim
WORKDIR /app
COPY . /app/
COPY ./tests/test_vgg_service.py /app/test_vgg_service.py
RUN pip install --no-cache-dir --timeout=300 streamlit librosa numpy joblib tensorflow
RUN pip install pytest
EXPOSE 5001
CMD ["streamlit", "run", "vgg_service.py", "--server.port=5001", "--server.address=0.0.0.0"]