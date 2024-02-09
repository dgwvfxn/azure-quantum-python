[![Build Status](https://dev.azure.com/ms-quantum-public/Microsoft%20Quantum%20(public)/_apis/build/status/microsoft.qdk-python?branchName=main)](https://dev.azure.com/ms-quantum-public/Microsoft%20Quantum%20(public)/_build/latest?definitionId=32&branchName=main)

# Azure Quantum SDK

## Introduction

This repository contains the azure-quantum Python SDK.

Use azure-quantum SDK to submit quantum jobs written in Q#, Qiskit, or Cirq to the Azure Quantum service:

- `azure-quantum` [![PyPI version](https://badge.fury.io/py/azure-quantum.svg)](https://badge.fury.io/py/azure-quantum)

## Installation and getting started

To install the Azure Quantum package, run:

```bash
pip install azure-quantum
```

If using qiskit, cirq or qsharp, include the optional dependency as part of the install command:

```bash
pip install azure-quantum[qiskit]
pip install azure-quantum[cirq]
pip install azure-quantum[qsharp]
```

To get started, visit the following Quickstart guides:

- [Quickstart: Submit a circuit with Qiskit](https://learn.microsoft.com/azure/quantum/quickstart-microsoft-qiskit)
- [Quickstart: Submit a circuit with Cirq](https://learn.microsoft.com/azure/quantum/quickstart-microsoft-qiskit)
- [Quickstart: Submit a circuit with a provider-specific format](https://learn.microsoft.com/azure/quantum/quickstart-microsoft-provider-format).

## Development

See [CONTRIBUTING](./CONTRIBUTING.md) for instructions on how to build and test.

## Contributing

For details on contributing to this repository, see the [contributing guide](https://github.com/microsoft/azure-quantum-python/blob/main/CONTRIBUTING.md).

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

### Note on Packages

While we encourage contributions in any part of the code, there are some exceptions to take into account.
- The package `azure.quantum._client` is autogenerated using the [Azure Quantum Swagger spec](https://github.com/Azure/azure-rest-api-specs/tree/master/specification/quantum/data-plane). No manual changes to this code are accepted (because they will be lost next time we regenerate the client).

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
