# protobuf-tutorial

## Setup
> Python >= 3.6

### 1. Download and Install Packages
```shell
$ git clone https://github.com/HughKu/protobuf-tutorial.git
$ cd protobuf-tutorial
$ pip install -r requirements.txt
```

### 2. Install protobuffer compiler
#### Mac OSX
```shell
$ brew install protobuf
```
#### Linux
```shell
TBD
```

### Compile
```shell
protoc -I=./proto --python_out=./proto ./proto/book.proto
```

## Run

#### 1. Write a minimum example

```python
pass
```