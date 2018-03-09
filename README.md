[![Documentation Status](https://readthedocs.org/projects/flying-circus/badge/?version=latest)](http://flying-circus.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/flying-circus.svg)](https://badge.fury.io/py/flying-circus)

# flying-circus

Flying Circus is a tool for describing AWS infrastructure.
It uses the same data structures as the AWS Cloud Formation service,
wrapped up as Python code instead of the usual YAML. The Python program
can then generate a YAML template, which is passed across to Cloud
Formation in the usual manner. 

It may seem unusual to use a programming language to create descriptions of
infrastructure, instead of a configuration file like many of us are used to
(whether or not we also utilise a templating tool).
We hope that the Flying Circus library can empower DevOps folk by 
unlocking some of the powerful techniques that are available
for software code, like named variables and methods to structure code 
independently of the output format, libraries to allow code re-use with versioning,
automated refactoring and so on.

You can learn how to use Flying Circus yourself by reading the
[documentation](http://flying-circus.readthedocs.io/)

# Is/Is Not

There's a lot of tools for managing Infrastructure as Code, often with subtle
differences and passionate advocates. A quick discussion of it's scope may
help you understand where Flying Circus fits into this ecosystem, and whether it can
help you. This is presented in the simple "Is/Is Not" format.

## Flying Circus Is...

* ...a Pythonic DSL for writing fully featured Python code
* ...for Amazon Web Services infrastructure
* ...built on top of AWS [Cloud Formation templates](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html)
* ...a generator that always produces valid, consistent, human-readable, good-practice YAML

## Flying Circus Is Not...

* ...YAML or JSON. It's Python.
* ...a tool to make it easier to write YAML or JSON. You write Python, and YAML is an output.
* ...a DSL with a completely new syntax. You use normal Python syntax with all
  of it's features and nothing changed.
* ...a templating language, like Jinja2.
* ...a template management tool, like Ansible.
* ...an independent implementation of infrastructure management, like AWS
  Cloud Formation stacks, or Terraform.
* ...a cloud-agnostic abstraction layer.
* ...multi-cloud - although it could become this in the future.
  The current implementation is focused on representing AWS infrastructure
  using the CloudFormation data model. Other cloud providers have similar
  native data models, so it is feasible that we could re-use the concepts and
  tooling to support Google Cloud Platform, etc.
* ...a tool for interacting with the Cloud Formation service. There
  are other tools that can do this for you (such as boto3 or the AWS CLI,
  for starters)
* ...a validation tool - although it could become this in the future, and
  already has elements of validation as a by-product of presenting a helpful
  interface to users.

# Sounds Great, Can I Use It?
Sure, just install it through the Python packaging system:

```bash
  pip install flying-circus
```

Flying Circus is currently in **Alpha**. This means it may not work, and the
interface may change completely without warning. Additionally, the raw
service classes are currently generated by hand and there's not many of
them, so you will probably need to write some yourself.

# How Do I Help?
For now, just use it. See [the contributor's guidelines](./CONTRIBUTING.md)
