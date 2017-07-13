.. vim: foldmarker=[[[,]]]:foldmethod=marker

pip ansible role default variables
==================================

.. contents:: Sections
   :local:

elastic_e2e packaging
---------------------

.. envvar:: elastic_e2e_docker_imagen

   elastic_e2e docker image

::

  elastic_e2e_docker_image: melodous/elastic_e2e




.. envvar:: elastic_e2e_version

   elastic_e2e docker image version (TAG)

::

  elastic_e2e_version: latest




.. envvar:: elastic_e2e_docker_labels

   Yaml dictionary which maps Docker labels.
   os_environment: Name of the environment, example: Production, by default "default".
   os_contianer_type: Type of the container, by default elastic_e2e.

::

  elastic_e2e_docker_labels:
    os_environment: "{{ docker_os_environment | default('default') }}"
    os_contianer_type: elastic-e2e




elastic_e2e configuration
-------------------------

.. envvar:: elastic_e2e

   Max number of proccess running

::

  elastic_e2e_max_process: 3




.. envvar:: elastic_e2e_zabbix_server

   Zabbix server to connect

::

  elastic_e2e_zabbix_server: "zabbix"




.. envvar:: elastic_e2e_zabbix_user

   zabbix user to connect zabbix API

::

  elastic_e2e_zabbix_user: "Admin"




.. envvar: elastic_e2e_zabbix_pass

   zabbix password to connect zabbix API

::

  elastic_e2e_zabbix_pass: "zabbix"




.. envvar:: elastic_e2e_zabbix_host

   zabbix host with configured item to send the trap

::

  elastic_e2e_zabbix_host: "elasticsearch"




.. envvar:: elastic_e2e_zabbix_key

   zabbix key to send the trap

::

  elastic_e2e_zabbix_key: "elasticsearch.e2e"




.. envvar:: elastic_e2e_redis_hosts

   List of redis server to send the log

::

  elastic_e2e_redis_hosts:
    - "indexer-01"
    - "indexer-02"




.. envvar:: elastic_e2e_redis_port

   Redis servers port

::

  elastic_e2e_redis_port: 6379




.. envvar:: elastic_e2e_redis_queue

   redis queue to send the log

::

  elastic_e2e_redis_queue: 'filebeat'




.. envvar:: elastic_e2e_message_type

   type of the log that will be send as probe

::

  elastic_e2e_message_type: 'monitoring'




.. envvar:: elastic_e2e_es_servers

   List with the ElasticSearch servers

::

  elastic_e2e_es_servers:
    - "es-master-01"
    - "es-master-02"
    - "es-master-03"




.. envvar:: elastic_e2e_es_index
   Index where to check the log/probe

::

  elastic_e2e_es_index: "logstash-*"




.. envvar:: elastic_e2e_conf_dir

   Directory of config file

::

  elastic_e2e_conf_dir: /etc/opensolutions



