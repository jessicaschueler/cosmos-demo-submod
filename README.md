# cosmos-demo

This repo contains a dbt project and a set of Airflow DAGs showing how to run dbt in Airflow using [Cosmos](https://github.com/astronomer/astronomer-cosmos).

To run this, you'll need:

- [The Astro CLI installed](https://docs.astronomer.io/astro/cli/overview)
- Docker

## Setup

1. Clone this repo
2. Run `astro dev start` to start the Airflow instance

## The DAGs

The DAGs in this repo are meant to illustrate how to run dbt in Airflow using Cosmos. They use dbt's jaffle_shop example project.

This example utilizes git [submodules](https://github.blog/2016-02-01-working-with-submodules/) to keep the dbt example project, jaffle-shop, in a seperate repo. 
