# WOD
APIs that provide the word of the day.

## Set up
1. Install [pyenv](https://github.com/pyenv/pyenv)
2. Install fastapi: `pip install fastapi`
3. Install uvicorn: `pip install "uvicorn[standard]"`

## Run locally
Execute the following command:
```sh
uvicorn main:app --reload --reload-include *.json
```

If you need to keep the server running all the time, you could use [Supervisor](http://supervisord.org/). Here's a sample config:
```conf
[program:wod]
numprocs=1
directory=/home/user/projects/wod/
command=/home/user/projects/wod/scripts/server.sh
autostart=true
autorestart=true
stderr_logfile=/home/user/projects/wod/logs/wod.err.log
stdout_logfile=/home/user/projects/wod/logs/wod.out.log
```
