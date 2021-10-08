# nyko

### GNS3 Server in VMWare Fusion on OSX
![image](https://user-images.githubusercontent.com/306971/136234919-9cee597a-06d7-41d4-9e69-9143fe54431f.png)

### GNS3 User Interface
![image](https://user-images.githubusercontent.com/306971/136235044-3313a515-9e1e-440a-a6a8-ac961943bcf5.png)

### GNS3 Desktop Interface
![image](https://user-images.githubusercontent.com/306971/136235190-680af203-9beb-4469-85cb-b9f122435cf7.png)

### GNS3 Web Interface
![image](https://user-images.githubusercontent.com/306971/136235895-0def3be8-6320-453e-90bb-3c2a755ac366.png)

### ExaBGP Simulator with Dynamic Routes 
![image](https://user-images.githubusercontent.com/306971/136235512-f3c4e14d-839f-4ad5-8bad-e0263577ac7c.png)

# Faucet

### VMWare Fusion

The Fusion VM [binary](https://github.com/faucetsdn/faucet/releases) is a qcow2 but VMWare fusion wants a vmdk. I used [qemu](https://www.virtualdennis.com/how-to-convert-qcow2-to-vmdk-for-vmware-using-macos/) to convert it.
```
qemu-img convert -f qcow2 -O vmdk ~/Downloads/faucet-amd64-1.9.55.qcow2 ~/Downloads/faucet-amd64-1.9.55.vmdk
```
Create a new VM, select Ubuntu as the OS and UEFI as the boot type, and start the VM.

My network adapter is set like this
![image](https://user-images.githubusercontent.com/306971/136431019-06755730-85ff-4c09-829f-dda4e541ff6e.png)

Find the VM's IP address.

![image](https://user-images.githubusercontent.com/306971/136431587-14e81d71-49ef-4ea7-a203-572240dfc3ad.png)

Login to Grafana
![image](https://user-images.githubusercontent.com/306971/136431438-12cc57b9-cb78-4d45-b6e9-3e6fdef1f1dd.png)

The Faucet configuration instructions say http://localhost:9090 for the Prometheus data source address. I guess my networking's wonky but I used http://172.16.182.3:9090/ (the VM's address) and that works.


