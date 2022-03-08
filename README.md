# CS208Project

Running HpBandSter Distriputed mode

run init script for all server to install requirement

`sudo bash init`

Change the path in the NFSsetup-host to a directory you like and run NFSsetup-host on one server

`sodo bash NFssetup-host`

Change the path in the NFSsetup-client to a directory you like and run NFSsetup-client on other server

`sodo bash NFssetup-client`

run hpb-cluster.py on a server as the master 
`python3 hpb-cluster.py --run_id $run_id --nic_name $ethId(e.g. eno1d1) --shared_directory $your_NFSdic`
run hpb-cluster.py on other server as the worker 
`python3 hpb-cluster.py  --run_id $run_id --nic_name $ethId(e.g. eno1d1)  --shared_directory $your_NFSdic --worker`

