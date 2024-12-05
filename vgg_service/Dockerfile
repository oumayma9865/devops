FROM python:3.10-slim
WORKDIR /app
COPY vgg_service.py /app/
RUN pip install --no-cache-dir streamlit librosa numpy joblib tensorflow
EXPOSE 5001
CMD ["python", "vgg_service.py"]