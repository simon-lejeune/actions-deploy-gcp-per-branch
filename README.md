# actions-deploy-gcp-per-branch

## presentation
Feature branch deployment/runbot for a dummy python application on a e2-micro
of Google Cloud Platform.

## server setup

Installation:
Follow the instructions to [install a GitHub self-hosted runner](https://docs.github.com/en/actions/hosting-your-own-runners/adding-self-hosted-runners) in `~/actions-runner`, then execute:

```
apt install docker docker-compose tmux
sudo usermod -aG docker $USER
reboot
sudo docker network create network-traefik
```

On Google Cloud Platform, it is necessary to add a rule to the firewall if we want to access the dashboard on the port 8080.

The setup is now done. To start the runbot, use two `tmux` windows to run:

```
cd actions-runner
./run.sh
```

```
cd traefik
docker-compose up
```

## documentation

- [Feature branch testing with Github Actions and Traefik](https://diyor28.medium.com/feature-branch-testing-with-github-actions-and-traefik-b27936ec2a7e)

- [Continuous Delivery With Github Actions, Docker and Traefik on a Virtual Private Server (Part 1)](https://dev.to/alexandrupero/continuous-delivery-with-github-actions-docker-and-traefik-on-a-virtual-private-server-part-1-3285)

- [Traefik quick start](https://doc.traefik.io/traefik/getting-started/quick-start/)

## todo

- [ ] fix image deletion
- [ ] move branchname to subdomain
- [ ] letsencrypt integration
- [ ] make a test with a database
- [ ] feedback when eror in code and the server doesn't start
