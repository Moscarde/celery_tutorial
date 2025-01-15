# Celery Tutorial

![Celery Logo](https://docs.celeryq.dev/en/latest/_images/celery-banner-small.png)

Este repositório é um estudo simples sobre a biblioteca [Celery](https://docs.celeryq.dev/en/stable/) do Python, seguindo sua documentação oficial.

## Pré-requisitos

Certifique-se de ter os seguintes componentes instalados:
- Python (3.7 ou superior)
- Docker (para rodar o RabbitMQ)

## Como executar

### 1. Iniciar o RabbitMQ
O Celery utiliza uma fila de mensagens para gerenciar tarefas assíncronas. Neste tutorial, usaremos o RabbitMQ como broker. Para iniciá-lo, execute o comando abaixo:

```bash
docker run -d -p 5672:5672 rabbitmq
```

### 2. Iniciar o Celery

No terminal, inicie o Celery apontando para o módulo `tasks`:

```bash
celery -A tasks worker --loglevel=INFO
```

### 3. Executar tarefas no Python Shell

Abra um shell Python em outro terminal e execute os comandos abaixo:
```bash
from tasks import add, add__slow

# Executa uma tarefa simples
add.delay(10, 10)

# Executa uma tarefa que simula processamento demorado
add__slow.delay(20, 20)

# Executa a mesma função diretamente (bloqueia o terminal)
add__slow(20, 20)
```

### Observação

A função `add__slow` possui um `time.sleep(15)` para simular um processamento demorado.

- Quando você usa o método `.delay()`, a tarefa é enviada para a fila e processada por um worker. O shell Python não fica bloqueado enquanto a tarefa é executada.
- Quando a função é chamada diretamente, sem `.delay()`, o processamento ocorre no próprio shell Python, bloqueando-o até a conclusão.

## Monitorando o estado de uma tarefa

Você pode armazenar o resultado de uma tarefa em uma variável e monitorar seu estado ou buscar o resultado ao final:

```bash
# Envia a tarefa para a fila
result_slow = add__slow.delay(20, 20)

# Verifica se a tarefa foi concluída
result_slow.ready()  # Retorna False enquanto o processamento não for concluído

# Obtém o resultado da tarefa (aguarda até 15 segundos)
result_slow.get(timeout=15)  # Retorna 40
```

- O método `.ready()` retorna `True` se a tarefa foi concluída.
- O método `.get(timeout=x)` espera até `x` segundos pela conclusão da tarefa. Caso o tempo limite seja excedido, um `TimeoutError` será levantado.

## Conclusão

Este tutorial demonstra como usar o Celery para executar tarefas de forma assíncrona e acompanhar seu progresso. Para mais informações, consulte a documentação oficial do Celery.