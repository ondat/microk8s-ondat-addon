## Contributing

- [Contributing](#contributing)
  - [Opening an Issue](#opening-an-issue)
  - [Opening a Pull Request](#opening-a-pull-request)
    - [Environment Setup](#environment-setup)
    - [Submit Your Changes](#submit-your-changes)

### Opening an Issue

* If you experience or notice an error, bug, documentation issue, feel free to;
  1. [Open a GitHub Issue](https://github.com//ondat/microk8s-ondat-addon/issues) against the project.
  2. Provide details and logs in the description on how to reproduce the issue.
  3. Provide details of the operating system type and version, custom configurations, versions of applications that are displaying the issue, if applicable.

### Opening a Pull Request

#### Environment Setup

1. To quickly get started with MicroK8s, use a supported Ubuntu distribution and follow the [Getting Started](https://microk8s.io/docs/getting-started) MicroK8s guide.
2. To create a multi-node MicroK8s cluster, review the [Create a MicroK8s cluster](https://microk8s.io/docs/clustering) guide. Ensure that you install the MicroK8s package on the node(s) that will be used to join your cluster.

	 > 💡When adding nodes to a cluster, end users may experience a similar error message `Connection failed. The hostname (node-fcac1e38-6872-4839-b2a0-e3c34db85428) of the joining node does not resolve to the IP "188.166.144.180". Refusing join (400).` - To resolve this issue, a recommendation would be to review the [issue #3225](https://github.com/canonical/microk8s/issues/3225#issuecomment-1178287337) and apply the workaround solution in the comment.

3. Once your cluster is up and running, follow the detailed instructions on how to develop MicroK8s add-ons by reviewing the [HACKING.md](https://github.com/canonical/microk8s-community-addons/blob/main/HACKING.md) document located in the MicroK8s Community add-on repository. 
	 > Ensure that the unit tests are applied as you will not be able to successflly enable or disable the add-on without them.
5. Lastly, before running Ondat, ensure that the `enable` and `disable` scripts are executable files otherwise you will experience permission related issues.

```bash
# navigate into the Ondat directory.
cd addons/ondat/

# make "enable" and "disable" into executable files.
chmod +x enable disable

# enable the Ondat add-on.
microk8s enable ondat
```

#### Submit Your Changes

* If you would like to contribute to the project, feel free to create a Pull Request;
  1. [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) the upstream repository.
  2. [Clone](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) the recently forked repository to your workstation.
  3. Navigate into the repository and [create a branch and checkout](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) into the new branch.
  4. Make changes that you would like to contribute, then [add and commit changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository) to the repository.
  5. [Push](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository) the changes you made in the local branch to your remote fork.
  6. [Create a Pull Request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) against the upstream repository.

* When working on the bash `enable` and `disable` scripts, a recommendation would be to leverage [ShellCheck](https://github.com/koalaman/shellcheck), which is a static analysis tool for checking shell scripts for bugs, warnings and providing suggestions to address issues found. 
* For the Python unit tests, a recommendation would be to use [Black](https://github.com/psf/black), which is an uncompromising Python code formatter that is useful for consistent code styling.
