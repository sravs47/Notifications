FROM centos:7
ENV PYTHON_VERSION "3.6.0"

RUN yum -y install epel-release \
&& yum -y install https://centos7.iuscommunity.org/ius-release.rpm \
&& yum -y install python36u python36-setuptools \
&& easy_install-3.6 pip


WORKDIR /Notifications
COPY . .

RUN pip install -r requirements.txt
RUN pip install -e .
EXPOSE 5000

CMD python3.6 /Notifications/Notifications/__init__.py




