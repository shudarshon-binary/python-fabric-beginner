# configure VM

in this example `multipass` is used to spin up local VM. you can use any tool as per your choince. try customizing SSH key and username in cloud init config
```
multipass launch -n testvm --cloud-init config.yaml
multipass ls
ssh chaks@VM_IP_HERE
```

# how to run
modify VM ip and username in `fabfile.py`

```
virtualenv --python=`which python3` venv
source venv/bin/activate  
which python3
pip3 install -r requirements.txt
fab -V
fab test
fab -H example.com -u ${USER} test # only if you want to run this to remote host
deactivate
which python3
```
