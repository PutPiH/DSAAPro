# Chainstack Core

Official golang implementation of the Chainstack protocol.

## Building the source

Requires both a Go (version 1.9 or later) and a C compiler.

### Mac & Linux

Get source code to your go path

```shell
$ mkdir -p ~/go/src/github.com/caiqingfeng
$ cd ~/go/src/github.com/caiqingfeng
$ git clone git@github.com:caiqingfeng/chainstack-core.git
```

Run tests

```shell
$ cd ~/go/src/github.com/caiqingfeng/chainstack-core
$ make test
# or
$ ./cs.sh
```

Build chainstack to `~/go/bin`

```shell
$ cd ~/go/src/github.com/caiqingfeng/chainstack-core
$ make build
# or
$ ./cs.sh install
```

### Windows

The Chocolatey package manager provides an easy way to get the required build tools installed. If you don't have chocolatey yet, follow the instructions on [https://chocolatey.org](https://chocolatey.org) to install it first.

Then open an Administrator command prompt and install the build tools we need:

```shell
C:\Windows\system32> choco install git
C:\Windows\system32> choco install golang
C:\Windows\system32> choco install mingw
```

Use git shell run commands below

Get source code to your go path

```shell
$ mkdir -p ~/go/src/github.com/caiqingfeng
$ cd ~/go/src/github.com/caiqingfeng
$ git clone git@github.com:caiqingfeng/chainstack-core.git
```

Run tests

```shell
$ cd ~/go/src/github.com/caiqingfeng/chainstack-core
$ go test -p 1 ./...
```

Build chainstack to `~/go/bin`

```shell
$ cd ~/go/src/github.com/caiqingfeng/chainstack-core/cmd/chainstack
$ go install
```

## Executables

The chainstack-core project comes with several wrappers/executables found in the `cmd` directory.

|    Command    | Description                                                  |
| :-----------: | :----------------------------------------------------------- |
|  chainstack   | Our chain CLI client. It is the entry point into the Chainstack network, capable of running as a full node. It can be used by other processes as a gateway into the Chainstack network via JSON RPC endpoints exposed on top of HTTP, WebSocket and/or IPC transports. |
| chainstackcli | Our chain CLI client with console. It has all features of `chainstack`, and provides a easy way to start the node. You can input some commands to node in it, like `rpc -m StartMine` or `rpc -m CurrentBlock` |
|   bootnode    | Stripped down version of our Chainstack client implementation that only takes part in the network node discovery protocol, but does not run any of the higher level application protocols. It can be used as a lightweight bootstrap node to aid in finding peers in private networks. |
|     miner     | Mine block client, It must work with a `mine master` started by `chainstack` or `chainstackcli`. `mine master` dispatch sharding works for every miner registered. So all miner do different works when mining a block. |

## Running chainstack

Going through all the possible command line flags

```shell
$ chainstack -h
# or
$ chainstackcli -h
```

### Full node on the main Chainstack network

```shell
$ boots_env=mercury chainstackcli
```

This command will:

 * Guide you to setup your personal chainstack start config, and will write these args to your `$HOME/.chainstack/start_conf.json`, you can change these start args in this file.
 * Start sync chainstack test-net data from other nodes.
