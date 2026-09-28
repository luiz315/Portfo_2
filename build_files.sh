#!/bin/bash
# build_files.sh - corrigido para estrutura seproject/

echo "Instalando dependências..."
pip install -r requirements.txt

echo "Coletando arquivos estáticos..."
python seproject/manage.py collectstatic --noinput