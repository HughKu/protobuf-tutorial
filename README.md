# protobuf-tutorial

## Setup
> Python >= 3.6

### 1. Download and install packages
```sh
git clone https://github.com/HughKu/protobuf-tutorial.git
cd protobuf-tutorial
pip install -r requirements.txt
```

### 2. Installing protoc (protobuf compiler)
> This tutorial uses **protoc-3.10.0** and it is suggested that your protoc version is later than 3.7.0.
#### Mac OSX
```sh
brew install protobuf
```
#### Linux
```sh
PROTOC_ZIP=protoc-3.10.0-linux-x86_64.zip
curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v3.10.0/${PROTOC_ZIP}
sudo unzip -o ${PROTOC_ZIP} -d /usr/local bin/protoc
sudo unzip -o ${PROTOC_ZIP} -d /usr/local 'include/*'
rm -f ${PROTOC_ZIP}
```

### Compile
```sh
protoc -I=./proto --python_out=./proto ./proto/**/*.proto
```

## Run

#### 1. Write a minimum example

```python
pass
```