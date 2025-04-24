# Utiliza a imagem oficial do Prometheus
FROM prom/prometheus:latest

# Copia o arquivo de configuração do Prometheus para o contêiner
COPY prometheus.yml /etc/prometheus/prometheus.yml

# Define o diretório de trabalho
WORKDIR /etc/prometheus

# Exponha a porta padrão do Prometheus
EXPOSE 9090

# Comando para iniciar o Prometheus
CMD ["--config.file=/etc/prometheus/prometheus.yml"]