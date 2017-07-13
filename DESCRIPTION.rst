Elastic-e2e
===========

End to end to check the status of the stack -> Redis -> Logstash -> Elasticsearch -> Zabbix

It send a log message to the redis, pulling elasticsearch until receive the log message and send a trap to zabbix with the process time

Requirements
------------

ElasticSearch
Redis
Logstash
zabbix

Dependencies
------------

Docker

Example Playbook
----------------

.. code::

  - hosts: servers
    roles:
      - { role: elastic-e2e }
