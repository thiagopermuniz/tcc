docker run -it --rm \
    --name my_python_container \
    --cpus=1 \
    --memory=2g \
    -v /cria_tabela.py:/app/cria_tabela.py \
    -v /popula_tabela.py:/app/popula_tabela.py \
    python:latest 