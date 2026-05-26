#!/bin/bash
echo "Iniciando el despliegue automatico de Don Albert"
echo "Trayendo la ultima version desde git"
git pull origin main
echo "Asegurando las dependencias"
pip install -r requirements.txt
echo "Reiniciando el motor gunicorn"
sudo systemctl restart moto-api.service
echo "Despliegue completado con exito. El estado actual es:"
systemctl status moto-api.service --no-pager
