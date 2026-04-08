FROM python:3.10-slim

# Working directory set karo
WORKDIR /app

# Sabhi files copy karo
COPY . .

# Zaruri libraries install karo (Flask add kiya hai health check ke liye)
RUN pip install --no-cache-dir gymnasium numpy openai openenv-core flask

# Hugging Face isi port par check karta hai
#EXPOSE 7860

# Main execution command
CMD ["python", "inference.py"]
