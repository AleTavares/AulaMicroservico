FROM grafana/grafana:latest

# Copia os arquivos de provisionamento
COPY provisioning /etc/grafana/provisioning

# Define o diretório de trabalho
WORKDIR /usr/share/grafana

# Expõe a porta padrão do Grafana
EXPOSE 3000

# Comando padrão para iniciar o Grafana
CMD ["grafana-server", "--homepath=/usr/share/grafana"]