# A Framework With Flask 

## 1 Abstract
I create a project to show how to program with flask.

## 2 Install
### 2.1 Dependency 

```
pip install -r requirements.txt
```

### 2.2 Database
Referrence to script.




## 3 Start
### 3.1 Configuration

#### 3.1.1 General Configuration

#### 3.1.2 Special Configuration 

### 3.2 Create Database

Referrence to script.

### 3.3 Start App

- Formal Environment

```
$ ./start_rest.sh # 启动rest服务
#!/usr/bin/env bash
export FLASK_COMMON_CONF=~/python/ProofOfReserves/config/production.py
export FLASK_INSTANCE_CONF=~/python/ProofOfReserves/instance/production.py
# python app.py
gunicorn -w 1 -b 127.0.0.1:6000 app:app --daemon
```

- Test Environment
```
$ ./t_start_rest.sh
$ ./t_start_cron.sh
```

## 4 Nginx

Configuration

```angular2html
sudo apt install nginx
sudo vim /etc/nginx/sites-enabled/default
sudo systemctl restart nginx
```

## 5 Test Rest Services

```angular2html
curl http://127.0.0.1:6000/asset/btc/statistic
curl http://127.0.0.1:6000/asset/btc/reserve
curl http://127.0.0.1:6000/user/12560005/asset/btc/validation
curl http://127.0.0.1:6000/user/12560005/asset/btc/validation?mark=0
curl http://127.0.0.1:6000/user/12560005/asset/btc/validation?mark=1
curl http://127.0.0.1:6000/user/12560005/asset/btc/isvalidated
curl http://127.0.0.1:6000/asset/btc/count
curl http://127.0.0.1:6000/count
curl http://127.0.0.1:6000/asset/btc/merkleroot
curl http://127.0.0.1:6000/asset/btc/merkle
curl http://127.0.0.1:6000/asset
```

