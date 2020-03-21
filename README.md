# Aura Bot

**Note: This project has been discontinued, please refer to [Aura-Rewrite](https://github.com/Gryphticon/Aura-Rewrite) for ongoing development**

Aura bot is a clicker-type bot coded in Python 3.4 that I have created during the Summer of 2019 to increase participation within my Discord server, Gryphus Tech. This bot uses voice chat activity and text chat activity as clicks. These clicks can then be used to upgrade perks that increase your click rate.

This project is being open sourced as I have discontinued development due to school and other interests. This bot depends on an external postgresql server for storing user data. However, once connected and given permission to the database server, it should be able to set everything it needs to run automatically.

## Running the bot

The bot is run through the main.py script. I highly recommend running it in Docker in a Linux environment for easier hosting. Do not forget to install Python 3.4 alongside the dependencies listed below. If you have any issues, feel free to ask here on this Github. I will do my best to answer them.

## Dependencies

* Discord.py
* asyncpg
* numpy
