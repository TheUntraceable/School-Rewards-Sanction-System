

## What is it?
My school use ePraise as their rewards system, so I made my own system, I am currently bored and I wanted to make something similar to it, but because it already exists, this will just be a virtual environment where you can mess around with and not use as a long-term solution.

## Ok, how do I use it?
There should be a `config.json` file somewhere and you should input something such as the following the following data 
```json
{
    "mongo_url" : "mongodb://username:password@ip_address:port/", // The MongoDB URL
    "teacher_weekly_points" : 150, // How many points teachers start off with each week. This will not stack with the currently owned points.
    // More data will be wanted in future updates possibly.
}
```
After you do this, run `root.py`. I may later make this an entire system including a website, if I do complete my wishes, there will most likely be a `Dockerfile` where you should  install Docker, and `build` the Dockerfile and running the image. Incase I lose all senses of boredom this project will be archived, I will most likely also use [School-Bot](https://github.com/TheUntraceable/School-Bot) to manage this.

## It's not working!!!!!!!
Go create an issue.

## How do I contribute?
Create a pull request with what you changed and I'll review it and probably merge it. Thanks. I won't be giving any rewards.