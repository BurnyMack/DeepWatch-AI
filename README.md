## About

This project is a POC to create a central database that takes big data from several open source threat-intelligence systems, combine this data with homegrown threat intelligence and analyse them using AI to % match against a list of indicators observed from within a given environment. The system must then return an approximate match to a user that feeds an ML engine by rating the match accordingly.

# Purpose

To provide cybersecurity teams the ability to create possible detections in the gaps of their security tool suite that are not able to be integrated, connecting these ecosystems and providing a threat intelligence capability to security systems that hold vast amounts of valuable datapoints that are unused.

## Components

The system from a high level perspective is divided into the following components:

* collectors- numerous crawlers of data feeds to consume data.
* normaliser - normalisers ingest data from bots in real time and parse them into a SCHEMA.
* analysers - consumes normalised data andcorrelates events and indicators using AI.
* workers - shift data through workflows, read and write from databases, maintain and update the system.

# Tech Stack

The systems tech stack likely changes as the POC progresses and capabilities and features are updated.

[MongoDB](https://learn.mongodb.com/learning-paths/using-mongodb-with-python?_ga=2.179144166.354275378.1696858985-712848114.1696858985)

[Compute](https://www.digitalocean.com/?refcode=e8a7842ff717https://www.digitalocean.com/?refcode=e8a7842ff717) (Digital Ocean Droplet)

[DataFrames](https://pandas.pydata.org/docs/) (NumPy, Pandas,)

[Artificial Intelligence &amp; ML](https://pytorch.org/) (PyTorch)

# Design

![image](https://github.com/BurnyMack/DeepWatch-AI/assets/58530324/8a8b8468-53b4-42b7-8a06-3496295d4f22)

