<div align="center">
<h1>
Hello World Example
</h1>

Built with `asyncflows`

[![main repo](https://img.shields.io/badge/main_repo-1f425f)](https://github.com/asynchronous-flows/asyncflows)
[![Discord](https://img.shields.io/badge/discord-7289da)](https://discord.gg/AGZ6GrcJCh)

</div>

## Introduction

Getting started with asyncflows, here is the "Hello World" example, prompting the language model to say "Hello, world!"  

<div align="center">
<img width="465" alt="hello world" src="https://github.com/asynchronous-flows/hello-world-example/assets/24586651/9f542c84-392c-4539-877a-0f40faeac39b">
</div>

## Running the Example

To run the example:

1. Set up [Ollama](https://github.com/asynchronous-flows/asyncflows#setting-up-ollama-for-local-inference) or configure [another language model](https://github.com/asynchronous-flows/asyncflows#using-any-language-model)  

2. Clone the repository

```bash
git clone ssh://git@github.com/asynchronous-flows/hello-world-example
```

3. Change into the directory

```bash
cd hello-world-example
```

4. Create and activate your virtual environment (with, for example)

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

5. Install the dependencies

```bash
pip install -r requirements.txt
```

6. Run the example

```bash
python hello_world.py
```
