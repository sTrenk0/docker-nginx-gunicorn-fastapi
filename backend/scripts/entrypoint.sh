#!/bin/sh

SCRIPT_DIR="$(dirname "$0")"
. "$SCRIPT_DIR/gunicorn.conf.sh"


if [ "$GUNICORN_CAPTURE_OUTPUT" = "True" ] \
 || [ "$GUNICORN_CAPTURE_OUTPUT" = "true" ] \
 || [ "$GUNICORN_CAPTURE_OUTPUT" = "1" ] \
 || [ "$GUNICORN_CAPTURE_OUTPUT" = 1 ] \
 ; then
  CAPTURE_FLAG="--capture-output"
else
  CAPTURE_FLAG=""
fi


echo "Starting Gunicorn with:"
echo "  - workers: $GUNICORN_WORKERS"
echo "  - worker class: $GUNICORN_WORKER_CLASS"
echo "  - bind: $GUNICORN_SOCKET_PATH"
echo "  - log level: $GUNICORN_LOG_LEVEL"
echo "  - error log: $GUNICORN_ERROR_LOG"
echo "  - access log: $GUNICORN_ACCESS_LOG"
echo "  - capture output: $GUNICORN_CAPTURE_OUTPUT"
echo "  - keep alive: $GUNICORN_KEEP_ALIVE"
echo "  - timeout: $GUNICORN_TIMEOUT"
echo "  - logger: $GUNICORN_LOGGER"
echo "  - forwarded allow ips: $GUNICORN_FORWARDED_ALLOW_IPS"


exec python3 -m gunicorn app.main:app \
 --workers=$GUNICORN_WORKERS \
 --worker-class=$GUNICORN_WORKER_CLASS \
 --bind=$GUNICORN_SOCKET_PATH \
 --log-level=$GUNICORN_LOG_LEVEL \
 --error-logfile=$GUNICORN_ERROR_LOG_FILE \
 --access-logfile=$GUNICORN_ACCESS_LOG_FILE \
 --keep-alive=$GUNICORN_KEEP_ALIVE \
 --timeout=$GUNICORN_TIMEOUT \
 --logger-class=$GUNICORN_LOGGER \
 --forwarded-allow-ips=$GUNICORN_FORWARDED_ALLOW_IPS \
 $CAPTURE_FLAG


