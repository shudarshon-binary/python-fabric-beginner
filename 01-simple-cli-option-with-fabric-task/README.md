# how to run ( WIP )
modify VM ip and username in `config.ini`

```
virtualenv --python=`which python3` venv
source venv/bin/activate  
which python3
pip3 install -r requirements.txt
./script.sh deploy -e dev
or
./script.sh deploy -e stage
```

# configure VM ()

in this example `multipass` is used to spin up local VM. you can use any tool as per your choice. try customizing SSH key and username in cloud init config
```
multipass launch -n testvm --cloud-init cloud-init.yaml
multipass ls
ssh chaks@VM_IP_HERE
```
