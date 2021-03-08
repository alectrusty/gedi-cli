FROM python:3.6

# Copy source code and set working directory
COPY . /app
WORKDIR /app
COPY src/ .

# Install GDAL dependencies
RUN apt-get update && apt-get install -y libgdal-dev

# Update C env vars so compiler can find gdal
RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
RUN export C_INCLUDE_PATH=/usr/include/gdal

# Install dependencies
RUN pip install GDAL==$(gdal-config --version)
RUN pip install -r requirements.txt
RUN pip install pyGEDI

# Run the CLI app
CMD ["python"]