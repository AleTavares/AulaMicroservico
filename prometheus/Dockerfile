FROM prom/prometheus:latest

# Copia o arquivo de configuração para o contêiner
COPY prometheus.yml /etc/prometheus/prometheus.yml

# Define o diretório de trabalho
WORKDIR /etc/prometheus

# Expõe a porta padrão do Prometheus
EXPOSE 9090

# Comando padrão para iniciar o Prometheus
CMD ["--config.file=/etc/prometheus/prometheus.yml"]