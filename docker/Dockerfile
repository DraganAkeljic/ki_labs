FROM centos/python-36-centos7
MAINTAINER "dragan.akeljic@gmail.com"
USER root
ADD requirements.txt /tmp
RUN pip3.6 install -U -r /tmp/requirements.txt
EXPOSE 8005
ENV HOME "/home/build"
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
WORKDIR "/home/build"
ENTRYPOINT ["/bin/bash"]
#ENTRYPOINT ["/usr/bin/python3.6", "app.py"]