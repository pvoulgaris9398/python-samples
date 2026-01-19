# python-samples

- Note, run `conda activate {environment-name1}` prior to running `vscode`

## Sub-Folder/Project: `data-analysis`

### `Sunday, 1/18/2026`

- Found interesting discussion of using proxy-server for managing services and routes in home lab setup
- TODO: Checkout [traefik](https://traefik.io/traefik)
- Got my local python postgres database connectivity test sample working, connecting to the container running in my raspberry pi server
- (Note, very, very slow. Really need to install the HAT and an SSD via NVMe connector rather than relying on even USB 3.0)
- Pointing to named `server-name` via entry in:

```text
C:\Windows\System32\drivers\etc\hosts
```

- Create local `.env` file with the following contents:

```bash
DBSERVER=****
DBNAME=****
DBPORT=****
DEVUSERNAME=****
DEVUSERPASSWORD=****
```

### `Saturday, 1/17/2026`

- Working on connecting to my postgres instance running in docker
- Added host ip address and dns name to `hosts` file:
- `C:\Windows\System32\drivers\etc`

## Algorithms

```text
Self-explanatory
```

## Playground

```text
This is an area I am using for playing around with various interesting code snippets
```
