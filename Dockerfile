FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
# Run the application
CMD ["mcpo", "--port", "8000", "--api-key", "5101ca9bdbabf9be1ace8fba39c298dc", "--", "python3", "NetscalerMCPserver.py"]