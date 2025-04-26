FROM grafana/grafana:latest

# Instalar plugins necessários
RUN grafana-cli plugins install grafana-piechart-panel \
    && grafana-cli plugins install grafana-clock-panel \
    && grafana-cli plugins install grafana-simple-json-datasource

# Configuração adicional (se necessário)
# COPY custom.ini /etc/grafana/grafana.ini