[![Build Status](https://travis-ci.org/leonid133/mesos-cli.svg?branch=master)](https://travis-ci.org/leonid133/mesos-cli)

##CLI for Mesos HTTP API

####Features

- List active frameworks 
- Kill framework by id

####Config

```
mesos_config.cfg

[Mesos]
host: http://172.17.0.4 #Mesos HOST  
port: 5050              #Mesos PORT

```

####How to use

```shell
> python mesos-command-line.py list

List active frameworks id:
6c97e50a-a2d7-43f5-9286-ca3564abab07-0000


> python mesos-command-line.py kill 6c97e50a-a2d7-43f5-9286-ca3564abab07-0000
 
Kill framework by id, 6c97e50a-a2d7-43f5-9286-ca3564abab07-0000


> python mesos-command-line.py list                                          

List active frameworks id:
Not active frameworks

```


