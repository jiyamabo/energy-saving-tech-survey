FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

# Adds metadata to the image as a key value pair example LABEL version="1.0"
# LABEL maintainer="J Iyamabo ji@iyamabo.net"

## Set environment variables
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH="/root/anaconda3/bin:${PATH}"
ARG PATH="/root/anaconda3/bin:${PATH}"

RUN apt-get update --fix-missing && apt-get install -y \
	wget \
	bzip2 \
	ca-certificates \
    build-essential \
    byobu \
    curl \
    git-core \
    htop \
    pkg-config \
    python3-dev \
    python-setuptools \
    unzip \
    && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

## Install Anaconda
# RUN echo "export PATH=/opt/conda/bin:$PATH" > /etc/profile.d/conda.sh && \
# 	wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh -O ~/anaconda.sh && \
#     # wget --quiet https://repo.continuum.io/archive/Anaconda3-5.0.0.1-Linux-x86_64.sh -O ~/anaconda.sh && \
#     /bin/bash ~/anaconda.sh -b -p /opt/conda && \
#     rm ~/anaconda.sh

# ENV PATH /opt/conda/bin:$PATH

# RUN pip --no-cache-dir install --upgrade \
#         altair \
#         sklearn-pandas

RUN wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh \
	&& mkdir root/.conda \
	&& sh Anaconda3-2022.05-Linux-x86_64.sh -b \
	&& rm -f Anaconda3-2022.05-Linux-x86_64.sh

RUN conda create -y --name venv python=3.9

COPY . src/
RUN /bin/bash -c "cd src \
	&& source activate venv \
	&& pip install -r requirements.txt"