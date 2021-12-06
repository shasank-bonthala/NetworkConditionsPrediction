# Base image
FROM ucsdets/datascience-notebook:2020.2-stable

USER root


# Install python3, pip3
RUN apt-get update --fix-missing && \
    apt-get install -y git \
                       build-essential \
                       cmake \
                       vim \
                       wget
                       

# Upgrade pip
RUN pip install --upgrade pip

RUN pip install --no-cache-dir numpy \
                               pandas \
                               matplotlib \
                               sklearn
# Cloning
USER jovyan
WORKDIR /tmp
RUN /bin/bash -c "git clone https://github.com/shasank-bonthala/NetworkConditionsPrediction.git"
