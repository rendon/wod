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

Deploy to production with Docker
Build:
```sh
docker build -t wod-api .
```

Run and publish ports:
```sh
docker run -d --rm --name wod-api -p 8888:8888 wod-api
```

## TODO
- Make /wod/ query merriam webster everyday for the new word of the day
- Build a database of the 20K most common English words
- Add /words api that returns all 20K words in pages
- Add /words/{word} api
- Collect request metrics

