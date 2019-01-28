FROM java

RUN mkdir /disyo
WORKDIR /disyo

RUN wget mirrors.m247.ro/apache/jena/binaries/apache-jena-fuseki-3.10.0.tar.gz && tar -zxvf apache-jena-fuseki-3.10.0.tar.gz && rm apache-jena-fuseki-3.10.0.tar.gz
WORKDIR /disyo/apache-jena-fuseki-3.10.0

COPY disyo.owl disyo.owl
RUN mkdir run
COPY shiro.ini run/shiro.ini
CMD ./fuseki-server --update --debug --file=disyo.owl /disyo
