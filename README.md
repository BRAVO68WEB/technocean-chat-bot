<h1 align="center">Welcome to technocean-chat-bot 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.0.1-blue.svg?cacheSeconds=2592000" />
  <a href="LICENCE" target="_blank">
    <img alt="License: ISC" src="https://img.shields.io/badge/License-ISC-yellow.svg" />
  </a>
  <a href="https://twitter.com/gdsclpu" target="_blank">
    <img alt="Twitter: gdsclpu" src="https://img.shields.io/twitter/follow/gdsclpu.svg?style=social" />
  </a>
</p>

> ChatBot Repo for TechNOcean Website

## Install Rasa Open Source

Ubuntu · macOS · Windows

- First make sure your pip version is up to date:
```sh
pip3 install -U pip
```

- Then install Rasa Open Source using pip:
```sh
pip3 install rasa
```

## Congratulations! You have successfully installed Rasa Open Source!

- You can now create a new project with:

```sh
rasa init
```

## Build for Production

- To build development version of the Rasa, run:

```sh
curl -sSL https://install.python-poetry.org | python3 -
git clone https://github.com/RasaHQ/rasa.git
cd rasa
poetry install
```

## Additional dependencies

- For some ML components, you will need to install additional dependencies. Which are not installed by default.
- To install them, run:

```sh
pip3 install rasa[full]
```

## Dependencies for spaCy

- spaCy is the recommended library for doing most NLU-related tasks in Rasa. To install it, run:

```sh
pip3 install rasa[spacy]
python3 -m spacy download en_core_web_md
```

## Author

👤 **GDSC LPU**

* Website: https://gdsclpu.live/
* Twitter: [@gdsclpu](https://twitter.com/gdsclpu)
* Github: [@gdsclpu](https://github.com/gdsclpu)
* LinkedIn: [@gdsclpu](https://www.linkedin.com/company/gdsclpu/)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/gdsclpu/technocean-chat-bot/issues). 

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2023 [GDSC LPU](https://github.com/gdsclpu).<br />
This project is [ISC](LICENCE) licensed.
