Welcome to elastic-e2e Ansible Role’s documentation!
====================================================

Elastic-e2e
-----------

End to end to check the status of the stack -&gt; Redis -&gt; Logstash
-&gt; Elasticsearch -&gt; Zabbix

It send a log message to the redis, pulling elasticsearch until receive
the log message and send a trap to zabbix with the process time

### Requirements

ElasticSearch Redis Logstash zabbix

### Dependencies

Docker

### Example Playbook

    - hosts: servers
      roles:
        - { role: elastic-e2e }

pip ansible role default variables
----------------------------------

#### Sections

-   elastic\_e2e packaging
-   elastic\_e2e configuration

### elastic\_e2e packaging

`elastic_e2e_docker_imagen`

> elastic\_e2e docker image

    elastic_e2e_docker_image: melodous/elastic_e2e

`elastic_e2e_version`

> elastic\_e2e docker image version (TAG)

    elastic_e2e_version: latest

`elastic_e2e_docker_labels`

> Yaml dictionary which maps Docker labels. os\_environment: Name of the
> environment, example: Production, by default “default”.
> os\_contianer\_type: Type of the container, by default elastic\_e2e.

    elastic_e2e_docker_labels:
      os_environment: "{{ docker_os_environment | default('default') }}"
      os_contianer_type: elastic-e2e

### elastic\_e2e configuration

`elastic_e2e`

> Max number of proccess running

    elastic_e2e_max_process: 3

`elastic_e2e_zabbix_server`

> Zabbix server to connect

    elastic_e2e_zabbix_server: "zabbix"

`elastic_e2e_zabbix_user`

> zabbix user to connect zabbix API

    elastic_e2e_zabbix_user: "Admin"

    elastic_e2e_zabbix_pass: "zabbix"

`elastic_e2e_zabbix_host`

> zabbix host with configured item to send the trap

    elastic_e2e_zabbix_host: "elasticsearch"

`elastic_e2e_zabbix_key`

> zabbix key to send the trap

    elastic_e2e_zabbix_key: "elasticsearch.e2e"

`elastic_e2e_redis_hosts`

> List of redis server to send the log

    elastic_e2e_redis_hosts:
      - "indexer-01"
      - "indexer-02"

`elastic_e2e_redis_port`

> Redis servers port

    elastic_e2e_redis_port: 6379

`elastic_e2e_redis_queue`

> redis queue to send the log

    elastic_e2e_redis_queue: 'filebeat'

`elastic_e2e_message_type`

> type of the log that will be send as probe

    elastic_e2e_message_type: 'monitoring'

`elastic_e2e_es_servers`

> List with the ElasticSearch servers

    elastic_e2e_es_servers:
      - "es-master-01"
      - "es-master-02"
      - "es-master-03"

`elastic_e2e_es_index``Index where to check the log/probe`

    elastic_e2e_es_index: "logstash-*"

`elastic_e2e_conf_dir`

> Directory of config file

    elastic_e2e_conf_dir: /etc/opensolutions

Changelog
---------

**elastic-e2e**

This project adheres to Semantic Versioning and human-readable
changelog.

### elastic-e2e master - unreleased

##### Added

-   First addition

##### Changed

-   First change

### elastic-e2e v0.0.2 - 2017/07/17

##### Added

-   Fixed playbook.yml

### elastic-e2e v0.0.1 - 2017/07/13

##### Added

-   Initial version

Copyright
---------

elastic-e2e

Copyright (C) 2017/07/13 Raúl Melo
&lt;<raul.melo@opensolutions.cloud>&gt;

LICENSE
