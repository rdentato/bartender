
# Bartender: A GPT-based Processing Pipeline Demo

Bartender is a demonstration of how to create a Custom GPTs completely based on its knowledge base.

It illustrates a general architecture for GPTs that use both "documents", i.e. static knowldge, and "scripts", i.e. dynamic knowldge.

The diagram below shows the architecture.

![Architecture Overview Placeholder](https://raw.githubusercontent.com/rdentato/bartender/main/imgs/SimpleGPTs_arch.png)

Note that this is equivalent to the process below:

## Objective

The core objective of Bartender is to illustrate the construction of a pipeline where the initial step involves a Language Model (LLM) processing the user's input. This output is then passed to a deterministic script, which performs specific, predefined operations. The result of this script is subsequently fed into another LLM step, culminating in the final output. This approach highlights the seamless integration of AI-driven and deterministic processes in a single workflow.

![Process flow](https://raw.githubusercontent.com/rdentato/bartender/main/imgs/SimpleGPT_flow.png)

Where the LLM is used to process the Input/Output of a regular program.

## License

[MIT](LICENSE.txt)

