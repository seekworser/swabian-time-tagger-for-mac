FROM centos:7
LABEL maintainer="seekworser1963@gmail.com"

ARG rpm_file="timetagger-2.4.4-1.el7.x86_64.rpm"

ENV rpm_FILE=${rpm_file} \
  DISPLAY=${host_display}

COPY ${rpm_file} /

RUN yum -y update \
  && yum -y localinstall /${rpm_file} \
  && yum install -y mesa-libGL.x86_64 \
  && rm -rf /var/cache/yum/* \
  && yum clean all

CMD ["timetagger", "-p", "8888" ,"server"]
