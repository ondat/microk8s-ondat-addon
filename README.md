## MicroK8s Ondat Add-on

- [MicroK8s Ondat Add-on](#microk8s-ondat-add-on)
  - [What is this?](#what-is-this)
  - [Resource Requirements](#resource-requirements)
  - [Dependencies](#dependencies)
  - [Supported Distributions](#supported-distributions)
  - [Quick-start & Usage](#quick-start--usage)
  - [Contributing](#contributing)
  - [License](#license)
  - [Code of Conduct](#code-of-conduct)
  - [Security](#security)
  - [Acknowledgements](#acknowledgements)

### What is this?

- This is an Ondat add-on that provides a software-defined, cloud native storage platform for [MicroK8s](https://github.com/canonical/microk8s) - a small, fast, single-package Kubernetes distribution for developers, IoT and edge.

### Resource Requirements

- For minimum Ondat resource requirements, refer to the [official Ondat - Prerequisites](https://docs.ondat.io/docs/prerequisites/) documentation. 
- For minimum MicroK8s resource requirements, refer to the [official MicroK8s - Getting Started](https://microk8s.io/docs/getting-started) documentation.

### Dependencies

- For Ondat to be successfully deployed onto a MicroK8s cluster, the following [Core add-ons](https://microk8s.io/docs/addon-dns) should be available:
  -  [`dns`](https://microk8s.io/docs/addon-dns) - [CoreDNS](https://coredns.io/) to provide address resolution services and service discovery in your MicroK8s cluster.
  - [`hostpath-storage`](https://microk8s.io/docs/addon-hostpath-storage) - Host storage for Ondat's `etcd` cluster.
  - [`helm3`](https://helm.sh/) - Helm 3 package manager for Kubernetes to deploy the Ondat Helm chart.

> 💡 The Ondat add-on will automatically check and deploy the required core add-ons if they are not already deployed in the MicroK8s cluster.

### Supported Distributions

- Tested on the following Ubuntu distributions:
  - Ubuntu 22.04 LTS (Jammy Jellyfish)
  - Ubuntu 20.04 LTS (Focal Fossa)
  - Ubuntu 18.04 LTS (BionicBeaver)
- Tested on the following architectures:
  - [x86-64 (64)](https://en.wikipedia.org/wiki/X86-64)

### Quick-start & Usage

```bash
# enable the Community repository first.
microk8s enable community

# run the command to install Ondat into your MicroK8s cluster.
microk8s enable ondat

# run the command to remove Ondat from your MicroK8s cluster.
microk8s disable ondat
```

### Contributing
- Contribution guidelines for this project can be found in the  [Contributing](./CONTRIBUTING.md)  document.

### License

- Licensed under the  [Apache License, Version 2.0](./LICENSE).

### Code of Conduct

- For more information on the project's CoC, review the  [Code of Conduct](./CODE_OF_CONDUCT.md)  document.

### Security

- For more information on the project's security policy and how to report potential security issues, review the  [Security](./SECURITY.md)  document.

### Acknowledgements

- [Use, edit or create addons - MicroK8s How To Guides](https://microk8s.io/docs/howto-addons)
- [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html).
- [ShellCheck](https://github.com/koalaman/shellcheck).
- [Black](https://github.com/psf/black).
