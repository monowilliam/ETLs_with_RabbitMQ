# Proyecto ETLs con Mensajería
Estudiante: William Aguirre Zapata

## ETL para el archivo de conceptos

`$ cd  environment/etls`

`$ python concepts_etl.py`

Al final en la base de datos hacemos un count de la tabla concepts 
`SELECT count(*) FROM myDB.concepts;`
Y deben existir 22.255 registros

##  ETL de conceptos con el Worker
### En MV del Consumidor

`$ vagrant ssh consumer`

`$ cd etls` 

`$ python3 concepts_worker.py`

### En MV del Productor 
`$ vagrant ssh producer`

`$ cd task` 

`$ python3 send_task_oneConsumer.py 1Jx_Rt1nGpHuNZ8EOaDayjg_LpUFmd4AF concepts`

## Escenario de RabbitMQ con dos consumidores
### En MV del Consumidor 1
`$ vagrant ssh consumer`

`$ cd etls` 

`$ python3 generic_worker.py`

### En MV del Consumidor 2
`$ vagrant ssh consumer2`

`$ cd etls` 

`$ python3 generic_worker.py`

### En MV de Productor
`$vagrant ssh producer`

`$ cd task`

Primero cargaremos la BD con más datos:

`$ python3 send_task.py 1Jx_Rt1nGpHuNZ8EOaDayjg_LpUFmd4AF concepts`

Después cargamos la BD con menos datos para visualizar la Work Queues de RabbitMQ:

`$ python3 send_task.py 1hAmILJWUsMULDDj2g65BbTMPL_IEUev6 vocabulary`
