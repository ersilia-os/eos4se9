FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install tensorflow==2.10.1
RUN pip install pystow==0.8.5
RUN pip install rdkit==2025.3.2
RUN pip install numpy==1.26.4

WORKDIR /repo
COPY . /repo
