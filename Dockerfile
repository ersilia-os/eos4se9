FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install STOUT-pypi==2.0.5
RUN pip install rdkit==2025.3.2
RUN pip install numpy==1.26.4

WORKDIR /repo
COPY . /repo
