# facemeplz

Web-based Python Application (Flask) to predict/recognize faces.

## Local Development

1. Clone project.
2. Create virtual environment for local development and install project dependencies:

   `pip install -r requirements.txt`.
 
3. Configure local dev by creating `.env` file and specifying project config (see the content of `.env.example`)
4. Run `docker-compose -f docker-compose.yml -f docker-compose.override.yml -f docker-compose.access.yml up`
5. Access service via browser `127.0.0.1:80` (`localhost`) or use `curl` to perform `POST` calls to respective endpoints:
    * `/api/v1/predictions/` (eg. `curl  -F "file=@000323.png" http://127.0.0.1/api/v1/predictions/`)
    * `/api/v1/recognitions/`

## Deployment

Project is configured to be deployed in Google Cloud Platform via Google Kubernetes Engine.

To deploy a new version of app just run `./deploy.sh`. 

*Note*: Make sure that `kubectl` and `gcloud` CLI tools are installed and properly configured.

## TODO

- [ ] Add batch image processing support for face detection.
- [ ] Implement face recognition endpoint - `/api/v1/recognitions/`.
- [ ] Add authorization flow.
- [ ] Add tests.